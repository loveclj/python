#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: build_cn_en_label.py.py
@time: 5/17/16 11:02 AM
"""
import codecs
import json

# dynamodb field
primary_key = "patent_id"
label_en_field = "label_en"
label_cn_field = "label_cn"


# read a line, no empty pid or label return, except finish is true
def get_pid_label(fd):
    pid = ""
    label = ""
    finish = False
    while True:
        line = fd.readline()

        if not line:
            finish = True
            break

        try:
            pid, label = line.strip("\n").split(":")

            if not pid or not label:
                continue
            else:
                break

        except:
            continue

    return pid, label, finish


def build_json(pk_field, en_fd=None, en_label=None, en_finish=True, cn_fd=None, cn_label=None, cn_finish=True):
    label_json = {}
    label_json[primary_key] = pk_field

    mode = ""
    if en_label and cn_label:
        mode = "ALL"
    elif en_label:
        mode = "EN"
    else:
        mode = "CN"

    if en_label:
        label_json[label_en_field] = en_label
        en_pid, en_label, en_finish = get_pid_label(en_fd)

    if cn_label:
        label_json[label_cn_field] = cn_label
        cn_pid, cn_label, cn_finish = get_pid_label(cn_fd)

    label_str = json.dumps(label_json, encoding="utf-8", ensure_ascii=False) + "\n"

    if mode == "ALL":
        return en_pid, cn_pid, en_label, cn_label, en_finish, cn_finish, label_str
    elif mode == "EN":
        return en_pid, en_label, en_finish, label_str
    else:
        return cn_pid, cn_label, cn_finish, label_str

if __name__ == '__main__':

    # label file (cn & en)
    fd = codecs.open("label_json.text", "w", "utf-8")

    # label file (cn | en)
    en_fd = codecs.open("./label/en_label.text", "r", "utf-8")
    cn_fd = codecs.open("./label/cn_label.text", "r", "utf-8")

    # for debug
    # en_fd = codecs.open("./label/en_label_50k.text", "r", "utf-8")
    # cn_fd = codecs.open("./label/cn_label_50k.text", "r", "utf-8")

    en_pid, en_label, en_finish = get_pid_label(en_fd)
    cn_pid, cn_label, cn_finish = get_pid_label(cn_fd)

    label_str = ""
    while not en_finish and not cn_finish:

        label_json = {}

        if en_pid > cn_pid:

            cn_pid, cn_label, cn_finish, label_str = build_json(pk_field=cn_pid, cn_fd=cn_fd, cn_label=cn_label, cn_finish=cn_finish)
            # label_json[primary_key] = cn_pid
            # label_json[label_cn_field] = cn_label
            # cn_pid, cn_label, cn_finish = get_pid_label(cn_fd)

        elif en_pid < cn_pid:
            en_pid, en_label, en_finish, label_str = build_json(pk_field=en_pid, en_fd=en_fd, en_label=en_label, en_finish=en_finish)

            # label_json[primary_key] = en_pid
            # label_json[label_en_field] = en_label
            # en_pid, en_label, en_finish = get_pid_label(en_fd)

        else:  # equal

            en_pid, cn_pid, en_label, cn_label, en_finish, cn_finish, label_str = \
                build_json(pk_field=en_pid, en_fd=en_fd, en_label=en_label, en_finish=en_finish, cn_fd=cn_fd, cn_label=cn_label, cn_finish=cn_finish)

            # print en_pid, cn_pid
            # label_en_field[primary_key] = cn_pid
            # label_json[label_cn_field] = cn_label
            # label_json[label_en_field] = en_label
            #
            # cn_pid, cn_label, cn_finish = get_pid_label(cn_fd)
            # en_pid, en_label, en_finish = get_pid_label(en_fd)

        fd.write(label_str)
        # print label_str,


    while not en_finish:
        en_pid, en_label, en_finish, label_str = build_json(pk_field=en_pid, en_fd=en_fd, en_label=en_label, en_finish=en_finish)
        fd.write(label_str)
        # print label_str,

        # label_json = {}
        # label_json[primary_key] = en_pid
        # label_json[label_en_field] = en_label
        # en_pid, en_label, en_finish = get_pid_label(en_fd)


    while not cn_finish:
        cn_pid, cn_label, cn_finish, label_str = build_json(pk_field=cn_pid, cn_fd=cn_fd, cn_label=cn_label, cn_finish=cn_finish)
        fd.write(label_str)
        # print label_str,

        #
        # label_json = {}
        # label_json[primary_key] = cn_pid
        # label_json[label_cn_field] = cn_label
        # cn_pid, cn_label, cn_finish = get_pid_label(cn_fd)

    fd.close()
    cn_fd.close()
    en_fd.close()




