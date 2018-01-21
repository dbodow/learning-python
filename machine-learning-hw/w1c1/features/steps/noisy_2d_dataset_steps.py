from behave import *
import noisy_2d_dataset as _

@given('true model parameters of ts = {ts}, ti = {ti}')
def step_impl(ctx, ts, ti):
    ctx.slope, ctx.intercept = float(ts), float(ti)
    ctx.true_model = lambda x: float(ts) * x + float(ti)

@given('other parameters of normal stddev = {dev}, num_points = {n}')
def step_impl(ctx, dev, n):
    ctx.stddev, ctx.num_points = float(dev), int(n)

@when('the noisy dataset is generated')
def step_impl(ctx):
    ctx.result = _.noisy_2d_dataset(\
        ctx.slope,\
        ctx.intercept,\
        ctx.stddev,\
        ctx.num_points)

@then('we should still get a result of correct length')
def step_impl(ctx):
    length = len(ctx.result)
    msg = f'expected {ctx.num_points} datapoints, got {length}'
    assert length is ctx.num_points, msg

@then('we should not get points > {tolerance} std devs from the true model')
def step_impl(ctx, tolerance):
    max_error = float(tolerance) * ctx.stddev
    for x, y in ctx.result:
        true_y = ctx.true_model(x)
        error = abs(y - true_y)
        msg = f"error was {error}, should be below {max_error}"
        assert error < max_error, msg

@then('jitter should be detectable')
def step_impl(ctx):
    x = ctx.result[0][0]
    y = ctx.result[0][1]
    true_y = ctx.true_model(x)
    jitter = y - true_y
    assert jitter != 0, msg
