import cv2
img = cv2.imread(r'C:\Users\SAMEER\OneDrive\Desktop\Data Science 6pm\Projects\My Projects\CV2\image processing 2\a.jpg')
img_1 = cv2.imread(r'C:\Users\SAMEER\OneDrive\Desktop\Data Science 6pm\Projects\My Projects\CV2\image processing 2\b.jpg')

#HOW COMPUTER READS IMAGE

#print(img)
#print(img_1)

#DISPLAY IMAGE

cv2.imshow(" Horse ", img)
cv2.imshow(" Fruits ", img_1)

cv2.waitKey(0)
cv2.destroyAllWindows()

print(img.shape)
print(img_1.shape)

#PIXELS
print(img.size)
print(img_1.size)

print(img.dtype)
print(img_1.dtype)


