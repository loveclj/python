# __author__ = 'lizhifeng'
import multiprocessing
import pantent_preprocess
import search
import dynamodb_api
import aws4_signature
import os
from ipc_to_id import get_ipc_info
from string_utility import *


def worker(pid_pn, client, table_name, table_range_name, table_key_name, fields_type,bathch):
    pid = os.getpid()
    rlt = dynamodb_api.batch_get(client, pid_pn, table_name, table_range_name, table_key_name,
              fields_type, table_range="", batch=50)
    pid_ipc = pantent_preprocess.get_ipc_vector(rlt)

    ipc_info = get_ipc_info("ipcs")
    ipc_to_id = ipc_info[2]
    file_name = "file_" + str(pid)
    fd = open(file_name,"w")
    for pid, ipcs in pid_ipc.items():
        line = ""
        line += pid
        ipc_vector = set()
        for ipc in ipcs:
            try:
                split_ipc(ipc, '/', ipc_vector)
            except:
                print ipc

        for v in ipc_vector:
            try:
                print v,
                line += " " + str(ipc_to_id[v])
            except:
                continue
        print ipc_vector
                # print pi

        line += "\n"
       # print line
        fd.write(line.encode("ascii", "ignore"))

    fd.close()


if __name__ == "__main__":

    p = search.SearchSolr()
    pid_pn = p.get_pid_pn()

    client = aws4_signature.GetDynamodbClient()
    table_name = "patent_biblio"
    table_range_name = ""
    table_key_name = "patent_id"
    fields_type = ["patent_id", "ipc", "ipcr"]

    thread_num = 1
    pid_pn_split = []
    for i in range(thread_num):
        pid_pn_split.append({})

    count = 0
    for pantent_id,pn in pid_pn.items():
        pid_pn_split[count%thread_num][pantent_id] = pn
        count += 1

    jobs = []
    for i in range(thread_num):
        p = multiprocessing.Process(target=worker, args=(pid_pn_split[i], client, table_name, table_range_name, table_key_name, fields_type, 50))
        jobs.append(p)
        p.start()

    for p in jobs:
        p.join()
        print p.exitcode
