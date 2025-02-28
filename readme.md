# Gesture Recognition [ Exact Use case to be identified later ]
Team Members:
- Om Samel, ompradee@buffalo.edu
- Chigozie Eke, cmeke@buffalo.edu

---

## Gesture Recognition with a Robotic Arm
We propose to develop a gesture recognition system that detects and classifies hand gestures in real-time using computer vision. The system will serve as a foundational module for controlling robotic systems through natural human gestures. This can later be applied to robotic arms, drones, smart wheelchairs, or warehouse automation.

## Contributions
- Gesture-based control offers an **intuitive** and **hands-free** method of interacting with robotic systems.
- Unlike traditional control systems (buttons, joysticks, or voice commands), gesture recognition enables **natural** interaction.
- This project lays the groundwork for **human-robot collaboration**, **assistive robotics**, and **industrial automation**.
- The project is **scalable** and can be integrated with **ROS-based robotic systems, drones, or AR/VR interfaces** in the future.

## Project Plan
- **Online Materials:**
  - Official **Mediapipe** documentation (Google) for hand tracking  
  - OpenCV tutorials for **computer vision**  
  - Research papers on **gesture-based HRI (Human-Robot Interaction)**  
  - WeBots tutorials for robotic simulation  
- **Textbook References:**
  - *Robotics: Modelling, Planning and Control* – Siciliano & Khatib  
  - *Computer Vision: Algorithms and Applications* – Szeliski (for OpenCV basics)  
- **Development Tools:**
  - **Python, OpenCV, Mediapipe** for gesture recognition  
  - **Jupyter Notebook/PyCharm** for development  
  - **GitHub** for documentation and collaboration  
  - *(Optional)* ROS/Gazebo/WeBots for simulated robotic control

## Milestones/Schedule Checklist
| **Task** | **Assigned To** | **Due Date** | **Status** |
|----------|---------------|-------------|------------|
| Complete this proposal document |  | **Feb 28** |Pending |
| Set up environment (install OpenCV, Mediapipe) |  | **March 3rd** | Pending |
| Explore hardware options to implement the robotic functionality|  | **March 7th** | Pending |
| Study/Explore OpenCV and WeBots (2 days and in conjuction with harware research) |  | **March 7th** | Pending |
| Implement real-time hand tracking |  | **March 12** | Pending |
| Develop a gesture classification model |  | **March 19** | Pending |
| Map gestures to robotic commands (simulation) |  | **March 26** | Pending |
| Create progress report |  | **April 3** | Pending |
| Test and refine gesture recognition accuracy |  | **April 10** | Pending |
| Prepare demo with a simple robotic control application |  | **April 24** | Pending |
| Create final presentation |  | **May 6** | Pending |
| Provide system documentation (README.md) |  | **May 13** | Pending |

## Measures of Success
The system should be able to **accurately detect and classify hand gestures** with at least **90% accuracy** in varied lighting conditions.  
The gestures should trigger corresponding robotic commands (e.g., **"move left" when swiping left**).  
A **demonstration (real-time video or simulation)** should show the system in action.  

### Quantitative Metrics:
- **Gesture Classification Accuracy:** 
  - Achieve at least **90% accuracy** in controlled environments.
  - Maintain at least **85% accuracy** in varying lighting conditions and backgrounds.
- **Latency:** 
  - System should process gestures within **200ms** to allow real-time control.
- **Robotic Response Rate:** 
  - At least **95% of detected gestures** should trigger the intended robotic command successfully.
- **Gesture Set Coverage:** 
  - System must support and correctly classify **at least 5 different gestures** consistently.
- **User Testing Feedback:** 
  - Achieve a **satisfaction rating of 4 out of 5** in user testing for ease of use and responsiveness.
- **Manual Success Tracking:** 
  - We will manually track the number of successful movements. For example, if we wave our hand and the robot successfully follows, that is counted as a success. If this is done successfully **7 out of 10 times**, we will report a **70% success rate** for that specific gesture.


