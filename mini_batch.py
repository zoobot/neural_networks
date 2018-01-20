# Question 1

# Calculate the memory size of train_features, train_labels, weights, and bias in bytes. Ignore memory for overhead, just calculate the memory required for the stored data.

# You may have to look up how much memory a float32 requires, using this link.

# train_features Shape: (55000, 784) Type: float32

# train_labels Shape: (55000, 10) Type: float32

# weights Shape: (784, 10) Type: float32

# bias Shape: (10,) Type: float32

# Question 2

# Use the parameters below, how many batches are there, and what is the last batch size?

# features is (50000, 400)

# labels is (50000, 10)

# batch_size is 128

#


from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

n_input = 784  # MNIST data input (img shape: 28*28)
n_classes = 10  # MNIST total classes (0-9 digits)

# Import MNIST data
mnist = input_data.read_data_sets('/datasets/ud730/mnist', one_hot=True)

# The features are already scaled and the data is shuffled
train_features = mnist.train.images
test_features = mnist.test.images

train_labels = mnist.train.labels.astype(np.float32)
test_labels = mnist.test.labels.astype(np.float32)

# Weights & bias
weights = tf.Variable(tf.random_normal([n_input, n_classes]))
bias = tf.Variable(tf.random_normal([n_classes]))
