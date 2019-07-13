import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2

def main():


   imgpath = "E:\\OpenCV\\dataset\\lena_color_256.tif" 
   
   img = cv2.imread(imgpath, 0) 
   cv2.namedWindow('Lena', cv2.WINDOW_AUTOSIZE)
   
   
   cv2.imshow('Lena', img)
   cv2.waitKey(0)
   cv2.destroyWindow('Lena')

   
if __name__ == "__main__":
    main()