from leds import blink
import machine
from server import connect_to_wifi, open_socket, serve


print("Hello Pico!")
blink()

try:
    ip = connect_to_wifi()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
