#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#
#   ______________________________________________________________   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   |  <<  <<  <>  <|   Advent  of  Code  2022   |>  <>  >>  >>  |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   | + ::|  Day  3  |:: + ::|  Jesse Williams  ∕  xram64  |:: + |   #
#   |~+~===~+==<>==+~===~+~===~+==<>==+~===~+~===~+==<>==+~===~+~|   #
#   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾   #
#             __.-----------.___________________________             #
#            |  |  Answers  |   Part 1: 8105            |            #
#            |  `-----------'   Part 2:                 |            #
#            `------------------------------------------'            #
#│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│#

from collections import namedtuple
Sack = namedtuple('Sack', ['left', 'right'])

def get_priority(char):
    offset_lower = ord('a') - 1
    offset_upper = ord('A') - 1 - 26
    
    if char == char.lower():
        return ord(char) - offset_lower  # char is lowercase
    else:
        return ord(char) - offset_upper  # char is uppercase

if __name__ == '__main__':
    
    #╷----------.
    #│  Part 1  │
    #╵----------'
    with open('day03_input.txt') as f:
        lines = f.readlines()

    sacks = []
    for line in lines:
        ln = line.strip()
        half = int(len(ln)/2)
        sacks.append(Sack(set(ln[:half]), set(ln[half:])))

    split_item_priorities = []
    for sack in sacks:
        split_item = sack.left & sack.right  # set intersection
        # print(f"{sack}  ||  {split_item} == {get_priority(split_item.pop())}")
        split_item_priorities.append(get_priority(split_item.pop()))
    
    print(f"[Part 1] The sum of priorities of items that are split between two compartments is {sum(split_item_priorities)}.")






