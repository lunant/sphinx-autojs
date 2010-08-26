"""
Sphinx-AutoJS
-------------

Generates documentation from your JavaScript docstring automatically.

"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name="Sphinx-AutoJS",
      version="0.10",
      url="http://github.com/sublee/sphinx-autojs",
      license="GPL+MIT",
      author="Lee Heung-sub",
      author_email="heung@sublee.kr",
      description="Generates documentation from your JavaScript "
                  "docstring automatically",
      long_description=__doc__,
      packages=["sphinx.ext"],
      namespace_packages=["sphinx"],
      install_requires=["Sphinx"])

