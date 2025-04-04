# Gesture Recognition – Robotics 1 Progress Report  
**Team Members:**  
- **Om Samel** (ompradee@buffalo.edu)  
- **Chigozie Eke** (cmeke@buffalo.edu)  

---

## 🧠 Project Overview  
We are developing a gesture recognition system capable of detecting and classifying hand gestures in real-time using computer vision techniques. This system is intended to serve as a foundational control module for robotic platforms, providing natural and intuitive interaction. The goal is to enable gesture-based robotic control, with future applications in robotic arms, drones, smart wheelchairs, and warehouse automation.

---

## 🔄 Pivot from Arduino  
Initially, the project was intended to interface with an **Arduino-controlled robot**, but due to **time constraints and hardware costs**, we pivoted to a fully **simulated environment using Webots and Gazebo**. This change allows us to focus on the software and control systems while maintaining project goals and feasibility.

---

## ✅ Progress Summary

### 🔧 Development and Research
- **Chigozie** has been exploring **Webots**, creating simulations using a variety of built-in robots, writing custom Python controllers, and gaining fluency with motor control and sensor interaction within Webots.
- **Om** has been evaluating the best **libraries** for gesture detection (e.g., OpenCV + Mediapipe) and setting up **Gazebo** on macOS, which required additional dependencies and configurations.
- Both members have continued to review **relevant literature** on gesture-based HRI (Human-Robot Interaction) and robotic simulation tools.

---
## 🧰 Tools and References

### 📚 Online Materials
- Mediapipe (Google) Documentation  
- OpenCV Tutorials  
- Webots and Gazebo Simulation Tutorials  
- Research articles on Gesture-Based HRI

### 🛠️ Development Stack
- Python, OpenCV, Mediapipe  
- Jupyter Notebook, PyCharm  
- GitHub for documentation  
- Webots (in use), Gazebo (in progress)  

---

## 📅 Updated Milestones and Checklist

| **Task**                                                      | **Assigned To**     | **Due Date** | **Status**       |
|---------------------------------------------------------------|----------------------|--------------|------------------|
| Complete project proposal document                            | Both                 | Feb 28       | ✅ Completed      |
| Set up development environment (OpenCV, Mediapipe)            | Both                 | March 3      | ✅ Completed      |
| Explore hardware options (Pivoted to simulation)              | Both                 | March 7      | ❌ Cancelled (Pivoted) |
| Study/Explore OpenCV and Webots                               | Chigozie             | March 7      | ✅ Completed      |
| Implement real-time hand tracking                             | Om                   | March 12     | 🟡 In Progress    |
| Test and refine gesture recognition accurac                   | Om                   | March 19     | 🟡 In Progress    |
| Map gestures to robotic commands in simulation                | Chigozie             | March 26     | 🟡 In Progress    |
| Create progress report                                         | Both                 | April 3      | ✅ **This File**  |
| Develop a gesture classification model                   | Both                 | April 10     | ⏳ Not Started    |
| Prepare demo with robotic control application (simulated)     | Both                 | April 24     | ⏳ Not Started    |
| Create final presentation                                     | Both                 | May 6        | ⏳ Not Started    |
| Provide system documentation (README.md)                      | Both                 | May 13       | ⏳ Not Started    |

---

---
Putting our research phase into action is our next steps, Heres's How we will do this:

---

## 🧠 Goal
Use **real-time gesture recognition** (via webcam and MediaPipe) to **replace keyboard controls** and command the robot in **Webots** using Python.

---

## ✅ Overall Architecture

```
[OpenCV + MediaPipe]
↓
Detect Hand Gestures
↓
Map Gesture → Direction Command
↓
Webots Controller → Move Robot
```

---

## 🔧 Setup Checklist

### 1. **Install Required Libraries**
```bash
pip install opencv-python mediapipe
```

---

### 2. **Design Gesture → Command Mapping**

| Hand Gesture            | Command         | Webots Equivalent |
|-------------------------|------------------|-------------------|
| Open palm facing camera | Move Forward     | W                 |
| Fist                    | Stop             | None (key == -1)  |
| Thumb left              | Turn Left        | A                 |
| Thumb right             | Turn Right       | D                 |
| Palm down               | Move Backward    | S                 |

---

## 👨‍💻 Implementation Plan

### 🧩 **Step 1: Create a Separate Gesture Detection Module (Python File)**

```python
# gesture_control.py
import cv2
import mediapipe as mp

class GestureRecognizer:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(max_num_hands=1)
        self.mp_draw = mp.solutions.drawing_utils
        self.cap = cv2.VideoCapture(0)

    def get_gesture(self):
        success, img = self.cap.read()
        if not success:
            return "none"

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = self.hands.process(img_rgb)

        gesture = "none"

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                # You can calculate distances or angles between landmarks here
                # For now, use hand openness as a basic example:
                thumb_tip = handLms.landmark[4].x
                index_tip = handLms.landmark[8].x

                if abs(thumb_tip - index_tip) < 0.05:
                    gesture = "fist"
                else:
                    gesture = "open"

                # Example: Add custom logic for thumb left/right
                # gesture = "left" or "right" etc.

        return gesture
```

---

### 🧩 **Step 2: Integrate Into Webots Controller**

Replace your `keyboard.getKey()` logic with gesture detection:

```python
from controller import Robot
from gesture_control import GestureRecognizer

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Motors
left_motor = robot.getMotor('left wheel motor')
right_motor = robot.getMotor('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Gesture recognizer
gesture_recognizer = GestureRecognizer()
max_speed = 10

while robot.step(timestep) != -1:
    left_speed = max_speed
    right_speed = max_speed

    gesture = gesture_recognizer.get_gesture()
    
    if gesture == "open":  # Forward
        left_motor.setVelocity(-left_speed)
        right_motor.setVelocity(-right_speed)

    elif gesture == "fist":  # Stop
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)

    elif gesture == "left":
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(-right_speed)

    elif gesture == "right":
        left_motor.setVelocity(-left_speed)
        right_motor.setVelocity(0.0)

    elif gesture == "down":
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

    else:
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
```

---

## 🧪 Testing Strategy
- Test `gesture_control.py` standalone with a live webcam window to debug gesture accuracy.
- Once confirmed, run the Webots controller to ensure the robot responds as expected.

---

## 📈 Stretch Goals
- Add **gesture smoothing** (using frame buffer)
- Add **more gestures** (e.g., peace sign, two hands)
- Use **hand landmarks and angles** for precise classification

---


## 📏 Measures of Success  
The system will be evaluated on the following criteria:

- **Gesture Classification Accuracy**: ≥ 75% in varied conditions  
- **Real-Time Performance**: Latency < 200ms  
- **Command Accuracy**: ≥ 75% of gestures trigger correct robot responses  
- **Gesture Set**: Minimum of 5 reliably detected gestures  
- **User Testing**: Target satisfaction ≥ 4/5 for intuitiveness and responsiveness  
- **Manual Success Rate**: Tracking success per gesture during trials (e.g., 7/10 success = 70%)
