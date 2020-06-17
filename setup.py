from setuptools import setup

setup(name='rpi_ws281x',
      version='1.0.1',
      author='Andy Werner',
      author_email='dev@mr-beam.org',
      description='Mr Beam\'s precompiled version of https://github.com/mrbeam/rpi_ws281x',
      license='MIT',
      url='https://github.com/mrbeam/rpi_ws281x/',
      py_modules=['neopixel'],
      
      # this is hacky but I couldn't find any other way to get this .so file
      # into the root package folder (/usr/local/lib/python2.7/dist-packages)
      # if package (first arg) is '' (empty sting), .so file and up in /usr/local/lib
      # if package (first arg) is 'foo' so file and up in /usr/local/lib/python2.7/dist-packages/foo
      data_files=[('/usr/local/lib/python2.7/dist-packages', ['_rpi_ws281x.so'])],
      )
