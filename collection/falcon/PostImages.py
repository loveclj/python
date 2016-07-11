#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: First_Test.py.py
@time: 2/17/16 4:35 PM
"""

import falcon
import os
import uuid

def _media_type_to_ext(media_type):
    return media_type[6:]

def _generate_id():
    return str(uuid.uuid4())

class Resource(object):

    def __init__(self, storage_path):
        self.storage_path = storage_path

    def on_post(self, req, resp):
        image_id = _generate_id()
        ext = _media_type_to_ext(req.content_type)
        filename = image_id + "." + ext
        image_path = os.path.join(self.storage_path, filename)

        with open(image_path, "wb") as image_file:
            while True:
                chunk = req.stream.read(4096)
                if not chunk:
                    break
                image_file.write(chunk)

        resp.status = falcon.HTTP_200
        resp.location = "./images/" + image_id


app = falcon.API()

images = Resource("./")

app.add_route('/images', images)