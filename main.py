from leds import blink
from server import connect_to_wifi, serve

print("Hello Pico!")
blink()

try:
    connect_to_wifi()
    serve()
except KeyboardInterrupt:
    pass
