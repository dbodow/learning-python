Feature: my_sum

  Scenario: summing positive integers
    Given 5 and 7 to sum
    when we call the my_sum function
    then it returns a sum of 12

  Scenario: summing negative integers
    Given -5 and 7 to sum
    when we call the my_sum function
    then it returns a sum of 2
