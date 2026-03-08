import cv2


def draw_rect(image, percent):
    cv2.rectangle(image, (30, 620), (500, 570), (255, 255, 5), 2)
    cv2.rectangle(image, (30, 620), (int(percent), 570), (255, 255, 5), -2)


def apply_blur(image, percent):
    return cv2.blur(image, (int(percent * 0.08), 10))