#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: test.py
@time: 8/18/16 3:58 PM
"""

from keras.layers import Input, Dense
from keras.models import Model
import numpy as np
from keras import backend

def singal(x):
    # return (backend.sign(x) + 1)/2
    return x
    # if x < 0.5:
    #     return 0
    # else:
    #     return 1


def load_matrix(file_name, train_sample_count,  test_sample_count):
    i = 0

    train_matrix = []
    test_matrix = []

    for line in open(file_name):
        vec = []
        id, fp = line.strip('\n').split(',')
        for v in fp:
            vec.append(int(v))

        if i < train_sample_count:
            train_matrix.append(vec)
        elif i < train_sample_count + test_sample_count:
            test_matrix.append(vec)
        else:
            break

        i += 1

    return np.array(train_matrix), np.array(test_matrix)


dim1 = 440
dim2 = 220
dim3 = 110
dim4 = 55

encoding_dim = 2
input_vec = Input(shape=(881, ))

encode_active_fun = 'sigmoid'
decode_active_fun = 'relu'
# decode_active_fun = signal

encoded = Dense(dim1, activation=encode_active_fun)(input_vec)
encoded = Dense(dim2, activation=encode_active_fun)(encoded)
encoded = Dense(dim3, activation=encode_active_fun)(encoded)
encoded = Dense(dim4, activation=encode_active_fun)(encoded)

encoded = Dense(encoding_dim, activation=encode_active_fun)(encoded)  # compress

decoded = Dense(dim4, activation=encode_active_fun)(encoded)
decoded = Dense(dim3, activation=encode_active_fun)(decoded)
decoded = Dense(dim2, activation=encode_active_fun)(decoded)
decoded = Dense(dim1, activation=encode_active_fun)(decoded)

decoded = Dense(881, activation=decode_active_fun)(encoded)  # decompress

autoencoder = Model(input=input_vec, output=decoded)

autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')
encoder = Model(input=input_vec, output=encoded)

encoded_input = Input(shape=(encoding_dim,))
decoder_layer = autoencoder.layers[-1]
decoder = Model(input=encoded_input, output=decoder_layer(encoded_input))

if __name__ == '__main__':
    feature_file = '../file_convert/chemical_data_10k'
    train_set, test_set = load_matrix(file_name=feature_file, train_sample_count=9900, test_sample_count=10)
    print train_set.shape

    autoencoder.fit(train_set, train_set,
                    nb_epoch=1000,
                    batch_size=10,
                    shuffle=True,
                    validation_data=(test_set, test_set))

    encode_vec = encoder.predict(test_set)
    print encode_vec

    output = decoder.predict(encode_vec)
    for i in range(10):
        z = 0
        k = 0

        for j in range(881):

            if test_set[i][j] == 1 or output[i][j] > 0.5:

                diff = test_set[i][j] - output[i][j]
                if abs(diff) > 0.2:
                    # print diff
                    z += 1
                else:
                    # print "xxx"
                    k += 1
        print z, k


        # break