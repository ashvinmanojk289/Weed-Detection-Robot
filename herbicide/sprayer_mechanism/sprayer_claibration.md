# Sprayer Calibration Guide

## Purpose
To ensure precise herbicide application, the sprayer must be calibrated for:
- Spray duration
- Flow rate

## Steps

1. **Setup**:
   - Connect the sprayer to the GPIO pin.
   - Fill the sprayer tank with water for testing.

2. **Measure Flow Rate**:
   - Run the sprayer for 5 seconds:
     ```bash
     python3 sprayer_control.py
     ```
   - Measure the volume of water sprayed.

3. **Adjust Duration**:
   - Modify the `duration` parameter in `sprayer_control.py` to achieve the desired flow rate.

4. **Final Test**:
   - Test the sprayer with herbicide under field conditions.
