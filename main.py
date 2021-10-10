from gpiozero import PWMOutputDevice
from time import sleep, time

motor1 = PWMOutputDevice(21)
motor2 = PWMOutputDevice(20)

def MotorControl(power,time):
    motor1.value = power
    motor2.value = power
    sleep(time)

MotorControl(1,0.5)
MotorControl(0.5,0.5)
MotorControl(1,0.5)
MotorControl(0,2)

while True:

    MotorControl(1,30)
    MotorControl(0.9,30)
    MotorControl(0.8,30)
    MotorControl(1,30)
    MotorControl(0,30)