"""
EHP Hypergraph Physics Simulator — True Hypergraph Version (hypernetx)
Rule #1.5+: Density-driven hyperedge rewriting + node birth
"""

import hypernetx as hnx
import random
import numpy as np

class EHPHypergraphSimulator:
    def __init__(self, num_nodes: int = 400, seed: int = 42):
        random.seed(seed)
        np.random.seed(seed)
        
        self.H = hnx.Hypergraph()
        self.tick = 0
        
        # Nodes as strings (более стабильная работа с hypernetx)
        self.nodes = [f"n{i}" for i in range(num_nodes)]
        for n in self.nodes:
            self.H.add_node(n)
        
        self._create_initial_structure()
        self._create_mass_cluster()
        
        print(f"✅ EHP Hypergraph initialized | Nodes: {len(self.H.nodes)} | Hyperedges: {len(self.H.edges)}")

    def _create_initial_structure(self):
        """Базовая структура + случайные гиперрёбра"""
        n = len(self.nodes)
        for i in range(n):
            node = self.nodes[i]
            # Локальные связи
            for j in range(1, min(5, n - i)):
                if random.random() < 0.6:
                    self.H.add_edge(f"base_{i}_{j}", [node, self.nodes[i+j]])
            # Высокоразмерные гиперрёбра
            if random.random() < 0.15:
                k = random.randint(3, 5)
                subset = random.sample(self.nodes[max(0, i-10):i+10], k)
                self.H.add_edge(f"init_{i}", subset)

    def _create_mass_cluster(self):
        """Центральный mass cluster"""
        cluster = self.nodes[:len(self.nodes)//8]
        for i in range(60):
            k = random.randint(3, 6)
            subset = random.sample(cluster, k)
            self.H.add_edge(f"mass_{i}", subset)

    def get_density(self, node: str) -> int:
        """Плотность = количество инцидентных гиперрёбер"""
        return len(self.H.incidence_dict.get(node, []))

    def apply_rewriting_rule(self):
        """Основное правило перезаписи"""
        current_nodes = list(self.H.nodes)
        random.shuffle(current_nodes)
        added = 0
        
        for node in current_nodes[:len(current_nodes)//3]:  # частичная обработка
            density = self.get_density(node)
            if density > 5:  # порог высокой плотности
                # Рождение нового узла
                new_node = f"n_new_t{self.tick}_{added}"
                self.H.add_node(new_node)
                added += 1
                
                # Создаём новое гиперребро (emergent connection)
                incident = list(self.H.incidence_dict.get(node, []))
                if incident:
                    sample = random.sample(incident, min(3, len(incident)))
                    related = set()
                    for eid in sample:
                        related.update(self.H.edge(eid))
                    related_list = list(related)[:5]
                    related_list.append(new_node)
                    self.H.add_edge(f"split_t{self.tick}_{added}", related_list)
        
        self.tick += 1
        return added

    def run(self, iterations: int = 10):
        for _ in range(iterations):
            added = self.apply_rewriting_rule()
            print(f"Tick {self.tick:3d} | Nodes: {len(self.H.nodes):5d} | "
                  f"Hyperedges: {len(self.H.edges):5d} | Added: {added}")

    def stats(self):
        densities = [self.get_density(n) for n in list(self.H.nodes)[:400]]
        avg_density = sum(densities) / len(densities) if densities else 0
        print(f"\n=== Final Stats ===")
        print(f"Nodes: {len(self.H.nodes)}")
        print(f"Hyperedges: {len(self.H.edges)}")
        print(f"Avg Density: {avg_density:.2f}")
        print(f"Max Order: {max((len(self.H.edge(e)) for e in self.H.edges), default=0)}")


if __name__ == "__main__":
    sim = EHPHypergraphSimulator(num_nodes=350, seed=42)
    sim.run(iterations=8)
    sim.stats()
