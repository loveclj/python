#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: GetImages.py.py
@time: 2/17/16 5:19 PM
"""

import os
import time
import uuid

import falcon


def _media_type_to_ext(media_type):
    return media_type[6:]


def _ext_to_media_type(ext):
    return 'image/' + ext


def _generate_id():
    return str(uuid.uuid4())


class Collection(object):
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def on_post(self, req, resp):
        image_id = _generate_id()
        ext = _media_type_to_ext(req.content_type)
        filaename = image_id + '.' + ext

        image_path = os.path.join(self.storage_path, filaename)

        with open(image_path, "wb") as image_file:
            while True:
                chunk = req.stream.read(4096)
                if not chunk:
                    break
                image_file.write(chunk)

        resp.status = falcon.HTTP_201
        resp.location = '/images/' + filaename

class Item(object):
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def on_get(self, req, resp, name):
        ext = os.path.splitext(name)[1][1:]
        resp.content_type = _ext_to_media_type(ext)

        image_path = os.path.join(self.storage_path, name)
        resp.stream = open(image_path, "rb")
        resp.stream_len = os.path.getsize(image_path)

app = falcon.API()

post_images = Collection("./")
get_images = Item("./")

app.add_route("/images", post_images)
app.add_route("/images/{name}", get_images)