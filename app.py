import os
import cv2 as cv
from instagrapi import Client
from termcolor import colored
from PIL import Image, ImageOps


def resize_with_padding(img, expected_size):
    img.thumbnail((expected_size[0], expected_size[1]))
    delta_width = expected_size[0] - img.size[0]
    delta_height = expected_size[1] - img.size[1]
    pad_width = delta_width // 2
    pad_height = delta_height // 2
    padding = (pad_width, pad_height, delta_width - pad_width, delta_height - pad_height)
    return ImageOps.expand(img, padding)


""" Initial """
PICTURE_NAME = 'subject1.jpg'
WATERMARK = 'watermark.png'
TOP_SIGN = 'top-bar.jpg'
BOTTOM_SIGN = 'like-bar.jpg'
ACCOUNT_USER = '__akbar__akbar__123'
ACCOUNT_PASS = 'akbar'

""" Read Images """
like_bar = cv.imread(BOTTOM_SIGN, 0)
top_bar = cv.imread(TOP_SIGN, 0)
template = cv.imread(PICTURE_NAME, 0)
picture = cv.imread(PICTURE_NAME)
watermark = cv.imread(WATERMARK)

w, _ = template.shape[::-1]
watermark_height, watermark_width, _ = watermark.shape

""" Find Top Of Base Image """
res2 = cv.matchTemplate(top_bar, template, cv.TM_CCOEFF_NORMED)
top_bar_height, _ = top_bar.shape
_, _, _, _top = cv.minMaxLoc(res2)

""" Find Bottom Of Base Image """
res = cv.matchTemplate(like_bar, template, cv.TM_CCOEFF_NORMED)
_, _, _, _bottom = cv.minMaxLoc(res)


""" Crop Base Image """
top = _top[1] + top_bar_height
bottom = _bottom[1]
left = 0
right = w
cropped_img = picture[top:bottom, left:right]
# cropped_img = cv.flip(cropped_img, 1)  # Flip Image (doesnt work if image has words)

""" Add Watermark To Base Image """
# Watermark Position In Cropped Picture
_top, _left, _bottom, _right = 0, 0, watermark_height, watermark_width
# Get ROI
roi = cropped_img[_top: _bottom, _left: _right]
# Add the Logo to the Roi
result = cv.addWeighted(roi, 0.5, watermark, 1, 1)
# Replace the ROI on the image
cropped_img[_top: _bottom, _left: _right] = result
# Write Final Image
final_h, final_w, _ = cropped_img.shape
cv.imwrite('cropped_img.jpg', cropped_img)
if final_h < final_w and final_h < 500:
    final_img = Image.open('./cropped_img.jpg')
    final_img = resize_with_padding(final_img, (final_w, 500))
    final_img.save('final_img.jpg')
else:
    cv.imwrite('final_img.jpg', cropped_img)
# Remove Cropped Image
os.remove('cropped_img.jpg')

# Show The Final Image
# final_img = Image.open('./final_img.jpg')
# final_img.show()


""" Post It On Instagram """
cl = Client()
cl.login(ACCOUNT_USER, ACCOUNT_PASS)
media = cl.photo_upload(
    path='final_img.jpg',
    caption='this is the test caption from ali :)'
)
photo_url = media.dict().get('thumbnail_url')
if photo_url is not None:
    print(colored('Upload Successfully', 'green'))
    print('Photo Url: ', media.dict().get('thumbnail_url'))
    # Remove Final Image
    os.remove('final_img.jpg')
else:
    print(colored('Failed To Upload', 'red'))
