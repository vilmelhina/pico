from picozero import pinout, pico_led, LED
from time import sleep

def flash(led):
    led.on()
    sleep(1)
    led.off()

green_led = LED(1)
red_led = LED(14)

flash(pico_led)
flash(green_led)
flash(red_led)