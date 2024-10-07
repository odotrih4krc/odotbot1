from machine import Pin
import time

# motor works
motor_a1 = Pin(14, Pin.OUT)
motor_a2 = Pin(15, Pin.OUT)
motor_b1 = Pin(16, Pin.OUT)
motor_b2 = Pin(17, Pin.OUT)


# controls
def move_forward(duration):
    motor_a1.on()
    motor_a2.off()
    motor_b1.on()
    motor_b2.off()
    time.sleep(duration)
    stop_motors()

def move_backward(duration):
    motor_a1.off()
    motor_a2.on()
    motor_b1.off()
    motor_b2.on()
    time.sleep(duration)
    stop_motors()

def turn_left(duration):
    motor_a1.off()
    motor_a2.on()
    motor_b1.on()
    motor_b2.off()
    time.sleep(duration)
    stop_motors()

def turn_right(duration):
    motor_a1.on()
    motor_a2.off()
    motor_b1.off()
    motor_b2.on()
    time.sleep(duration)
    stop_motors()

def stop_motors():
    motor_a1.off()
    motor_a2.off()
    motor_b1.off()
    motor_b2.off()

# usage of bot
while True:
    move_forward(10)  # movemnt in secs
    turn_left(5)     
    move_backward(10) 
    turn_right(5)    
