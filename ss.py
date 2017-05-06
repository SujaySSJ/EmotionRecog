import cv2
import numpy as np 


img = cv2.imread('image1.png',0)
if img is not None:
	cv2.imshow('image',img)
	cv2.imwrite('test.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()