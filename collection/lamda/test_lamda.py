#!/usr/bin/env python
# coding=utf-8

import boto3
import time

if __name__ == "__main__":

        label_lang = "label_en"
        label = "as;dx"
        landscape_feature_table = "landscape_feature_sync"

        client = boto3.client('dynamodb')

        patent_id = "sadfadf"
        current_time_in_ms = int(time.time() * 1000)

        updateExpression = "SET " + label_lang + "=:val1," \
                           "updated_ts=:val2," \
                           "created_ts = if_not_exists(created_ts,:val2)" \
                           "ADD version  :val3"

        expressionAttributesValues = {
            ":val1": {"S": label},
            ":val2": {"S": str(current_time_in_ms)},
            ":val3": {"N": "1"}
        }

        response = client.update_item(TableName=landscape_feature_table,
                                      Key={'patent_id': {'S': patent_id}},
                                      UpdateExpression=updateExpression,
                                      ExpressionAttributeValues=expressionAttributesValues)
        print response
