# calculates score of rock-paper-scissors game
def first_part():
    total_score = 0
    map_p2_p1 = {'X': ('A', 1), 'Y': ('B', 2), 'Z': ('C', 3)}
    # Game symbols: A = Rock, B = Paper, C = Scissor
    round_score_table = ['A', 'B', 'C']
    with open("2/input", 'r') as f:
        line = f.readline()
        p1 = line[0]
        p2 = map_p2_p1[line[2]]
        while line:
            # index[p1] == index[p2] --> draw: 3 pt.
            if p1 == p2[0]:
                total_score += 3 + p2[1]
            # index[p1] == index[p2]-1 --> win: 6 pt.
            elif p1 == round_score_table[round_score_table.index(p2[0])-1]:
                total_score += p2[1]
            # index[p1] == index[p2]-2 --> loss: 0 pt.
            else:
                total_score += 6 + p2[1]
            line = f.readline()
            if line == "": # skip last line
                break
            p1 = line[0]
            p2 = map_p2_p1[line[2]]
    print(f'Total score: {total_score}')

def second_part():
    # X --> need to lose
    # Y --> need to draw
    # Z --> need to win
    total_score = 0
    # Game symbols: A = Rock, B = Paper, C = Scissor
    round_score_table = ['A', 'B', 'C']
    with open("2/input", 'r') as f:
        line = f.readline()
        p1 = line[0]
        outcome = line[2]
        while line:
            # draw: outcome = Y --> p2 = p1
            if outcome == 'Y':
                total_score += 3 + round_score_table.index(p1) + 1
            # loss: outcome = Z --> p2 = p1 - 1
            elif outcome == 'X':
                p2 = round_score_table[round_score_table.index(p1)-1]
                total_score += round_score_table.index(p2) + 1
            # win: outcome = X --> p2 = p1 - 2
            else:
                p2 = round_score_table[round_score_table.index(p1)-2]
                total_score += 6 + round_score_table.index(p2) + 1
            line = f.readline()
            if line == "": # skip last line
                break
            p1 = line[0]
            outcome = line[2]
    print(f'Total score: {total_score}')

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()