from gpiozero import PWMOutputDevice
from time import sleep, time

motor1 = PWMOutputDevice(21)
motor2 = PWMOutputDevice(20)


print("Running at 100%")
motor1.value = 1
motor2.value = 1
