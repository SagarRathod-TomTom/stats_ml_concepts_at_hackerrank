"""
Problem Statement:
https://www.hackerrank.com/challenges/correlation-and-regression-lines-8/problem

Useful Link:
https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/regression-analysis/find-a-linear-regression-equation/
"""

#physics_scores = list(map(int, input().split(',')))
physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]

# Takes comma separated values as input
# 10, 25, 17, 11, 13, 17, 20, 13, 9, 15
# history_scores = list(map(int, input().split(',')))
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

# Using Linear Regression Equation: y = a + bX

def squared_sum(scores):
    return sum([x ** 2 for x in scores])

n_samples = len(physics_scores)

x_sum = sum(physics_scores)
x_squared_sum = squared_sum(physics_scores)

y_sum = sum(history_scores)
xy_sum = sum([x * y for x,y in zip(physics_scores, history_scores)])

# Calculate values of a and b
a = ((y_sum * x_squared_sum) - (x_sum * xy_sum)) / (n_samples * x_squared_sum - (x_sum ** 2))
b = ((n_samples * xy_sum) - (x_sum * y_sum)) / (n_samples * x_squared_sum - (x_sum ** 2))

# Calculate the probable score for history(y=dependent) using physics(x, independent) = 10
y = a + b * 10

print('%.3f' % y)