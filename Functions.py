import math

# common statistical functions


def average(values):
    dividend = 0
    for i in range(0, len(values)):
        dividend += values[i]
    avg = dividend/(len(values))
    return avg


def median(values):
    return values[int(len(values)/2)]


def trend(values):
    the_most_frequent = 0
    for value in values:
        if values.count(value) > the_most_frequent:
            the_most_frequent = value
    return the_most_frequent


def distance(val, avg):
    dist = val - avg
    return dist**2


def std_deviation(values):                # mean squared error
    dividend = 0
    for value in values:
        dividend += distance(value, average(values))
    to_square = dividend/(len(values)-1)
    return math.sqrt(to_square)





