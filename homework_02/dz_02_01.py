import itertools
from typing import NamedTuple


class Point(NamedTuple):
    """Точки на двумерной плоскости"""
    X: int
    Y: int


def main(start_point: Point, points: list) -> str:
    """Выводит кротчайший маршрут от точки к точке в формате:
    Координаты точек, следующие друг за другом, показывают найденный кратчайший путь
    с указанием промежуточной длины пути у каждой следующей точки.
    Полная продолжительность всего маршрута указана после символа равенства."""
    route = f'{start_point.X, start_point.Y}'
    paths = itertools.permutations(points, len(points))
    shortest_path, distance = _finding_the_shortest_path(start_point, paths)
    for index in range(0, len(shortest_path) - 1):
        distance_between_points = _calculates_the_distance_between_points(shortest_path[index],
                                                                          shortest_path[index + 1])
        route += f' -> {shortest_path[index + 1].X, shortest_path[index + 1].Y}[{distance_between_points}]'
    route += f' = {distance}'
    return route


def _finding_the_shortest_path(start_point: Point, paths: itertools.permutations) -> tuple:
    """Находит самый короткий маршрут"""
    result = []
    for path in paths:
        path = (start_point,) + path + (start_point,)
        distance = 0
        for index in range(0, len(path) - 1):
            distance += _calculates_the_distance_between_points(path[index], path[index + 1])
        result.append((path, distance))
    result.sort(key=lambda x: x[1])
    return result[0]


def _calculates_the_distance_between_points(point_1: Point, point_2: Point) -> float:
    """Находит расстояние между двумя точками на двумерной плоскости."""
    distance = ((point_2.X - point_1.X) ** 2 + (point_2.Y - point_1.Y) ** 2) ** 0.5
    return distance


if __name__ == '__main__':
    post_office = Point(0, 2)
    griboyedov_st = Point(2, 5)
    baker_street = Point(5, 2)
    bolshaya_sadovaya_st = Point(6, 6)
    evergreen_alley = Point(8, 3)
    one_more = Point(7, 7)

    addresses = [griboyedov_st, baker_street, bolshaya_sadovaya_st, evergreen_alley, one_more]
    print(main(post_office, addresses))
