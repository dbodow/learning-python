Feature: make_noisy_2d_dataset

  Scenario: I give a true slope, true intercept, and noise stddev
    Given true model parameters of ts = 5, ti = 30
    and other parameters of normal stddev = 25, num_points = 100
    when the noisy dataset is generated
    then we should not get points > 5 standard devs from the true model

    Given true model parameters of ts = 0.5, ti = 30
    and other parameters of normal stddev = 25, num_points = 100
    when the noisy dataset is generated
    then we should not get points > 5 standard devs from the true model

    Given true model parameters of ts = -1, ti = 30
    and other parameters of normal stddev = 25, num_points = 100
    when the noisy dataset is generated
    then we should not get points > 5 standard devs from the true model

Feature: mse

  Scenario: I give a model slope, model intercept, and observed data
    Given model slope is 0 and intercept is 0
    and xs is 1,2,3,4,5
    and ys is 1,1,1,1,1
    when the mse is computed
    then we expect the mse to be 1

    Given model slope is 1 and intercept is 0
    and xs is 1,2,3,4,5
    and ys is 0,3,2,5,4
    when the mse is computed
    then we expect the mse to be 1

    Given model slope is 0 and intercept is 5
    and xs is 1,2,3,4,5
    and ys is 6,6,6,6,6
    when the mse is computed
    then we expect the mse to be 1

    Given model slope is 1 and intercept is 0
    and xs is 1,2,3,4,5
    and ys is 1,3,5,7,9
    when the mse is computed
    then we expect the mse to be 6
