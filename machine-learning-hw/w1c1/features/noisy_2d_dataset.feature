Feature: Generate a dataset from a linear model with normal noise

  Scenario: The true slope is greater than 1
    Given true model parameters of ts = 5, ti = 30
    and other parameters of normal stddev = 25, num_points = 100
    when the noisy dataset is generated
    then we should still get a result of correct length
    and jitter should be detectable
    and we should not get points > 3.5 std devs from the true model

  Scenario: The true slope is a fraction less than 1
    Given true model parameters of ts = 0.5, ti = 30
    and other parameters of normal stddev = 25, num_points = 100
    when the noisy dataset is generated
    then we should still get a result of correct length
    and jitter should be detectable
    and we should not get points > 3.5 std devs from the true model

  Scenario: The true slope is negative
    Given true model parameters of ts = -1, ti = 30
    and other parameters of normal stddev = 25, num_points = 100
    when the noisy dataset is generated
    then we should still get a result of correct length
    and jitter should be detectable
    and we should not get points > 3.5 std devs from the true model
