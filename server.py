from time import sleep
import network
import socket
import os
from my_config import ssid, password
from leds import start_green, stop_green, start_red, stop_red


def connect_to_wifi():
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


def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection


def serve(connection):
    print("Serving...")
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        print(request)
        try:
            print(parseRequest(request))
            request = request.split(" ")[1]
        except IndexError:
            print("error")
            pass
        if request == "/redLED":
            print("RED LED")
        elif request == "/greenLED":
            print("GREEN LED")
        client.close()


def parseRequest(request):
    lines = request.split("\r\n")
    method = lines[0].split(" ")[0]
    path = lines[0].split(" ")[1]
    body = lines[-1]
    return {"method": method, "path": path, "body": body}
