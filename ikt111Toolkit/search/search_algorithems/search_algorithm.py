from typing import List, Tuple
from abc import ABC, abstractmethod
from graphs.city_graph import CityGraph


class SearchAlgorithm(ABC):
    def __init__(self, graph: CityGraph):
        self.graph = graph

    @abstractmethod
    def search(self, start: str, goal: str) -> Tuple[List[Tuple[List[str], int]], List[List[str]]]:
        pass
