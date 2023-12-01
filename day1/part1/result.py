from re import finditer


def part1(data):
    total = 0
    for line in data:
        # Use regex to find all numbers.
        matches = finditer("\d", line)
        match_mapping = {match.start(): match for match in matches}

        # Get the first and last number.
        first_number = match_mapping[min(match_mapping.keys())].group(0)
        last_number = match_mapping[max(match_mapping.keys())].group(0)

        total += int(first_number + last_number)

    return total
