from collections import deque

with open("12/test_input", 'r') as f:
    in_file = f.read().splitlines()
    grid = [[ord(letter)-ord('a') for letter in line] for line in in_file]
    # TODO handle case S and E -> save coordinates of nodes and
    # set S = 0, E = 26
    # set correct value in grid

print(grid)

def first_part():
    return

def bfs_with_predecessors(graph, node):
    predecessor = {}
    queue = deque()
    predecessor[node] = node
    queue.append(node)
    while queue:
        v = queue.popleft()
        for s in graph.successors(v):
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
    return

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()