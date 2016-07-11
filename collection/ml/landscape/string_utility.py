
def split_ipc(ipc, dmt, ipc_vector):
    # dmt += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:
        if dmt not in ipc:
            return ipc

        i = 0
        ipc_len = len(ipc)
        ipc_vector.add(ipc[0])
        i += 1
        while i < ipc_len:
            if ipc[i] not in "0123456789":
                break
            i += 1

        ipc_vector.add(ipc[0:i])
        ipc_vector.add(ipc[0:i + 1])

        i += 1

        while i < ipc_len:
            if ipc[i] == dmt:
                break
            i += 1

        ipc_vector.add(ipc[0:i])
        ipc_vector.add(ipc)

        pass
    except:
        pass

if __name__ == "__main__":
     #ipcs = split_ipc("A01", '/')
    fd = open("patent_classifcation_ipc", "r")
    lines = fd.readlines()
    full = 0
    for line in lines:
        if '/' not in line:
            full += 1
            continue
        ipc = line.strip('\n')
        ipc_vector = split_ipc(ipc, '/')
        for v in ipc_vector:
            print v
    # print full

       # print ipc_vector
     #print(ipcs)


