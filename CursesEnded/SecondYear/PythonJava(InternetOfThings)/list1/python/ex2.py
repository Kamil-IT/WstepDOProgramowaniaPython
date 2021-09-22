import time

import paho.mqtt.client as mqtt
import requests


def get_time(tz):
    res = requests.get('http://localhost:5002/time?tz=' + tz)
    print(res.text.__str__())
    return res.text.__str__()


def publish_time_mqtt(client):
    client.publish("time", get_time('Europe/Berlin'))


client = mqtt.Client("P1")
client.connect("192.168.1.13")
client.subscribe("time")

while True:
    publish_time_mqtt(client)
    time.sleep(5)
