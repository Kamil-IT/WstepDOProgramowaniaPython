import json

import click as click
from flask import Flask, request

app = Flask(__name__)
process = []
configuration_sensor = {
    "port": "6001",
    "status": "on",
    "type": "1",
    "reverse": "off"
}


@app.route('/val', methods=['GET'])
def get_boost_val():
    if configuration_sensor["status"] == "off":
        return json.dumps({"val": 0})
    elif configuration_sensor["type"] == "1":
        if configuration_sensor["reverse"] == "on":
            return json.dumps({"val": -2})
        return json.dumps({"val": 2})
    else:
        if configuration_sensor["reverse"] == "on":
            return json.dumps({"val": -0.01})
        return json.dumps({"val": 0.01})


@app.route('/status', methods=['GET'])
def get_status():
    return json.dumps(configuration_sensor["status"])


@app.route('/status', methods=['post'])
def post_status():
    req = str(request.get_data(), 'utf-8')
    loads = json.loads(req)
    for key in loads.keys():
        configuration_sensor[key] = loads[key]
    print("Actuator 1 status is: " + configuration_sensor["status"])
    return "success"


@click.command()
@click.option("--port",
              default='aa',
              help='Port for actuator')
@click.option("--status",
              default='off',
              help='Status on or off')
@click.option("--type",
              default='1',
              help='Number off app')
def main(port, status, type):
    configuration_sensor["port"] = port
    configuration_sensor["status"] = status
    configuration_sensor["type"] = type
    app.run(port=configuration_sensor["port"])


if __name__ == '__main__':
    main()
