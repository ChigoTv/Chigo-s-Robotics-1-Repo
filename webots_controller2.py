from controller import Robot, Keyboard
import os

# Get the absolute path to gesture.txt
PROJECT_FOLDER = "C:/Users/Chigo/Documents/Robotics_Project2025"
GESTURE_FILE = os.path.join(PROJECT_FOLDER, "gesture.txt")
USE_GESTURES = True

robot = Robot()
keyboard = Keyboard()
timestep = int(robot.getBasicTimeStep())
keyboard.enable(timestep)

left_motor = robot.getMotor('left wheel motor')
right_motor = robot.getMotor('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

max_speed = 10

print("🚀 Webots controller running")
print("📂 Controller looking for gesture.txt at:", GESTURE_FILE)

while robot.step(timestep) != -1:
    gesture = "none"
    key = keyboard.getKey()

    if USE_GESTURES and os.path.exists(GESTURE_FILE):
        try:
            with open(GESTURE_FILE, "r") as f:
                gesture = f.read().strip()
        except:
            print("⚠️ Could not read gesture.txt")

    if USE_GESTURES:
        print(f"📄 Gesture read: {gesture}")
        if gesture == "fist":
            left_motor.setVelocity(max_speed)
            right_motor.setVelocity(max_speed)
        elif gesture == "open":
            left_motor.setVelocity(-max_speed)
            right_motor.setVelocity(-max_speed)
        else:
            left_motor.setVelocity(0.0)
            right_motor.setVelocity(0.0)

    # WASD override
    if key != -1:
        print(f"⌨️ Key pressed: {chr(key)}")
    if key == ord('W'):
        left_motor.setVelocity(-max_speed)
        right_motor.setVelocity(-max_speed)
    elif key == ord('S'):
        left_motor.setVelocity(max_speed)
        right_motor.setVelocity(max_speed)
    elif key == ord('A'):
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(-max_speed)
    elif key == ord('D'):
        left_motor.setVelocity(-max_speed)
        right_motor.setVelocity(0.0)
    elif key == -1 and not USE_GESTURES:
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
