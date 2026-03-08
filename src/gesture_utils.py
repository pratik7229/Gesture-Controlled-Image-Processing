import numpy as np


def calculate_distance(finger, thumb):
    dist = np.sqrt(np.square(finger[0] - thumb[0]) + np.square(finger[1] - thumb[1]))

    max_val = 0.033
    percent = (dist / max_val) * 100

    if percent > 520:
        return 499
    elif percent < 30:
        return 30
    else:
        return percent