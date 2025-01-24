#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Point
import RPi.GPIO as GPIO

# GPIO setup for sprayer
sprayer_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(sprayer_pin, GPIO.OUT)

def spray_weed(location):
    rospy.loginfo(f"Spraying weed at {location.x}, {location.y}")
    GPIO.output(sprayer_pin, GPIO.HIGH)
    rospy.sleep(2)  # Spray duration
    GPIO.output(sprayer_pin, GPIO.LOW)

def weed_callback(msg):
    spray_weed(msg)

if __name__ == "__main__":
    rospy.init_node("control_node")
    rospy.Subscriber("weed_locations", Point, weed_callback)
    rospy.spin()
    GPIO.cleanup()
