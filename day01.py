from copy import deepcopy

def parse_input(file = 'day01.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day01example.txt')

def format_input(inp: list[str]):
    return inp

def solve(inp, part, example):
    if part == 1:
        return sum(int(v) for v in inp)
    f = 0
    seen = set()
    iters = 0
    while iters < 10_000:
        iters += 1
        for line in inp:
            f += int(line)
            if f in seen:
                return f
            seen.add(f)

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
