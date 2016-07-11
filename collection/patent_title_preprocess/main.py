#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: main.py
@time: 4/26/16 4:13 PM
"""

import time
import multiprocessing
import codecs

import process
import scanner


def get_pid2title(items_list, lang):


    pid2title = {}
    if not items_list:
        return pid2title

    for item in items_list:
        if lang != item['lang']:
            continue

        pid = item[u'patent_id']
        title = process.binary2string(item[u'title'])

        pid2title[pid] = title

    return pid2title


def extract_keywords(pid2title, lock, parser, stopwords):

    pid2keywords = {}
    fail_pids = []
    for pid, title in pid2title.items():
        try:
            # title = title.decode('utf-8').encode('ascii')
            keywords = process.split_as_phrase(title, parser, stopwords)
            pid2keywords[pid] = keywords
        except:

            fail_pids.append(pid)

    return pid2keywords, fail_pids


def dump_to_file(pid2keywords, pids, pid2title):
    minitues = int(time.time()/60)
    filename = "./result/" + str(minitues) + ".text"

    keywords_fd = codecs.open(filename, "a", 'utf-8')
    # keywords_fd = open(filename, "a")
    fail_fd = codecs.open("fail_pids.text", "a", "utf-8")

    for pid, keywords in pid2keywords.items():
        try:
            # print pid
            # print keywords
            line = u"" + pid + u":" + keywords + u"\n"

            keywords_fd.write(line)

            # keywords_fd.write(pid + u":")
            # keywords_fd.write(keywords)
            # keywords_fd.write(u"\n")

        except UnicodeDecodeError:
            pids.append(pid)
            print pid
            print keywords
            # print UnboundLocalError.message

    print "===="
    print pids
    for pid in pids:
        try:
            line = pid + "\n"
            fail_fd.write(line)
        except UnicodeDecodeError:
            print pid,
            # print UnicodeDecodeError.message


    # keywords_fd.close()
    # fail_fd.close()


def extract_process(pid2title, parser, stopwords, lock):
    # print "process start"
    pid2keywords, fail_pids = extract_keywords(pid2title, lock, parser, stopwords)
    print fail_pids

    lock.acquire()
    dump_to_file(pid2keywords, fail_pids, pid2title)

    lock.release()

    pass
if __name__ == '__main__':

    # parameter of key-phrase split

    lang = "EN"
    grammar = "NP: {<NNS|NN|NNP|NNPS|JJ><NN|NNS>}"

    parser = process.sentence_parse(grammar)
    stopwords = process.load_list("stopwords.text")

    # dynamodb

    tablename = "patent_title"
    attribute_get = ['lang', 'patent_id', 'title']
    title_scanner = scanner.Scanner(tablename, attribute_get)

    # process

    lock = multiprocessing.Lock()
    process_count = 3



    lastkey  = {}

    start = time.time()
    items, lastkey = title_scanner.scan(lastkey)

    pid2title = get_pid2title(items, lang)

    pid2title_list = [{} for i in range(process_count)]
    pid2title_list[0] = pid2title

    while True:


        start = time.time()
        processes = [multiprocessing.Process(target=extract_process, args=(pid2title_list[i], parser, stopwords, lock))
                     for i in range(process_count)]



        for p in processes:
            p.start()

        for p in processes:
            p.join()
        # for i in range(process_count):
            # pid2title_loc = pid2title[i::process_count]
            # pool.apply_async(extract_process, (1, 1, 1, 1,))
            # pool.apply_async(extract_process, (pid2title[i::process_count], parser, stopwords, lock))

        print time.time() - start

        if not lastkey:
            break

        start = time.time()
        for i in range(process_count):
            if not lastkey:
                pid2title_list[i] = {}
                continue

            items, lastkey = title_scanner.scan(lastkey)

            pid2title = get_pid2title(items, lang)
            pid2title_list[i] = pid2title

        print time.time() - start







