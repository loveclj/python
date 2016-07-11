#__author__ = 'lizhifeng'
#coding=utf-8

from aws4_signature import GetDynamodbClient
# from utility import binary2string


def batch_get(client, pid_pn, table_name, table_range_name="", table_key_name="patent_id",
              fields_type=None, table_range="", batch=10):
    _request = {table_name: {}}
    _request[table_name]["Keys"] = []
    if len(fields_type) != 0:
            project_expression = ",".join(fields_type)
            _request[table_name]["ProjectionExpression"] = project_expression

    rlt = []

    i = 0
    count = 0
    patent_num = len(pid_pn)
    patent_ids = pid_pn.keys()
    for patent_id in patent_ids:

        key_dict = {table_key_name: {}}
        key_dict[table_key_name]["S"] = patent_id

        _request[table_name]["Keys"].append(key_dict)
        if table_range != "":
            _request[table_name]["Keys"][i]["lang"] = {"S": range}

        i += 1
        count += 1

        if i == batch or count == patent_num:

            # print _request
            _response = client.batch_get_item(RequestItems=_request)
            rlt.append(_response)

            # parse_batch_get(_response, rlt, table_name, table_range_name, table_key_name, fields_type)

            i = 0
            _request[table_name]["Keys"] = []

    return rlt


def parse_batch_get(response, rlt, table_name, table_range_name="", table_key="patent_id", field_type_dict=""):

    _fields = field_type_dict.keys()
    for item in response["Responses"][table_name]:

        _key = item[table_key]["S"]
        if table_range_name != "":
            _range = item[table_range_name]["S"]
            _key += _range

        for _field in _fields:
            _type = field_type_dict[_field]
            _content = item[_field][_type]
            rlt[_field][_key] = _content

