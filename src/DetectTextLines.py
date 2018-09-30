import numpy as np
import cv2
import math
import sys
from Util import *

# Print full numpy array
# np.set_printoptio	ns(threshold=np.nan)

input_img_path="../resources/document.png"
input_img = cv2.imread(input_img_path,0)

bin_img = binarize(input_img, 13, 8)
show(bin_img)

# show(invert(bin_img))

num_labels,labels,stats,centroids = connected_components(bin_img)
# print(num_labels)
# print(centroids)


# DAFAQ is this
# def getmarkerboundingrect(img, mkpos, mksize):
#     buffer = int(mksize * 0.15)
#     x = mkpos[0] - buffer
#     y = mkpos[1] - buffer
#     w = mksize + buffer*2
#     h = mksize + buffer*2
#     roi = img[y:y+h, x:x+w]
    
#     # grayroi = getgrayimage(roi)
#     # ret, binimage = cv2.threshold(grayroi,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#     binimage = binarize(img, 13, 8)
#     nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(binimage)
#     # stats[0], centroids[0] are for the background label. ignore
#     # cv2.CC_STAT_LEFT, cv2.CC_STAT_TOP, cv2.CC_STAT_WIDTH, cv2.CC_STAT_HEIGHT
#     lblareas = stats[1:,cv2.CC_STAT_AREA]
#     imax = max(enumerate(lblareas), key=(lambda x: x[1]))[0] + 1
#     boundingrect = Rect(stats[imax, cv2.CC_STAT_LEFT],
#                         stats[imax, cv2.CC_STAT_TOP], 
#                         stats[imax, cv2.CC_STAT_WIDTH], 
#                         stats[imax, cv2.CC_STAT_HEIGHT])
#     return boundingrect.addoffset((x,y)) 

# print(getmarkerboundingrect(bin_img,[0,0],1))