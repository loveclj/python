#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: dict_vector.py
@time: 9/23/16 10:43 AM
"""



# 转换器用于数据预处理和数据转换，主要是三个方法：

# fit()：训练算法，设置内部参数。
# transform()：数据转换。
# fit_transform()：合并fit和transform两个方法。
from sklearn.feature_extraction import DictVectorizer
onehot_encoder = DictVectorizer()

instance = [{'city': 'Beijing', 'Nation': 'China'},
            {'city': 'Shanghai', 'Country': 'China'},
            {'city': 'Suzhou', 'Nation': 'China'}]

# print onehot_encoder.fit_transform(instance).toarray()
print onehot_encoder.fit(instance)
print onehot_encoder.transform(instance).toarray()
if __name__ == '__main__':

    pass