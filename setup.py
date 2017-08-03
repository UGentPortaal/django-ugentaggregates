import os
import os.path

from setuptools import find_packages
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-ugentaggregates",
    version="1.1.0",
    author="UGent Portaal Team",
    author_email="portaal-tech@ugent.be",
    description="Aggregates for Django.",
    long_description=README,
    license="BSD",
    url="https://github.com/UGentPortaal/django-ugentaggregates",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=["django"],
    test_suite="ugentaggregates.tests",
)
