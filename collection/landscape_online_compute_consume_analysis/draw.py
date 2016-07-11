#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: draw.py
@time: 6/6/16 4:17 PM
"""
import datetime
import time
import matplotlib.pyplot as plt

from text_process import load_info_from_json_file


def convert_date_to_sec(s):
    d = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    sec = time.mktime(d.timetuple())
    return sec


def preprocess_info_tupple_list(infos):
    processed_info = []
    for i in infos:
        print i[0]
        time_start = int(convert_date_to_sec(i[0]))
        time_end = int(convert_date_to_sec(i[1]))
        nProcs = int(i[2])
        item_count = int(i[3])
        label_execute_time = float(i[4])

        item = (time_start, time_end, nProcs, item_count, label_execute_time)
        processed_info.append(item)

    return sorted(processed_info)


def time_nProc_and_time_item_count_plot(infos, duration, time_step=1):

    first_log_time_begin = infos[0][0]/time_step
    last_log_time_end = infos[-1][1]/time_step

    if duration <= 0:
        duration = last_log_time_end - first_log_time_begin

    loop_count = 0

    x_time = range(duration/time_step)

    y_item_count = []
    y_nProcs = []

    for x in x_time:

        # if x%10000 == 0:
        #     print x/10000

        total_nprocs = 0
        item_count = 0

        for i in infos:
            if x + first_log_time_begin < i[0]/time_step:
                break

            if x + first_log_time_begin <= i[1]/time_step:

                total_nprocs += i[2]

                single_log_time_duration = i[1]/time_step - i[0]/time_step

                if single_log_time_duration:
                    item_count += float(i[3]) / i[4]
                    # item_count += float(i[3]) / single_log_time_duration
                else:
                    item_count += float(i[3])

            else:
                continue

        # if total_nprocs >= 12:
        #     print total_nprocs
        y_item_count.append(item_count/100/time_step)
        y_nProcs.append(float(total_nprocs)/time_step)

    return x_time, y_item_count, y_nProcs


def draw_scatter(title, x, y, y_label, x2, y2, y2_label):
    fig = plt.figure()

    # figure, ax = plt.subplots()
    # ax.set_title(title)

    x_y = plt.subplot(211)
    x2_y2 = plt.subplot(212)

    plt.sca(x_y)
    plt.scatter(x, y)
    x_max = max(x) + 1
    y_max = int(max(y)) + 1
    plt.xlabel("minute")
    plt.ylabel(y_label)
    plt.axis([0, x_max, 0, y_max])

    plt.sca(x2_y2)
    plt.scatter(x2, y2)
    x2_max = max(x2) + 1
    y2_max = int(max(y2)) + 1
    plt.xlabel("minute")
    plt.ylabel(y2_label)
    plt.axis([0, x2_max, 0, y2_max])

    plt.suptitle(title)

    plt.show()


def range_overlap_count(infos):

    item_count = len(infos)

    overlap_count_list = [0] * item_count

    if item_count <= 1:
        return overlap_count_list

    for i in range(item_count - 1):
        for j in range(i+1, item_count):
            if infos[i][1] > infos[j][0]:
                overlap_count_list[i] += 1
                overlap_count_list[j] += 1
            else:
                break

    return overlap_count_list


if __name__ == '__main__':

    # ''' cn cluster cuda1 '''
    # info_log_file = "cn_cuda1_log_info.text"

    # ''' cn cluster cuda '''
    # info_log_file = "cn_cuda_log_info.text"

    # ''' cn cluster cuda '''
    # info_log_file = "cn_all_log_info.text"

    ''' us cluster cuda '''
    info_log_file = "us_all_log_info.text"

    info = load_info_from_json_file(info_log_file)

    processed_info = preprocess_info_tupple_list(info)

    time_step = 60
    duration = 3600 * 24 * 7 * 4
    title = "landscape us cluster"

    x, y1, y2 = time_nProc_and_time_item_count_plot(processed_info, duration, time_step)

    draw_scatter(title, x[:duration], y1, "read throughoutput per sec", x[:duration], y2, "cpu count per sec")


    # overlap_count_list = range_overlap_count(processed_info)
    #
    # for i in range(len(overlap_count_list)):
    #     if overlap_count_list[i] == 11:
    #         print i
    #         print processed_info[i]

    # max_differ = -1
    # id = 0
    # for i in range(len(overlap_count_list)-1):
    #     time_diff = processed_info[i+1][0] - processed_info[i][0]
    #     print time_diff
    #     if time_diff > max_differ:
    #         max_differ = time_diff
    #         id = i
    #
    # print max_differ
    # print processed_info[id]
    # print processed_info[id+1]




