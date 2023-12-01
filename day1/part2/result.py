from re import finditer

number_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part2(data):
    total = 0
    for line in data:
        # Use regex to find all numbers and number words.
        keys = "|".join(number_mapping.keys())
        matches = finditer(rf"(?=({keys}))" + "|\d", line)
        match_mapping = {match.start(): match for match in matches}

        # Get the first and last number.
        first_match = match_mapping[min(match_mapping.keys())]
        last_match = match_mapping[max(match_mapping.keys())]
        first_number = (
            first_match.group(1) if first_match.group(1) else first_match.group(0)
        )
        last_number = (
            last_match.group(1) if last_match.group(1) else last_match.group(0)
        )

        # Convert number words to numbers when needed.
        if not first_number.isdigit():
            first_number = number_mapping[first_number]
        if not last_number.isdigit():
            last_number = number_mapping[last_number]

        total += int(first_number + last_number)

    return total
