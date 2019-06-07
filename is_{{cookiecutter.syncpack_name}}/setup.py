#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='{{cookiecutter.syncpack_name}}',
    version='{{cookiecutter.version}}',
    description='{{cookiecutter.project_short_description}}',
    author='{{cookiecutter.author}}',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    url='https://code.eng.sciencelogic.com/projects/AIR/repos/is_{{cookiecutter.syncpack_name}}',
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Other/Nonlisted Topic'
    ]
)



