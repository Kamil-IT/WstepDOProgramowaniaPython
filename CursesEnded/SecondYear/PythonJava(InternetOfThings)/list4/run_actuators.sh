#!/bin/bash

python3 actuator.py --port=6001 --status=on --type=1 &
python3 actuator.py --port=6002 --status=on --type=2