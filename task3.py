import heapq


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances


# Граф для тестування з вагами на ребрах
weighted_graph = {
    1: {2: 1, 3: 2},
    2: {1: 1, 4: 3},
    3: {1: 2, 4: 1},
    4: {2: 3, 3: 1, 5: 2, 6: 3},
    5: {4: 2},
    6: {4: 3},
}

# Знаходження найкоротших шляхів від вершини 1 до всіх інших
shortest_paths = {vertex: dijkstra(weighted_graph, vertex) for vertex in weighted_graph}

for vertex in shortest_paths:
    print(f"Найкоротші шляхи від вершини 1 до {vertex}: {shortest_paths[vertex]}")
