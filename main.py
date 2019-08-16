"""
Feature based SLAM, using ORB features
"""


import cv2
import numpy as np
from display import Display2D
from extractor import FeatureExtractor

W = 1920//2
H = 1080//2

disp = Display2D(W, H)
fe = FeatureExtractor()

def process_frame(img):
    img = cv2.resize(img, (W, H))
    matches= fe.extract(img)


    for pt1, pt2 in matches:
        u1,v1 = map(lambda x: int(round(x)), pt1)
        u2,v2 = map(lambda x: int(round(x)), pt2)
        cv2.circle(img, (u1,v1), color = (0,255,0), radius = 3) #draw circle over img
        cv2.line(img, (u1,v1), (u2,v2), color = (255, 0, 0))

    disp.paint(img)

if __name__ == "__main__":
    cap = cv2.VideoCapture('./videos/test_countryroad.mp4') #live capture
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break
