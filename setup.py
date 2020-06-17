from setuptools import setup

setup(name='rpi_ws281x',
      version='1.0.1',
      author='Andy Werner',
      author_email='dev@mr-beam.org',
      description='Mr Beam\'s precompiled version of https://github.com/mrbeam/rpi_ws281x',
      license='MIT',
      url='https://github.com/mrbeam/rpi_ws281x/',
      py_modules=['neopixel'],

      # _rpi_ws281x.so needs to be on root package, same level as neopixel.py
      # which is not so easy. I didn't find a better way than this.
      # I simply accept that I have the file three times on the divice.
      # Depending whether you install from a .ZIP file or from a folder (`pip install .`)
      data_files=[
	      # does not bring the file where we want it at all.
	      ('', ['_rpi_ws281x.so']),
	      # relative path, works if installed from zip
	      ('lib/python2.7/dist-packages', ['_rpi_ws281x.so']),
	      # absolute path, works if installed from folder
	      # If installed from zip the file will end up in `/usr/local/lib/python2.7/dist-packages/usr/local/lib/python2.7/dist-packages/_rpi_ws281x.so`
	      ('/usr/local/lib/python2.7/dist-packages', ['_rpi_ws281x.so']),
      ],
      )
