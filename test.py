from gpiozero import OutputDevice
from time import sleep

print("output device")
led = OutputDevice(7)

while True:
    print("loop")
    led.on()
    sleep(1)
    led.off()
    sleep(1)