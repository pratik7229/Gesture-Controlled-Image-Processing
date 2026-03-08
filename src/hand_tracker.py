import mediapipe as mp


class HandTracker:

    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_drawing = mp.solutions.drawing_utils

    def process(self, image):
        return self.hands.process(image)

    def draw(self, image, landmarks):
        self.mp_drawing.draw_landmarks(
            image,
            landmarks,
            self.mp_hands.HAND_CONNECTIONS
        )

    def get_finger_positions(self, landmarks):
        index = (
            landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x,
            landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y
        )

        thumb = (
            landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x,
            landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y
        )

        return index, thumb