# Gesture-Controlled Robot using Webots and Mediapipe

## 🧠 Project Overview

This project demonstrates a multi-device robotic control system using **hand gestures**. A webcam-powered gesture recognition system on **Laptop A (Mac)** sends real-time commands to a simulated robot in **Webots** running on **Laptop B (Windows)** using a **Wi-Fi socket connection**.

The system enables gesture-based movement:

* ✊ Fist → Move forward
* ✋ Open palm → Move backward
* ↩️ Tilt hand left → Turn left
* ↪️ Tilt hand right → Turn right

A fallback manual control system using **WASD keys** is also built in for robustness. This functionality was implemented for users who are running the full program on one windows computer.

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

* Python 3.8–3.10
* pip-installed:

  * `opencv-python`
  * `mediapipe`

To install Python:
Download from [https://www.python.org/downloads/](https://www.python.org/downloads/)

To install required packages:

```bash
pip3 install opencv-python mediapipe
```

---

### 💻 Laptop B (Webots Simulation - Windows)

* Webots (installed as above)
* Python 3.8–3.10
* Webots Python controller bindings (comes with Webots)

To verify the Python path in Webots:

* Go to: `Tools > Preferences > Python command`
* Set it to your Python 3.8–3.10 interpreter path

---

## 🌐 Network Setup (Critical for Dual-Laptop Functionality)

> ⚠️ **IMPORTANT:** Both laptops **must be on the same network**.

Recommended:

* Use a **personal mobile hotspot** to connect both machines
* Avoid networks with **firmware-based firewalls** or **client isolation**

To find your IP on **Laptop B** (Windows):

```bash
ipconfig
```

Copy the `IPv4 Address` from the wireless section and paste it into the Mac script, gesture1.py, as `SERVER_IP`.

---

## 📁 Project Structure

```
Robotics_Project2025/
├── controllers/
│   ├── webots_controller_socket/
│   │   └── webots_controller.py
│   └── webots_controller2/
│       └── webots_controller2.py
├── gesture_sender_client.py      (Run on Laptop A)
├── gesture_sender2.py            (Run on Windows – self-controlled)
├── gesture.txt                   (Gesture data file for single-laptop mode)

```

---

## 📂 Accessing the Source Code

You can find all the code files used in this project — including both dual-device and single-device modes — inside the **GitHub repository** attached with this project.

> 💡 **Feel free to explore and modify the code for personal use**, testing, and further development!

---

## 🚀 How to Run the Project

### On Laptop B (Windows – Webots for Dual-Laptop Mode)

1. Open Webots and load your world.
2. Set your robot’s controller to:

   ```
   "webots_controller_socket"
   ```
3. Click ▶️ Play to start simulation.
4. You should see:

   ```
   🟢 Listening for gesture sender on port 8080...
   ```

### On Laptop A (Mac – Gesture Sender)

1. In Terminal:

   ```bash
   cd ~/Path/To/Project
   ```
2. Open `gesture_sender_client.py` and set the correct IP:

   ```python
   SERVER_IP = "192.168.x.x"
   ```
3. Run:

   ```bash
   python3 gesture_sender_client.py
   ```

---

## 🖥️ 🧍‍♂️ Self-Running Setup (Single Laptop on Windows)

You can also run this project **entirely on one Windows machine** for testing and development.

### 🔧 Setup:

1. Set your Webots robot controller to:

   ```
   "webots_controller2"
   ```
2. Ensure the project folder has `gesture_sender2.py` and `gesture.txt`.

### ▶️ Run the Following:

* In Webots, start the simulation (this runs `webots_controller2.py`).
* In another terminal window:

  ```bash
  python gesture_sender2.py
  ```

### 💡 Notes:

* This version uses a shared file `gesture.txt` to pass gesture data.
* WASD fallback controls are **also supported** using your keyboard.
* Key Mappings:

  * `W` → Move forward
  * `S` → Move backward
  * `A` → Turn left
  * `D` → Turn right

---

## 🎮 Gesture Controls

| Gesture       | Action        |
| ------------- | ------------- |
| ✊ Fist        | Move Forward  |
| ✋ Open        | Move Backward |
| ↩️ Tilt Left  | Turn Left     |
| ↪️ Tilt Right | Turn Right    |

---

## ⌨️ Failsafe Controls via WASD Keyboard Input

This system includes a built-in **WASD keyboard fallback** to control the robot in case the gesture input fails (e.g., poor lighting, camera issues):

| Key | Action        |
| --- | ------------- |
| W   | Move Forward  |
| A   | Turn Left     |
| S   | Move Backward |
| D   | Turn Right    |

---
## 🖥️ 🧍‍♂️ Self-Running Setup (Single Windows Computer)
You can run the full gesture-controlled robot simulation using just one Windows computer. This is useful for local testing, demos, or if a second device isn't available.

📦 Files Required
Ensure the following files are in your project directory (e.g., C:/Users/YourName/Documents/Robotics_Project2025/):

gesture_sender2.py → Gesture detection script

webots_controller2.py → Webots controller script

gesture.txt → A plain text file that will be automatically created to store gesture states

🧠 How It Works
gesture_sender2.py uses your webcam and MediaPipe to detect hand gestures.

The detected gesture is written to gesture.txt.

webots_controller2.py, running in Webots, reads from gesture.txt and moves the robot accordingly.

If you press W, A, S, or D, manual keyboard control takes over.

🔧 Setup Instructions
1. Set Controller in Webots
Open Webots.

Select your robot.

In the controller field, set the controller to:

nginx
Copy
Edit
webots_controller2
Make sure this points to the file: webots_controller2.py.

2. Install Python Requirements
Ensure you have Python 3.8–3.10 installed.

Install the required Python packages in Command Prompt:

bash
Copy
Edit
pip install opencv-python mediapipe
▶️ Running the Project
Step 1: Start Webots
Open your project world in Webots.

Press the Play button (▶️) to start the simulation.

The robot controller (webots_controller2.py) will begin reading gestures.

You should see messages like:

swift
Copy
Edit
🚀 Webots controller running
📂 Controller looking for gesture.txt at: C:/Users/Chigo/Documents/Robotics_Project2025/gesture.txt
Step 2: Start Gesture Detection
Open a new Command Prompt window and run:

bash
Copy
Edit
cd C:\Users\Chigo\Documents\Robotics_Project2025
python gesture_sender2.py
A webcam window will appear with gesture feedback text like:

makefile
Copy
Edit
Gesture: fist
Press q in the webcam window to quit.

🤖 Gesture-to-Action Mapping
Gesture	Action
✊ Fist	Move Forward
✋ Open	Move Backward
none	Stop

⌨️ Manual WASD Controls (Keyboard Override)
The robot also supports manual override using your keyboard:

Key	Action
W	Move Forward
S	Move Backward
A	Turn Left
D	Turn Right

If you press a key, it takes control over gesture input.

🛠️ Troubleshooting
No gesture detected? Make sure the room is well-lit and your hand is visible to the webcam.

No robot motion? Verify that gesture.txt is being updated. Try printing the file contents.

Controller not working in Webots? Double-check that the controller name matches "webots_controller2" exactly in the Webots robot settings.

Keyboard not responsive? Ensure the Webots simulation window is active and focused.

---

## 🛠️ Future Improvements

* Add gestures for `stop`, `turbo`, or `spin`.
* Integrate voice command fallback.
* GUI switch to toggle gesture/manual mode.
* Deploy on edge device (e.g., Raspberry Pi).
* Incorporate camera tracking via ArUco markers.

---

## 🧠 Use Case in Industrial Robotics Integration

This dual-device gesture control system is a **practical prototype for industrial robotics**. Potential applications include:

* **Remote Hazardous Control**
* **Smart Factories**
* **Warehouse Automation**
* **Hands-Free Robotics** in sterile environments

By enhancing this system with camera tracking, secure communication protocols, and physical robot integration, it forms a solid foundation for intuitive, modern **human-robot interaction** systems in Industry 4.0.

---

## 🧾 Code File Explanations

### 📁 `gesture_sender_client.py` (Mac – Dual Device)

Detects gestures via webcam, uses **MediaPipe**, sends gesture via **TCP** to Windows Webots machine.

### 📁 `webots_controller.py` (Windows – Dual Device)

Socket server receives gestures and drives motors accordingly.

### 📁 `gesture_sender2.py` (Windows – Single Device)

Detects gestures via webcam and writes them to `gesture.txt` file.

### 📁 `webots_controller2.py` (Windows – Single Device)

Reads gestures from `gesture.txt` and moves motors. Supports WASD manual control.

---

## 👥 Authors

* **Chigozie Eke** – Lead Developer, Gesture Control & Robotics Integration
* **Om Samel** – Gesture Control Integration

---
## 📚 References

* [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html)
* [OpenCV](https://opencv.org/)
* [Webots Documentation](https://cyberbotics.com/doc/guide/index)

---
