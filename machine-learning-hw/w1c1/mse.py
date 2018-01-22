"""
mse: (float => float), list_of_pairs_of_floats

given a proposed linear model, and
a list of observed (x, y) pairs

returns the Mean Squared Error of the proposed model for the dataset
"""

def mse(model, dataset):
    error = 0
    for x, y in dataset:
        error += squared_error(x, y, model)
    return error / len(dataset)

def squared_error(x, y, model):
    y_hat = model(x)
    return (y - y_hat) ** 2
