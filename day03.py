from collections import defaultdict
from copy import deepcopy

def parse_input(file = 'day03.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day03example.txt')

def format_input(inp: list[str]):
    claims = []
    for line in inp:
        words = line.split()
        id = words[0].lstrip('#')
        x, y = map(int, words[2].rstrip(':').split(','))
        sx, sy = map(int, words[3].split('x'))
        claims.append((id, x, y, sx, sy))
    return claims

def solve(inp, part, example):
    claimed = defaultdict(int)
    for id, cx, cy, sx, sy in inp:
        for x in range(cx, cx + sx):
            for y in range(cy, cy + sy):
                claimed[x, y] += 1
    if part == 1:
        return len([item for item in claimed if claimed[item] > 1])
    
    for id, cx, cy, sx, sy in inp:
        dupl = False
        for x in range(cx, cx + sx):
            for y in range(cy, cy + sy):
                if claimed[x, y] > 1:
                    dupl = True
                    break
            if dupl:
                break
        else:
            return id

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
