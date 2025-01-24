import RPi.GPIO as GPIO
import time

# Define GPIO pin for sprayer
sprayer_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(sprayer_pin, GPIO.OUT)

def activate_sprayer():
    GPIO.output(sprayer_pin, GPIO.HIGH)  # Turn on sprayer
    print("Sprayer activated.")
    time.sleep(5)  # Keep sprayer on for 5 seconds
    GPIO.output(sprayer_pin, GPIO.LOW)   # Turn off sprayer
    print("Sprayer deactivated.")

if __name__ == "__main__":
    activate_sprayer()
    GPIO.cleanup()
