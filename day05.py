from copy import deepcopy
from string import ascii_lowercase

def parse_input(file = 'day05.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day05example.txt')

def format_input(inp: list[str]):
    return inp[0]

def react(polymer):
    i = 0
    while i < len(polymer) - 1:
        if polymer[i] == polymer[i+1] or polymer[i].lower() != polymer[i+1].lower():
            i += 1
        else:
            polymer = polymer[:i] + polymer[i+2:]
            if i > 0:
                i -= 1
    return polymer

def solve(polymer, part, example):
    if part == 1:
        return len(react(polymer))
    best = len(polymer)
    for c in ascii_lowercase:
        reacted = react(polymer.replace(c, '').replace(c.upper(), ''))
        if len(reacted) < best:
            best = len(reacted)
    return best

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
