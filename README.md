Gesture-Controlled Robot using Webots and Mediapipe
🧠 Project Overview
This project demonstrates a multi-device robotic control system using hand gestures. A webcam-powered gesture recognition system on Laptop A (Mac) sends real-time commands to a simulated robot in Webots running on Laptop B (Windows) using a Wi-Fi socket connection.

The system enables gesture-based movement:

✊ Fist → Move forward

✋ Open palm → Move backward

↩️ Tilt hand left → Turn left

↪️ Tilt hand right → Turn right

A fallback manual control system using WASD keys is also built in for robustness.

🖥️ What is Webots?
Webots is an open-source 3D robot simulator used to design, test, and visualize robotic systems in real time.

🔗 Website: https://cyberbotics.com
📄 Documentation: https://cyberbotics.com/doc/guide/index

🧩 How to Install Webots (Laptop B)
Go to the Webots Download Page.

Download the Windows version.

Run the installer and follow the prompts.

After installation, launch Webots and open or create your robot world.

Ensure you configure your robot to use the provided controller webots_controller_socket.

🔧 Project Requirements
💻 Laptop A (Gesture Detection - Mac)
Python 3.8–3.10

pip-installed:

opencv-python

mediapipe

To install Python:
Download from https://www.python.org/downloads/

To install required packages:

bash
Copy
Edit
pip3 install opencv-python mediapipe
💻 Laptop B (Webots Simulation - Windows)
Webots (installed as above)

Python 3.8–3.10

Webots Python controller bindings (comes with Webots)

To verify the Python path in Webots:

Go to: Tools > Preferences > Python command

Set it to your Python 3.8–3.10 interpreter path

🌐 Network Setup (Critical for Dual-Laptop Functionality)
⚠️ IMPORTANT: Both laptops must be on the same network.

Recommended:

Use a personal mobile hotspot to connect both machines

Avoid networks with firmware-based firewalls or client isolation

To find your IP on Laptop B (Windows):

bash
Copy
Edit
ipconfig
Copy the IPv4 Address from the wireless section and paste it into the Mac script as SERVER_IP.

📁 Project Structure
vbnet
Copy
Edit
Robotics_Project2025/
├── controllers/
│   ├── webots_controller_socket/
│   │   └── webots_controller.py
│   └── webots_controller2/
│       └── webots_controller2.py
├── gesture_sender_client.py      (Run on Laptop A)
├── gesture_sender2.py            (Run on Windows – self-controlled)
├── gesture.txt                   (Gesture data file for single-laptop mode)
├── README.md
📂 Accessing the Source Code
You can find all the code files used in this project — including both dual-device and single-device modes — inside the GitHub repository attached with this project.

💡 Feel free to explore and modify the code for personal use, testing, and further development!

🚀 How to Run the Project
On Laptop B (Windows – Webots for Dual-Laptop Mode)
Open Webots and load your world.

Set your robot’s controller to:

arduino
Copy
Edit
"webots_controller_socket"
Click ▶️ Play to start simulation.

You should see:

csharp
Copy
Edit
🟢 Listening for gesture sender on port 8080...
On Laptop A (Mac – Gesture Sender)
In Terminal:

bash
Copy
Edit
cd ~/Path/To/Project
Open gesture_sender_client.py and set the correct IP:

python
Copy
Edit
SERVER_IP = "192.168.x.x"
Run:

bash
Copy
Edit
python3 gesture_sender_client.py
🖥️ 🧍‍♂️ Self-Running Setup (Single Laptop on Windows)
You can also run this project entirely on one Windows machine for testing and development.

🔧 Setup:
Set your Webots robot controller to:

arduino
Copy
Edit
"webots_controller2"
Ensure the project folder has gesture_sender2.py and gesture.txt.

▶️ Run the Following:
In Webots, start the simulation (this runs webots_controller2.py).

In another terminal window:

bash
Copy
Edit
python gesture_sender2.py
💡 Notes:
This version uses a shared file gesture.txt to pass gesture data.

WASD fallback controls are also supported using your keyboard.

Key Mappings:

W → Move forward

S → Move backward

A → Turn left

D → Turn right

🎮 Gesture Controls
Gesture	Action
✊ Fist	Move Forward
✋ Open	Move Backward
↩️ Tilt Left	Turn Left
↪️ Tilt Right	Turn Right

⌨️ Failsafe Controls via WASD Keyboard Input
This system includes a built-in WASD keyboard fallback to control the robot in case the gesture input fails (e.g., poor lighting, camera issues):

Key	Action
W	Move Forward
A	Turn Left
S	Move Backward
D	Turn Right

📚 References
MediaPipe Hands

OpenCV

Webots Documentation

🛠️ Future Improvements
Add gestures for stop, turbo, or spin.

Integrate voice command fallback.

GUI switch to toggle gesture/manual mode.

Deploy on edge device (e.g., Raspberry Pi).

Incorporate camera tracking via ArUco markers.

🧠 Use Case in Industrial Robotics Integration
This dual-device gesture control system is a practical prototype for industrial robotics. Potential applications include:

Remote Hazardous Control

Smart Factories

Warehouse Automation

Hands-Free Robotics in sterile environments

By enhancing this system with camera tracking, secure communication protocols, and physical robot integration, it forms a solid foundation for intuitive, modern human-robot interaction systems in Industry 4.0.

🧾 Code File Explanations
📁 gesture_sender_client.py (Mac – Dual Device)
Detects gestures via webcam, uses MediaPipe, sends gesture via TCP to Windows Webots machine.

📁 webots_controller.py (Windows – Dual Device)
Socket server receives gestures and drives motors accordingly.

📁 gesture_sender2.py (Windows – Single Device)
Detects gestures via webcam and writes them to gesture.txt file.

📁 webots_controller2.py (Windows – Single Device)
Reads gestures from gesture.txt and moves motors. Supports WASD manual control.

👥 Authors
Chigozie Eke – Lead Developer, Gesture Control & Robotics Integration

Om Samel – Gesture Control Integration
