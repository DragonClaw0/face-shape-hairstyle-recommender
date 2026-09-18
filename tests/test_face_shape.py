from src.face_shape import FaceShapeAnalyzer


class MockLandmark:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def create_landmarks():
    """
    Create a minimal set of mock landmarks
    required by FaceShapeAnalyzer.

    Landmark indexes used:
    10  -> forehead
    152 -> chin
    234 -> left cheek
    454 -> right cheek
    """

    landmarks = [
        MockLandmark(0, 0)
        for _ in range(455)
    ]

    # Forehead
    landmarks[10] = MockLandmark(0.5, 0.2)

    # Chin
    landmarks[152] = MockLandmark(0.5, 0.8)

    # Left cheek
    landmarks[234] = MockLandmark(0.25, 0.5)

    # Right cheek
    landmarks[454] = MockLandmark(0.75, 0.5)

    return landmarks


def test_measurements():
    analyzer = FaceShapeAnalyzer()

    landmarks = create_landmarks()

    measurements = analyzer.calculate_measurements(
        landmarks,
        1000,
        1000
    )

    assert measurements["face_width"] > 0
    assert measurements["face_height"] > 0
    assert measurements["width_height_ratio"] > 0


def test_face_shape_detection():
    analyzer = FaceShapeAnalyzer()

    landmarks = create_landmarks()

    shape = analyzer.detect_shape(
        landmarks,
        1000,
        1000
    )

    assert shape in [
        "oval",
        "round",
        "square",
        "heart",
        "diamond"
    ]
