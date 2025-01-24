import RPi.GPIO as GPIO
import time

# GPIO pin for sprayer
sprayer_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(sprayer_pin, GPIO.OUT)

def activate_sprayer(duration=2):
    GPIO.output(sprayer_pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(sprayer_pin, GPIO.LOW)

if __name__ == "__main__":
    activate_sprayer()
    GPIO.cleanup()
