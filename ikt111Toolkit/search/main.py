import tkinter as tk
from graphs.city_graph import CityGraph
from graphs.grid_graph import GridGraph
# from breadth_first_search import BreadthFirstSearch
# from search_algorithems.a_star import AStar
from search_algorithems.a_star_simple import astar
# from simple_search import SimpleSearch
# from search_algorithems.djikstra import DijkstraSearch 

from search_visualization import SearchVisualization

def main():
    root = tk.Tk()
    # graph = CityGraph()
    graph = GridGraph(6,6)
    # search_algorithm = BreadthFirstSearch(graph)
    search_algorithm = astar(graph)
    # search_algorithm = SimpleSearch(graph)
    # search_algorithm = AStarSearch(graph)
    app = SearchVisualization(root, graph, search_algorithm)
    root.mainloop()

if __name__ == "__main__":
    main()