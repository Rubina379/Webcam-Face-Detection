import cv2
import streamlit as st
from datetime import datetime
import os

# --- Streamlit UI Setup ---
st.set_page_config(page_title="Face Detection App", layout="wide")
st.title("📸 Real-Time Face Detection")
st.sidebar.header("Detection Info")

# --- Load Haar Cascade ---
haar_cascade_path = 'haar_face.xml'
if not os.path.exists(haar_cascade_path):
    st.warning("Custom Haar cascade not found. Using OpenCV default.")
    haar_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(haar_cascade_path)

# --- Webcam Start ---
run = st.checkbox("Start Webcam")
save_faces = st.sidebar.checkbox("Save Detected Faces")

FRAME_WINDOW = st.image([])

if run:
    cap = cv2.VideoCapture(0)
    st.sidebar.success("Webcam is running...")

    while run:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to read frame from webcam.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        face_count = len(faces)
        st.sidebar.metric("Faces Detected", face_count)

        for i, (x, y, w, h) in enumerate(faces):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cv2.putText(frame, timestamp, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

            if save_faces:
                face_img = frame[y:y+h, x:x+w]
                filename = f"face_{i}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                cv2.imwrite(filename, face_img)

        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    cap.release()
else:
    st.info("Check the box above to start webcam.")

``
