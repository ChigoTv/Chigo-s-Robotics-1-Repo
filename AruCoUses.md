# 📄 README: ArUco Detection and Distance Estimation

## 📌 Overview
This program **detects ArUco markers using a camera**, **estimates their distance**, and **displays the fixed camera position** in real-time. 
The detected markers are highlighted with **green bounding boxes**, and their **3D position (X, Y, Z) relative to the camera** is calculated.

This program can be **integrated into robotic vision systems**, including **robotic arms**, **RC cars**, and **autonomous systems**.

## 🚀 Features
✅ **Detects multiple ArUco markers** and tracks them in real-time  
✅ **Estimates the marker’s distance from the camera**  
✅ **Draws a green bounding box** and an **axis on each detected marker**  
✅ **Displays the camera’s fixed position** in the top-left corner  
✅ **Handles errors gracefully** to prevent program crashes  

## 📦 Installation
### 🔧 Requirements
- Python 3.x
- OpenCV (with ArUco support)
- NumPy

### 🛠 Install Dependencies
Run the following command to install required packages:
```bash
pip install opencv-contrib-python numpy
```

## 📸 Usage
### 🔹 Run the Program
```bash
python Aruco_Detection.py
```

### 🔹 How It Works
1. **Opens the webcam** and starts detecting ArUco markers.
2. **Identifies each marker’s ID** and **calculates its position** relative to the camera.
3. **Draws a bounding box and axis** on each detected marker.
4. **Displays the camera’s fixed position** in the top-left corner.
5. **Prints marker information (ID, position, and distance)** in the terminal.
6. **Press 'q' to exit** the program.

## 🦾 How to Integrate with a Camera Vision-Controlled Robotic Arm
### 🔷 Step 1: Connect the Camera to Your Robotic Arm System
- Attach a **USB camera** or a **Raspberry Pi Camera Module** to your robotic arm’s processing unit.
- Modify the script to access the correct camera feed if using an **external camera module**.

### 🔷 Step 2: Use Marker Position for Robot Movement
- The program outputs the **(X, Y, Z) position of the marker**.
- Send this position to your robotic arm’s **inverse kinematics (IK) system** to guide the arm towards the marker.

Example:
```python
marker_position = (x, y, z)  # Position from ArUco detection
robotic_arm.move_to_position(marker_position)
```

### 🔷 Step 3: Integrate with a ROS-Based Robotic Arm
- If using **ROS (Robot Operating System)**:
  - Publish the marker’s **(X, Y, Z) position** to a ROS topic.
  - Subscribe to this topic in your robotic arm’s **motion control node**.

Example (ROS Publisher):
```python
import rospy
from geometry_msgs.msg import Point

rospy.init_node("aruco_detector")
pub = rospy.Publisher("aruco_position", Point, queue_size=10)

marker_position = Point(x, y, z)
pub.publish(marker_position)
```

### 🔷 Step 4: Implement Closed-Loop Control
- The robotic arm should continuously adjust its position **based on real-time ArUco detection**.
- Implement a **PID controller** to smooth out movements and avoid overshooting.

### 🔷 Step 5: Add Object Grasping Logic
- Once the robotic arm reaches the ArUco marker’s location, trigger the **gripper mechanism** to grasp the object.
- Use **distance estimation (Z-axis value)** to determine the **optimal gripping height**.

## 🛠 Troubleshooting
| Issue | Solution |
|--------|---------|
| The program crashes when detecting a tag | Ensure OpenCV **contrib** module is installed (`opencv-contrib-python`) |
| No markers detected | Ensure proper **lighting conditions** and **clear marker visibility** |
| Distance measurements are inaccurate | Calibrate the camera properly to get the correct **camera matrix** and **distortion coefficients** |

## 📜 License
This project is open-source and free to use.

## 🙌 Contributing
Feel free to **fork** this repository and submit **pull requests** with improvements!
