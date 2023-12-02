from re import split
from math import prod


def part2(data):
    total = 0
    for game in data:
        rolls = split(r";|,|:", game)[1:]

        max_values = {"red": 0, "green": 0, "blue": 0}
        for rol in rolls:
            rol = rol.strip().split(" ")
            if max_values[rol[1]] < int(rol[0]):
                max_values[rol[1]] = int(rol[0])

        total += prod(max_values.values())

    return total
