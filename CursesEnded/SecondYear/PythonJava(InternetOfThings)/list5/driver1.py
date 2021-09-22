import json

import paho.mqtt.client as mqtt
import requests


def subscribe_topic(broker_url, topic, on_message):
    client = mqtt.Client()
    client.connect(broker_url)
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_forever()


def on_message_app1_driver(client, userdata, msg):
    if 20.0 < float(json.loads(str(msg.payload.decode('utf-8')))["Water Temperature"]):
        requests.post("http://127.0.0.1:6001/status", json={"reverse": "on", "status": "on"})
        print("Temperature too big " + str(json.loads(str(msg.payload.decode('utf-8')))["Water Temperature"]))
    elif float(json.loads(str(msg.payload.decode('utf-8')))["Water Temperature"]) < 17.0:
        requests.post("http://127.0.0.1:6001/status", json={"reverse": "off", "status": "on"})
        print("Temperature too small " + str(json.loads(str(msg.payload.decode('utf-8')))["Water Temperature"]))
    else:
        requests.post("http://127.0.0.1:6001/status", json={"status": "off"})
        print("good temperature")


def main():
    subscribe_topic("127.0.0.1", "beach_water_quality", on_message_app1_driver)


if __name__ == '__main__':
    main()
