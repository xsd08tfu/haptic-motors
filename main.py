from gpiozero import PWMOutputDevice
from time import sleep, time

motor1 = PWMOutputDevice(21)
motor2 = PWMOutputDevice(20)
motor1.value = 1.0
motor2.value = 1.0

sleep(5)
motor1.value = 0.75
motor2.value = 0.75

sleep(5)
motor1.value = 0.5
motor2.value = 0.5
sleep(5)
exit()