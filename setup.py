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
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'],
      keywords = ['locale', 'measurement', 'unit', 'conversion'],\
      url='https://github.com/srcecde/locale-measurement',
      author='Srce Cde (Chirag Rathod)',
      author_email='chiragr83@gmail.com',
      license='MIT',
      packages=['localemeasurement'],
      install_requires=[
          'measurement', 'quantities', 'babel', 'pytz', 'simple-date'
      ],
      include_package_data=True,
      zip_safe=False)