import cv2
import cvlib as cv
# from helper_fcns.audio_maker import make_aud

def counting():
    img = cv2.imread("res/temp.png")
    box, label, count = cv.detect_common_objects(img)
    counts = dict()
    for i in label:
        counts[i] = counts.get(i, 0) + 1
    statement = "There are"
    for j in list(counts.keys()):
        statement = statement +" "+ str(counts[j])+ " " + j
        if counts[j] > 1:
            statement = statement + "s"
    if len(counts) == 0:
        statement = statement + " no countable objects"
    # make_aud(statement)
    return statement