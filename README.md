# Webcam Face Detection 🎥🧠

A simple Python script that uses OpenCV to perform real-time face detection from your webcam using Haar Cascade classifiers.

## Features

- Detects faces in real-time using your webcam
- Draws bounding boxes around detected faces
- Uses OpenCV’s pre-trained Haar Cascade model
- Lightweight and easy to run

## Requirements

- Python 3.6+
- OpenCV

Install dependencies:
```bash
pip install opencv-python

## How to Run
1. Clone the repository or download the script:

  ```bash
  git clone https://github.com/your-username/webcam-face-detection.git
  cd webcam-face-detection

2. Run the script
  ```bash
  python face_detection.py

3. Press q to quit the webcam window.

## Project Structure

webcam-face-detection/
├── face_detection.py
└── README.md

## Notes
- Make sure your webcam is connected and accessible.
- If you encounter a camera error, try changing the camera index in cv2.VideoCapture(0) to cv2.VideoCapture(1) or higher.
