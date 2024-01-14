import mtcnn
from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt
import cv2
def draw_facebox(filename, result_list):
    plt.imshow(filename)
    ax = plt.gca()
    for result in result_list:
        x, y, width, height = result['box']
        #rect = plt.Rectangle((x, y), width, height, fill=False, color='green')
        #ax.add_patch(rect)
        img=filename
        cv2.rectangle(img,(x,y),(width+x,height+y),(0,127,255),2)
        cv2.imshow("ss",img)
    #return plt
    return img
