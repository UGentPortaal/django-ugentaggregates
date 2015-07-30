import os.path

from setuptools import setup, find_packages

setup(name="django-aggregates",
      version="0.0.1",
      author="UGent Portaal Team",
      author_email="portaal-tech@ugent.be",
      description="Aggregates for Django.",
      long_description=open(os.path.join(os.path.dirname(__file__),
                                         "README.rst")).read(),
      license="BSD",
      url="https://github.com/UGentPortaal/django-aggregates",
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
      test_suite="aggregates.tests")
