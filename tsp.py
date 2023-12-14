import itertools

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def distance(city1, city2):
    return distances_between_cities[city1][city2]

def traveling_salesman(cities):
    best_path = None
    min_distance = float('inf')

    for path in itertools.permutations(cities):
        path_distance = 0
        for i in range(len(path) - 1):
            path_distance += distance(path[i], path[i + 1])

        path_distance += distance(path[-1], path[0])

        if path_distance < min_distance:
            min_distance = path_distance
            best_path = path

    return best_path, min_distance

cities = [0, 1, 2, 3]
distances_between_cities = [
    [0, 29, 20, 21],
    [29, 0, 15, 18],
    [20, 15, 0, 25],
    [21, 18, 25, 0]
]

best_path, min_distance = traveling_salesman(cities)
print(f"Optimal path: {best_path}")
print(f"Minimum distance: {min_distance}")