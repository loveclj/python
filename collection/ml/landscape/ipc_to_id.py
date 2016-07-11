__author__ = 'lizhifeng'

def get_ipc_info(filename):
    fd = open(filename, "r")
    lines = fd.readlines()
    ipc_number = 0
    ipc_id = {}
    ipc_list = []
    for line in lines:
        ipc = line.strip('\n').decode("ascii").encode("utf-8")
        ipc_id[ipc] = ipc_number
        ipc_list.append(ipc)
        ipc_number += 1

    return ( ipc_number, ipc_list, ipc_id )


if __name__ == "__main__":

    ipc_table = get_ipc_info("ipcs")
    for (k, v) in ipc_table[2].items():
        print k, v

    for ipc in ipc_table[1]:
        print ipc
    print(ipc_table[0])