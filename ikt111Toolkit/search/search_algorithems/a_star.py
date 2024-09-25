from search_algorithems.search_algorithm import SearchAlgorithm
from typing import List, Tuple, Any, Dict
import heapq

class AStar(SearchAlgorithm):
    
    def heuristic(self, node: Tuple[int, int], goal: Tuple[int, int]) -> float:
        # Manhattan Distance heuristic
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    
    def search(self, start: Tuple[int, int], goal: Tuple[int, int]) -> Tuple[List[Tuple[List[Tuple[int, int]], int]], List[List[Tuple[int, int]]]]:
        queue = [(0, 0, start, [start])]  # (f_score, g_score, node, path)
        g_scores = {start: 0}
        search_process = []
        
        while queue:
            f, g, node, path = heapq.heappop(queue)
            
            if node == goal:
                return [(path, g)], search_process
            
            search_process.append(path)
            
            for neighbor, cost in self.graph.get_neighbors(node).items():
                new_g = g + cost
                if neighbor not in g_scores or new_g < g_scores[neighbor]:
                    g_scores[neighbor] = new_g
                    new_f = new_g + self.heuristic(neighbor, goal)
                    new_path = path + [neighbor]
                    heapq.heappush(queue, (new_f, new_g, neighbor, new_path))
        
        return [], search_process  # No path found