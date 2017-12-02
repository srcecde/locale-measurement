"""
Python Locale Measurement
========================
Developed by: Chirag Rathod (Srce Cde)
Email: chiragr83@gmail.com
========================
"""
import sys, os
from datetime import datetime
from measurement.measures import Distance, Weight, Temperature, Speed, Volume, Area
import quantities as qn
from babel.units import format_unit
import pytz
from simpledate import SimpleDate

DISTANCE = Distance
WEIGHT = Weight
TEMPERATURE = Temperature
SPEED = Speed
VOLUME = Volume
AREA = Area
PRESSURE = qn

SI_STANDARD = {
        'distance': 'm',
        'weight': 'kg',
        'temperature': 'k',
        'volume': 'l',
        'area': 'sq_m',
        'speed': 'm__hr',
        'pressure': 'Pa'
    }

IMPERIAL_STANDARD = {
        'distance': 'mi',
        'weight': 'lb',
        'temperature': 'f',
        'volume': 'us_g',
        'area': 'sq_mi',
        'speed': 'mi__hr',
        'pressure': 'psi'
}

METRIC_STANDARD_LOCALE = { 
        'm': 'meter', 
        'kg': 'mass-kilogram', 
        'k': 'temperature-kelvin', 
        'l': 'volume-liter', 
        'sq_m': 'area-square-meter', 
        'm__hr': 'speed-meter-per-second',
        'Pa': 'pascal'
    }

USA_METRIC_STANDARD_LOCALE = {
        'mi': 'length-mile',
        'lb': 'mass-pound',
        'f': 'temperature-fahrenheit',
        'us_g': 'volume-gallon',
        'sq_mi': 'area-square-mile',
        'mi__hr': 'speed-mile-per-hour',
        'psi': 'pressure-pound-per-square-inch'
}

def decorate(func):
    def func_wrapper(*args, **kwargs):
        if args[1] == 'en_US' or args[1] == 'my_MM':
            MS = IMPERIAL_STANDARD
            MSL = USA_METRIC_STANDARD_LOCALE
        else:
            MS = SI_STANDARD
            MSL = METRIC_STANDARD_LOCALE

        OBJ_STR = args[0].__name__.lower()
        if args[0].__name__.lower() == 'mass':
            OBJ_STR = 'weight'

        if OBJ_STR in MS and OBJ_STR is not list(MS.keys())[-1]:
            if args[1] == 'en_GB' and OBJ_STR == 'distance':
                TO_METRIC = 'mi'
                METRIC = 'length-mile'
            else:
                TO_METRIC = MS[OBJ_STR]
                METRIC = MSL[TO_METRIC]

            return {
                    "from": str(*kwargs), 
                    "to": METRIC, 
                    "unit": kwargs[str(*kwargs)], 
                    "convertedUnit": [format_unit(str(getattr(args[0](**{str(*kwargs): i}), TO_METRIC)), METRIC, locale=args[1]) for i in list(*kwargs.values())]
                    }

        if OBJ_STR == 'quantities':
            TO_METRIC = MS['pressure']
            METRIC = MSL[TO_METRIC]
            source, unit = zip(*kwargs.items())
            sourceObj = getattr(qn, source[0])

            return {"from": str(*kwargs), 
                    "to": METRIC, 
                    "unit": kwargs[str(*kwargs)], 
                    "convertedUnit": [format_unit(float(str((i * sourceObj).rescale(TO_METRIC)).split(' ')[0]), METRIC, locale=args[1]) for i in list(*kwargs.values())]} 
    return func_wrapper

@decorate
def unitConversion(unit, scale, conType):
    return
