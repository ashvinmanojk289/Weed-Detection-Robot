import RPi.GPIO as GPIO
import time

# Setup for servo motor
servo_pin = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Set up PWM for servo motor
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz frequency
pwm.start(0)  # Initialize with 0% duty cycle

def control_servo(angle):
    duty_cycle = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

if __name__ == "__main__":
    control_servo(90)  # Rotate servo to 90 degrees
    time.sleep(2)
    control_servo(0)   # Rotate servo back to 0 degrees
    GPIO.cleanup()
