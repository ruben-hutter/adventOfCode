stacks = [[] for _ in range(9)]

with open("5/input", 'r') as f:
    lines = f.read().splitlines()
init_state, instructions = lines[:8][::-1], [line.split() for line in lines[10:]]

def parse_crates(init_state):
    for line in init_state:
        n = 0
        for i in range(1, len(line), 4):
            if line[i].isalpha():
                stacks[n].append(line[i])
            n += 1

def first_part():
    # initialize stacks with init_state
    parse_crates(init_state)
    # execute moves
    parse_moves(instructions)
    print(f'Crates on top: {"".join([crate[-1] for crate in stacks])}')

def parse_moves(instructions):
    for line in instructions:
        how_many = int(line[1])
        from_ = int(line[3]) - 1
        to_ = int(line[5]) - 1
        for _ in range(how_many):
            stacks[to_].append(stacks[from_].pop())

def second_part():
    # initialize stacks with init_state
    parse_crates(init_state)
    # execute moves
    parse_moves_2(instructions)
    print(f'Crates on top: {"".join([crate[-1] for crate in stacks])}')

def parse_moves_2(instructions):
    for line in instructions:
        how_many = int(line[1])
        from_ = int(line[3]) - 1
        to_ = int(line[5]) - 1
        crates = stacks[from_][-how_many:]
        stacks[from_] = stacks[from_][:-how_many]
        stacks[to_].extend(crates)

def main():
    # execute only one part at a time!
    first_part()
    second_part()

if __name__ == '__main__':
    main()