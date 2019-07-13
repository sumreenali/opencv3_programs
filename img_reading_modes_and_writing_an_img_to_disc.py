import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2

def main():
   # print(cv2.__version__)
   
   
   #IMPORT IMAGE PATH  , READ IMAGE & DISPLAY IMAGE  
   imgpath = "E:\\OpenCV\\dataset\\lena_color_256.tif" 
   
   # DEFINING AND OUTPUT PATH FOR SAVING IMAGE IN JPG FORMAT BY CHANGING THE FORMAT INTO JPG 
   outpath ="E:\\OpenCV\\output\\lena_color_256.jpg"
   
   
   #IMAGE REDAING MODES WHICH USES AS THE 2ND ARG FOR   IMREAD METHOD
   #THERE ARE THREE MODES  1 FOR DEFAULT COLOR IMAGE , 0 FOR GRAYSCALE,
   #-1 USED TO STORE, READ IMAGE AS IT IS ALSO SAVES THE 
   # ALPHA TRANSPARENCY CHANNEL IN THE IMAGES 
   
   img = cv2.imread(imgpath, 0) 
   
  #TO CREATE A SEPARATE WINDOW
   cv2.namedWindow('Lena', cv2.WINDOW_AUTOSIZE)
   
   #DISPLAY IMAGE
   cv2.imshow('Lena', img)
    
   #SAVING IMAGE
   cv2.imwrite(outpath, img)
    
   #THIS FUNCTOION IS TO DESTROY THE WINDOW ON PRESSING ANY OF THE KEYBOARD 
   # - IN SHORT BINDING THE WINDOW WITH KEYBOARD
   cv2.waitKey(0)
   #FOR DISTROYING ALL WINDOWS
   # cv2.destroyAllWindows()  
   
   #FOR DISTROYING SINGLE WINDOWS
   cv2.destroyWindow('Lena')

   
if __name__ == "__main__":
    main()