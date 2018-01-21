Feature: Compute Mean Squared Error of observed data and a model

  Scenario: The model is a perfect fit
    Given model slope is 1 and intercept is 5
    and xs is 1,2,3,4,5; ys is 6,7,8,9,10
    when the mse is computed
    then we expect the mse to be 0

  Scenario: The model's slope is biased
    Given model slope is 1 and intercept is 0
    and xs is 1,2,3,4,5; ys is 1,3,5,7,9
    when the mse is computed
    then we expect the mse to be 6

  Scenario: The model's intercept is biased
    Given model slope is 0 and intercept is 0
    and xs is 1,2,3,4,5; ys is 1,1,1,1,1
    when the mse is computed
    then we expect the mse to be 1

  Scenario: The model's error alternates positive to negative
    Given model slope is 1 and intercept is 0
    and xs is 1,2,3,4,5; ys is 0,3,2,5,4
    when the mse is computed
    then we expect the mse to be 1
