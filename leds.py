from picozero import pico_led, LED, Button
from time import sleep

green_led = LED(1)
red_led = LED(14)
button = Button(6)


def start_green():
    green_led.on()


def stop_green():
    green_led.off()


def start_red():
    red_led.on()


def stop_red():
    red_led.off()


def blink():
    start_all()
    sleep(1)
    stop_all()


def start_all():
    pico_led.on()
    start_green()
    start_red()


def stop_all():
    pico_led.off()
    stop_green()
    stop_red()
