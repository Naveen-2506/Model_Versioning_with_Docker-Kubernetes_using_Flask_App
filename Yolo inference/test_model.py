import cv2
import requests
import base64
from YoloDetector import YoloDetector

# Define the API endpoints for YOLO files
cfg_url = 'http://localhost:80/api/cfg'
weights_url = 'http://localhost:80/api/weights'

# Function to decode Base64 content
def decode_content(encoded_content):
    decoded_data = base64.b64decode(encoded_content)
    return decoded_data

# Download YOLO files from the API
cfg_content = requests.get(cfg_url).text
weights_content = requests.get(weights_url).text

# Decode the downloaded files
yolo_cfg = decode_content(cfg_content)
yolo_weights = decode_content(weights_content)

# Initialize the YOLO detector with the decoded files
detector = YoloDetector(yolo_cfg, yolo_weights, ["vehicle", "small_vehicle", "number_plate", "unique"])

cap = cv2.VideoCapture("video/loading.mp4")
videosave = cv2.VideoWriter('2.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 3, (640, 360))
ret, frame = cap.read()
ft = 120

def draw_on_frame(frame, results):
    for cls, objs in results.items():
        for x1, y1, x2, y2 in objs:
            print(x1, y1, x2, y2, '---------', cls)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255))
            cv2.putText(frame, cls, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), thickness=2)
    return frame

while cap.isOpened():
    ret, frame = cap.read()
    ret, frame = cap.read()
    ret, frame = cap.read()
    ret, frame = cap.read()
    ret, frame = cap.read()
    ret, frame = cap.read()
    ret, frame = cap.read()
    results = detector.detect(frame, conf=0.2)
    print(results)
    frame = draw_on_frame(frame, results)
    frame = cv2.resize(frame, None, fx=0.4, fy=0.4)
    print(frame.shape)
    videosave.write(frame)
    cv2.imshow("frame", frame)
    key = cv2.waitKey(ft) & 0xFF
    if key == ord('q'):
        break

cap.release()
videosave.release()
cv2.destroyAllWindows()
