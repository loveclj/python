#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: gather_en_cn_label.py
@time: 5/16/16 11:41 AM
"""


import codecs
import commands
import re
import time


def list_dir(dir):

    cmd = "ls " + dir
    status, output = commands.getstatusoutput(cmd)
    file_list = output.split()

    for i in range(len(file_list)):
        file_list[i] = dir + "/" + file_list[i]

    return file_list


def load_stopwords(filename):

    with codecs.open(filename, "r", "utf-8") as fd:
        stopwords = set()

        lines = fd.readlines()
        for line in lines:
            word = line.strip("\n")
            stopwords.add(line)

        return stopwords


def load_en_cn_dict(filename):
    en_cn_dict = {}

    with codecs.open(filename, "r", "utf-8") as fd:
        lines = fd.readlines()
        for line in lines:
            try:
                en_word, cn_word = line.strip("\n").split(":")

                en_word = en_word.strip().replace('=', "-")
                cn_word = cn_word.strip().split('=')
                cn_word = u"".join(cn_word).replace(" ", "")

                if cn_word and en_word:
                    en_cn_dict[en_word] = cn_word

            except:
                print line

    return en_cn_dict

def get_cn_pids(filename):
   cn_pids = set()
   with codecs.open(filename, "r", "utf-8") as fd:
	while True:
 		line = fd.readline()
		if not line:
			break
		pid = line.split(":")[0]
		cn_pids.add(pid)
	return cn_pids 
	



def load_en_label_from_file(filename, pid2label, stopwords, word_len_low_limit=4):

    with codecs.open(filename, "r", "utf-8") as fd:
        for line in fd.readlines():
            line = line.strip().replace('=', '-').split(":")
            pid = line[0]
            label_origin = set(u",".join(line[1:]).split(","))

            label = set()

            for w in label_origin:
                if len(w) < word_len_low_limit:
                    continue
                else:
                    w = w.strip("[|]|")

                    if w not in stopwords:
                        label.add(w)

            if label:
                pid2label[pid] = label
                # print label
            # else:
            #     print pid, label_origin, line


def load_cn_label_from_file(filename, pid2label, stopwords, word_len_low_limit=2, word_len_high_limit=7):

    count = 0
    pattern = re.compile(r"\d+")
    with codecs.open(filename, "r", "utf-8") as fd:
        while True:
            line = fd.readline().strip("\n")
            if not line:
                break

            line = line.split(":")

            pid = line[0]
            label_orgin = set(line[1].split(","))

            # filter meaningless word
            label = set()
            for w in label_orgin:
                word_len = len(w)
                if word_len < word_len_low_limit or word_len > word_len_high_limit:
                    continue

                if w in stopwords:
                    continue

                if pattern.findall(w):
                    continue

                label.add(w)

            # build pid2label
            if label:
                pid2label[pid] = label
	    
	    count += 1

	    if count %10000 == 0:
		print count


def trans_en_to_cn(en_pid2label, cn_pids, translate_label, cn_stopwords, en_cn_dict):

    en_pids = set(en_pid2label.keys())

    find_count = 0
    not_fount_count = 0
    for pid in en_pids:

        # cn label exists, no need translate
        if pid in cn_pids:
	    print "find", pid
            continue

        cn_label = set()
        for en_word in en_pid2label[pid]:

            if en_cn_dict.get(en_word):
                trans_word = en_cn_dict[en_word]

                if trans_word not in cn_stopwords:
                    cn_label.add(trans_word)

                find_count += 1

            else:
                not_fount_count += 1
                en_word = en_word.split(" ")
                for w in en_word:
                    if en_cn_dict.get(w):
                        trans_word = en_cn_dict[w]
                        if trans_word not in cn_stopwords:
                            cn_label.add(trans_word)

        if cn_label:
            translate_label[pid] = cn_label

    print find_count
    print not_fount_count


def dumps_pid2label_to_file(fd, pid2label):

    # with codecs.open(filename, "w", "utf-8") as fd:
        for k, v in pid2label.items():
            line = ":" + u";".join(v) + "\n"
            line = line.upper()
	    line = k + line
            fd.write(line)


if __name__ == '__main__':

    en_stopwords = load_stopwords("enStopwords.text")
    cn_stopwords = load_stopwords("cnStopwords.text")

    en_cn_dict = load_en_cn_dict("en_cn_dict_new.text")
	

    cn_write_fd = codecs.open("update_cn_label.text", "w", "utf-8")
    en_write_fd = codecs.open("update_en_label.text", "w", "utf-8")
    
    cn_pids = get_cn_pids("cn_label_new.text")

    cn_pid2label = {}
#    load_cn_label_from_file(filename="cn_label.text", pid2label=cn_pid2label, stopwords=cn_stopwords)
#    load_cn_label_from_file(filename="cn_label_100k.text", pid2label=cn_pid2label, stopwords=cn_stopwords)
#    dumps_pid2label_to_file(cn_write_fd, cn_pid2label)

    en_data_dir = "./en_label"
    en_file_list = list_dir(en_data_dir)
    for file in en_file_list:

	start = time.time()
        en_pid2label = {}
        translate_label = {}
        load_en_label_from_file(filename=file, pid2label=en_pid2label, stopwords=en_stopwords)
        trans_en_to_cn(en_pid2label, cn_pids, translate_label, cn_stopwords, en_cn_dict)

        dumps_pid2label_to_file(cn_write_fd, translate_label)
        dumps_pid2label_to_file(en_write_fd, en_pid2label)
        print file, time.time()-start

    cn_write_fd.close()
    en_write_fd.close()






    # dumps_pid2label_to_file("update_cn_label.text", cn_pid2label)
    # dumps_pid2label_to_file("update_en_label.text", en_pid2label)

