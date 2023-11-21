
import cv2
import numpy as np

#LOAD IMAGE

input = cv2.imread(r'C:\Users\SAMEER\OneDrive\Desktop\Data Science 6pm\Projects\My Projects\CV2\Image processing\ele.jpeg')

cv2.imshow('Elephant', input)
cv2.waitKey()
cv2.destroyAllWindows()


import cv2

input1 = cv2.imread(r'C:\Users\SAMEER\OneDrive\Desktop\Data Science 6pm\Projects\My Projects\CV2\Image processing\mypic\mypic.jpg')

cv2.imshow('My Pic', input1)
cv2.waitKey()
cv2.destroyAllWindows()


#lets print the dimensions of the image array

print('height of image:', int(input1.shape[0]), 'pixels')
print('width of image:', int(input1.shape[1]), 'pixels')


#How do we save images we edit in OpenCV?

cv2.imwrite('output.jpg', input1)
cv2.imwrite('output.png', input1)


'''
# Define the desired height and width
desired_height = 500
desired_width = 500


# Resize the image
resized_image = cv2.resize(img, (desired_width, desired_height))

cv2.imshow('Original Image', img)
cv2.imshow('Resized image', resized_image)

'''