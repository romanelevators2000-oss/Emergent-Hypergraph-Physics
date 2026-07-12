"""
rule15_simulator.py: The core rewrite engine for EHP.
Implements the node-density gravity simulation via deterministic graph rewriting.
"""

import networkx as nx
import random

class EHP_Simulator:
    def __init__(self, num_nodes):
        # Инициализируем плоскую решетку как начальное состояние
        self.graph = nx.grid_2d_graph(int(num_nodes**0.5), int(num_nodes**0.5))
        self.tick = 0

    def get_node_density(self, node):
        """Возвращает количество связей (степень узла) как индикатор плотности."""
        return self.graph.degree[node]

    def apply_rewriting_rule(self):
        """
        Основное правило перезаписи (The Rewrite Rule):
        Если узел имеет плотность > порога, он 'расщепляется', 
        увеличивая локальное количество узлов.
        """
        nodes_to_split = [n for n in self.graph.nodes if self.graph.degree[n] > 4]
        
        for node in nodes_to_split:
            # Алгоритмическое 'сжатие' (увеличение локальной плотности графа)
            self._split_node(node)
        
        self.tick += 1

    def _split_node(self, node):
        """Логика 'алгоритмического уплотнения' (интеграция новых узлов)."""
        # Добавляем новый узел в гиперграф для компенсации высокого 'давления'
        new_node = (node[0], node[1], self.tick) 
        self.graph.add_node(new_node)
        self.graph.add_edge(node, new_node)

    def run(self, iterations):
        for _ in range(iterations):
            self.apply_rewriting_rule()
            print(f"Tick {self.tick}: Total nodes = {self.graph.number_of_nodes()}")

# Пример запуска симуляции
if __name__ == "__main__":
    sim = EHP_Simulator(num_nodes=100)
    sim.run(iterations=5)
