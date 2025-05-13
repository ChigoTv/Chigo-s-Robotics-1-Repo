import cv2
import mediapipe as mp
import socket
import time

SERVER_IP ="172.20.10.3"  # ← CHANGE THIS TO Laptop B's IP
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_IP, PORT))
print(f"📡 Connected to Webots controller at {SERVER_IP}:{PORT}")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

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
            wrist_x = handLms.landmark[0].x
            index_tip_x = handLms.landmark[8].x
            thumb_tip_x = handLms.landmark[4].x

            if abs(thumb_tip_x - index_tip_x) < 0.05:
                gesture = "fist"
            else:
                if wrist_x - index_tip_x > 0.1:
                    gesture = "left"
                elif index_tip_x - wrist_x > 0.1:
                    gesture = "right"
                else:
                    gesture = "open"

    s.sendall(gesture.encode('utf-8'))
    cv2.putText(img, f"Gesture: {gesture}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Gesture Sender", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

s.close()
cap.release()
cv2.destroyAllWindows()