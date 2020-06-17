from setuptools import setup

setup(name='rpi_ws281x',
      version='1.0.1',
      author='Andy Werner',
      author_email='dev@mr-beam.org',
      description='Mr Beam\'s precompiled version of https://github.com/mrbeam/rpi_ws281x',
      license='MIT',
      url='https://github.com/mrbeam/rpi_ws281x/',
      py_modules=['neopixel'],
      
      # this seems to work only if installed from zip file.
      # if installed from folder (`pip install .`) this file end up in ` /usr/local/lib/`
      data_files=[('', ['_rpi_ws281x.so'])],
      )
