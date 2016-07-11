#!/usr/bin/env python
# coding=utf-8

import json
import codecs
import random


def remove_dumplicate(infilename, outfilename):
    infd = codecs.open(infilename, "r", "utf-8")
    outfd = codecs.open(outfilename, "w", "utf-8")

    cur_pid = ""
    pre_pid = ""

    total_count = 0
    dumplicate_count = 0
    while True:
        line = infd.readline()

        if not line:
            break

        label = json.loads(line.strip('\n'), encoding="utf-8")
        cur_pid = label['patent_id']

        if cur_pid == pre_pid:
            print line,
            dumplicate_count += 1
            continue
        else:
            pre_pid = cur_pid
            outfd.write(line)
            total_count += 1

    print total_count
    print dumplicate_count
    outfd.close()
    infd.close()


def add_random_num_at_begin(infilename, outfilename):
    infd = codecs.open(infilename, mode="r", encoding="utf-8")
    outfd = codecs.open(outfilename, mode="w", encoding="utf-8")

    i = 0
    while True:
        line = infd.readline()
        if not line:
            break

        rand_num = random.random()

        outfd.write(str(rand_num) + ":" + line)
        print rand_num

        if i < 1000000:
            i += 1
        else:
            break

    infd.close()
    outfd.close()

if __name__ == "__main__":
    origin_file = "label_json.text"
    processed_file = "label_json_with_no_duplicate.text"

    add_num_filename ="label_json_with_no_duplicate_with_num.text"
    # remove_dumplicate(origin_file, processed_file)
    add_random_num_at_begin(processed_file, add_num_filename)


