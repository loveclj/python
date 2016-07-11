# __author__ = 'lizhifeng'

import search
import dynamodb_api
import aws4_signature



def get_ipc_vector(rlt):
    pid_ipc = {}

    for res in rlt:
        # try:
            #res_json = json.loads(res_str)
            response = res["Responses"]
            for item in response["patent_biblio"]:
                ipc_vector = []
                if "ipcr" in item.keys():
                    ipcr_list = item["ipcr"]["L"]
                    for ipcr in ipcr_list:
                        ipc_vector.append(ipcr["M"]["code"]["M"]["full"]["S"])

                if "ipc" in item.keys():
                    ipc_list = item["ipc"]["L"]
                    for ipc in ipc_list:
                        ipc_vector.append(ipc["M"]["code"]["M"]["full"]["S"])

                if ipc_vector:
                    patent_id = item["patent_id"]["S"]
                    pid_ipc[patent_id] = ipc_vector

    return pid_ipc


if __name__ == "__main__":
    p = search.SearchSolr()
    pid_pn = p.get_pid_pn()

    client = aws4_signature.GetDynamodbClient()
    table_name = "patent_biblio"
    table_range_name = ""
    table_key_name = "patent_id"
    fields_type = ["patent_id", "ipc", "ipcr"]

    rlt = dynamodb_api.batch_get(client, pid_pn, table_name, table_range_name, table_key_name,
              fields_type, table_range="", batch=50)

    pid_ipc = get_ipc_vector(rlt, 0, 1)
