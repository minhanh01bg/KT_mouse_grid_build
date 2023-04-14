import math 
import numpy as np

# Define function to calculate Euclidean norm
def euclidean_norm(vector):
    sum = 0
    for i in vector:
        sum += i**2
    return math.sqrt(sum)

# Define function to calculate dot product
def dot(vector1, vector2):
    sum = 0
    for i in range(len(vector1)):
        sum += vector1[i] * vector2[i]
    return sum

def cosine_similarity(vector1, vector2):
    return np.dot(vector1, vector2) / (euclidean_norm(vector1) * euclidean_norm(vector2))
    # return np.dot(np.mean(vector1,axis=0), np.mean(vector2,axis=0)) / (euclidean_norm(vector1) * euclidean_norm(vector2))



vector1 = np.array([3, 4, 5])
vector2 = np.array([6, 8, 10])

# print(euclidean_norm(vector1))
# print(euclidean_norm(vector2))
# print(cosine_similarity(vector1, vector2))

