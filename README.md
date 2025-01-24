# Weed Detection Robot

This repository contains the code for a weed detection robot designed to autonomously detect and spray herbicide on weeds in agricultural fields using a combination of ROS, AI, and precision agriculture techniques.

## Project Structure

- **hardware**: Contains code and documentation for the hardware setup, including the robot base, sensors, actuators, and computing platform.
- **model**: Contains code for training and running the transformer-based weed detection model.
- **ros**: Contains ROS nodes for perception, control, and navigation of the robot.
- **herbicide**: Contains code for the herbicide spraying mechanism.
- **docs**: Contains additional documentation and images.

## Installation

### Dependencies

- ROS Noetic (or your preferred version)
- Python 3.x
- PyTorch
- OpenCV
- TensorFlow (if needed)
- CUDA (for GPU acceleration)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/weed-detection-robot.git
   cd weed-detection-robot
2. Install ROS dependencies:
   ```bash
   rosdep install --from-paths src --ignore-src -r -y
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
4. Build the ROS workspace:
   ```bash
   catkin_make

### Usage

1. Launch the robot:
   ```bash
   roslaunch weed_detection_robot launch/robot_launch_file.launch
2. The robot will start moving and spraying herbicide when weeds are detected.

## Contributing

Feel free to fork this repository, open issues, or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
