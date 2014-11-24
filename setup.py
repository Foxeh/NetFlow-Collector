#!/usr/bin/env python

from setuptools import setup, find_packages
import collector

setup(name='netflowinterface',
      version=collector.__version__,
      author=collector.__author__,
      url=collector.__url__,
      description='netflow interface module',
      packages=find_packages(),
      package_data={'':['*.ini','*.dat']},
      install_requires=["gevent>=1.0.1",
                        "dpkt>=1.7"],
      dependency_links=["https://pypi.python.org/packages/source/g/gevent/gevent-1.0.1.tar.gz",
                        "http://dpkt.googlecode.com/files/dpkt-1.7.tar.gz"]
      )
