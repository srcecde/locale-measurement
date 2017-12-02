Locale Based Measurement Unit Conversion (Python)
=================================================

.. raw:: html

   <hr>

A Python wrapper around measurement, quantities, babel, pytz,
simple-date for conversion of Distance, Weight, Temperature, Volume,
Area, Speed and Pressure.

.. raw:: html

   <hr>

.. raw:: html

   <h3>

Installation

.. raw:: html

   </h3>

::

    pip3 install localemeasurement

.. raw:: html

   <h3>

How to USE

.. raw:: html

   </h3>

::

    # unitConversion accepts 3 parameters
    # Measurement Unit, locale, dict args
    from localeconversion import unitConversion

.. raw:: html

   <ul>

.. raw:: html

   <li>

DISTANCE

.. raw:: html

   </li>

.. raw:: html

   </ul>

::

      from localeconversion import DISTANCE
      unitConversion(DISTANCE, 'hi_IN', **{"km": [1,2,3]})
      

.. raw:: html

   <ul>

.. raw:: html

   <li>

WEIGHT

.. raw:: html

   </li>

.. raw:: html

   </ul>

::

      from localeconversion import WEIGHT
      unitConversion(WEIGHT, 'hi_IN', **{"g": [1,2,3]})
      

.. raw:: html

   <ul>

.. raw:: html

   <li>

TEMPERATURE

.. raw:: html

   </li>

.. raw:: html

   </ul>

::

      from localeconversion import TEMPERATURE
      unitConversion(TEMPERATURE, 'hi_IN', **{"f": [1,2,3]})
      

.. raw:: html

   <ul>

.. raw:: html

   <li>

VOLUME

.. raw:: html

   </li>

.. raw:: html

   </ul>

::

      from localeconversion import VOLUME
      unitConversion(VOLUME, 'hi_IN', **{"l": [1,2,3]})
      

.. raw:: html

   <ul>

.. raw:: html

   <li>

AREA

.. raw:: html

   </li>

.. raw:: html

   </ul>

::

      from localeconversion import AREA
      unitConversion(AREA, 'hi_IN', **{"kPa": [1,2,3]})
      

.. raw:: html

   <ul>

.. raw:: html

   <li>

SPEED

.. raw:: html

   </li>

.. raw:: html

   </ul>

::

      from localeconversion import SPEED
      unitConversion(SPEED, 'hi_IN', **{km__hr: [1,2,3]})
      

.. raw:: html

   <ul>

.. raw:: html

   <li>

PRESSURE

.. raw:: html

   </li>

.. raw:: html

   </ul>

::

      from localeconversion import PRESSURE
      unitConversion(PRESSURE, 'hi_IN', **{"kPa": [1,2,3]}

 The paramters that are passed in the dict args, should follow
measurement standards. For queries or issues, feel free to contact or
open an issue
