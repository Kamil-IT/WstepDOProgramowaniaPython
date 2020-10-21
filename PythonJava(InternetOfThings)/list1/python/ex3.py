import paho.mqtt.client as mqtt
import requests


def on_message(clt, userdata, message):
    requests.post('http://localhost:5002/mqtt', {"students": [254331], "received_time": str(message.payload.decode('utf-8'))})


client = mqtt.Client("P2")
client.connect("192.168.1.13")
client.on_connect = lambda a, b, c, d: client.subscribe("time")

client.on_message = on_message
client.loop_forever()
