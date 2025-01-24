# Raspberry Pi Setup for Weed Detection Robot

## Requirements:
- Raspberry Pi 3 or higher
- Raspbian OS installed
- Internet connection (for package installation)

## Steps:

1. **Install Raspbian OS**:
   - Download the latest Raspbian OS image from [Raspberry Pi website](https://www.raspberrypi.org/software/).
   - Flash the image to an SD card using [Raspberry Pi Imager](https://www.raspberrypi.org/software/).

2. **Connect to Wi-Fi**:
   - Connect your Raspberry Pi to Wi-Fi using the desktop GUI or terminal.

3. **Update and Upgrade**:
   ```bash
   sudo apt update
   sudo apt upgrade
4. Install Dependencies:
   ```bash
   sudo apt install python3-pip
   sudo apt install python3-dev
   sudo apt install python3-opencv
6. Enable I2C:
   ```bash
   sudo raspi-config
   # Enable I2C under 'Interfacing Options'
8. Reboot Raspberry Pi:
   ```bash
   sudo reboot

You are now ready to run the robot code!
