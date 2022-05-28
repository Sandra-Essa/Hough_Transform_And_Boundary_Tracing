import numpy as np
import cv2
from matplotlib import pyplot as plt


def pic():
    # initialize our canvas as a 300x300 pixel image with 3 channels
    # (Red, Green, and Blue) with a black background
    canvas3 = np.zeros((300, 300, 1), dtype="uint8")
    # blue=(0,0,255)
    cv2.rectangle(canvas3, (100, 100), (200, 200), 1, -1)

    plt.subplot(221), plt.imshow(canvas3, cmap='gray')
    plt.title('Single Region'), plt.xticks([]), plt.yticks([])
   # cv2.imshow("Canvas", canvas)
   # cv2.waitKey(0)

   #  print(length, width)
    # print(canvas3[150][150])
    return canvas3


def find_first_pixel():
    canvas3 = pic()
    width = canvas3.shape[0]
    length = canvas3.shape[1]
    for i in range(length):
        for j in range(width):
            if (canvas3[i][j] == 1):
                x = i
                y = j
                break
    return x, y


f = find_first_pixel()
print(f)
