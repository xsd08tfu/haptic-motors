from gpiozero import PWMOutputDevice
from time import sleep, time

motor = PWMOutputDevice(21)
motor.value = 0.5

sleep(2)
exit()