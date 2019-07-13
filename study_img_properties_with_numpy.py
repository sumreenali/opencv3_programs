import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2

def main():


   imgpath = "E:\\OpenCV\\dataset\\lena_color_256.tif" 
   
   img = cv2.imread(imgpath, 0) 
   cv2.namedWindow('Lena', cv2.WINDOW_AUTOSIZE)
   #cv2.imshow('Lena', img)
   
   #this will print the img and you can see the computer reads the img in terms of numeric arrays 
   print(img)
   
   #type of image
   print(type(img))
   
   #type of img data
   print(img.dtype)
   
   #shape of image - width , height , no_of_channels which is 3 for color and 2 for grayscale
   print(img.shape)
   
   # dimensions of images 
   print(img.ndim)
   
   #size of image - width x height x no_of_channels
   print(img.size)
   
   #cv2.waitKey(0)
   #cv2.destroyWindow('Lena')

   
if __name__ == "__main__":
    main()