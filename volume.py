import cv2
import mediapipe as mp
import numpy as np
import osascript

# Initialize video capture
vid = cv2.VideoCapture(1)
vid.set(3, 960)  # Set width
vid.set(4, 720)  # Set height

if not vid.isOpened():
    print("Error: Could not open video source.")
    exit()

# Initialize Mediapipe Hands solution
mphands = mp.solutions.hands
Hands = mphands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.6)
mpdraw = mp.solutions.drawing_utils

# Global variable for volume control
prev_tip_pos = 0

def control_volume(hand_landmarks):
    global prev_tip_pos

    for id, lm in enumerate(hand_landmarks.landmark):
        h, w, _ = frame.shape
        cx, cy = int(lm.x * w), int(lm.y * h)
        # Detect tip of index finger (tip of finger is index 8)
        if id == 8:
            if prev_tip_pos == 0:
                prev_tip_pos = cy
            else:
                # Calculate difference in y position
                delta_y = cy - prev_tip_pos
                # Define a threshold for finger movement the vertical movement of the index finger exceeds 10 pixels (upwards or downwards),
                # it will be considered significant enough to trigger a volume change.
                threshold = 10
                if delta_y < -threshold:
                    # Increase volume
                    osascript.osascript("set volume output volume (output volume of (get volume settings) + 10)")
                elif delta_y > threshold:
                    # Decrease volume
                    osascript.osascript("set volume output volume (output volume of (get volume settings) - 10)")
                # Update previous tip position
                prev_tip_pos = cy

while True:
    success, frame = vid.read()
    if not success:
        print("Error: Could not read frame.")
        break

    # Convert the frame to RGB
    RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Mediapipe Hands
    result = Hands.process(RGBframe)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mpdraw.draw_landmarks(frame, hand_landmarks, mphands.HAND_CONNECTIONS)
            control_volume(hand_landmarks)

    # Display the resulting frame
    cv2.imshow("video", frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy all windows
vid.release()
cv2.destroyAllWindows()
