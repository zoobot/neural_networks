# Solution is available in the other "quiz_solution.py" tab
import tensorflow as tf

def get_weights(n_features, n_labels):
    # param n_features: Number of features
    # param n_labels: Number of labels
    weights = tf.Variable(tf.truncated_normal((n_features, n_labels)))
    return weights


def get_biases(n_labels):
    bias = tf.Variable(tf.zeros(n_labels))
    return bias


def linear(input, w, b):
    return tf.add(tf.matmul(input, w), b)
    # TODO: Linear Function (xW + b)
    xW = tf.matmul(input,w)
    linear_function =  tf.add(xW,b)
    return linear_function