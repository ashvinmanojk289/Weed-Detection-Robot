import smbus
import time

# Initialize I2C bus
bus = smbus.SMBus(1)
address = 0x68  # MPU6050 I2C address

# Wake up the MPU6050 (default is sleep mode)
bus.write_byte_data(address, 0x6B, 0)

def read_imu():
    # Read accelerometer and gyroscope data
    acc_x = bus.read_byte_data(address, 0x3B)
    acc_y = bus.read_byte_data(address, 0x3D)
    acc_z = bus.read_byte_data(address, 0x3F)
    
    gyro_x = bus.read_byte_data(address, 0x43)
    gyro_y = bus.read_byte_data(address, 0x45)
    gyro_z = bus.read_byte_data(address, 0x47)
    
    print(f"Accelerometer: X={acc_x}, Y={acc_y}, Z={acc_z}")
    print(f"Gyroscope: X={gyro_x}, Y={gyro_y}, Z={gyro_z}")

if __name__ == "__main__":
    read_imu()
