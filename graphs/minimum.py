from collections import deque, defaultdict


def all_pairs_shortest_path(graph):
    vertices = list(graph.keys())
    num_vertices = len(vertices)
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        start_vertex = vertices[i]
        queue = deque()
        queue.append(start_vertex)
        dist[i][i] = 0

        while queue:
            current_vertex = queue.popleft()
            current_index = vertices.index(current_vertex)

            for neighbor in graph[current_vertex]:
                neighbor_index = vertices.index(neighbor)
                if dist[i][neighbor_index] == float('inf'):  # If not visited
                    dist[i][neighbor_index] = dist[i][current_index] + 1
                    queue.append(neighbor)

    return dist


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    dist_matrix = all_pairs_shortest_path(graph)

    vertices = list(graph.keys())
    print("Distance matrix:")
    print("    " + "   ".join(vertices))
    for i in range(len(vertices)):
        print(vertices[i], end=": ")
        for j in range(len(vertices)):
            print(f"{dist_matrix[i][j]:2}", end="  ")
        print()
