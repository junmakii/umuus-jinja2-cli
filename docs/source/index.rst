
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

Table of Contents
-----------------
.. toctree::
   :maxdepth: 2
   :glob:

   *

