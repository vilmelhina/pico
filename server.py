from time import sleep
import network
from my_config import ssid, password
from leds import start_green, stop_green, start_red, stop_red
from microdot import Microdot


def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    print("Connecting to WIFI...")
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print("Waiting for connection...")
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f"Connected on {ip}")


def serve():
    app = Microdot()

    @app.route("/")
    async def index(request):
        return "Hello, world!"

    @app.post("/redLED")
    async def postRedLed(request):
        if request.json.get("state") == "ON":
            start_red()
            return {"success": True}
        if request.json.get("state") == "OFF":
            stop_red()
            return {"success": True}
        return "Bad request", 400

    @app.post("/greenLED")
    async def postGreenLed(request):
        if request.json.get("state") == "ON":
            start_green()
            return {"success": True}
        if request.json.get("state") == "OFF":
            stop_green()
            return {"success": True}
        return "Bad request", 400

    app.run()
