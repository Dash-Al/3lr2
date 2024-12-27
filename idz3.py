from collections import deque


def bfs_min_distance(distance_matrix, start, end):
    """Поиск минимального расстояния с помощью алгоритма BFS."""

    # Количество городов
    num_cities = len(distance_matrix)

    # Очередь для BFS
    queue = deque([start])

    # Список для хранения расстояний
    distances = [float('inf')] * num_cities
    distances[start] = 0

    # Массив для отслеживания посещенных узлов
    visited = [False] * num_cities
    visited[start] = True

    while queue:
        current = queue.popleft()

        for neighbor in range(num_cities):
            if distance_matrix[current][neighbor] > 0 and not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[current] + distance_matrix[current][neighbor]
                queue.append(neighbor)

    return distances[end] if distances[end] != float('inf') else -1  # -1 если путь не найден


# Пример использования
if __name__ == "__main__":
    # Матрица расстояний между городами
    distance_matrix = [
        [0, 222, 234, 420, 498, 677, 853, 555, 457, 455],
        [222, 0, 59, 545, 732, 456, 17, 109, 983, 833],
        [234, 59, 0, 232, 183, 100, 938, 78, 73, 284],
        [420, 545, 232, 0, 37, 274, 112, 82, 877, 458],
        [498, 732, 183, 37, 0, 883, 755, 560, 555, 101],
        [677, 456, 100, 274, 883, 0, 768, 643, 638, 184],
        [853, 17, 938, 112, 755, 768, 0, 462, 674, 654],
        [555, 109, 78, 82, 560, 643, 462, 0, 212, 666],
        [457, 983, 73, 877, 555, 638, 674, 212, 0, 656],
        [455, 833, 284, 458, 101, 184, 654, 666, 656, 0],
    ]

    start_city = 0  # Начальный город (индекс)
    end_city = 3  # Конечный город (индекс)

    min_distance = bfs_min_distance(distance_matrix, start_city, end_city)

    if min_distance != -1:
        print(f"Минимальное расстояние между городами {start_city} и {end_city}: {min_distance}")
    else:
        print(f"Путь между городами {start_city} и {end_city} не найден.")
