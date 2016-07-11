#__author__ = 'lizhifeng'
#coding=utf-8

from aws4_signature import GetDynamodbClient
from utility import binary2string


def get_patent_ids_from_file(patent_file):
    fd = open(patent_file)
    _patent_list = []
    for line in fd.readlines():
        patent = line.strip('\n')
        _patent_list.append(patent)

    return _patent_list


def batch_get(client, patent_ids, table_name, table_range, table_key, content, language="EN", batch=10):
    _request = {table_name: {}}
    _request[table_name]["Keys"] = []

    rlt = {}
    i = 0
    count = 0
    patent_num = len(patent_ids)
    for patent_id in patent_ids:

        key_dict = {"patent_id": {}}
        key_dict["patent_id"]["S"] = patent_id

        _request[table_name]["Keys"].append(key_dict)
        _request[table_name]["Keys"][i]["lang"] = {"S": language}

        i += 1
        count += 1

        if i == batch or count == patent_num:

            _response = client.batch_get_item(RequestItems=_request)
            parse_batch_get(_response, rlt, table_name, table_range, table_key, content)

            i = 0
            _request[table_name]["Keys"] = []

    return rlt


def parse_batch_get(response, rlt, table_name, table_range, table_key, content):

    for item in response["Responses"][table_name]:
        _lang = item[table_range]["S"]
        _patent_id = item[table_key]["S"]
        _content = item[content]["B"]

        _content = binary2string(_content)

        _key = _patent_id + _lang
        rlt[_key] = _content


def query_pn(client, pn_list, table_name, field):
    key_conditions = {"pn": {}}
    key_conditions["pn"]["AttributeValueList"] = []

    key_attribute = {'S': ""}
    key_conditions["pn"]["AttributeValueList"].append(key_attribute)
    key_conditions["pn"]["ComparisonOperator"] = 'EQ'

    patent_ids = []

    for pn in pn_list:
        if pn == "":
            continue
        key_conditions["pn"]["AttributeValueList"][0]["S"] = pn
#        print key_conditions
        _response = client.query(TableName=table_name, IndexName="pn-index", KeyConditions=key_conditions)
        parse_query_pn(_response, patent_ids, field)

    return patent_ids


def parse_query_pn(response, patent_ids, field):
    for item in response[u'Items']:
        patent_ids.append(item[field][u'S'])


def generate_pid_by_pn(pn_file, patent_file):
    client = GetDynamodbClient()
    pn_list = get_patent_ids_from_file(pn_file)
    pid_list = query_pn(client, pn_list, "patent", "patent_id")
    fd = open(patent_file, "w")
    for pid in pid_list:
        fd.write(pid + '\n')
    fd.close()