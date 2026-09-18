import cv2
import mediapipe as mp
import math

# Initialize MediaPipe face mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False)

# Haircut suggestions dictionary
haircut_suggestions = {
    "oval": ["Layered Cut", "Bob Cut", "Slick Back", "Side Part"],
    "round": ["Pompadour", "Undercut", "High Volume Top", "Side Bangs"],
    "square": ["Soft Waves", "Side Swept", "Textured Crop", "Fringe"],
    "heart": ["Long Layers", "Pixie Cut", "Side Fringe", "Chin-length Bob"],
    "diamond": ["Messy Fringe", "Shaggy Cut", "Shoulder Waves"]
}

def detect_face_shape(landmarks, img_width, img_height):
    def get_point(idx):
        return (int(landmarks[idx].x * img_width), int(landmarks[idx].y * img_height))

    chin = get_point(152)
    left_cheek = get_point(234)
    right_cheek = get_point(454)
    forehead = get_point(10)

    width = math.dist(left_cheek, right_cheek)
    height = math.dist(forehead, chin)

    if abs(width - height) < 30:
        return "round"
    elif height > width:
        return "oval"
    elif width > height * 1.2:
        return "square"
    elif forehead[1] < left_cheek[1] and chin[1] > right_cheek[1]:
        return "heart"
    else:
        return "diamond"

# Start webcam
cap = cv2.VideoCapture(0)
captured = False

print("Press 'c' to capture the image and analyze face shape.")
print("Press 'q' to quit without capturing.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            for lm in face_landmarks.landmark:
                x = int(lm.x * frame.shape[1])
                y = int(lm.y * frame.shape[0])
                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

    cv2.imshow("Live Face Capture", frame)

    key = cv2.waitKey(1)
    if key == ord('c'):  # Capture image on 'c'
        if results.multi_face_landmarks:
            captured = True
            face_landmarks = results.multi_face_landmarks[0]
            shape = detect_face_shape(face_landmarks.landmark, frame.shape[1], frame.shape[0])
            suggestions = haircut_suggestions.get(shape, ["No suggestions available"])

            print(f"\nDetected Face Shape: {shape.capitalize()}")
            print("Suggested Haircuts:")
            for cut in suggestions:
                print(f" - {cut}")

            # Show result on image
            cv2.putText(frame, f"Face Shape: {shape}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow("Result", frame)
            cv2.waitKey(0)
        else:
            print("No face detected.")
        break

    elif key == ord('q'):
        print("Quitting without capture.")
        break

cap.release()
cv2.destroyAllWindows()