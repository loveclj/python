from file_read import *


def perceptron(feature, label, learn_rate):

    row = feature.shape[0]
    col = feature.shape[1]
    w = np.zeros(col)
    trans_w = np.transpose(w)
    b = 0

    while True:
        error = 0
        for i in range(row):
            out = np.dot(feature[i], trans_w) + b

            if out*label[i] <= 0:
                trans_w += learn_rate * label[i] * np.transpose(feature[i])
                b += learn_rate * label[i]
                error += 1

        if error == 0:
            break

    return trans_w, b


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
    w, b = perceptron(matrix_feature, cluster_labels, learn_rate)

    print w
    print b

    # for i in range(matrix_feature.shape[0]):
    #     out = np.dot(matrix_feature[i], w) + b
    #     print out, cluster_labels[i]







