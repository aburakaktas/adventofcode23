import re
from typing import List


def write_lines_to_list(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.strip())    
    return lines

# converts a string list to a useful piece of dict
def convert_list_to_dic(result_list: List[str]):
    results_list_dic = []

    color_list = ['red', 'green', 'blue']
    for turn in result_list:
        splitted = turn.split(', ')
        color_count = {}
        for item in splitted:
            count_color_pair_list = item.split(" ")
            color_count[count_color_pair_list[1]] = int(count_color_pair_list[0])

            # add zero if a color is not mentioned
            for color in color_list:
                if not color_count.get(color):
                    color_count[color] = 0
        results_list_dic.append(color_count)
    return results_list_dic

# converts a string input to a nice and shiny dict
def organize_lines(lines:str):
    games = {}
    game_number = 1
    for line in lines:
        #split the input on ; character 
        result_list = [x.strip() for x in line.split(';')]

        # strip the "Game 1: " part from the first element
        result_list[0] = re.sub(r"Game (\d*): ", "", result_list[0])
        # print(convert_list_to_dic(result_list))
        games[game_number] = convert_list_to_dic(result_list)
        game_number += 1

    return games




def main():
    bag = {
        "red" : 12,
        "green" : 13,
        "blue" : 14,
    }
    
    lines = write_lines_to_list("data.txt")
    organized_lines = organize_lines(lines)

    sum = 0
    flag = 0
    for game, turns in organized_lines.items():
        # print(game)
        for turn in turns:
            for color, count in turn.items():
                if count > bag[color]:
                    # print (f"Elf pulled {count} {color} but we have {bag[color]}")
                    flag = 1
        if flag == 1:
            flag = 0
            # print(f"This game {game} is not possible")
            continue
        sum += game
    print(sum)

if __name__ == "__main__":
    main()


# Game 1
#     round 1
#         green 4
#         blue 2
#     round 2
#         red 1
#         blue 1
#         green 4
#     round 3..

