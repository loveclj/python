from file_read import *


def gram_matrix(matrix):
    m_tranpose = np.transpose(matrix)
    return np.dot(matrix, m_tranpose)


def perceptron(feature, label, learn_rate):

    row = feature.shape[0]
    col = feature.shape[1]

    gram = gram_matrix(matrix_feature)

    n = np.zeros(row).reshape([row, 1])

    w = np.zeros(col)
    b = 0

    while True:
        error = 0
        for i in range(row):
            out = np.dot(gram[i], n) * learn_rate + b

            if out*label[i] <= 0:

                if label[i] > 0:
                    n[i] += 1
                else:
                    n[i] -= 1

                b += learn_rate * label[i]
                error += 1

        if error == 0:
            break

    return n, b


if __name__ == "__main__":

    filename = "./data/iris.data"

    lines = load_file(filename)

    matrix_feature, labels = extract_feature_label(lines)

    map_label = {"Iris-setosa":1, "Iris-versicolor":-1}

    cluster_labels = []
    for label in labels:
        if label == "Iris-setosa":
            cluster_labels.append(1)
        else:
            cluster_labels.append(-1)

    learn_rate = 0.1
    n, b = perceptron(matrix_feature, cluster_labels, learn_rate)

    # print n
    # print b

    w = learn_rate * np.dot(np.transpose(n), matrix_feature)
    print w
    w = np.transpose(w)

    for i in range(matrix_feature.shape[0]):
        out = np.dot(matrix_feature[i], w) + b
        print out, cluster_labels[i]







