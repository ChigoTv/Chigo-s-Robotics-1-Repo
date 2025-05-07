# Gesture-Controlled Robot using Webots and Mediapipe

## 🧠 Project Overview

This project demonstrates a multi-device robotic control system using **hand gestures**. A webcam-powered gesture recognition system on **Laptop A (Mac)** sends real-time commands to a simulated robot in **Webots** running on **Laptop B (Windows)** using a **Wi-Fi socket connection**. 

The system enables gesture-based movement:
- ✊ Fist → Move forward
- ✋ Open palm → Move backward
- ↩️ Tilt hand left → Turn left
- ↪️ Tilt hand right → Turn right

A fallback manual control system using **WASD keys** is also built in for robustness.

---

## 🖥️ What is Webots?

**Webots** is an open-source 3D robot simulator used to design, test, and visualize robotic systems in real time.

🔗 Website: [https://cyberbotics.com](https://cyberbotics.com)  
📄 Documentation: [https://cyberbotics.com/doc/guide/index](https://cyberbotics.com/doc/guide/index)

### 🧩 How to Install Webots (Laptop B)

1. Go to the [Webots Download Page](https://cyberbotics.com/#download).
2. Download the **Windows version**.
3. Run the installer and follow the prompts.
4. After installation, launch Webots and open or create your robot world.
5. Ensure you configure your robot to use the provided controller `webots_controller_socket`.

---

## 🔧 Project Requirements

### 💻 Laptop A (Gesture Detection - Mac)

- Python 3.8–3.10
- pip-installed:
  - `opencv-python`
  - `mediapipe`

To install Python:  
Download from [https://www.python.org/downloads/](https://www.python.org/downloads/)

To install required packages:
```bash
pip3 install opencv-python mediapipe
```

---

### 💻 Laptop B (Webots Simulation - Windows)

- Webots (installed as above)
- Python 3.8–3.10
- Webots Python controller bindings (comes with Webots)

To verify the Python path in Webots:
- Go to: `Tools > Preferences > Python command`
- Set it to your Python 3.8–3.10 interpreter path

---

## 🌐 Network Setup (Critical for Dual-Laptop Functionality)

> ⚠️ **IMPORTANT:** Both laptops **must be on the same network**.

Recommended:
- Use a **personal mobile hotspot** to connect both machines
- Avoid networks with **firmware-based firewalls** or **client isolation**

To find your IP on **Laptop B** (Windows):
```bash
ipconfig
```
Copy the `IPv4 Address` from the wireless section and paste it into the Mac script as `SERVER_IP`.

---

## 📁 Project Structure

```
Robotics_Project2025/
├── controllers/
│   └── webots_controller_socket/
│       └── webots_controller_socket.py
├── gesture_sender_client.py  (Run on Laptop A)
├── README.md
```

---

## 🚀 How to Run the Project

### On Laptop B (Windows – Webots)

1. Open Webots and load your world.
2. Make sure your robot’s controller is set to:
   ```
   "webots_controller_socket"
   ```
3. Click ▶️ Play to start simulation.
4. You should see in the terminal:
   ```
   🟢 Listening for gesture sender on port 5050...
   ```

### On Laptop A (Mac – Gesture Sender)

1. Open Terminal and navigate to the project folder:
   ```bash
   cd ~/Path/To/Project
   ```
2. Open `gesture_sender_client.py` and set the correct IP:
   ```python
   SERVER_IP = "192.168.x.x"  # Replace with IP of Laptop B
   ```
3. Run:
   ```bash
   python3 gesture_sender_client.py
   ```
4. The camera window will open, and gestures will begin sending to Laptop B.

---

## 🎮 Gesture Controls

| Gesture | Action        |
|---------|---------------|
| ✊ Fist  | Move Forward  |
| ✋ Open  | Move Backward |
| ↩️ Tilt Left | Turn Left    |
| ↪️ Tilt Right | Turn Right   |

---

## ⌨️ Failsafe Controls via WASD Keyboard Input

This system includes a built-in **WASD keyboard fallback** to control the robot in case the gesture input fails (e.g., poor lighting, camera issues):

| Key | Action         |
|-----|----------------|
| W   | Move Forward   |
| A   | Turn Left      |
| S   | Move Backward  |
| D   | Turn Right     |

---

## 📚 References

- [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html)
- [OpenCV](https://opencv.org/)
- [Webots Documentation](https://cyberbotics.com/doc/guide/index)

---

## 🛠️ Future Improvements

- Add gestures for `stop`, `turbo`, or `spin`.
- Integrate voice command fallback.
- GUI switch to toggle gesture/manual mode.
- Deploy on edge device (e.g., Raspberry Pi).
- Incorporate camera tracking via ArUco markers.

---

## 🧠 Use Case in Industrial Robotics Integration

This dual-device gesture control system is a **practical prototype for industrial robotics**. Potential applications include:

- **Remote Hazardous Control**: Operators can control robots in chemical plants, nuclear facilities, or firefighting scenarios with gestures — avoiding danger.
- **Smart Factories**: Supervisors can redirect robots mid-task using hand signals, reducing dependence on physical terminals.
- **Warehouse Automation**: Workers can reroute AGVs while holding materials.
- **Hands-Free Robotics**: Useful in sterile environments (labs, cleanrooms) where touch interfaces are impractical.

By enhancing this system with camera tracking, secure communication protocols, and physical robot integration, it forms a solid foundation for intuitive, modern **human-robot interaction** systems in Industry 4.0.

---

## 🧾 Code File Explanations

### 📁 `gesture_sender_client.py` (Run on Laptop A - Mac)

This Python script uses a webcam to detect hand gestures using **MediaPipe**, classifies them, and sends the result over a **socket connection** to the Webots controller on another laptop.

**Key Steps:**
- `cv2.VideoCapture(0)` opens the webcam.
- `mediapipe.solutions.hands` is used to detect hand landmarks.
- Each frame is processed to determine hand gesture:
  - If the **thumb and index finger are close**, it's a `"fist"` (move forward).
  - If the hand is **tilted left**, it's `"left"`.
  - If tilted right, `"right"`.
  - Else it's considered `"open"` (move backward).
- The classified gesture is **sent over a TCP socket** to Laptop B (Webots).
- OpenCV shows a window with live video and current gesture label.
- Quitting the program (`q` key) will close the connection and camera.

---

### 📁 `webots_controller.py` (Run on Laptop B - Windows)

This script runs as a **Webots controller**, receiving gestures from Laptop A and commanding the simulated robot accordingly.

**Key Sections:**
- A **socket server** listens on port `8080` for gesture data sent from `gesture_sender_client.py`.
- A separate **thread** handles incoming socket data so it doesn't block the robot's control loop.
- The robot uses Webots API calls:
  - `robot.getMotor(...)` grabs the left and right motors.
  - `motor.setVelocity(...)` sets the wheel speeds based on the gesture.

**Gesture-to-Action Mapping:**
- `"fist"` → Move forward (`+speed` on both wheels)
- `"open"` → Move backward (`-speed` on both wheels)
- `"left"` → Rotate left (left wheel backward, right wheel forward)
- `"right"` → Rotate right (left wheel forward, right wheel backward)
- `"none"` or unrecognized → Stop (set velocity to `0.0`)

This controller logic ensures real-time, responsive robot motion based on socket-fed gestures.

---

## 👥 Authors

- Chigozie Eke (Lead Developer, Gesture Control & Robotics Integration)
- [Team Member Name] – [Role, if applicable]
