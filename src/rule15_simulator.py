# src/rule15_simulator.py
# Simple implementation of Rule #1.5 Hypergraph Simulator

import random
import networkx as nx
from collections import defaultdict

class Rule15Simulator:
    def __init__(self, initial_nodes=30, initial_hyperedges=20):
        self.G = nx.Graph()  # For visualization, we use simple graph + hyperedge tracking
        self.nodes = list(range(initial_nodes))
        self.hyperedges = []  # list of tuples (a,b,c, phase)
        
        for i in range(initial_nodes):
            self.G.add_node(i)
        
        # Create initial random hyperedges
        for _ in range(initial_hyperedges):
            a, b, c = random.sample(self.nodes, 3)
            phase = random.randint(0, 2)
            self.hyperedges.append((a, b, c, phase))
    
    def compute_delta(self, hyperedge):
        a, b, c, phi = hyperedge
        # Simplified delta calculation
        incident = 0
        for he in self.hyperedges:
            if a in he[:3] or b in he[:3] or c in he[:3]:
                incident += he[3]
        return (incident % 3)
    
    def step(self):
        new_hyperedges = []
        for he in self.hyperedges:
            delta = self.compute_delta(he)
            a, b, c, phi = he
            
            if delta == 0:
                # Cyclic rotation
                new_phi = (phi + 1) % 3
                new_hyperedges.append((a, b, c, new_phi))
            else:
                # Diffusion: add new node
                d = max(self.nodes) + 1
                self.nodes.append(d)
                self.G.add_node(d)
                
                p1 = random.randint(0, 2)
                p2 = (3 - (p1 + phi) % 3) % 3
                p3 = (3 - (p1 + p2)) % 3
                
                new_hyperedges.append((a, b, d, p1))
                new_hyperedges.append((b, c, d, p2))
                new_hyperedges.append((c, a, d, p3))
        
        self.hyperedges = new_hyperedges
        return len(self.nodes), len(self.hyperedges)
    
    def run(self, steps=200):
        history = []
        for i in range(steps):
            n_nodes, n_edges = self.step()
            neutral = sum(1 for he in self.hyperedges if self.compute_delta(he) == 0)
            history.append((n_nodes, n_edges, neutral))
            if i % 50 == 0:
                print(f"Step {i}: Nodes={n_nodes}, Edges={n_edges}, Neutral={neutral}")
        return history

# Example run
if __name__ == "__main__":
    sim = Rule15Simulator()
    sim.run(300)
