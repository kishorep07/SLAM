import cv2
import pygame
from display import Display2D

W = 1920//2
H = 1080//2

disp = Display2D(W, H)

def process_frame(img):
    img = cv2.resize(img, (W, H))
    disp.paint(img)

if __name__ == "__main__":
    cap = cv2.VideoCapture('./videos/test_countryroad.mp4') #live capture
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break
