from behave import *
from scipy.stats import norm

import gradient_descent as gd
import noisy_2d_dataset as ds
import mse

@given('alpha is {alpha} and beta is {beta}')
def step_impl(ctx, alpha, beta):
    ctx.alpha = float(alpha)
    ctx.beta = float(beta)
    ctx.true_model = lambda x: ctx.alpha + ctx.beta * x

@given('noise stddev is {stddev} for {num_points} datapoints')
def step_impl(ctx, stddev, num_points):
    ctx.stddev = float(stddev)
    ctx.num_points = int(num_points)
    ctx.dataset = ds.noisy_2d_dataset(ctx.true_model,\
        ctx.stddev, ctx.num_points)

@given('learning rate A of {lambda_A}; learning rate B of {lambda_B}')
def step_impl(ctx, lambda_A, lambda_B):
    ctx.learning_rates = (float(lambda_A), float(lambda_B))

@when('the gradient descent is run')
def step_impl(ctx):
    try:
        ctx.A_obs, ctx.B_obs =\
            gd.gradient_descent(ctx.dataset, ctx.learning_rates)
        ctx.overflow = False
    except OverflowError:
        ctx.overflow = True

@then('the result should converge')
def step_impl(ctx):
    msg = 'the model diverged with an OverflowError'
    assert ctx.overflow is False, msg

# Simple reference: https://onlinecourses.science.psu.edu/stat414/node/280
# Main idea: A ~ N(alpha, variance / n) in OLS
@then('observed A should be within a {tolerance} CI for A')
def step_impl(ctx, tolerance):
    # Set critical value
    z_star = norm.ppf(float(tolerance))

    # Check A is within an acceptable range
    A_range = z_star * ctx.stddev / (ctx.num_points ** 0.5)
    A_min = ctx.alpha - A_range
    A_max = ctx.alpha + A_range

    # Run test
    msg = f'expected A to be within {A_range} of {ctx.alpha}\
        got A is {ctx.A_obs}'
    assert A_min < ctx.A_obs < A_max, msg

# Main idea: B ~ N(beta, variance / SSE) in OLS
@then('observed B should be within a {tolerance} CI for B')
def step_impl(ctx, tolerance):
    # Set critical value, SSE
    z_star = norm.ppf(float(tolerance))
    sse = len(ctx.dataset) * mse.mse(ctx.true_model, ctx.dataset)

    # Check B is within an acceptable range
    B_range = z_star * ctx.stddev / (sse ** 0.5)
    B_min = ctx.beta - B_range
    B_max = ctx.beta + B_range

    # Run test
    msg = f'expected B to be within {B_range} of {ctx.beta}\
        got B is {ctx.B_obs}'
    assert B_min < ctx.B_obs < B_max, msg


@then('the result should diverge with an OverflowError')
def step_impl(ctx):
    msg = 'expected an OverflowError, but it was not thrown'
    assert ctx.overflow is True, msg
