#Code to print the image And its size

import cv2
#read the image
image=cv2.imread(r"D:\one drive\OneDrive\Pictures\Saved Pictures\SSDN.png")

cv2.imshow("Logo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
image.shape
h,w=image.shape[:2]
print("Height={}, Weigth{}".format(h,w))
