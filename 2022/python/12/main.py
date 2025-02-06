import sys
from collections import deque

graph = {}
starting_nodes = []
in_width = 0
in_height = 0

def calc_step(letter):
    if letter == 'S':
        return 0
    elif letter == 'E':
        return 26
    return ord(letter) - ord('a')

def append_neighbors(row, col):
    if col > 0 and (row,col-1) in graph: # has left neighbor
        difference = graph[(row,col-1)][0] - graph[(row,col)][0]
        if difference <= 1:
            graph[(row,col)][1].append((row,col-1))
    if col < in_width-1: # has right neighbor
        difference = calc_step(in_file[row][col+1]) - graph[(row,col)][0]
        if difference <= 1:
            graph[(row,col)][1].append((row,col+1))
    if row > 0 and (row-1,col) in graph: # has upper neighbor
        difference = graph[(row-1,col)][0] - graph[(row,col)][0]
        if difference <= 1:
            graph[(row,col)][1].append((row-1,col))
    if row < in_height-1: # has lower neighbor
        difference = calc_step(in_file[row+1][col]) - graph[(row,col)][0]
        if difference <= 1:
            graph[(row,col)][1].append((row+1,col))

with open("12/input", 'r') as f:
    in_file = f.read().splitlines()
    in_height = len(in_file)
    in_width = len(in_file[0])
    for row, line in enumerate(in_file):
        for col, letter in enumerate(line):
            # starting_nodes
            if letter == 'S':
                starting_nodes.insert(0, (row,col))
            elif letter == 'a':
                starting_nodes.append((row,col))
            elif letter == 'E':
                # end_node
                end_node = (row,col)
            graph[(row,col)] = (calc_step(letter), [])
            # append neighbors
            append_neighbors(row, col)

def first_part():
    path = shortest_path(graph, starting_nodes[0], end_node)
    print(f'Shortest path: {len(path)} steps')

def bfs_with_predecessors(graph, node):
    predecessor = {}
    queue = deque()
    predecessor[node] = node
    queue.append(node)
    while queue:
        v = queue.popleft()
        for s in graph[v][1]:
            if s not in predecessor:
                predecessor[s] = v
                queue.append(s)
    return predecessor

def shortest_path(graph, from_node, to_node):
    predecessor = bfs_with_predecessors(graph, from_node)
    if to_node not in predecessor:
        print(f'There is no path from {from_node} to {to_node}')
        return None
    
    path = deque()
    current_node = to_node
    pre = predecessor[current_node]
    while pre != current_node:
        path.appendleft((pre, current_node))
        current_node = pre
        pre = predecessor[current_node]
    return path

def second_part():
    shortest_size = sys.maxsize
    shortest = 0
    for start_node in starting_nodes:
        path = shortest_path(graph, start_node, end_node)
        if path and len(path) < shortest_size:
            shortest = path
            shortest_size = len(shortest)
    print(f'Shortest path: {shortest_size} steps')

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()