from part1.result import part1
from part2.result import part2


def task1_example_test():
    file = open("day2/part1/example.txt", "r").read().splitlines()
    if part1(file) != 8:
        raise Exception("Test failed")


def task1_test():
    file = open("day2/input.txt", "r").read().splitlines()
    if part1(file) != 2285:
        raise Exception("Test failed")


def task2_example_test():
    file = open("day2/part2/example.txt", "r").read().splitlines()
    if part2(file) != 2286:
        raise Exception("Test failed")


def task2_test():
    file = open("day2/input.txt", "r").read().splitlines()
    if part2(file) != 77021:
        raise Exception("Test failed")


task1_test()
task1_example_test()
task2_example_test()
task2_test()
