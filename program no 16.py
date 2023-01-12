from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Example usage:
if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }
    bfs(graph, 2)
    
    output:
      2
      0
      3
      1
