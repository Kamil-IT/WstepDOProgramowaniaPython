import configparser
import csv
import json
import multiprocessing
import time

import click as click
import paho.mqtt.client as mqtt
import requests
from flask import Flask, request

app = Flask(__name__)
process = []
configuration_sensor = {
    # Data file name
    "data-file-name": "dane1.csv",

    # Time to send new info about sensor (in seconds)
    "time": "10",
    # Protocol with data will be send
    "protocol": "mqtt",

    # Config http message system
    "http-url-send-request": "http://localhost:8000/dane1",

    # Port for external properties
    "external-properties-Port": "5001",
    "topic": "topic1",

    # Status turn on/off
    "status": "on",
}


@app.route('/config', methods=['POST'])
def post_config():
    process[0].kill()
    req = str(request.get_data(), 'utf-8')
    loads = json.loads(req)
    for key in loads.keys():
        configuration_sensor[key] = loads[key]
    if configuration_sensor["actuator"]:
        process_send_sensor_info = multiprocessing.Process(target=send_sensor_info,
                                                           args=(configuration_sensor["frequency"],
                                                                 configuration_sensor["protocol"],
                                                                 configuration_sensor["url"],
                                                                 configuration_sensor["topic"]),
                                                           name="send_sensor_info")
        process_send_sensor_info.start()
        process[0] = process_send_sensor_info
    return "success"


@app.route('/config', methods=['GET'])
def get_config():
    sensor_copy = configuration_sensor.copy()
    sensor_copy.pop("data-file-name")
    sensor_copy.pop("http-url-send-request")
    sensor_copy.pop("external-properties-Port")
    return json.dumps(sensor_copy)


@click.command()
@click.option("--config_location",
              default='app1/beach_water_quality_config.ini',
              help='Path with file name to configure app.')
def main(config_location):
    print('Configuration location: ' + config_location)

    config = configparser.ConfigParser()
    config.read(config_location)
    print(config.sections())

    protocol_, frequency_, dataSource_ = read_config_file_default(config_location)
    config_external_port_ = get_external_settings_config(config_location)
    url_mqtt_, topic_mqtt_, client_ = get_mqtt_config(config_location)
    http_url_ = get_http_url(config_location)
    rows_ = get_data_from_csv_file(get_app_folder(config_location) + "/" + dataSource_)

    print('Use external port for config: ' + config_external_port_)
    print('Use protocol: ' + protocol_)
    print('Use frequency: ' + frequency_)
    print('Use data source: ' + dataSource_)
    print(f'Processed {len(rows_)} lines.')
    configuration_sensor["protocol"] = protocol_
    configuration_sensor["frequency"] = frequency_
    configuration_sensor["dataSource"] = dataSource_
    configuration_sensor["config_location"] = config_location
    configuration_sensor["external-properties-Port"] = config_external_port_
    if protocol_ == "http":
        configuration_sensor["url"] = http_url_
    else:
        configuration_sensor["url"] = url_mqtt_
    configuration_sensor["topic"] = topic_mqtt_
    configuration_sensor["status"] = "on"

    process_send_sensor_info = multiprocessing.Process(target=send_sensor_info,
                                                       args=(frequency_, protocol_,
                                                             configuration_sensor["url"], topic_mqtt_),
                                                       name="send_sensor_info")
    process_send_sensor_info.start()
    process.append(process_send_sensor_info)
    app.run(port=configuration_sensor["external-properties-Port"])


def get_boost_val(row):
    try:
        if configuration_sensor["topic"] == "beach_water_quality":
            boost = json.loads(requests.get("http://127.0.0.1:6001/val").json())["val"]
            row["Water Temperature"] = float(row["Water Temperature"]) + boost
        elif configuration_sensor["topic"] == "phone_location":
            boost = json.loads(requests.get("http://127.0.0.1:6002/val").json())["val"]
            row["Latitude"] = float(row["Latitude"]) + boost
    except:
        print("actuator is off")
    return row


def send_sensor_info(frequency_, protocol_, url, topic):
    config_location = configuration_sensor["config_location"]
    rows_ = get_data_from_csv_file(get_app_folder(config_location) + "/" + configuration_sensor["dataSource"])
    if protocol_ == 'http':
        url_ = url
        while True:
            for row in rows_:
                send_http_message(url_, json.dumps(get_boost_val(row)))
                time.sleep(float(frequency_))
    elif protocol_ == 'mqtt':
        print('Use protocol: mqtt')
        url_, topic_, client_ = get_mqtt_config(config_location)
        url_ = url
        topic_ = topic
        client = mqtt.Client(client_)
        client.connect(url_)
        client.subscribe(topic_)
        while True:
            for row in rows_:
                publish_mqtt_message(client, topic_, json.dumps(get_boost_val(row)))
                time.sleep(float(frequency_))


def read_config_file_default(config_location):
    config = configparser.ConfigParser()
    config.read(config_location)
    return config['DEFAULT']['Protocol'], config['DEFAULT']['Frequency'], config['DEFAULT']['Data']


def get_http_url(config_location):
    config = configparser.ConfigParser()
    config.read(config_location)
    return config['protocol.http']['Url'] + config['protocol.http']['Path']


def get_app_folder(config_location):
    config = configparser.ConfigParser()
    config.read(config_location)
    return config['DEFAULT']['App']


def get_mqtt_config(config_location):
    config = configparser.ConfigParser()
    config.read(config_location)
    return config['protocol.mqtt']['Url'], config['protocol.mqtt']['Topic'], config['protocol.mqtt']['Client']


def get_external_settings_config(config_location):
    config = configparser.ConfigParser()
    config.read(config_location)
    return config['external.properties']['Port']


def get_data_from_csv_file(file_name):
    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        list_rows = []
        for row in csv_reader:
            list_rows.append(row)
        return list_rows


def send_http_message(url, json_message):
    requests.post(url, data=json_message, headers={'content-type': 'application/json'})
    print("sent: http url:" + url + " message:" + json_message)


def publish_mqtt_message(client, topic, json_message):
    client.publish(topic, json_message)
    print("sent: mqtt topic:" + topic + " message:" + json_message)

def on_mesage(message):
    mesg_to_client = do_something_with_message(message)
    send_to_client(mesg_to_client)

if __name__ == '__main__':
    main()
