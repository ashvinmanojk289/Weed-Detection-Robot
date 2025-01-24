#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
from cv_bridge import CvBridge
import cv2

bridge = CvBridge()

def detect_weeds(image):
    # Placeholder for weed detection logic
    detected_weeds = [Point(1.0, 2.0, 0.0)]  # Example detected weed location
    return detected_weeds

def image_callback(msg):
    rospy.loginfo("Received image")
    frame = bridge.imgmsg_to_cv2(msg, "bgr8")
    weeds = detect_weeds(frame)
    for weed in weeds:
        weed_pub.publish(weed)

if __name__ == "__main__":
    rospy.init_node("perception_node")
    weed_pub = rospy.Publisher("weed_locations", Point, queue_size=10)
    rospy.Subscriber("camera/image_raw", Image, image_callback)
    rospy.spin()
