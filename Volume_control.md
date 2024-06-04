# Hand Gesture Volume Control

This Python script uses OpenCV, MediaPipe, and osascript to control the system volume with hand gestures captured from a webcam.

## Libraries Used

- `cv2`: OpenCV library for real-time computer vision.
- `mediapipe`: MediaPipe is a cross-platform framework for building multimodal applied machine learning pipelines.
- `numpy`: A library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
- `osascript`: This library allows you to execute osascript commands, which are a way to control your Mac OS with scripts.

## Code Explanation

1. **Video Capture Initialization**: The script starts by initializing a video capture object with a width of 960 pixels and a height of 720 pixels.

2. **MediaPipe Hands Initialization**: The script then initializes a MediaPipe Hands object with a maximum of 2 hands, a minimum detection confidence of 0.7, and a minimum tracking confidence of 0.6.

3. **Volume Control Function**: The `control_volume` function is defined to control the system volume based on the vertical movement of the index finger. If the vertical movement of the index finger exceeds 10 pixels (upwards or downwards), it will be considered significant enough to trigger a volume change.

4. **Main Loop**: The script enters a main loop where it reads frames from the video capture, processes them with MediaPipe Hands, and controls the volume based on the hand landmarks. The processed frames are displayed in a window.

5. **Exit Condition**: The loop continues until the 'q' key is pressed. After that, the video capture is released and all windows are destroyed.

Please note that this script is designed to work on a Mac OS, as it uses the `osascript` library for volume control. For other operating systems, you would need to use a different method for volume control.
