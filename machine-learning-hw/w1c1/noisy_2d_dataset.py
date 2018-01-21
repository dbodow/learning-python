from numpy import random

MAX_X = 100
MIN_X = 0
RANGE_X = MAX_X - MIN_X

def noisy_2d_dataset(slope, intercept, stddev, num_points = 250):
    true_model = lambda x: slope * x + intercept
    xs = random.uniform(size = num_points) * RANGE_X + MIN_X
    noise = random.normal(size = num_points) * stddev
    ys = [true_model(x) + err for x, err in zip(xs, noise)]
    return list(zip(xs, ys))
