# # # Section 1 # # #
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('like-bar3.jpg', 0)
img5 = cv.imread('top-bar2.jpg', 0)
img2 = img.copy()
template = cv.imread('subject1.jpg',0)
w, h = template.shape[::-1]



# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for meth in methods[1:2]:
    img = img2.copy()
    method = eval(meth)
    res = cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    # bottom_right = (top_left[0] + w, top_left[1])

    # #cv.imshow('image', template)
    # #cv.waitKey(0)
    # print(top_left, bottom_right)
    # top_right = (720, bottom_right[1])
    bottom = top_left[1]
    x = template.copy()
    x = cv.rectangle(x, (0, top_left[1]), (w, top_left[1]), (0, 0, 255), 10)

    res2 = cv.matchTemplate(img5, template, method)
    min_vali2, max_val2, min_loc2, max_loc2 = cv.minMaxLoc(res2)
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left2 = min_loc2
    else:
        top_left2 = max_loc2

    # bottom_right2 = (w, top_left[1] + 123)
    # y = x.copy()
    # top_left2 = (0, top_left2[1])
    # y = cv.rectangle(y, (0, top_left2[1] + 123), (w, top_left2[1] + 123), (0, 0, 255), 10)

    z = template.copy()

    z = cv.rectangle(z, (0, top_left2[1] + 123), (w-1, bottom), 100, 10)

    #cv.imshow('image2', template)
    #plt.subplot(121),plt.imshow(res,cmap = 'gray')
    #plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    #plt.subplot(122),plt.imshow(img,cmap = 'gray')
    #plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    #plt.suptitle(meth)
    #plt.show()
    cv.imshow('image4', z)
    cv.waitKey(0)
"""


# # # Section 2 # # #
from PIL import Image

"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

like_bar = cv.imread('like-bar3.jpg', 0)
top_bar = cv.imread('top-bar2.jpg', 0)
template = cv.imread('subject2.jpg', 0)
w, h = template.shape[::-1]


res2 = cv.matchTemplate(top_bar, template, cv.TM_CCOEFF_NORMED)
_, _, _, _top = cv.minMaxLoc(res2)
top_left = (0, _top[1] + 123)

res = cv.matchTemplate(like_bar, template, cv.TM_CCOEFF_NORMED)
_, _, _, _bottom = cv.minMaxLoc(res)
bottom_right = (w, _bottom[1])

template = cv.rectangle(template, top_left, bottom_right, 100, 1)
cv.imshow('image', template)
cv.waitKey(0)
"""

# # # Section 3 # # #

import time
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import cv2
import glob
import os

from instabot import Bot

# PICTURE_NAME = 'subject2.jpg'

# like_bar = cv.imread('like-bar3.jpg', 0)
# top_bar = cv.imread('top-bar2.jpg', 0)
# template = cv.imread(PICTURE_NAME, 0)
# picture = cv.imread(PICTURE_NAME)
# w, _ = template.shape[::-1]
#
# res2 = cv.matchTemplate(top_bar, template, cv.TM_CCOEFF_NORMED)
# _, _, _, _top = cv.minMaxLoc(res2)
# top_left = (0, _top[1] + 123)
#
# res = cv.matchTemplate(like_bar, template, cv.TM_CCOEFF_NORMED)
# _, _, _, _bottom = cv.minMaxLoc(res)
# bottom_right = (w, _bottom[1])
#
# crop_img = picture[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
#
# cv.imshow("cropped", crop_img)
# cv.waitKey(0)
# cv.destroyAllWindows()


""" Read Images """
PICTURE_NAME = 'subject1.jpg'
# WATERMARK = '4902194.jpg'
# WATERMARK = 'Untitled-2.jpg'
# WATERMARK = 'new2-Artboard 1-100.jpg'
WATERMARK = '3434.png'
# WATERMARK = 'new-Artboard 1.png'
# WATERMARK = 'photo_2021-07-01_13-33-32.jpg'
# ACCOUNT_USER = 'programmers_n1'
# ACCOUNT_PASS = 'aliALI2252'
ACCOUNT_USER = '__akbar__akbar__123'
ACCOUNT_PASS = '__akbar__akbar'


