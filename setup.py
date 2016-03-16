from os import path
from codecs import open
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='django-crowd-auth',
    version='1.0.0',
    description="Django authentication backend for Atlassian Crowd REST",
    long_description=long_description,

    license='MIT',

    classifiers=[
        "Development Status :: 5 - Production/Stable"
        "Environment :: Web Environment",
        'Framework :: Django',
        'Intended Audience :: Developers',
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
    ],

    keywords='django crowd auth backend',
    packages=find_packages(exclude=['tests']),

    install_requires=['requests'],
)
