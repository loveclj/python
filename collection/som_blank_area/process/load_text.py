#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: load_text.py
@time: 4/12/16 2:01 PM
"""
import ipc2upc
import dynaodb_access
import label_process
import sys


def swap_key_value(key_value):
    value_key = {}
    for k, v in key_value.items():
        value_key[v] = k

    return value_key


def load_map_from_text(filename):
    key_value = {}
    with open(filename, "r") as fd:
        lines = fd.readlines()
        for line in lines:
            elements = line.strip('\n').split()
            key_value[elements[0]] = elements[1]

    return key_value


def dump_map_to_text(key_value, filename):
    fd = open(filename, "w")

    keys = key_value.keys()
    sorted_keys = sorted(keys, key=eval )
    for key in sorted_keys:
        line = key + " " + key_value[key] + '\n'
        fd.write(line)

    fd.close()


def load_matrix(filename):
    matrix = {}
    with open(filename, "r") as fd:
        lines = fd.readlines()

        row = 0
        for line in lines:
            elements = line.strip('\n').split()
            matrix[row] = []
            for element in elements:
                matrix[row].append(eval(element))

            row += 1

    return matrix


def sub_vector(v1, v2):
    diff = []
    size = len(v1)
    for i in range(size):
        diff.append(v1[i] - v2[i])

    return diff


def grid_ipc_freq():
    pass


def load_pid2ipc(prefix_name, num):
    pid2ipc = {}
    for i in range(num):
        filename = prefix_name + str(i) + ".text"

        with open(filename, "r") as fd:
            lines = fd.readlines()

            line_count = len(lines)

            for j in range(line_count/2):
                pid = lines[2*j].strip('\n')
                ipcs = lines[2*j+1].strip('\n').split()
                pid2ipc[pid] = ipcs

    return pid2ipc


def load_grid2pid(prefix_name, num):
    grid2pid = {}
    for i in range(num):
        filename = prefix_name + str(i) + ".text"

        grid2pid[i] = []

        try:
            with open(filename, "r") as fd:
                lines = fd.readlines()

                line_count = len(lines)

                for j in range(line_count):
                    grid2pid[i].append(lines[j].strip('\n'))
        except:
            pass

    return grid2pid


def grid2ipc_freq(pid2ipc, grid2pid):
    grid2ipc = {}
    for grid, pids in grid2pid.items():
        grid2ipc[grid] = {}
        for pid in pids:
            ipcs = pid2ipc[pid]
            for ipc in ipcs:

                if ipc in grid2ipc[grid].keys():
                    grid2ipc[grid][ipc] += 1
                else:
                    grid2ipc[grid][ipc] = 1

    return grid2ipc


def split_ipcs_to_feature(ipcs):
    feature = []
    for ipc in ipcs:
        feature.append(ipc[:1])
        feature.append(ipc[:3])
        feature.append(ipc[:4])
        feature.append(ipc)

        e = ipc.split('/')[0]
        if len(e)  != 4:
            e += '/'
        feature.append(e)

    return sorted(list(set(feature)))


def get_max_weight_ipc(ipcs):
    ipcs_sorted = sorted(ipcs)
    max_ipcs = []

    size = len(ipcs_sorted)

    for i in range(size):
        if i == size - 1:
            max_ipcs.append(ipcs_sorted[i])
        else:
            if ipcs_sorted[i+1].startswith(ipcs_sorted[i]):
                continue
            else:
                max_ipcs.append(ipcs_sorted[i])

    return max_ipcs


def dump_blank_grid_pid(grid2pid, filename="../text/whitespace_bmu.text"):
    with open(filename, "w") as fd:

        for grid, pids in grid2pid.items():
            line = str(grid) + " "
            for pid in pids:
                line += pid + " "
            line += '\n'
            fd.write(line)




def find_bmu_blank(pid2ipc, codebook, grid2pid, term2Gid, grid_num):

    blank_grid2ipc = {}
    for pid, ipcs in pid2ipc.items():
        terms = split_ipcs_to_feature(ipcs)

        gids = []

        for term in terms:
            gids.append(term2Gid[term])

        min = sys.float_info
        bmu = 0

        no_empty_grids = []
        for i in range(grid_num):
            if  grid2pid[i]:
                no_empty_grids.append(i)

        for i in range(grid_num):
            dist = 0.0
            for gid in gids:
                diff = 1 - codebook[i][eval(gid)]
                dist += diff * diff

            if dist < min:
                if i in no_empty_grids:
                    print no_empty_grids
                    print pid, i
                    continue

                min = dist
                bmu = i

        if bmu in blank_grid2ipc.keys():
            blank_grid2ipc[bmu].append(pid)
        else:
            blank_grid2ipc[bmu] = []
            blank_grid2ipc[bmu].append(pid)

    return blank_grid2ipc


if __name__ == '__main__':
    term2gid = load_map_from_text("../text/term2Gid.text")
    gid2term = swap_key_value(term2gid)
    print term2gid
    print gid2term
    dump_map_to_text(gid2term, "../text/gid2term.text")
    matrix = load_matrix("../text/codebook.text")
    #

    pid2ipc = load_pid2ipc("../text/pid2ipc", 1)
    print pid2ipc
    grid2pid = load_grid2pid("../text/grid2pid", 35)
    print grid2pid

    grid2ipc = grid2ipc_freq(pid2ipc, grid2pid)
    print grid2ipc


    N = 10
    topN = {}
    for row, vector in matrix.items():
        matrix_sorted = sorted(vector, reverse=True)

        threashold = matrix_sorted[N]
        topN[row] = []
        for index, element in enumerate(vector):
            if element > threashold:
                topN[row].append(index)
        # print row, matrix_sorted
        # print row, vector
    print topN

    # for row, vector in topN.items():
    #     print row
    #
    #     for pid in grid2pid[row]:
    #         feature = split_ipcs_to_feature(pid2ipc[pid])
    #         print feature
    #
    #     for element in vector:
    #         print gid2term[str(element)], matrix[row][element],
    #     print
    #
    # ipc_upc = ipc2upc.load_ipc2upc("../text/ipc2upc.text")
    #
    #
    # blank_area_ipcs = {}
    # for row, vector in topN.items():
    #     if grid2pid[row]:
    #         continue
    #
    #     indexes = topN[row]
    #     ipcs = []
    #
    #
    #     for index in indexes:
    #
    #         ipcs.append(gid2term[str(index)])
    #
    #
    #     blank_area_ipcs[row] = get_max_weight_ipc(ipcs)
    #
    # print blank_area_ipcs
    #
    # grid2label = {}
    #
    # for grid, ipcs in blank_area_ipcs.items():
    #     print ipcs
    #     words_freq = dynaodb_access.get_label_by_ipc(ipcs)
    #
    #     labels = ""
    #
    #     for words in words_freq.keys():
    #         labels += words.upper() + ";"
    #
    #     grid2label[grid] = labels
    #
    #
    # label_process.dumps_map(grid2label, "../blank_label.text")



    blank2pid = find_bmu_blank(pid2ipc, matrix, grid2pid, term2gid, 35)
    dump_blank_grid_pid(blank2pid)














    # print sorted(sub_vector(matrix[0], matrix[1]), reverse=True)
    # print sorted(sub_vector(matrix[1], matrix[2]), reverse=True)
    # print sorted(sub_vector(matrix[2], matrix[9]), reverse=True)
    # print sorted(sub_vector(matrix[0], matrix[7]), reverse=True)

