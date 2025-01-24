#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseStamped

def send_goal(x, y):
    goal = PoseStamped()
    goal.header.frame_id = "map"
    goal.pose.position.x = x
    goal.pose.position.y = y
    goal.pose.orientation.w = 1.0
    goal_pub.publish(goal)

if __name__ == "__main__":
    rospy.init_node("navigation_node")
    goal_pub = rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=10)
    rospy.loginfo("Navigation node ready")
    send_goal(5.0, 5.0)  # Example goal
    rospy.spin()
