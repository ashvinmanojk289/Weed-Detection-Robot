import time
import RPi.GPIO as GPIO
import cv2
from imu_setup import read_imu
from actuator_control import control_servo
from sprayer_control import activate_sprayer

# Initialize GPIO
GPIO.setmode(GPIO.BCM)

# Initialize Camera (for weed detection)
camera = cv2.VideoCapture(0)

def detect_weed():
    # Simple weed detection logic (replace with model inference later)
    ret, frame = camera.read()
    if ret:
        # Display the frame for testing
        cv2.imshow("Camera Feed", frame)
        cv2.waitKey(1)

def main():
    try:
        while True:
            # Read IMU data
            read_imu()

            # Detect weeds using camera
            detect_weed()

            # Control actuator (servo example)
            control_servo(90)

            # Activate sprayer if weed detected (for demo)
            activate_sprayer()

            time.sleep(2)

    except KeyboardInterrupt:
        print("Shutting down robot...")
        camera.release()
        GPIO.cleanup()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
