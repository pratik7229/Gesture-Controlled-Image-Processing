import cv2

from hand_tracker import HandTracker
from gesture_utils import calculate_distance
from blur_controller import draw_rect, apply_blur


def main():

    cap = cv2.VideoCapture(0)
    tracker = HandTracker()

    while True:

        ret, image = cap.read()

        image = cv2.resize(image, None, None, fx=1.5, fy=1.5)
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        results = tracker.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                tracker.draw(image, hand_landmarks)

                index, thumb = tracker.get_finger_positions(hand_landmarks)

                percent = calculate_distance(index, thumb)

                draw_rect(image, percent)

                image = apply_blur(image, percent)

        cv2.imshow("Gesture Blur Controller", image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()