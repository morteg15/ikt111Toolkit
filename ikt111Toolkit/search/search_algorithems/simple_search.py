from search_algorithems.search_algorithm import SearchAlgorithm
from typing import List, Tuple, Any

class Simple(SearchAlgorithm):
    def search(self, start: Any, goal: Any) -> Tuple[List[Tuple[List[Any], int]], List[List[Any]]]:
        queue = [(start,)]
        visited = set()
        complete_paths = []
        search_process = []

        while queue:
            path = queue.pop(0)
            node = path[-1]
            search_process.append(path)

            if node == goal:
                cost = len(path) - 1  # Simple cost calculation: number of steps
                complete_paths.append((path, cost))
                break  # Stop after finding the first path

            if node not in visited:
                visited.add(node)
                for neighbor in self.graph.get_neighbors(node):
                    if neighbor not in visited:
                        new_path = path + (neighbor,)
                        queue.append(new_path)

        return complete_paths, search_process
