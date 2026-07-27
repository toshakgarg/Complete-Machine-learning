import cv2
import numpy as np
#read the image
image1=cv2.imread(r"D:\one drive\OneDrive\Pictures\Saved Pictures\SSDN.png")
image2=cv2.imread(r"D:\one drive\OneDrive\Pictures\Saved Pictures\SSDN.png")
#Adding two image
sum=cv2.add(image1,image2)
cv2.imshow("image1", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("image2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("added", sum)
cv2.waitKey(0)
cv2.destroyAllWindows()
