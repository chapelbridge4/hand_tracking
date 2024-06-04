import cv2
import mediapipe as mp

# Initialize video capture
vid = cv2.VideoCapture(0)
vid.set(3, 960)  # Set width
vid.set(4, 720)  # Set height

if not vid.isOpened():
    print("Error: Could not open video source.")
    exit()

# Initialize Mediapipe Hands solution
mphands = mp.solutions.hands
Hands = mphands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.6)
mpdraw = mp.solutions.drawing_utils

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
        for handLm in result.multi_hand_landmarks:
            mpdraw.draw_landmarks(frame, handLm, mphands.HAND_CONNECTIONS)
            for id, lm in enumerate(handLm.landmark):
                h, w, _ = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                cv2.circle(frame, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

    # Display the resulting frame
    cv2.imshow("video", frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy all windows
vid.release()
cv2.destroyAllWindows()