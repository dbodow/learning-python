# Ignore this, I'm just learning behave for the first time
# and wanted some practice.

from behave import *
import testing_behave

@given('{a1} and {a2} to sum')
def step_impl(context, a1, a2):
    context.arg1, context.arg2 = int(a1), int(a2)

@when('we call the my_sum function')
def step_impl(context):
    context.result = testing_behave.my_sum(context.arg1, context.arg2)

@then('it returns a sum of {expected_res}')
def step_impl(context, expected_res):
    msg = f"expected: {expected_res}, got {context.result}"
    assert context.result is int(expected_res), msg
