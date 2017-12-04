# Locale Based Measurement Unit Conversion (Python)
<hr>
A Python wrapper around measurement, quantities, babel, pytz, simple-date for conversion of Distance, Weight, Temperature, Volume, Area, Speed and Pressure.
<hr>
<h3>Installation</h3>

    pip3 install localemeasurement

<h3>How to USE</h3>

    # unitConversion accepts 3 parameters
    # Measurement Unit, locale, dict args
    from localeconversion import unitConversion
    
<ul>
  <li><b>DISTANCE</li></b></ul>
  
      from localeconversion import DISTANCE
      unitConversion(DISTANCE, 'hi_IN', **{"km": [1,2,3]})
      
  <ul><li><b>WEIGHT</b></li></ul>
  
      from localeconversion import WEIGHT
      unitConversion(WEIGHT, 'hi_IN', **{"g": [1,2,3]})
      
  <ul><li><b>TEMPERATURE</b></li></ul>
  
      from localeconversion import TEMPERATURE
      unitConversion(TEMPERATURE, 'hi_IN', **{"f": [1,2,3]})
      
  <ul><li><b>VOLUME</b></li></ul>
  
      from localeconversion import VOLUME
      unitConversion(VOLUME, 'hi_IN', **{"l": [1,2,3]})
      
  <ul><li><b>AREA</b></li></ul>
  
      from localeconversion import AREA
      unitConversion(AREA, 'hi_IN', **{"kPa": [1,2,3]})
      
  <ul><li><b>SPEED</b></li></ul>
  
      from localeconversion import SPEED
      unitConversion(SPEED, 'hi_IN', **{km__hr: [1,2,3]})
      
  <ul><li><b>PRESSURE</b></li></ul>
  
      from localeconversion import PRESSURE
      unitConversion(PRESSURE, 'hi_IN', **{"kPa": [1,2,3]}


The paramters that are passed in the dict args, should follow <a href="http://python-measurement.readthedocs.io/en/latest/">measurement</a> standards.


<b>For queries or issues, feel free to contact or open an <a href="https://github.com/srcecde/locale-measurement/issues">issue</a></b>
