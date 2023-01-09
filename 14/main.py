from enum import Enum

with open("14/test_input", 'r') as f:
    in_file = f.read().splitlines()
    in_file = [[eval(c) for c in l.split(" -> ")] for l in in_file]

POURING_POINT = (500, 0)
class Type(Enum):
    ROCK = 1
    AIR = 2
    SAND = 3

coordinates = {}

def first_part():
    # initial setup from input
    for line in in_file:
        for coord in line:
            coordinates[coord] = Type.ROCK

def second_part():
    return

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()