def mse(slope, intercept, xs, ys):
    model = lambda x: float(slope) * x + float(intercept)
    error = 0
    for x, y in zip(xs, ys):
        error += squared_error(x, y, model)
    return error / len(xs)

def squared_error(x, y, model):
    y_hat = model(x)
    return (y - y_hat) ** 2
