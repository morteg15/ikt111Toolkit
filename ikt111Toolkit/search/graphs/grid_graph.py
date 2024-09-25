from graphs.graphs import Graph
from typing import Dict, List, Tuple
import random



class GridGraph(Graph):

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = self._generate_grid()

    def _generate_grid(self) -> Dict[Tuple[int, int], Dict]:
        grid = {}
        for x in range(self.width):
            for y in range(self.height):
                neighbors = {}
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if random.random() > 0.3:  # 70% chance of connection
                            neighbors[(nx, ny)] = 1
                grid[(x, y)] = {'neighbors': neighbors}
        return grid

    def get_nodes(self) -> List[Tuple[int, int]]:
        return list(self.grid.keys())

    def get_neighbors(self, node: Tuple[int, int]) -> Dict[Tuple[int, int], int]:
        return self.grid[node]['neighbors']

    def get_position(self, node: Tuple[int, int]) -> Tuple[int, int]:
        x, y = node
        # Calculate the center of the canvas
        canvas_center_x = 500  # Assuming canvas width is 1000
        canvas_center_y = 500  # Assuming canvas height is 1000
        
        # Calculate the total width and height of the grid
        grid_width = self.width * 50
        grid_height = self.height * 50
        
        # Calculate the top-left corner of the grid
        grid_start_x = canvas_center_x - grid_width // 2
        grid_start_y = canvas_center_y - grid_height // 2
        
        # Calculate the position of the node
        node_x = grid_start_x + x * 50 + 25
        node_y = grid_start_y + y * 50 + 25
        
        return (node_x, node_y)