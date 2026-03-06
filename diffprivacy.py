import numpy as np

true_avg = 40000
epsilon = 1.0  # privacy budget
sensitivity = 10000

scale = sensitivity / epsilon
noise = np.random.laplace(0, scale)

private_avg = true_avg + noise

print("True Average:", true_avg)
print("Private Average:", private_avg)
