import math
import os
# common statistical functions


def data_cleaner(input_file):
    finale = []
    data = []
    target = []     # occurences for value

    with open(input_file) as fobj:
        for line in fobj:
            row = line.split()
            data.append(row[:-1])
            target.append(row[-1])

    for el in range(len(data)):  # for every value
        num = int(target[el])  # how much occurences
        for occ in range(num):
            finale.append(data[el])  # final data

    file = open("to_rem_parentheses.txt", "w")
    file.writelines(["%s\n" % item for item in finale])

    with open('converter_output_example.txt', 'w') as f_out:           # removes parentheses
        with open('to_rem_parentheses.txt') as f_in:
            for line in f_in:
                for ch in ['[', ']', "'"]:
                    line = line.replace(ch, '')
                f_out.write(line)

    file.close()
    os.remove("to_rem_parentheses.txt")


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


def velocity(s0, v0, t, a):
    distance = s0 + v0 * t + 0.5 * a * t ** 2
    return distance



