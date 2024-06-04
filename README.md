# Hand Gesture

This repository contains three Python scripts that use OpenCV and MediaPipe to control the system volume with hand gestures captured from a webcam. The scripts are:

1. `volume_control.py`
2. `main.py`
3. `test_camera.py`

## Libraries Used

- `cv2`: OpenCV library for real-time computer vision.
- `mediapipe`: MediaPipe is a cross-platform framework for building multimodal applied machine learning pipelines.
- `numpy`: A library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
- `osascript`: This library allows you to execute osascript commands, which are a way to control your Mac OS with scripts.

## Code Explanation

### volume_control.py

This script controls the system volume based on the vertical movement of the index finger. If the vertical movement of the index finger exceeds 10 pixels (upwards or downwards), it will be considered significant enough to trigger a volume change.

### main.py

This script is similar to `volume_control.py` but without the volume control part. It captures hand gestures from a webcam and processes them using MediaPipe.

### test_camera.py

This script checks which camera is being used and its index. It's useful for setups where multiple cameras might be connected to the system.

Please note that these scripts are designed to work on a Mac OS, as they use the `osascript` library for volume control. For other operating systems, you would need to use a different method for volume control.
