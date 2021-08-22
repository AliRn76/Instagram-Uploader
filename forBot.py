import os
import cv2 as cv
from instagrapi import Client
from termcolor import colored
from PIL import Image

from secret_keys import WATERMARK, ACCOUNT_USER, ACCOUNT_PASS

""" Read Images """
# picture = cv.imread(PICTURE_NAME)
picture = MAHAN_PICTURE
watermark = cv.imread(WATERMARK)
watermark_height, watermark_width, _ = watermark.shape

""" Add Watermark To Base Image """
# Watermark Position In Picture
top, left, bottom, right = 0, 0, watermark_height, watermark_width
# Get ROI
roi = picture[top: bottom, left: right]
# Add the Logo to the Roi
result = cv.addWeighted(roi, 0.5, watermark, 1, 1)
# Replace the ROI on the image
picture[top: bottom, left: right] = result
# Write Final Image
final_h, final_w, _ = picture.shape
cv.imwrite('final_img.jpg', picture)

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
