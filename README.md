# Face Detection with OpenCV

A simple real-time face detection project built with Python and OpenCV.

The program uses your webcam to detect human faces in real time and draws a green rectangle around each detected face.

## Features

Real-time face detection using a webcam

Uses OpenCV's Haar Cascade classifier

Displays the number of detected faces

Mirrors the webcam image for a natural camera experience

Press Q to exit the application

## Technologies

Python

OpenCV

NumPy

Haar Cascade Classifier

## Project Structure
```text
Face-Detection/
│
├── Face_detection.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

Make sure you have Python installed.

The project dependencies are listed in `requirements.txt`.

## Installation

Clone the repository:
```text
git clone https://github.com/Maged-Shabaka/Face-Detection.git
```

Go to the project directory:
```text
cd Face-Detection
```

Create a virtual environment:
```text
python -m venv .venv
```

Activate the virtual environment on Windows PowerShell:
```text
.\.venv\Scripts\Activate.ps1
```

Install the required packages:
```text
python -m pip install -r requirements.txt
```
Run the Project

Run:
```text
python Face_detection.py
```

Your webcam should open automatically.

The program will detect faces and display a green rectangle around each detected face.

Press:
```text
Q
```

to close the application.

## How It Works

The project uses OpenCV's **Haar Cascade Classifier** for face detection.

The webcam captures frames continuously. Each frame is converted from BGR to grayscale, then the Haar Cascade classifier searches for faces.

When a face is detected, the program draws a rectangle around it and displays the total number of detected faces.

## Example

When a face is detected, the program displays a green rectangle around the face and shows the number of detected faces at the top of the window.

Author

Maged Shabaka
