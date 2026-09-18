from src.face_detector import FaceDetector


def test_model_exists():
    detector = FaceDetector()

    assert detector.detector is not None

    detector.close()
