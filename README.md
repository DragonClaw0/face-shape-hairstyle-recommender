# Face Shape Detection & Haircut Recommendation System

A computer-vision tool that detects a person's face shape (oval, round,
square, heart, or diamond) from a webcam feed or a static photo using
**MediaPipe Face Mesh**, and recommends haircuts suited to that face shape.

## Features

- Real-time facial landmark detection via a webcam feed
- Static-image analysis mode (no camera required — useful for grading /
  headless environments)
- Geometric face-shape classification based on facial landmark distances
- Curated haircut suggestions for each detected face shape
- Saves an annotated result image to the `outputs/` folder

## Project Structure

```
FaceShapeHairstyle/
│
├── models/
│   └── face_landmarker.task
│
├── src/
│   ├── __init__.py
│   ├── Main.py
│   ├── face_detector.py
│   ├── face_shape.py
│   └── hairstyle_recommender.py
│
├── tests/
│   ├── test_face_detector.py
│   ├── test_face_shape.py
│   └── test_recommender.py
│
├── requirements.txt
├── .gitignore
└── README.md

```

## Project Architecture

                    ┌─────────────────┐
                    │   Input Image   │
                    │   / Webcam      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Face Detector   │
                    │   MediaPipe     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Face Shape      │
                    │ Analyzer        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Face Shape      │
                    │ Classification  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Hairstyle       │
                    │ Recommender     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Recommendations │
                    └─────────────────┘


## Requirements

- Python 3.9 – 3.11 (MediaPipe does not yet support every Python version;
  3.10 is recommended)
- A webcam (only needed for `--mode webcam`)
- OS: Windows, macOS, or Linux with a display (webcam mode) — image mode
  can run on a headless server / CI machine

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

## 2. Create and Activate a Virtual Environment (recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Project

### Option A — Webcam Mode (interactive, opens a live camera window)

```bash
python main.py --mode webcam
```

Controls while the webcam window is open:
- Press **`c`** to capture the current frame and analyze your face shape
- Press **`q`** to quit without capturing

The result (detected face shape + haircut suggestions) is printed to the
terminal, and an annotated snapshot is saved automatically to `outputs/`.

### Option B — Image Mode (no webcam needed, fully scriptable)

```bash
python main.py --mode image --image sample_images/your_photo.jpg
```

Add `--no-window` to skip the on-screen preview entirely (useful when
running on a machine without a display, e.g. a CI server or SSH session):

```bash
python main.py --mode image --image sample_images/your_photo.jpg --no-window
```

### Example Output

```
Detected Face Shape: Oval
Suggested Haircuts:
 - Layered Cut
 - Bob Cut
 - Slick Back
 - Side Part

Annotated result saved to: outputs/result_oval_20260917_101530.jpg
```

## How It Works

1. **Face landmark detection** — MediaPipe's Face Mesh model locates 468
   3D facial landmarks in the input frame/image.
2. **Geometric measurement** — Four key landmarks (forehead, chin, left
   cheek, right cheek) are used to compute the face's width and height.
3. **Shape classification** — A simple rule-based heuristic compares the
   width-to-height ratio and vertical landmark positions to classify the
   face as oval, round, square, heart, or diamond.
4. **Recommendation** — The classified shape is looked up in a static
   dictionary of haircut suggestions, which is printed to the console and
   drawn onto the output image.

## Troubleshooting

- **`ImportError: No module named mediapipe`** — Make sure your virtual
  environment is activated and `pip install -r requirements.txt` completed
  without errors. MediaPipe wheels are only published for specific Python
  versions; if installation fails, switch to Python 3.10.
- **Webcam does not open / `could not access the webcam`** — Check that no
  other application is using the camera, and that your OS has granted
  camera permissions to your terminal. As a fallback, use `--mode image`.
- **No display available (SSH / headless server)** — Use
  `--mode image --image <path> --no-window`.

## License

This project is released for academic/educational submission purposes.
