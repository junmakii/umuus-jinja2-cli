
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def run_tests(self):
        import sys
        import shlex
        import pytest
        errno = pytest.main(['--doctest-modules'])
        if errno != 0:
            raise Exception('An error occured during installution.')
        install.run(self)


setup(
    packages=setuptools.find_packages('.'),
    version='0.1',
    url='https://github.com/junmakii/umuus-jinja2-cli',
    author='Jun Makii',
    author_email='junmakii@gmail.com',
    keywords=[],
    license='GPLv3',
    scripts=[],
    install_requires=['addict>=2.2.0', 'fire>=0.1.3', 'PyYAML>=3.13', 'jinja2>=2.10', 'toolz>=0.9.0'],
    dependency_links=[],
    classifiers=[],
    entry_points={'console_scripts': ['umuus_jinja2_cli = umuus_jinja2_cli:main'],
 'gui_scripts': []},
    project_urls={},
    setup_requires=[],
    test_suite='',
    tests_require=[],
    extras_require={},
    package_data={},
    python_requires='',
    include_package_data=True,
    zip_safe=True,
    download_url='',
    name='umuus-jinja2-cli',
    description='A simple template utility with jinja2 syntax to use on Command-Line.',
    long_description=('A simple template utility with jinja2 syntax to use on Command-Line.\n'
 '\n'
 'umuus-jinja2-cli\n'
 '================\n'
 '\n'
 'Installation\n'
 '------------\n'
 '\n'
 '    $ pip install git+https://github.com/junmakii/umuus-jinja2-cli.git\n'
 '\n'
 'Example\n'
 '-------\n'
 '\n'
 "    $ umuus_jinja2_cli render --input 'Hello {{ name }}' --name James\n"
 '    Hello James\n'
 '\n'
 '    $ cat /tmp/FILE.txt\n'
 '    Hello {{ name }}\n'
 '\n'
 '    $ umuus_jinja2_cli render --file /tmp/FILE.txt --name James\n'
 '    Hello James\n'
 '\n'
 'Authors\n'
 '-------\n'
 '\n'
 '- Jun Makii <junmakii@gmail.com>\n'
 '\n'
 'License\n'
 '-------\n'
 '\n'
 'GPLv3 <https://www.gnu.org/licenses/>'),
    cmdclass={"pytest": PyTest},
)
