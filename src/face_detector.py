from pathlib import Path

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "face_landmarker.task"


class FaceDetector:
    """Detects facial landmarks using MediaPipe Face Landmarker."""

    def __init__(self):
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Face Landmarker model not found: {MODEL_PATH}"
            )

        base_options = python.BaseOptions(
            model_asset_path=str(MODEL_PATH)
        )

        options = vision.FaceLandmarkerOptions(
            base_options=base_options,
            running_mode=vision.RunningMode.IMAGE,
            num_faces=1,
        )

        self.detector = vision.FaceLandmarker.create_from_options(
            options
        )

    def detect(self, image):
        """
        Detect facial landmarks in an image.

        Args:
            image: MediaPipe Image object.

        Returns:
            MediaPipe FaceLandmarkerResult.
        """
        return self.detector.detect(image)

    def close(self):
        """Release the MediaPipe detector."""
        self.detector.close()
