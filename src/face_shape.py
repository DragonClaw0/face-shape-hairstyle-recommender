import math


class FaceShapeAnalyzer:
    """Analyzes facial landmarks and determines an approximate face shape."""

    def __init__(self):
        self.shape_names = [
            "oval",
            "round",
            "square",
            "heart",
            "diamond"
        ]

    @staticmethod
    def distance(point1, point2):
        """Calculate the distance between two points."""
        return math.dist(point1, point2)

    @staticmethod
    def get_point(landmarks, index, image_width, image_height):
        """Convert a MediaPipe landmark into image coordinates."""
        landmark = landmarks[index]

        return (
            landmark.x * image_width,
            landmark.y * image_height
        )

    def calculate_measurements(
        self,
        landmarks,
        image_width,
        image_height
    ):
        """
        Calculate basic facial measurements.

        MediaPipe landmark indexes:
        10  -> forehead
        152 -> chin
        234 -> left cheek
        454 -> right cheek
        """

        forehead = self.get_point(
            landmarks,
            10,
            image_width,
            image_height
        )

        chin = self.get_point(
            landmarks,
            152,
            image_width,
            image_height
        )

        left_cheek = self.get_point(
            landmarks,
            234,
            image_width,
            image_height
        )

        right_cheek = self.get_point(
            landmarks,
            454,
            image_width,
            image_height
        )

        face_width = self.distance(
            left_cheek,
            right_cheek
        )

        face_height = self.distance(
            forehead,
            chin
        )

        return {
            "face_width": face_width,
            "face_height": face_height,
            "width_height_ratio": face_width / face_height
            if face_height != 0 else 0
        }

    def detect_shape(
        self,
        landmarks,
        image_width,
        image_height
    ):
        """
        Determine the approximate face shape.

        Returns:
            str: Detected face shape.
        """

        measurements = self.calculate_measurements(
            landmarks,
            image_width,
            image_height
        )

        width = measurements["face_width"]
        height = measurements["face_height"]

        ratio = measurements["width_height_ratio"]

        # Approximately equal width and height
        if 0.90 <= ratio <= 1.10:
            return "round"

        # Face is noticeably longer than it is wide
        elif ratio < 0.90:
            return "oval"

        # Face is considerably wider than it is long
        elif ratio > 1.20:
            return "square"

        # Intermediate proportions
        elif 1.10 < ratio <= 1.20:
            return "diamond"

        return "oval"
