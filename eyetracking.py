import cv2
import mediapipe as mp

class EyeTracker:
    def __init__(self):
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

    def track(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.face_mesh.process(rgb)

        if result.multi_face_landmarks:
            for face in result.multi_face_landmarks:
                h, w, _ = frame.shape
                for idx in [474, 475, 476, 477]:  # Iris landmarks
                    x = int(face.landmark[idx].x * w)
                    y = int(face.landmark[idx].y * h)
                    cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)
        return frame
