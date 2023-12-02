from re import split


def part1(data):
    total = 0
    for game in data:
        split_game = split(r";|,|:", game)
        game_number = split_game[0].split(" ")[1]
        rolls = split_game[1:]
        valid_game = True
        for rol in rolls:
            rol = rol.strip().split(" ")
            if rol[1] == "red" and int(rol[0]) > 12:
                valid_game = False
                break
            if rol[1] == "green" and int(rol[0]) > 13:
                valid_game = False
                break
            if rol[1] == "blue" and int(rol[0]) > 14:
                valid_game = False
                break

        if not valid_game:
            continue

        total += int(game_number)

    return total
