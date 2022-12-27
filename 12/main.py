from collections import deque

graph = {}

with open("12/test_input", 'r') as f:
    in_file = f.read().splitlines()
    for row, line in enumerate(in_file):
        for col, letter in enumerate(line):
            if letter == 'S':
                # start_node
                start_node = (row,col)
                graph[(row,col)] = (0, [])
            elif letter == 'E':
                # end_node
                end_node = (row,col)
                graph[(row,col)] = (26, [])
            else:
                graph[(row,col)] = (ord(letter)-ord('a'), [])
            # append neighbors

print(graph)

def first_part():
    return

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
    return

def main():
    first_part()
    second_part()

if __name__ == '__main__':
    main()