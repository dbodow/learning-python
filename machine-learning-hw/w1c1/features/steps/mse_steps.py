from behave import *
import mse as _

@given('model slope is {ms} and intercept is {mi}')
def step_impl(ctx, ms, mi):
    ctx.slope, ctx.intercept = float(ms), float(mi)
    ctx.true_model = lambda x: float(ms) * x + float(mi)

@given('xs is {xs}; ys is {ys}')
def step_impl(ctx, xs, ys):
    xs = [int(x) for x in xs.split(',')]
    ys = [int(y) for y in ys.split(',')]
    ctx.dataset = list(zip(xs, ys))

@when('the mse is computed')
def step_impl(ctx):
    ctx.result = _.mse(ctx.true_model, ctx.dataset)

@then('we expect the mse to be {expected}')
def step_impl(ctx, expected):
    msg = f"expected: {expected}, got {ctx.result}"
    assert ctx.result == float(expected), msg
