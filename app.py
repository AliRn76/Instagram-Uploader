import os
from datetime import datetime

import cv2 as cv
from instagrapi import Client
from termcolor import colored
from PIL import Image, ImageOps
from dotenv import dotenv_values

config = dotenv_values('.secret_keys')
WATERMARK = 'watermark1080.png'
ACCOUNT_USER = config['ACCOUNT_USER']
ACCOUNT_PASS = config['ACCOUNT_PASS']
TEMP_USER = config['ACCOUNT_PASS']
TEMP_PASS = config['ACCOUNT_PASS']
BOT_KEY = config['BOT_KEY']


def handle_image_url(url: str) -> str:
    # picture_url = 'https://www.instagram.com/p/CTpABt4tJPU/' or
    #   'https://www.instagram.com/p/CTpABt4tJPU/?utm_source=ig_web_copy_link'
    first = 28
    last = url[first:].find('/')
    image_tag = url[first:first+last]
    # image_tag = 'CTpABt4tJPU'
    return image_tag

def download_image(image_tag: str):
    os.system(f'instaloader --login={TEMP_USER} --password={TEMP_PASS} -- -{image_tag}')

def get_image_path(folder_name):
    new = os.listdir('-' + folder_name)
    for i in new:
        if i.endswith('.jpg'):
            return f'-{folder_name}' + '/' + i

def resize_watermark(width):
    os.system(f'convert {WATERMARK} -resize {width}x123 temp_watermark.jpg')


def final_image(picture_url: str):
    """ Handle ImageUrl --> Download Image --> Find Image Path --> Read Image"""
    image_tag = handle_image_url(url=picture_url)
    # download_image(image_tag=image_tag)
    picture_path = get_image_path(folder_name=image_tag)
    picture_path = '-CTpABt4tJPU/2021-09-10_12-11-24_UTC.jpg'
    picture = cv.imread(picture_path)
    picture_height, picture_width, _ = picture.shape

    """ Resize Watermark With New Width --> Read Watermark --> Replace It On Picture --> Write New Picture """
    resize_watermark(width=picture_width)
    watermark = cv.imread('temp_watermark.jpg')
    # Add Watermark To Base Image
    watermark_height, _, _ = watermark.shape
    _top, _bottom, _left, _right = 0, watermark_height, 0, picture_width
    # Get ROI
    roi = picture[_top: _bottom, _left: _right]
    # Add the Logo to the Roi
    result = cv.addWeighted(roi, 0.5, watermark, 1, 1)
    # Replace the ROI on the image
    picture[_top: _bottom, _left: _right] = result
    # Write Final Image
    final_path = 'final_image.jpg'
    cv.imwrite(final_path, picture)

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


# final_image('https://www.instagram.com/p/CTpABt4tJPU/')


