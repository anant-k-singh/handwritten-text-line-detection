import numpy as np
import cv2
import math

# Prints the input image with name(optional)
def show(image,name="image"):
    cv2.imshow(name,image)
    cv2.waitKey(0)

def binarize(img, a, b):
	return cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,a,b)

def invert(img):
	return cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

def connected_components(img):
	return cv2.connectedComponentsWithStats(img, connectivity=8)