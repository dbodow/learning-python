# Ignore this, I'm just learning behave for the first time
# and wanted some practice.

from behave import *
import ols

# make_noisy_2d_dataset

@given('true model parameters of ts = {ts}, ti = {ti}')
def step_impl(ctx, a1, a2):
    ctx.slope, ctx.intercept = float(ts), float(ti)
    ctx.true_model = lambda x: float(ts) * x + float(ti)

@given('other parameters of normal stddev = {dev}, num_points = {n}')
def step_impl(ctx, a1, a2):
    ctx.stddev, ctx.num_points = int(dev), int(n)

@when('the noisy dataset is generated')
def step_impl(ctx):
    ctx.result = ols.make_noisy_2d_dataset(\
        ctx.slope,\
        ctx.intercept,\
        ctx.stddev,\
        ctx.num_points)

@then('we should not get points > 5 standard devs from the true model')
def step_impl(ctx, expected_res):
    msg = f"expected: {expected_res}, got {ctx.result}"
    assert ctx.result is int(expected_res), msg
