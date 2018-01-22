Feature: Use gradient descent to numerically estimate an OLS model

  Scenario: The observed dataset closely fits Y = alpha + beta X
    Given alpha is -17.5 and beta is 4
    and noise stddev is 5 for 100 datapoints
    and learning rate A of 0.000005; learning rate B of 0.000002
    when the gradient descent is run
    then the result should converge
    and observed A should be within a .99 CI for A
    and observed B should be within a .99 CI for B

  Scenario: The observed dataset loosely fits Y = alpha + beta X
    Given alpha is -17.5 and beta is 4
    and noise stddev is 25 for 100 datapoints
    and learning rate A of 0.000005; learning rate B of 0.000002
    when the gradient descent is run
    then the result should converge
    and observed A should be within a .99 CI for A
    and observed B should be within a .99 CI for B

  Scenario: The learning rate is too high for A
    Given alpha is -17.5 and beta is 4
    and noise stddev is 25 for 100 datapoints
    and learning rate A of 20; learning rate B of 0.015
    when the gradient descent is run
    then the result should diverge with an OverflowError

  Scenario: The learning rate is too high for B
    Given alpha is -17.5 and beta is 4
    and noise stddev is 25 for 100 datapoints
    and learning rate A of 0.01; learning rate B of 20
    when the gradient descent is run
    then the result should diverge with an OverflowError
