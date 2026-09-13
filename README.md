# Gesture Board

An interactive Python program that lets you draw and write using hand gestures.

## Live demo

https://youtu.be/-oaikJCR6ec

## Overview

The Hand-Controlled Drawing Board is an interactive Python program that allows users to create drawings and write text using hand gestures. By tracking the movement of the user's hand via computer vision, the program provides an interface for drawing without a mouse or stylus.

## Features

- **Hand tracking** — uses computer vision (OpenCV + MediaPipe) to detect and track hand movements in real time.
- **Gesture-based actions:**
  - One finger raised — freely write or draw on the virtual canvas.
  - Two fingers raised — cycle through a color palette by moving the hand horizontally.
  - Five fingers raised — clear the entire canvas.
- **Canvas interaction** — a virtual drawing surface where lines, shapes, and text follow hand movement, in the currently selected color.

## Tech stack

- Python
- OpenCV
- MediaPipe (hand tracking, via `HandModule.py`)
- NumPy

## Setup

```bash
git clone https://github.com/D-Majumder/gesture-board.git
cd gesture-board
pip install opencv-python numpy mediapipe
python DrawingBoard.py
```

## License

This project is licensed under the **GNU General Public License v3.0**. See [LICENSE](./LICENSE) for the full text.
