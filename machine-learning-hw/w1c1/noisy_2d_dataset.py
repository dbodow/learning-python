from numpy import random

"""
noisy_2d_dataset: (float => float), float, int => list_of_pairs_of_floats

given a true model, and
a standard deviation of a normal distribution (mean will be 0), and
optionally a number of points to simulate

simulates a dataset of (x,y) tuples w/ normal jitter added to the y's
"""

# Input Parameters
# Choose a range for the simulated x values
MAX_X = 100
MIN_X = 0

# Calculated intermediate values
RANGE_X = MAX_X - MIN_X

def noisy_2d_dataset(true_model, stddev, num_points = 250):
    xs = random.uniform(size = num_points) * RANGE_X + MIN_X
    noise = random.normal(size = num_points) * stddev
    ys = [true_model(x) + err for x, err in zip(xs, noise)]
    return list(zip(xs, ys))
