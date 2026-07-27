import cv2
#read the image
image=cv2.imread(r"D:\one drive\OneDrive\Pictures\Saved Pictures\SSDN.png")
#printing the orignal image
cv2.imshow("Logo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#printing the Gray image
gray_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
