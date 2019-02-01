#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Jun Makii <junmakii@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""A simple template utility with jinja2 syntax to use on Command-Line.

umuus-jinja2-cli
================

Installation
------------

    $ pip install git+https://github.com/junmakii/umuus-jinja2-cli.git

Example
-------

    $ umuus_jinja2_cli render --input 'Hello {{ name }}' --name James
    Hello James

    $ cat /tmp/FILE.txt
    Hello {{ name }}

    $ umuus_jinja2_cli render --file /tmp/FILE.txt --name James
    Hello James

Authors
-------

- Jun Makii <junmakii@gmail.com>

License
-------

GPLv3 <https://www.gnu.org/licenses/>

"""
import sys
import os
import re
import re
import jinja2
import yaml
import fire
import addict
__version__ = '0.1'
__url__ = 'https://github.com/junmakii/umuus-jinja2-cli'
__author__ = 'Jun Makii'
__author_email__ = 'junmakii@gmail.com'
__author_username__ = 'junmakii'
__keywords__ = []
__license__ = 'GPLv3'
__scripts__ = []
__install_requires__ = [
    'addict>=2.2.0',
    'fire>=0.1.3',
    'PyYAML>=3.13',
    'jinja2>=2.10',
    'toolz>=0.9.0',
]
__dependency_links__ = []
__classifiers__ = []
__entry_points__ = {
    'console_scripts': ['umuus_jinja2_cli = umuus_jinja2_cli:main'],
    'gui_scripts': [],
}
__project_urls__ = {}
__setup_requires__ = []
__test_suite__ = ''
__tests_require__ = []
__extras_require__ = {}
__package_data__ = {}
__python_requires__ = ''
__include_package_data__ = True
__zip_safe__ = True
__static_files__ = {}
__extra_options__ = {}
__download_url__ = ''
__all__ = []


def parse_metadata(content):
    return (content.startswith('---') and (
        lambda _: _ and (content[len(_[0][0]):], yaml.load(_[0][1])) or (content, None)
    )(re.findall('^(---\n((.|\n)*?)\n---\n)', content, re.MULTILINE))
            or (content, None))


def render(**kwargs):  # type: None
    options = addict.Dict(kwargs, **kwargs.get('options', {}))
    options.input = options.input or (open(options.file).read())
    content, metadata = parse_metadata(options.input)
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(([] + (
            options.file and [os.path.abspath(os.path.dirname(options.file))]
            or []) + [os.path.abspath('.')])))
    template = env.from_string(content)
    output = template.render(
        **{
            key: value
            for key, value in
            (list((metadata or {}).items()) + list(os.environ.items()) +
             list(options.items()) + list(options.get('options', {}).items()))
        })
    print(output)
    return


def main(argv=None):
    fire.Fire()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
