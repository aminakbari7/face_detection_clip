import mtcnn
from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt
from face import draw_facebox
import cv2
import os
import shutil
import time
import moviepy
def main():
    detector = MTCNN()
    cap = cv2.VideoCapture("face.mp4")
    while True:
        ret, frame = cap.read()
        img=frame
        results = detector.detect_faces(img)
        #draw_facebox(img,results).show()
        cv2.imshow("ss",draw_facebox(img,results))
        if cv2.waitKey(1) == ord('q'):
            break
if __name__=="__main__":
    main()