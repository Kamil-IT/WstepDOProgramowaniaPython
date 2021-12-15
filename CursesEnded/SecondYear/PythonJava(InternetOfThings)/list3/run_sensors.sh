#!/bin/bash

python3 fake_sensor.py --config_location=app1/beach_water_quality_config.ini &
python3 fake_sensor.py --config_location=app2/phone_location_config.ini &
python3 fake_sensor.py --config_location=app3/temperature_config.ini &
python3 fake_sensor.py --config_location=app4/air_quality_config.ini &
python3 fake_sensor.py --config_location=app5/humidity_config.ini &