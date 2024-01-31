# import the two modules
import cv2
import numpy as np

# part 1: load path of the image
original_image = cv2.imread("C:/Users/manav/OneDrive/Desktop/Images Samples/2.png")
original_image = cv2.resize(original_image,(200,200))
cv2.cvShowImage('original image',original_image)
cv2.waitKey(0)



# part 2: blur the images

# 1. simple blurring operation using cv2.blur() function
blur_image = cv2.blur(original_image,(3,3))
blur_image = cv2.resize(blur_image,(200,200))
cv2.cvShowImage('blur image',blur_image)

# 2. blurring operation using cv2.GaussianBlur() function
# blur_image = cv2.GaussianBlur(original_image,(9,9),1)
# sharp1 = cv2.addWeighted(original_image,1.1,blur_image,-0.1,0)
# blur_image = cv2.resize(blur_image,(200,200))
# cv2.imshow('Gaussian blur image',blur_image)



# part 3: create a sharpening kernel
sharpen_filter=np.array([[-1,-1,-1],
                 [-1,9,-1],
                [-1,-1,-1]])

sharp_image = cv2.filter2D(blur_image,-1,sharpen_filter)
# sharpening without blurring
# sharp_image = cv2.filter2D(original_image,-1,sharpen_filter)
sharp_image = cv2.resize(sharp_image,(200,200))
cv2.cvShowImage('sharp image',sharp_image)
cv2.waitKey(0)
cv2.destroyAllWindows()