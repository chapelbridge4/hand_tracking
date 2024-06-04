import cv2

# List available video capture devices
def list_cameras():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

print("Available camera indices:", list_cameras())

# Try using the available camera indices
for index in list_cameras():
    print(f"Trying camera index {index}")
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"Camera index {index} is not available.")
        continue
    
    ret, frame = cap.read()
    if ret:
        cv2.imshow(f"Camera index {index}", frame)
        if cv2.waitKey(3000) & 0xFF == ord('q'):
            break
        cv2.destroyAllWindows()
    cap.release()
