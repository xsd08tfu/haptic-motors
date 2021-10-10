from gpiozero import PWMOutputDevice
from time import sleep, time

motor1 = PWMOutputDevice(21)
motor2 = PWMOutputDevice(20)

def MotorControl(power,time):
    print("Setting motors to "+str(power*100)+"%")
    motor1.value = power
    motor2.value = power
    sleep(time-10)
    print("Changing in 10")
    sleep(5)
    print("Changing in 5")
    sleep(5)

while True:
    MotorControl(1,30)
    MotorControl(0.9,30)
    MotorControl(0.8,30)
    MotorControl(1,30)
    MotorControl(0,30)