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
| Develop a gesture classification model                        | Om                   | March 19     | ⏳ Not Started    |
| Map gestures to robotic commands in simulation                | Chigozie             | March 26     | ⏳ Not Started    |
| Create progress report                                         | Both                 | April 3      | ✅ **This File**  |
| Test and refine gesture recognition accuracy                  | Both                 | April 10     | ⏳ Not Started    |
| Prepare demo with robotic control application (simulated)     | Both                 | April 24     | ⏳ Not Started    |
| Create final presentation                                     | Both                 | May 6        | ⏳ Not Started    |
| Provide system documentation (README.md)                      | Both                 | May 13       | ⏳ Not Started    |

---

## 📏 Measures of Success  
The system will be evaluated on the following criteria:

- **Gesture Classification Accuracy**: ≥ 75% in varied conditions  
- **Real-Time Performance**: Latency < 200ms  
- **Command Accuracy**: ≥ 75% of gestures trigger correct robot responses  
- **Gesture Set**: Minimum of 5 reliably detected gestures  
- **User Testing**: Target satisfaction ≥ 4/5 for intuitiveness and responsiveness  
- **Manual Success Rate**: Tracking success per gesture during trials (e.g., 7/10 success = 70%)
