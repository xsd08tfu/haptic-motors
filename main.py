from gpiozero import PWMOutputDevice
from time import sleep, time

motor1 = PWMOutputDevice(21)
motor2 = PWMOutputDevice(20)
print("Running at 50%")
motor1.value = 0.5
motor2.value = 0.5

sleep(5)
print("Running at 75%")
motor1.value = 0.75
motor2.value = 0.75

sleep(5)

print("Running at 100%")
motor1.value = 1
motor2.value = 1
sleep(5)
print("Ending")
exit()