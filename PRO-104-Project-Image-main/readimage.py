import cv2
solar= cv2.imread('solar-system.jpg')
print(solar)
print(solar.shape)
cv2.imshow('solar-system', solar)
cv2.waitKey(0)