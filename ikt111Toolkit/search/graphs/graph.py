import tkinter as tk
from tkinter import ttk
import time
import math
from typing import Dict, List, Tuple, Any
from abc import ABC, abstractmethod
import random

class Graph(ABC):
    @abstractmethod
    def get_nodes(self) -> List[Any]:
        pass

    @abstractmethod
    def get_neighbors(self, node: Any) -> Dict[Any, int]:
        pass

    @abstractmethod
    def get_position(self, node: Any) -> Tuple[int, int]:
        pass


