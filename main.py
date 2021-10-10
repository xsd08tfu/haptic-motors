from gpiozero import PWMOutputDevice
from time import sleep, time

motor1 = PWMOutputDevice(21)
motor2 = PWMOutputDevice(20)


print("Running at 100%")

while True:
    print("Both at 100%")
    motor1.value = 1
    motor2.value = 1
    sleep(50)
    print("Changing in 10")
    sleep(10)
    print("Both at 90%")
    motor1.value = 0.9
    motor2.value = 0.9
    sleep(50)
    print("Changing in 10")
    sleep(10)
    print("Both at 0%")
    motor1.value = 0
    motor2.value = 0
    sleep(50)
    print("Changing in 10")
    sleep(10)
    