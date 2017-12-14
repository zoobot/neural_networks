# Solution is available in the other "solution.py" tab
import numpy as np


def softmax(z):
    """Compute softmax values for each sets of scores in z."""
    #print(z)
    results = []
    total = 0
    for x in z:
        total = total + np.exp(x)


    for item in z:
        results.append((np.exp(item)) / total)

    return results

    # return np.exp(z) / np.sum(np.exp(z), axis=0)
    # TODO: Compute and return softmax(z)

# logits = [3.0, 1.0, 0.2]
# print(softmax(logits))

# logits is a one-dimensional array with 3 elements
logits = [1.0, 2.0, 3.0]
# softmax will return a one-dimensional array with 3 elements
print softmax(logits)
# $ [ 0.09003057  0.24472847  0.66524096]