like_bar = cv.imread('like-bar3.jpg', 0)
top_bar = cv.imread('top-bar2.jpg', 0)
template = cv.imread(PICTURE_NAME, 0)
picture = cv.imread(PICTURE_NAME)
w, _ = template.shape[::-1]

""" Find Top Of Base Image """
res2 = cv.matchTemplate(top_bar, template, cv.TM_CCOEFF_NORMED)
_, _, _, _top = cv.minMaxLoc(res2)
top_left = (0, _top[1] + 123)  # 123 is height of top bar that we check (we minus 24 --> h_logo that we use later)

""" Find Bottom Of Base Image """
res = cv.matchTemplate(like_bar, template, cv.TM_CCOEFF_NORMED)
_, _, _, _bottom = cv.minMaxLoc(res)
bottom_right = (w, _bottom[1])

top = top_left[1]
bottom = bottom_right[1]
left = top_left[0]
right = bottom_right[0]
""" Crop Base Image """
crop_img = picture[top:bottom, left:right]

# cv.imshow('cropped', crop_img)
# cv.waitKey(0)

""" Add Watermark To Base Image """
logo = cv2.imread(WATERMARK)
h_logo, w_logo, _ = logo.shape

print(h_logo, w_logo)
h_img, w_img, _ = crop_img.shape

# Get the center of the original. It's the location where we will place the watermark
center_y = int(h_img)
center_x = int(w_img)
# top_y = center_y - int(h_logo)
top_y = 0   # The old one on bottom
left_x = center_x - int(w_logo)
# bottom_y = top_y + h_logo  # The old one on bottom
bottom_y = h_logo
right_x = left_x + w_logo
# Get ROI
roi = crop_img[top_y: bottom_y, left_x: right_x]
# Add the Logo to the Roi
result = cv2.addWeighted(roi, 0.5, logo, 1, 1)
# Replace the ROI on the image
crop_img[top_y: bottom_y, left_x: right_x] = result
# Get filename and save the image
# cv2.imshow('image', crop_img)
# cv2.waitKey(0)


cv.imwrite('new_image.jpg', crop_img)

from PIL import Image, ImageOps


def padding(img, expected_size):
    desired_size = expected_size
    delta_width = desired_size - img.size[0]
    delta_height = desired_size - img.size[1]
    pad_width = delta_width // 2
    pad_height = delta_height // 2
    padding = (pad_width, pad_height, delta_width - pad_width, delta_height - pad_height)
    return ImageOps.expand(img, padding)


def resize_with_padding(img, expected_size):
    img.thumbnail((expected_size[0], expected_size[1]))
    # print(img.size)
    delta_width = expected_size[0] - img.size[0]
    delta_height = expected_size[1] - img.size[1]
    pad_width = delta_width // 2
    pad_height = delta_height // 2
    padding = (pad_width, pad_height, delta_width - pad_width, delta_height - pad_height)
    return ImageOps.expand(img, padding)

h, w, _ = crop_img.shape
print(h, w)
print(h< w)

if h < w and h < 500:
    img6 = Image.open("./new_image.jpg")
    print(img6)
    img = resize_with_padding(img6, (w, 500))
    print(img.size)
    img.show()
    img.save("new_image.jpg")
else:
    img6 = Image.open("./new_image.jpg")
    img6.show()


""" Post It On Instagram """


# import os
# import glob
# cookie_del = glob.glob("config/*cookie.json")
# # os.remove(cookie_del[0])
# bot = Bot()
#
#
#
# bot.login(username=ACCOUNT_USER, password=ACCOUNT_PASS, is_threaded=True)
#
# bot.upload_photo('new_image.jpg', caption='hello')
#

