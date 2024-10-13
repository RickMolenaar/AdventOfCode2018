from copy import deepcopy

def parse_input(file = 'day02.txt'):
    with open(file) as f:
        s = map(lambda l: l.rstrip(), f.readlines())
    return list(s)

def parse_example():
    return parse_input('day02example.txt')

def format_input(inp: list[str]):
    return inp

def solve(inp, part, example):
    def has(id, amount):
        return any(id.count(c) == amount for c in set(id))
    
    if part == 1:
        return len([word for word in inp if has(word, 2)])*len([word for word in inp if has(word, 3)])

    for i, id1 in enumerate(inp):
        for id2 in inp[i+1:]:
            diffs = 0
            for j in range(len(id1)):
                if id1[j] != id2[j]:
                    diffs += 1
                    if diffs > 1:
                        break
            if diffs == 1:
                return(''.join(id1[j] for j in range(len(id1)) if id1[j] == id2[j]))


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
