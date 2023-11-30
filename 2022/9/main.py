with open("9/input", 'r') as f:
    lines = f.read().splitlines()

moves = [(line[0], int(line[2:])) for line in lines] # [('R', 12), ...]

def first_and_second_part(number_of_knots=2):
    visited = set()
    rope_knots_position = [[0, 0] for _ in range(number_of_knots)] # 9-8-7-6-5-4-3-2-1-H
    for move in moves:
        direction, value = move[0], move[1]
        # move head
        while value > 0:
            # check in which direction
            if direction == 'L': # move left
                rope_knots_position[0][0] -= 1
            elif direction == 'R': # move right
                rope_knots_position[0][0] += 1
            elif direction == 'U': # move up
                rope_knots_position[0][1] += 1
            elif direction == 'D': # move down
                rope_knots_position[0][1] -= 1
            # check if tail has to move
            update_tail(rope_knots_position)
            visited.add(tuple(rope_knots_position[-1]))
            # decrement value
            value -= 1
    print(f'Visited positions: {len(visited)}')

def update_tail(rope_knots_position, tail_index=1):
    if tail_index == len(rope_knots_position):
        return
    x_diff = rope_knots_position[tail_index-1][0] - rope_knots_position[tail_index][0]
    y_diff = rope_knots_position[tail_index-1][1] - rope_knots_position[tail_index][1]
    # no need to update tail
    if abs(x_diff) < 2 and abs(y_diff) < 2:
        return
    # change tail position
    if x_diff < 0: # H.T -> HT.
        rope_knots_position[tail_index][0] -= 1
    elif x_diff > 0: # T.H -> .TH
        rope_knots_position[tail_index][0] += 1
    if y_diff < 0: # head under tail -> move tail down
        rope_knots_position[tail_index][1] -= 1
    elif y_diff > 0: # tail under head -> move tail up
        rope_knots_position[tail_index][1] += 1
    update_tail(rope_knots_position, tail_index+1)

def main():
    first_and_second_part()
    first_and_second_part(10)

if __name__ == '__main__':
    main()