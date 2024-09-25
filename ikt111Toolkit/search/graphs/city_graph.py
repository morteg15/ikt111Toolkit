from typing import Dict, List, Tuple
from graphs.graphs import Graph

class CityGraph(Graph):
    def __init__(self):
        self.graph: Dict[str, Dict] = {
            'Grimstad': {'position': (300, 400), 'neighbors': {'Arendal': 5, 'Lillesand': 3, 'Fevik': 2}},
            'Arendal': {'position': (500, 300), 'neighbors': {'Tvedestrand': 4, 'Grimstad': 5, 'Froland': 3, 'Eydehavn': 2}},
            'Lillesand': {'position': (200, 600), 'neighbors': {'Kristiansand': 4, 'Grimstad': 3, 'Birkeland': 3}},
            'Tvedestrand': {'position': (700, 200), 'neighbors': {'Arendal': 4, 'Risør': 3, 'Vegårshei': 4}},
            'Kristiansand': {'position': (100, 800), 'neighbors': {'Lillesand': 4, 'Vennesla': 3, 'Søgne': 2}},
            'Risør': {'position': (900, 100), 'neighbors': {'Tvedestrand': 3, 'Gjerstad': 4}},
            'Froland': {'position': (600, 500), 'neighbors': {'Arendal': 3, 'Åmli': 5, 'Birkeland': 4}},
            'Birkeland': {'position': (400, 600), 'neighbors': {'Lillesand': 3, 'Froland': 4, 'Evje': 5}},
            'Vennesla': {'position': (200, 900), 'neighbors': {'Kristiansand': 3, 'Iveland': 4}},
            'Fevik': {'position': (360, 360), 'neighbors': {'Grimstad': 2, 'Arendal': 3}},
            'Eydehavn': {'position': (560, 260), 'neighbors': {'Arendal': 2, 'Tvedestrand': 3}},
            'Vegårshei': {'position': (800, 300), 'neighbors': {'Tvedestrand': 4, 'Åmli': 3, 'Gjerstad': 2}},
            'Søgne': {'position': (40, 760), 'neighbors': {'Kristiansand': 2, 'Mandal': 3}},
            'Gjerstad': {'position': (960, 200), 'neighbors': {'Risør': 4, 'Vegårshei': 2}},
            'Åmli': {'position': (700, 400), 'neighbors': {'Froland': 5, 'Vegårshei': 3, 'Evje': 4}},
            'Evje': {'position': (500, 700), 'neighbors': {'Birkeland': 5, 'Åmli': 4, 'Iveland': 3}},
            'Iveland': {'position': (300, 800), 'neighbors': {'Vennesla': 4, 'Evje': 3}},
            'Mandal': {'position': (0, 900), 'neighbors': {'Søgne': 3}}
        }

    def get_nodes(self) -> List[str]:
        return list(self.graph.keys())

    def get_neighbors(self, node: str) -> Dict[str, int]:
        return self.graph[node]['neighbors']

    def get_position(self, node: str) -> Tuple[int, int]:
        return self.graph[node]['position']
