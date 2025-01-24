import RPi.GPIO as GPIO
import time

# Define motor pins
motor1_pin1 = 17  # Motor 1 forward
motor1_pin2 = 18  # Motor 1 backward
motor2_pin1 = 22  # Motor 2 forward
motor2_pin2 = 23  # Motor 2 backward

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)
GPIO.setup(motor2_pin1, GPIO.OUT)
GPIO.setup(motor2_pin2, GPIO.OUT)

def move_forward():
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin2, GPIO.LOW)

def move_backward():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.HIGH)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.HIGH)

def stop():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.LOW)

# Test movement
move_forward()
time.sleep(2)
move_backward()
time.sleep(2)
stop()

# Clean up GPIO pins
GPIO.cleanup()
