"""
Python Locale Measurement
========================
Developed by: Chirag Rathod (Srce Cde)
Email: chiragr83@gmail.com
========================
"""
from setuptools import setup

setup(name='localemeasurement',
      version='0.1',
      description='locale based measurement',
      url='https://github.com/srcecde/locale-measurement',
      author='Srce Cde',
      author_email='chiragr83@gmail.com',
      license='MIT',
      packages=['measurement', 'quantities', 'babel', 'pytz', 'simpledate'],
      install_requires=[
          'markdown',
      ],
      zip_safe=False)