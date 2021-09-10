import os
from datetime import datetime

import cv2 as cv
from instagrapi import Client
from termcolor import colored
from PIL import Image, ImageOps
from dotenv import dotenv_values

config = dotenv_values('.secret_keys')
WATERMARK720 = 'watermark720.png'
WATERMARK1080 = 'watermark1080.png'
TOP_SIGN = 'top-bar.jpg'
BOTTOM_SIGN = 'like-bar.jpg'
ACCOUNT_USER = config['ACCOUNT_USER']
ACCOUNT_PASS = config['ACCOUNT_PASS']
BOT_KEY = config['BOT_KEY']


def resize_with_padding(img, expected_size):
    img.thumbnail((expected_size[0], expected_size[1]))
    delta_width = expected_size[0] - img.size[0]
    delta_height = expected_size[1] - img.size[1]
    pad_width = delta_width // 2
    pad_height = delta_height // 2
    padding = (pad_width, pad_height, delta_width - pad_width, delta_height - pad_height)
    return ImageOps.expand(img, padding)


def final_image(picture_url: str):
    """ Read Images """
    # picture_url = 'https://www.instagram.com/p/CTpABt4tJPU/' or
    #   'https://www.instagram.com/p/CTpABt4tJPU/?utm_source=ig_web_copy_link'
    first = 28
    last = picture_url[first:].find('/')
    image_tag = picture_url[first:first+last]
    # image_tag = 'CTpABt4tJPU'
    os.system(f'instaloader --login=programmers_n1_downloader2 --password=ali123 -- -{image_tag}')
    # TODO: go to the folder --> folder_name is = '-{image_tag}'
    # TODO: find the image
    # TODO: use the image_path as picture_path in line below
    picture_path = f'-{image_tag}' + '/' + ...
    cropped_img = picture_path

    # TODO: change the like_bar (it should handle the slide posts)
    like_bar = cv.imread(BOTTOM_SIGN, 0)
    top_bar = cv.imread(TOP_SIGN, 0)
    template = cv.imread(picture_path, 0)
    picture = cv.imread(picture_path)
    watermark = cv.imread(WATERMARK1080 if picture.shape[1] == 1080 else WATERMARK720)
    # TODO: we can use "convert ali.jpg -resize 720x123 alii.jpg" later
    w, _ = template.shape[::-1]
    # TODO: fix the width and height of watermark with original picture
    watermark_height, watermark_width, _ = watermark.shape

    # """ Find Top Of Base Image """
    # res2 = cv.matchTemplate(top_bar, template, cv.TM_CCOEFF_NORMED)
    # top_bar_height, _ = top_bar.shape
    # _, _, _, _top = cv.minMaxLoc(res2)

    # """ Find Bottom Of Base Image """
    # res = cv.matchTemplate(like_bar, template, cv.TM_CCOEFF_NORMED)
    # _, _, _, _bottom = cv.minMaxLoc(res)

    # """ Crop Base Image """
    # top = _top[1] + top_bar_height
    # bottom = _bottom[1]
    # left = 0
    # right = w
    # cropped_img = picture[top:bottom, left:right]
    # # cropped_img = cv.flip(cropped_img, 1)  # Flip Image (doesnt work if image has words)

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
    final_path = "images/final/" + str(datetime.now()) + '.jpg'
    if final_h < final_w and final_h < 500:
        final_img = Image.open('./cropped_img.jpg')
        final_img = resize_with_padding(final_img, (final_w, 500))
        final_img.save(final_path)
    else:
        cv.imwrite(final_path, cropped_img)
    # Remove Cropped Image
    os.remove('cropped_img.jpg')

    # Show The Final Image
    # final_img = Image.open(final_path)
    # final_img.show()
    # os.remove(final_path)
    # Upload To Instagram
    # upload_on_instagram(final_path)

    return final_path


def upload_on_instagram(image_path: str):
    """ Post It On Instagram """
    print('Start Uploading ... ')
    cl = Client()
    cl.login(ACCOUNT_USER, ACCOUNT_PASS)
    media = cl.photo_upload(
        path=image_path,
        caption='this is the test caption from ali :)'
    )
    photo_url = media.dict().get('thumbnail_url')
    if photo_url is not None:
        print(colored('Upload Successfully', 'green'))
        print('Photo Url: ', media.dict().get('thumbnail_url'))
        # Remove Final Image
        os.remove(image_path)
    else:
        print(colored('Failed To Upload', 'red'))


# final_image('photo_2021-09-10_15-24-13.jpg')


