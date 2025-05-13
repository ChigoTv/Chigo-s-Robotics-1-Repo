
from controller import Robot
import socket
import threading

# Setup socket listener
HOST = '0.0.0.0'   # Listen on all interfaces
PORT = 8080
gesture = "none"

def socket_listener():
    global gesture
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"🟢 Listening for gesture sender on port {PORT}...")

    conn, addr = s.accept()
    print(f"✅ Connected to: {addr}")

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            gesture = data.decode('utf-8').strip()
        except:
            break
    conn.close()

# Start socket in separate thread
threading.Thread(target=socket_listener, daemon=True).start()

# === Webots control logic ===
robot = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getMotor('left wheel motor')
right_motor = robot.getMotor('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

max_speed = 10
turn_speed = 5

print("🚀 Webots controller running (socket mode)")

while robot.step(timestep) != -1:
    print(f"📄 Gesture received: {gesture}")

    if gesture == "fist":
        left_motor.setVelocity(max_speed)
        right_motor.setVelocity(max_speed)
    elif gesture == "open":
        left_motor.setVelocity(-max_speed)
        right_motor.setVelocity(-max_speed)
    elif gesture == "left":
        left_motor.setVelocity(-turn_speed)
        right_motor.setVelocity(turn_speed)
    elif gesture == "right":
        left_motor.setVelocity(turn_speed)
        right_motor.setVelocity(-turn_speed)
    else:
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
