from time import sleep
from leds import blink
from picozero import pinout
import network
import socket
import machine
import os
from my_config import ssid, password


def connect():
    print("Connecting to WIFI...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print("Waiting for connection...")
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f"Connected on {ip}")
    return ip


print("Hello Pico!")
blink()

try:
    connect()
except KeyboardInterrupt:
    machine.reset()
