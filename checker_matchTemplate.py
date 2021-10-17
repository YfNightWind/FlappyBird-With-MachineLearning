import cv2
import numpy as np
import sys

sys.path.append("game/")
import game.wrapped_flappy_bird as game

from matchTemplate import matchTemplate


def check():
    game_state = game.GameState()
    bird = cv2.imread('assets/sprites/redbird-midflap.png')

    methods = ['cv2.TM_SQDIFF',
               'cv2.TM_SQDIFF_NORMED',
               'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED',
               'cv2.TM_CCOEFF',
               'cv2.TM_CCOEFF_NORMED']

    for method in methods:
        im, _, _ = game_state.frame_step([0, 1])
        raw_im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
        answer_res, answer_im = matchTemplate(raw_im, bird, method)
        raw_im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
        res, im = matchTemplate(raw_im, bird, method)

        if np.sum(answer_res - res) > 0 or np.sum(answer_im - raw_im) > 0:
            return False

    return True


if __name__ == '__main__':
    check()
