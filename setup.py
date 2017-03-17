import importlib
import sys

from distutils.core import setup
from setuptools import find_packages

from fabricio import __version__

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

min_fixed_versions = {
    'six': (1,4,0),
    'setuptools': (18,5),
    'pyparsing': (2,0,1),
}

for module_name, min_version in min_fixed_versions.items():
    try:
        module = importlib.import_module(module_name)
        installed_version = tuple(map(int, module.__version__.split('.')))
    except ImportError:
        installed_version = ()

    if installed_version >= min_version:
        install_requires.append('{module}=={version}'.format(
            module=module_name,
            version='.'.join(map(str, installed_version)),
        ))
    else:
        install_requires.append('{module}>={version}'.format(
            module=module_name,
            version='.'.join(map(str, min_version)),
        ))

if sys.version_info < (2,7):
    install_requires.append(
        'ordereddict>=1.1',
    )

setup(
    name='fabricio',
    version=__version__,
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
