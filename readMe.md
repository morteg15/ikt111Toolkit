# H1 IKT111 Toolkit - Search Visualizer

This toolkit provides utilities for the IKT111 course, including a search algorithm visualizer.
Installation

```bash
pip install ikt111Toolkit
```

Usage

**Import the necessary classes:**

```python
from ikt111Toolkit.search import GridGraph, SearchAlgorithm, SearchVisualization
import tkinter as tk`
```

**Create your own search algorithm by inheriting from SearchAlgorithm**

```python
class MySearch(SearchAlgorithm):
    def search(self, start, goal):
        # Implement your search algorithm here
        # Return (complete_paths, search_process)
        pass
```

**Set up the visualization**

```python
def main():
    root = tk.Tk()
    graph = GridGraph(6, 6)
    search_algorithm = MySearch(graph)
    app = SearchVisualization(root, graph, search_algorithm)
    root.mainloop()

if __name__ == "__main__":
    main()
```

**Run your script to see the visualization of your search algorithm!**
