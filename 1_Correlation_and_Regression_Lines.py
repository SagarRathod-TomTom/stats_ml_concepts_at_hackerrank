"""
Problem Statement:
https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem

Useful link:
https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
"""

# Pure Python Code

from math import sqrt

# Takes comma separated values as input
# 15, 12, 8, 8, 7, 7, 7, 6, 5, 3
#physics_scores = list(map(int, input().split(',')))
physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]

# Takes comma separated values as input
# 10, 25, 17, 11, 13, 17, 20, 13, 9, 15
# history_scores = list(map(int, input().split(',')))
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]


def mean(scores):
    return sum(scores) / len(scores)


def mean_normalize(scores):
    midpoint = mean(scores)
    return [x - midpoint for x in scores]


def squared_error(scores):
    m = mean(scores)
    return [(x - m) ** 2 for x in scores]


physics_normalized = mean_normalize(physics_scores)
history_normalized = mean_normalize(history_scores)

numerator = sum([ x * y for x,y in zip(physics_normalized, history_normalized)])
denominator = sqrt(sum(squared_error(physics_scores))) * sqrt(sum(squared_error(history_scores)))

print('%.3f' % (numerator / denominator))
