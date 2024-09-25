from search_algorithems.search_algorithm import SearchAlgorithm
from typing import List, Tuple
import heapq

class astar(SearchAlgorithm):
    
    def heuristic(self, node: str, goal: str) -> float:
        # Placeholder heuristic function
        # In a real implementation, this would estimate the cost from node to goal
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    
    def search(self, start: str, goal: str) -> Tuple[List[Tuple[List[str], int]], List[List[str]]]:
        queue = [(0, 0, [start])]  # Priority queue of (f_score, g_score, path)
        visited = set()
        complete_paths = []
        search_process = []
        
        while queue:
            f_score, g_score, path = heapq.heappop(queue)
            node = path[-1]
            search_process.append(path)
            
            if node == goal:
                complete_paths.append((path, g_score))
                break
            
            if node not in visited:
                visited.add(node)
                for neighbor, step_cost in self.graph.get_neighbors(node).items():
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        new_g_score = g_score + step_cost
                        new_f_score = new_g_score + self.heuristic(neighbor, goal)
                        heapq.heappush(queue, (new_f_score, new_g_score, new_path))
        
        return complete_paths, search_process