## Advent of Code 2022: Day 1
## https://adventofcode.com/2022/day/1
## Jesse Williams | github.com/xram64
## Answers: [Part 1]: 69310, [Part 2]: 206104

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
counts = [Count(i, sum(elf)) for i, elf in enumerate(elves)]

counts.sort(key=lambda x: x.value, reverse=True)

count_max = counts[0]
print(f"[Part 1] Elf #{count_max.elf+1:03d} is carrying the most calories, with {count_max.value} total calories.")


## Part 2
print(f"[Part 2] Elves #{counts[0].elf+1:03d}, #{counts[1].elf+1:03d}, and #{counts[2].elf+1:03d} carry the most calories",
      f"with {counts[0].value+counts[1].value+counts[2].value} total calories between them.")
