def dfs_paths(graph, start, end, path=None):
    if path is None:
        path = [start]
    if start == end:
        yield path
    for neighbor in graph[start]:
        if neighbor not in path:
            yield from dfs_paths(graph, neighbor, end, path + [neighbor])


def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


# Граф для тестування
graph = {1: {2, 3}, 2: {1, 4}, 3: {1, 4}, 4: {2, 3, 5, 6}, 5: {4}, 6: {4}}

# Знаходження шляхів за допомогою DFS та BFS
dfs_result = list(dfs_paths(graph, 1, 5))
bfs_result = list(bfs_paths(graph, 1, 5))

print("DFS шляхи:", dfs_result)
print("BFS шляхи:", bfs_result)
