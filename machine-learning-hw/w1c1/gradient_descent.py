from numpy import sum, array as np_sum, array
import mse

"""
gradient_descent: list_of_pairs_of_floats, pair => pair

given an observed dataset of (x, y) pairs,
and a pair of learning rate parameters (for A and B respectively),
uses gradient descent to estimate a linear model's alpha and beta

NOTE: uses the convention Y = alpha + beta X for a linear model
"""

def gradient_descent(dataset, learning_rates):
    xs, ys = array(dataset).T
    lambda_A, lambda_B = learning_rates
    num_points = len(dataset)

    errors = lambda a, b: np_sum(ys - a - b * xs)
    dMSE_dA = lambda a, b, errs: (-2 / num_points) * sum(errs)
    dMSE_dB = lambda a, b, errs: (-2 / num_points) * sum(xs * errs)
    report_epoch = lambda epoch, A, B, MSE: print(f"{epoch}, {A}, {B}, {MSE}")

    A, B = 0.0, 0.0
    # A, B = -20.0, -3.5 # Alternative start closer to test suite
    past_MSE = float('inf')
    print("EPOCH  |  A  |  B  |  MSE")
    print("-------------------------")
    for epoch in range(300):
        current_errors = errors(A, B)
        dA = dMSE_dA(A, B, current_errors)
        dB = dMSE_dB(A, B, current_errors)

        A -= lambda_A * dA
        B -= lambda_B * dB
        model = lambda x: A + B*x

        current_MSE = mse.mse(model, dataset)
        if epoch % 10 == 0:
            print(epoch, round(A, 2), round(B, 2), round(current_MSE, 2))

        if past_MSE < current_MSE:
            print('terminating due to model divergence')
            raise OverflowError('The model has diverged; lower lambdas')

        past_MSE = current_MSE

    return (A, B)
