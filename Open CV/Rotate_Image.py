import cv2
import numpy as np
#read the image
image=cv2.imread(r"D:\one drive\OneDrive\Pictures\Saved Pictures\SSDN.png")
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Rotating the image by 90 degree clockwise
image_90=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("rotated", image_90)
cv2.waitKey(0)
cv2.destroyAllWindows()
