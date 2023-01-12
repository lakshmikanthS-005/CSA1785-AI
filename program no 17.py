def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            stack.extend(graph[vertex] - visited)

# Example usage:
if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    dfs(graph, 2)
