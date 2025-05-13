import cv2
import mediapipe as mp
import os
import time

# Get absolute path to gesture.txt
PROJECT_FOLDER = "C:/Users/Chigo/Documents/Robotics_Project2025"
GESTURE_FILE = os.path.join(PROJECT_FOLDER, "gesture.txt")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

print("🎥 Gesture sender started...")

while True:
    success, img = cap.read()
    if not success:
        continue

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    gesture = "none"

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
            thumb_tip = handLms.landmark[4].x
            index_tip = handLms.landmark[8].x

            if abs(thumb_tip - index_tip) < 0.05:
                gesture = "fist"
            else:
                gesture = "open"

    # ✅ Write gesture to file
    with open(GESTURE_FILE, "w") as f:
        f.write(gesture)

    cv2.putText(img, f"Gesture: {gesture}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Gesture Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
