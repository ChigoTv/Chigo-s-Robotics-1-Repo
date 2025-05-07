# Gesture-Controlled Robot using Webots and Mediapipe

## 🧠 Project Overview

This project enables a differential-drive robot in Webots to be controlled via **hand gestures detected by a webcam**, using **MediaPipe** on one machine and **Webots simulation** on another — connected over a **Wi-Fi network using sockets**.

Gesture recognition is handled on a separate device (Laptop A), which sends commands like `fist`, `open`, `left`, and `right` to a Webots robot simulation running on another machine (Laptop B). The robot responds in real time to these commands.

---

## 🚀 How to Run the Project

### 🔧 Requirements

- Webots installed on Laptop B
- Python 3.8–3.10 on both machines
- `mediapipe`, `opencv-python` installed on Laptop A
- Both machines connected to the **same network** (Wi-Fi or hotspot)

> ⚠️ **IMPORTANT:** To access the dual-laptop gesture control functionality, both devices **must be on the same internet connection**.  
> It is highly recommended to use a **personal hotspot** if your Wi-Fi has firmware-based restrictions or peer-to-peer blockers.

### 📁 File Structure

```
Robotics_Project2025/
├── controllers/
│   └── webots_controller_socket/
│       └── webots_controller_socket.py
├── gesture_sender_client.py (run on Laptop A - Mac)
├── ULTRA_DETAILED_README.md
```

### 🖥 On Laptop B (Windows – Webots Host)

1. Open Webots and load the project world.
2. Ensure your robot’s controller is set to:
   ```
   "webots_controller_socket"
   ```
3. Run simulation (press ▶️).
4. Confirm terminal output:
   ```
   🟢 Listening for gesture sender on port 5050...
   ```

### 💻 On Laptop A (Mac – Gesture Detection)

1. Open Terminal.
2. Navigate to project folder.
3. Update the IP address in `gesture_sender_client.py`:
   ```python
   SERVER_IP = "192.168.x.x"  # ← IP of Laptop B
   ```
4. Run:
   ```bash
   python3 gesture_sender_client.py
   ```

---

## 🎮 Gesture Controls

| Gesture | Action            |
|---------|-------------------|
| ✊ Fist  | Move Forward      |
| ✋ Open  | Move Backward     |
| ↩️ Tilt Left | Turn Left         |
| ↪️ Tilt Right | Turn Right        |

---

## ⌨️ Failsafe Controls via WASD Keyboard Input

In addition to gesture recognition, the system includes a secondary **WASD keyboard control interface** as a fallback mechanism. This ensures that users can still operate the robot in case the gesture detection fails or becomes unresponsive due to lighting, occlusion, or webcam issues.

| Key | Action         |
|-----|----------------|
| W   | Move Forward   |
| A   | Turn Left      |
| S   | Move Backward  |
| D   | Turn Right     |

This dual-control strategy provides both **hands-free control** and **manual override**, improving the robustness and reliability of the system — particularly valuable during demos, testing, or industrial deployments where environmental factors may vary.

---

## 🧪 Example Outputs

- **Console on Laptop B:**
  ```
  📄 Gesture received: fist
  📄 Gesture received: left
  ```

- **Webots Output:**
  Robot drives forward, turns, or stops in sync with gestures.

- **Camera Window on Mac:**
  - Live feed with detected gesture printed on screen.

---

## 🧠 Use Case in Industrial Robotics Integration

This gesture control system demonstrates a practical foundation for **industrial human-robot interaction**, particularly in:

- **Hazardous environments**: Gesture control enables operation of robotic systems in areas with toxic chemicals, heat, or radiation — where direct human control is dangerous.
- **Assembly lines**: Technicians can issue commands quickly without physical interfaces, increasing workflow efficiency.
- **Warehouse automation**: Supervisors can redirect or guide autonomous mobile robots using gestures, even with both hands occupied.
- **Remote operation**: In field or off-site facilities, gesture-controlled systems allow more intuitive long-distance control over maintenance or inspection robots.

This approach supports safer, more intuitive, and contactless robotic control — aligning with trends in **Industry 4.0 and smart manufacturing.**

---

## 📚 References

- [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html)
- [OpenCV](https://opencv.org/)
- [Webots Documentation](https://cyberbotics.com/doc/guide/index)

---

## 🛠️ Future Improvements

- Add additional gestures (e.g., stop, turbo, spin)
- Implement voice control as a fallback
- Build a GUI toggle for switching between WASD and gesture mode
- Add ArUco markers for camera-based position feedback
- Package with Docker or installer for plug-and-play deployment

---

## 🧰 Step-by-Step Beginner Setup Instructions

This section walks through exactly how to prepare and run the system — perfect for someone unfamiliar with robotics or Webots.

### 🔌 Part 1: Setup on Laptop B (Robot Host – Webots, Windows)

#### Step 1: Install Webots
- Download from [https://cyberbotics.com](https://cyberbotics.com)
- Install and run once to complete setup

#### Step 2: Load Project
- Place project files in a local folder
- Launch your `.wbt` file in Webots
- Set robot’s controller to: `webots_controller_socket`

#### Step 3: Run Simulation
- Hit ▶️ in Webots
- Confirm socket listening message in console

### 📷 Part 2: Setup on Laptop A (Gesture Detection – Mac)

#### Step 1: Install Python 3.8–3.10
```bash
python3 --version
```

#### Step 2: Install Required Libraries
```bash
pip3 install mediapipe opencv-python
```

#### Step 3: Connect to Robot
Edit the IP of Laptop B in `gesture_sender_client.py`, then run:
```bash
python3 gesture_sender_client.py
```

---

## ✅ Testing Checklist

| Test | Expected Result |
|------|------------------|
| Webcam opens | Shows “Gesture: ___” |
| Mac console | Shows “📡 Connected…” |
| Windows console | Shows “📄 Gesture received…” |
| Robot | Moves with gestures or WASD |

---
