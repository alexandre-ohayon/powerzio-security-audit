from asyncio import open_connection
import paho.mqtt.client as mqtt
from time import sleep
import requests


def on_connect(client, userdata, flags, rc):
    client.subscribe('#', qos=1)
    # client.subscribe('$SYS/#')
    print("connected")


def on_message(client, userdata, message):
    print(f"Topic: {message.topic} | QOS: {message.qos}  | Message: {message.payload}")


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    print(client.connect("10.10.10.34", 1883))
    print(client)
    client.loop_start()
    while True:
        sleep(0.5)


if __name__ == "__main__":
    main()