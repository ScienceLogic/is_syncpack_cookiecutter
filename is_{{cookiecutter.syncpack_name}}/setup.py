#!/usr/bin/env python
from setuptools import setup, find_packages
import json
import os

# getting the path of the metajson file
metajson_path = ""
for r, _, f in os.walk("."):
    result_paths = [file for file in f if 'meta.json' in file]
    if len(result_paths) > 0:
        metajson_path = os.path.join(r, result_paths[0])
        break
if metajson_path:
    with open(metajson_path) as metajson_file:
        metadata_json = json.load(metajson_file)

setup(
    name=metadata_json["name"],
    version=metadata_json["version"],
    description=metadata_json.get("summary", ""),
    long_description=metadata_json.get("description", ""),
    author=metadata_json.get("author", ""),
    packages=find_packages(exclude=["docs", "tests*"]),
    include_package_data=True,
    url=metadata_json.get("home_page", ""),
    install_requires=metadata_json.get("requires_dist", []),
    classifiers=["Development Status :: 4 - Beta", "Topic :: Other/Nonlisted Topic"],
)
