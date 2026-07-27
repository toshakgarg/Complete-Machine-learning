import cv2
#read the image
image=cv2.imread(r"D:\one drive\OneDrive\Pictures\Saved Pictures\SSDN.png")
#print the orignal image and its dimention
cv2.imshow("Logo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Orignal dimention",image.shape)

#print the resized image and its dimention
w=1000
h=600
dim=(w,h)
resized=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("resied dimention",resized.shape)
