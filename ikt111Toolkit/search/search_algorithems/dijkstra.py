from search_algorithems.search_algorithm import SearchAlgorithm
from typing import List, Tuple, Any, Dict
import heapq

class Dijkstra(SearchAlgorithm):
    def search(self, start: Any, goal: Any) -> Tuple[List[Tuple[List[Any], int]], List[List[Any]]]:
        # Initialize the frontier with the start node
        # The frontier is a priority queue of tuples: (total_distance, path)
        # We use a list for the path to keep track of the route taken
        frontier = [(0, [start])]

        # Keep track of visited nodes to avoid cycles
        visited = set()

        # List to store the search process for visualization
        search_process = []

        while frontier:
            # Get the path with the smallest total distance
            current_distance, current_path = heapq.heappop(frontier)

            # The current node is the last node in the current path
            current = current_path[-1]

            # Add the current path to the search process for visualization
            search_process.append(current_path)

            # If we've reached the goal, we're done
            if current == goal:
                # Return the path and its total distance, along with the search process
                return [(current_path, current_distance)], search_process

            # If we've already visited this node, skip it
            if current in visited:
                continue

            # Mark the current node as visited
            visited.add(current)

            # Explore the neighbors of the current node
            for neighbor, weight in self.graph.get_neighbors(current).items():
                # Skip already visited neighbors
                if neighbor not in visited:
                    # Calculate the total distance to reach this neighbor
                    new_distance = current_distance + weight
                    # Create a new path by extending the current path
                    new_path = current_path + [neighbor]
                    # Add the new path to the frontier
                    heapq.heappush(frontier, (new_distance, new_path))

        # If we've exhausted all possibilities without finding the goal, return empty results
        return [], search_process  # No path found