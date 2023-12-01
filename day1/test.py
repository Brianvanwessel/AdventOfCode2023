from part2.result import part2
from part1.result import part1


def task1_example_test():
    file = open("day1/input.txt", "r").read().splitlines()

    if part1(file) != 142:
        raise Exception("Test failed")


def task1_test():
    file = open("day1/input.txt", "r").read().splitlines()

    if part1(file) != 54450:
        raise Exception("Test failed")


def task2_example_test():
    file = open("day1/part1/example.txt", "r").read().splitlines()

    if part2(file) != 281:
        raise Exception("Test failed")


def task2_test():
    file = open("day1/input.txt", "r").read().splitlines()

    if part2(file) != 54265:
        raise Exception("Test failed")


task1_test()
