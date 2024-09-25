
from search_algorithems.search_algorithm import SearchAlgorithm
from typing import List, Tuple


class BreadthFirstSearch(SearchAlgorithm):
    def search(self, start: str, goal: str) -> Tuple[List[Tuple[List[str], int]], List[List[str]]]:
        queue = [([start], 0)]
        visited = set()
        complete_paths = []
        search_process = []

        while queue:
            path, cost = queue.pop(0)
            city = path[-1]

            search_process.append(path)

            if city == goal:
                complete_paths.append((path, cost))
                continue

            if city not in visited:
                visited.add(city)

                for neighbor, step_cost in self.graph.get_neighbors(city).items():
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        new_cost = cost + step_cost
                        queue.append((new_path, new_cost))

        return complete_paths, search_process