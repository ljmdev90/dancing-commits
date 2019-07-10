#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(name='dancing-commits',
      version='0.1',
      description='纯属娱乐, 生成假的git提交记录',
      url='https://github.com/TimeFinger/dancing-commits',
      author='Lu Jiaming',
      author_email='hewn2011@126.com',
      license='MIT',
      packages=find_packages(),
      scripts=["bin/dancing"],
      zip_safe=False)