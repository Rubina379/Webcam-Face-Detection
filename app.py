import cv2
from datetime import datetime
import os

# --- Load Haar Cascade ---
haar_cascade_path = 'haar_face.xml'
if not os.path.exists(haar_cascade_path):
    print("Custom Haar cascade not found. Using OpenCV default.")
    haar_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(haar_cascade_path)

# --- Initialize Webcam ---
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("❌ Cannot access webcam. Please check your device.")

print("✅ Webcam started. Press 'q' to quit the application.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Failed to read frame from webcam.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cv2.putText(frame, timestamp, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    cv2.imshow('Webcam Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("👋 Exiting...")
        break

cap.release()
cv2.destroyAllWindows()
