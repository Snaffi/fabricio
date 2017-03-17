import sys

from distutils.core import setup
from setuptools import find_packages

with open('README.rst') as description:
    long_description = description.read()

required_six_version = (1,4,0)
required_setuptools_version = (18,5)
required_pyparsing_version = (2,0,1)

install_requires = [
    'Fabric>=1.1,<2.0',
    'frozendict>=1.2,<2.0',
    'cached-property>=1.3',
    'docker-py>=1.8.1,<2.0',
    'dpath>=1.4.0',
]

try:
    import six
    installed_six_version = tuple(map(int, six.__version__.split('.')))
except ImportError:
    installed_six_version = ()
if installed_six_version >= required_six_version:
    install_requires.append('six=={}'.format(six.__version__))
else:
    install_requires.append('six>=1.4.0')

try:
    import setuptools
    installed_setuptools_version = tuple(map(int, setuptools.__version__.split('.')))
except ImportError:
    installed_setuptools_version = ()
if installed_setuptools_version >= required_setuptools_version:
    install_requires.append('setuptools=={}'.format(setuptools.__version__))

try:
    import pyparsing
    installed_pyparsing_version = tuple(map(int, pyparsing.__version__.split('.')))
except ImportError:
    installed_pyparsing_version = ()
if installed_pyparsing_version >= required_pyparsing_version:
    install_requires.append('pyparsing=={}'.format(setuptools.__version__))

if sys.version_info < (2,7):
    install_requires.append(
        'ordereddict>=1.1',
    )

setup(
    name='fabricio',
    version='0.3.24',
    author='Rinat Khabibiev',
    author_email='srenskiy@gmail.com',
    packages=list(map('fabricio.'.__add__, find_packages('fabricio'))) + ['fabricio'],
    url='https://github.com/renskiy/fabricio',
    license='MIT',
    description='fabricio',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',
        'Topic :: System :: Networking',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
    ],
    install_requires=install_requires,
)
