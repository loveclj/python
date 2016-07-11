#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: text_process.py
@time: 6/6/16 2:45 PM
"""

import codecs
import commands
import json


def extract_info_from_file(keyword, filename, separator, index):

    cmd = "grep " + "\"" + keyword + "\"" " " + filename
    status, output = commands.getstatusoutput(cmd)

    if not output:
        return ""

    lines = output.split("\n")
    # if len(lines) > 1:
    #     return ""

    try:
        field = lines[0].split(separator)[index]
        return field
    except:
        return ""


def get_execute_duration_from_file(filename):

    duration = ""
    with codecs.open(filename=filename, mode="r", encoding="utf-8") as fd:
        lines = fd.readlines()
        line_count = len(lines)
        first_line = lines[0].strip()
        last_line = lines[line_count - 1].strip()
        time_start = first_line[1:20]
        time_end = last_line[1:20]

    return time_start, time_end


def list_log_file(dir_name):
    cmd = "find " + dir_name + " -name 0.log"
    status, output = commands.getstatusoutput(cmd)
    file_list = output.split()
    return file_list


def extract_landscape_info_from_single_log(filename):
    landscape_info = {}

    try:
        nProcs = extract_info_from_file(keyword="PreProcess Execution Time", filename=filename, separator=":", index=-1)

        preprocess_time = extract_info_from_file(keyword="PreProcess Execution Time", filename=filename,
                                             separator=":", index=-2).strip().split(" ")[0]

        num_item = extract_info_from_file(keyword="Total Patents", filename=filename, separator=":", index=-1).strip()

        label_execute_time = extract_info_from_file(keyword="LABEL Extracting Execution Time",
                                                filename=filename, separator=":", index=-3).strip().split()[0]

        som_training_time = extract_info_from_file(keyword="SOM Training Execution Time", filename=filename,
                                               separator=":", index=-2).strip().split()[0]

        time_start, time_end = get_execute_duration_from_file(filename)

        landscape_info["nProcs"] = nProcs
        landscape_info["preprocess_time"] = preprocess_time
        landscape_info["num_item"] = num_item
        landscape_info["label_execute_time"] = label_execute_time
        landscape_info["som_training_time"] = som_training_time
        landscape_info["time_start"] = time_start
        landscape_info["time_end"] = time_end
    except:
        landscape_info = {}

    return landscape_info


def get_landscape_info_from_dir(dir_name):
    landcape_info = []
    file_list = list_log_file(dir_name)

    if not file_list:
        return landcape_info

    for file in file_list:
        single_info = extract_landscape_info_from_single_log(file)

        if not single_info:
            continue

        landcape_info.append(single_info)

    return landcape_info


def dump_json_to_file(json_obj, filename):
    fp = codecs.open(filename=filename, encoding="utf-8", mode="w")
    json.dump(obj=json_obj, ensure_ascii=False, encoding="utf-8", fp=fp, indent=4)
    fp.close()


def load_info_from_json_file(filename):
    info_tupple_list = []
    fp = codecs.open(filename=filename, mode="r", encoding="utf-8")

    info_dict_list = json.load(fp=fp)

    for info_dict in info_dict_list:
        info_tupple = (info_dict["time_start"], info_dict["time_end"],
                       info_dict["nProcs"], info_dict["num_item"], info_dict["label_execute_time"])
        # print info_tupple
        info_tupple_list.append(info_tupple)

    return info_tupple_list


if __name__ == '__main__':

    ''' cluster cuda1 '''
    dir_name = "../data/us_log/jobs"
    info_file = "us_all_log_info.text"

    # ''' cluster cuda '''
    # dir_name = "../data/jobs"
    # info_file = "cn_cuda_log_info.text"

    landscape_info = get_landscape_info_from_dir(dir_name)
    dump_json_to_file(json_obj=landscape_info, filename=info_file)
    info = load_info_from_json_file(info_file)
    print sorted(info)









