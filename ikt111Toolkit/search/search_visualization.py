
import tkinter as tk
from tkinter import ttk
import time
from graphs.graphs import Graph
from search_algorithems.search_algorithm import SearchAlgorithm
from graphs.city_graph import CityGraph
from graphs.grid_graph import GridGraph
import tkinter as tk
from tkinter import ttk
import time
from typing import Any



class SearchVisualization:
    def __init__(self, master: tk.Tk, graph: Graph, search_algorithm: SearchAlgorithm):
        self.master = master
        self.master.title("Search Algorithm Visualization")
        
        self.graph = graph
        self.search_algorithm = search_algorithm

        self.canvas = tk.Canvas(master, width=1000, height=1000, bg='#F0F0F0')
        self.canvas.pack()

        self.start_var = tk.StringVar()
        self.goal_var = tk.StringVar()
        
        self.canvas.create_text(100, 20, text="Start Node:", anchor="w", font=("Arial", 12, "bold"))
        self.start_dropdown = ttk.Combobox(master, textvariable=self.start_var, values=self.get_node_values(), width=15)
        self.canvas.create_window(200, 20, window=self.start_dropdown, anchor="w")

        self.canvas.create_text(400, 20, text="Goal Node:", anchor="w", font=("Arial", 12, "bold"))
        self.goal_dropdown = ttk.Combobox(master, textvariable=self.goal_var, values=self.get_node_values(), width=15)
        self.canvas.create_window(500, 20, window=self.goal_dropdown, anchor="w")

        self.start_button = tk.Button(master, text="Start Search", command=self.start_search, bg='#4CAF50', fg='white', font=("Arial", 10, "bold"))
        self.canvas.create_window(700, 20, window=self.start_button)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_animation, bg='#f39c12', fg='white', font=("Arial", 10, "bold"))
        self.canvas.create_window(800, 20, window=self.reset_button)

        self.draw_graph()

    def get_node_values(self):
        if isinstance(self.graph, CityGraph):
            return self.graph.get_nodes()
        elif isinstance(self.graph, GridGraph):
            return [str(node) for node in self.graph.get_nodes()]

    def parse_node(self, node_str: str) -> Any:
        if isinstance(self.graph, CityGraph):
            return node_str
        elif isinstance(self.graph, GridGraph):
            return eval(node_str)  # Safe to use eval here as we control the input format

    def draw_graph(self):
        if isinstance(self.graph, CityGraph):
            self.draw_city_graph()
        elif isinstance(self.graph, GridGraph):
            self.draw_grid_graph()

    def draw_city_graph(self):
        for city in self.graph.get_nodes():
            x, y = self.graph.get_position(city)
            self.canvas.create_oval(x-8, y-8, x+8, y+8, fill="#3498db", outline="#2980b9", width=2, tags="node")
            self.canvas.create_text(x, y-20, text=city, font=("Arial", 10, "bold"), fill="#34495e", tags="node_label")

        for city in self.graph.get_nodes():
            x1, y1 = self.graph.get_position(city)
            for neighbor, cost in self.graph.get_neighbors(city).items():
                x2, y2 = self.graph.get_position(neighbor)
                self.canvas.create_line(x1, y1, x2, y2, fill="#95a5a6", width=2, tags="edge")
                midx, midy = (x1 + x2) / 2, (y1 + y2) / 2
                self.canvas.create_oval(midx-10, midy-10, midx+10, midy+10, fill="white", outline="#95a5a6", tags="cost_bg")
                self.canvas.create_text(midx, midy, text=str(cost), font=("Arial", 8, "bold"), fill="#34495e", tags="cost_label")

    def draw_grid_graph(self):
        for node in self.graph.get_nodes():
            x, y = self.graph.get_position(node)
            self.canvas.create_rectangle(x-20, y-20, x+20, y+20, fill="#3498db", outline="#2980b9", width=2, tags="node")

        for node in self.graph.get_nodes():
            x1, y1 = self.graph.get_position(node)
            for neighbor in self.graph.get_neighbors(node):
                x2, y2 = self.graph.get_position(neighbor)
                self.canvas.create_line(x1, y1, x2, y2, fill="#95a5a6", width=2, tags="edge")

    def start_search(self):
        start_node = self.parse_node(self.start_var.get())
        goal_node = self.parse_node(self.goal_var.get())
        if not start_node or not goal_node:
            return

        self.canvas.delete("highlight", "path", "cost", "current_search", "current_path")
        paths, search_process = self.search_algorithm.search(start_node, goal_node)
        
        if paths:
            optimal_path = min(paths, key=lambda x: x[1])
            self.animate_search(search_process, paths, optimal_path)
        else:
            print("No path found")

    def animate_search(self, search_process, all_paths, optimal_path):
        # Animate the search process
        for path in search_process:
            self.canvas.delete("current_search")
            for i in range(len(path)):
                x, y = self.graph.get_position(path[i])
                self.canvas.create_oval(x-10, y-10, x+10, y+10, outline="#9b59b6", width=3, tags="current_search")
                if i < len(path) - 1:
                    next_x, next_y = self.graph.get_position(path[i+1])
                    self.canvas.create_line(x, y, next_x, next_y, fill="#9b59b6", width=3, tags="current_search")
            
            self.master.update()
            time.sleep(0.3)

        # Animate all explored paths
        for path, _ in all_paths:
            self.canvas.delete("current_path")
            for i in range(len(path)):
                x, y = self.graph.get_position(path[i])
                self.canvas.create_oval(x-10, y-10, x+10, y+10, outline="#e67e22", width=3, tags="current_path")
                if i < len(path) - 1:
                    next_x, next_y = self.graph.get_position(path[i+1])
                    self.canvas.create_line(x, y, next_x, next_y, fill="#e67e22", width=3, tags="current_path")
            
            self.master.update()
            time.sleep(0.5)

        # Highlight the optimal path
        path, cost = optimal_path
        self.canvas.delete("highlight")
        for i in range(len(path)):
            x, y = self.graph.get_position(path[i])
            self.canvas.create_oval(x-10, y-10, x+10, y+10, outline="#e74c3c", width=3, tags="highlight")
            if i < len(path) - 1:
                next_x, next_y = self.graph.get_position(path[i+1])
                self.canvas.create_line(x, y, next_x, next_y, fill="#e74c3c", width=3, tags="highlight")

        # Display the total cost of the optimal path
        self.canvas.create_text(500, 980, text=f"Total Cost: {cost}", font=("Arial", 16, "bold"), fill="#2c3e50", tags="cost")

    def reset_animation(self):
        self.canvas.delete("highlight", "path", "cost", "current_search", "current_path")
        self.start_var.set('')
        self.goal_var.set('')