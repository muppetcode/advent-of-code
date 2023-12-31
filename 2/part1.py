import re
# I really cba so import re it is

def max_cubes(line: str, comparison_color: str) -> int:
    cubes = re.findall(r"(\d+) (\w+)", line)
    return max(int(count) for count, color in cubes if color == comparison_color)

input_data = open("2/1input.txt").read().splitlines()
possible_game_ids = []
for game_id, line in enumerate(input_data, start=1):
    if max_cubes(line, "red") <= 12 and max_cubes(line, "green") <= 13 and max_cubes(line, "blue") <= 14:
        possible_game_ids.append(game_id)

print(sum(possible_game_ids))