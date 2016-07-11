import time

file_name = "ipcs"
fd = open(file_name, "r")

lines = fd.readlines()
ipc_dict = {}
id = 0

time_start = time.time()
for line in lines:
    ipc = line.strip("\n")
    ipc_dict[ipc] = id
    id += 1

print time.time() - time_start