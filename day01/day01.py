## Advent of Code 2022: Day 1
## https://adventofcode.com/2021/day/1
## Jesse Williams | github.com/xram64
## Answers: [Part 1]: 69310

from collections import namedtuple
Count = namedtuple('Count', ['elf', 'value'])

## Part 1
with open('day01_input.txt') as f:
    lines = f.readlines()

# Gather counts for each elf
elves = [[]]

for line in lines:
    if (n := line.strip()) == '':
        elves.append([])
    else:
        elves[-1].append(int(n))

# Summarize calorie counts and print stats
counts = [sum(elf) for elf in elves]

count_max = Count(0, 0)
for i, val in enumerate(counts):
    if val > count_max.value:
        count_max = Count(i, val)

print(f"[Part 1] Elf #{count_max.elf+1:03d} is carrying the most calories, with {count_max.value} total calories.")
