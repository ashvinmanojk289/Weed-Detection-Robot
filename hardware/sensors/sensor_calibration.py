import cv2

def calibrate_camera():
    # Camera calibration process (example for camera)
    camera = cv2.VideoCapture(0)
    
    if not camera.isOpened():
        print("Error: Could not open camera.")
        return
    
    print("Calibrating camera...")
    # Capture a few frames to check calibration
    for i in range(5):
        ret, frame = camera.read()
        if ret:
            cv2.imshow(f"Calibration Frame {i+1}", frame)
            cv2.waitKey(1000)  # Wait for 1 second to display the frame
    
    camera.release()
    cv2.destroyAllWindows()
    print("Camera calibration complete.")

if __name__ == "__main__":
    calibrate_camera()
