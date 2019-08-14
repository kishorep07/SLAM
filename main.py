"""
Feature based SLAM, using ORB features
"""


import cv2
import numpy as np
from display import Display2D

W = 1920//2
H = 1080//2

disp = Display2D(W, H)
#print(dir(orb))

class FeatureExtractor(object):
    GX = 8
    GY = 6

    def __init__(self):
        self.orb = cv2.ORB_create(100)

    def extract(self, img):
        feats = cv2.goodFeaturesToTrack(np.mean(img, axis = 2).astype(np.uint8), 3000, qualityLevel = 0.01, minDistance = 3)
        self.orb.compute(img, )
        return feats

fe = FeatureExtractor()

def process_frame(img):
    img = cv2.resize(img, (W, H))
    kp= fe.extract(img)

    for p in kp:
        u,v = map(lambda x: int(round(x)), p[0])
        cv2.circle(img, (u,v), color = (0,255,0), radius = 3) #draw circle over img

    disp.paint(img)

if __name__ == "__main__":
    cap = cv2.VideoCapture('./videos/test_countryroad.mp4') #live capture
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break
