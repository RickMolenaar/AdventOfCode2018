from collections import defaultdict
from copy import deepcopy

def parse_input(file = 'day04.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return sorted(s)

def parse_example():
    return parse_input('day04example.txt')

def format_input(inp: list[str]):
    guards = defaultdict(list)
    active_guard = None
    for line in inp:
        date, time, *event = line.split()
        date = date.lstrip('[')
        time = time.rstrip(']')
        if 'begins' in event:
            active_guard = int(event[1].lstrip('#'))
        elif 'falls' in event:
            t0 = int(time.split(':')[1])
        else:
            guards[active_guard].append((t0, int(time.split(':')[1])))
    return guards

def solve(inp, part, example):
    if part == 1:
        most = 0
        for guard in inp:
            amount = 0
            for sleep in inp[guard]:
                amount += sleep[1] - sleep[0]
            if amount > most:
                most = amount
                sleepiest = guard
        
        minutes = defaultdict(int)
        for sleep in inp[sleepiest]:
            for m in range(sleep[0], sleep[1]):
                minutes[m] += 1
        return sleepiest * max(minutes, key = lambda m: minutes[m])
    else:
        most = 0
        for guard in inp:
            minutes = defaultdict(int)
            for sleep in inp[guard]:
                for m in range(sleep[0], sleep[1]):
                    minutes[m] += 1
            tb = max(minutes, key = lambda m: minutes[m])
            if minutes[tb] > most:
                most = minutes[tb]
                sleepiest = guard
                tbt = tb
        return sleepiest * tbt

def main():
    example_input = format_input(parse_example())
    actual_input = format_input(parse_input())
    for part in (1, 2):
        for example in (True, False):
            inp = deepcopy(example_input if example else actual_input)
            try:
                yield solve(inp, part, example)
            except KeyboardInterrupt:
                raise
            except Exception as e:
                yield e
