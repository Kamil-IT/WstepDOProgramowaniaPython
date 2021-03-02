import json

import paho.mqtt.client as mqtt
import requests


def subscribe_topic(broker_url, topic, on_message):
    client = mqtt.Client()
    client.connect(broker_url)
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_forever()


def on_message_app2_driver(client, userdata, msg):
    if 41.80 < float(json.loads(str(msg.payload.decode('utf-8')))["Latitude"]):
        requests.post("http://127.0.0.1:6002/status", json={"reverse": "on", "status": "on"})
        print("Latitude too big " + json.loads(str(msg.payload.decode('utf-8')))["Latitude"])
    elif float(json.loads(str(msg.payload.decode('utf-8')))["Latitude"]) < 41.78:
        requests.post("http://127.0.0.1:6002/status", json={"reverse": "off", "status": "on"})
        print("Latitude too small " + json.loads(str(msg.payload.decode('utf-8')))["Latitude"])
    else:
        requests.post("http://127.0.0.1:6002/status", json={"status": "off"})
        print("Latitude good")



def main():
    subscribe_topic("127.0.0.1", "phone_location", on_message_app2_driver)


if __name__ == '__main__':
    main()
