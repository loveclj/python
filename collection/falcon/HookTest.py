#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: HookTest.py.py
@time: 2/17/16 6:08 PM
"""


import falcon

type_list = ["jpg", "gif", "doc"]

def check_ext(req, resp, resource, params):
    ext = req.content_type.split('/')[1]
    if ext not in type_list:
        msg = "forbidden ext, " + ext
        raise falcon.HTTPBadRequest('Bad Request', msg)

class GetType(object):
    @falcon.before(check_ext)
    def on_post(self, req, resp):
        print req.content_type
        ext = req.content_type.split('/')[1]
        print ext
        resp.status = falcon.HTTP_200
        resp.body = req.content_type

judge_type = GetType()
app = falcon.API()
app.add_route("/type", judge_type)
