import cv2


def matchTemplate(im, template, method):
    res = cv2.matchTemplate(im, template, eval(method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in ['cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
    cv2.rectangle(im, top_left, bottom_right, 0, 2)
    return res, im