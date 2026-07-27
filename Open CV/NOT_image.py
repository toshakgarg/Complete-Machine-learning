import cv2
#read the image
image=cv2.imread(r"D:\one drive\OneDrive\Pictures\Saved Pictures\SSDN.png")

cv2.imshow("Logo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#NOT & Gray image
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
not_gray_img = cv2.bitwise_not(gray_img)
not_img = cv2.bitwise_not(image)
cv2.imshow("gray of image",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("NOT of gray Image",not_gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("NOT of orignal Image",not_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
