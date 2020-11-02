import configparser
import csv
import json
import time

import click as click
import paho.mqtt.client as mqtt
import requests


# @click.command()
# @click.option("--config", default='beach_water_quality_config', help='Path with file name to configure app.')
# def main(config):
#     return config


def read_config_file_default(config):
    config = configparser.ConfigParser()
    config.read('beach_water_quality_config.ini')
    return config['DEFAULT']['Protocol'], config['DEFAULT']['Frequency'], config['DEFAULT']['Data']


def get_http_url():
    config = configparser.ConfigParser()
    config.read(get_config_location())
    return config['protocol.http']['Url'] + config['protocol.http']['Path']


def get_mqtt_config():
    config = configparser.ConfigParser()
    config.read(get_config_location())
    return config['protocol.mqtt']['Url'], config['protocol.mqtt']['Topic'], config['protocol.mqtt']['Client']


def get_data_from_csv_file(file_name):
    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        list_rows = []
        for row in csv_reader:
            list_rows.append(row)
        return list_rows


def send_http_message(url, json_message):
    requests.post(url, json=json_message)
    print("sent: http url:" + url + " message:" + json_message)


def publish_mqtt_message(client, topic, json_message):
    client.publish(topic, json_message)
    print("sent: mqtt url:" + topic + " message:" + json_message)


config = 'beach_water_quality_config.ini'
print('Configuration location: ' + config)

config = configparser.ConfigParser()
config.read('beach_water_quality_config.ini')
print(config.sections())




protocol_, frequency_, dataSource_ = read_config_file_default(config)
rows_ = get_data_from_csv_file(dataSource_)
print('Use protocol: ' + protocol_)
print('Use frequency: ' + frequency_)
print('Use data source: ' + dataSource_)
print(f'Processed {len(rows_)} lines.')

if protocol_ == 'http':
    url_ = get_http_url()
    while True:
        for row in rows_:
            send_http_message(url_, json.dumps(row))
            time.sleep(float(frequency_))
elif protocol_ == 'mqtt':
    print('Use protocol: mqtt')
    url_, topic_, client_ = get_mqtt_config()
    client = mqtt.Client(client_)
    client.connect(url_)
    client.subscribe(topic_)
    while True:
        for row in rows_:
            publish_mqtt_message(client, topic_, json.dumps(row))
            time.sleep(float(frequency_))
