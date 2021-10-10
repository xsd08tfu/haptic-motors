from gpiozero import PWMOutputDevice
from time import sleep, time

motor = PWMOutputDevice(21)
motor.value = 1.0

sleep(2)
motor.value = 0.5

sleep(2)
motor.value = 0.1

exit()