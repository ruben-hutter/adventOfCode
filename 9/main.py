with open("9/test_input2", 'r') as f:
    lines = f.read().splitlines()

moves = [(line[0], int(line[2:])) for line in lines] # [('R', 12), ...]
head_position = [0, 0]

def first_part():
    visited = set()
    tail_position = [0, 0]
    for move in moves:
        direction, value = move[0], move[1]
        # move head
        while value > 0:
            # check in which direction
            if direction == 'L': # move left
                head_position[0] -= 1
            elif direction == 'R': # move right
                head_position[0] += 1
            elif direction == 'U': # move up
                head_position[1] += 1
            elif direction == 'D': # move down
                head_position[1] -= 1
            # check if tail has to move
            check_tail_update(head_position, tail_position)
            visited.add(tuple(tail_position))
            # decrement value
            value -= 1
    print(f'Visited positions: {len(visited)}')

def check_tail_update(head_position, tail_position):
    x_diff = head_position[0] - tail_position[0]
    y_diff = head_position[1] - tail_position[1]
    # no need to update tail
    if abs(x_diff) < 2 and abs(y_diff) < 2:
        return
    # change tail position
    if x_diff < 0: # H.T -> HT.
        tail_position[0] -= 1
    elif x_diff > 0: # T.H -> .TH
        tail_position[0] += 1
    if y_diff < 0: # head under tail -> move tail down
        tail_position[1] -= 1
    elif y_diff > 0: # tail under head -> move tail up
        tail_position[1] += 1

def second_part():
    visited = set()
    tail_position = [[0, 0] for _ in range(9)] # 9-8-7-6-5-4-3-2-1-H
    for move in moves:
        direction, value = move[0], move[1]
        # move head
        while value > 0:
            # check in which direction
            if direction == 'L': # move left
                head_position[0] -= 1
            elif direction == 'R': # move right
                head_position[0] += 1
            elif direction == 'U': # move up
                head_position[1] += 1
            elif direction == 'D': # move down
                head_position[1] -= 1
            # check if tail has to move
            check_tail_update2(head_position, tail_position)
            visited.add(tuple(tail_position[-1]))
            # decrement value
            value -= 1
    print(f'Visited positions: {len(visited)}')

def check_tail_update2(head_position, tail_position):
    x_diff = head_position[0] - tail_position[0]
    y_diff = head_position[1] - tail_position[1]
    # no need to update tail
    if abs(x_diff) < 2 and abs(y_diff) < 2:
        return
    # change tail position
    if x_diff < 0: # H.T -> HT.
        tail_position[0] -= 1
    elif x_diff > 0: # T.H -> .TH
        tail_position[0] += 1
    if y_diff < 0: # head under tail -> move tail down
        tail_position[1] -= 1
    elif y_diff > 0: # tail under head -> move tail up
        tail_position[1] += 1

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()