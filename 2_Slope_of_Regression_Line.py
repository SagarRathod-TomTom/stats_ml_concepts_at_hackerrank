"""
Problem Statement:
https://www.hackerrank.com/challenges/correlation-and-regression-lines-7/problem

Useful Links:
1. https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/regression-analysis/find-a-linear-regression-equation/
2. https://www.chegg.com/homework-help/definitions/slope-of-regression-line-31

"""

# Pure Python Code:
# Takes comma separated values as input
# 15, 12, 8, 8, 7, 7, 7, 6, 5, 3
# physics_scores = list(map(int, input().split(',')))
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

numerator = sum([x * y for x,y in zip(physics_normalized, history_normalized)])
denominator = sum(squared_error(physics_scores))

print('%.3f' % (numerator / denominator))
