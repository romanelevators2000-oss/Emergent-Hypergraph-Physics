# src/rule15_simulator.py
# Improved Rule #1.5 Hypergraph Simulator with statistics and plotting

import random
import matplotlib.pyplot as plt
from collections import defaultdict

class Rule15Simulator:
    def __init__(self, initial_nodes=40, initial_hyperedges=25, seed=42):
        random.seed(seed)
        self.nodes = list(range(initial_nodes))
        self.hyperedges = []  # (a, b, c, phase)
        
        # Create initial hyperedges
        for _ in range(initial_hyperedges):
            a, b, c = random.sample(self.nodes, 3)
            phase = random.randint(0, 2)
            self.hyperedges.append([a, b, c, phase])  # list for mutability if needed
    
    def compute_delta(self, idx):
        """Compute phase imbalance for a hyperedge"""
        a, b, c, phi = self.hyperedges[idx]
        incident_sum = phi
        for he in self.hyperedges:
            if a in he[:3] or b in he[:3] or c in he[:3]:
                incident_sum += he[3]
        return incident_sum % 3
    
    def step(self):
        new_hyperedges = []
        for i in range(len(self.hyperedges)):
            delta = self.compute_delta(i)
            a, b, c, phi = self.hyperedges[i]
            
            if delta == 0:
                # Cyclic rotation
                new_phi = (phi + 1) % 3
                new_hyperedges.append([a, b, c, new_phi])
            else:
                # Diffusion: add new node
                d = max(self.nodes) + 1
                self.nodes.append(d)
                
                # Choose phases to reduce imbalance
                p1 = random.randint(0, 2)
                p2 = (3 - (p1 + phi) % 3) % 3
                p3 = (3 - (p1 + p2)) % 3
                
                new_hyperedges.append([a, b, d, p1])
                new_hyperedges.append([b, c, d, p2])
                new_hyperedges.append([c, a, d, p3])
        
        self.hyperedges = new_hyperedges
        return len(self.nodes), len(self.hyperedges)
    
    def count_neutral(self):
        return sum(1 for i in range(len(self.hyperedges)) if self.compute_delta(i) == 0)
    
    def run(self, steps=500, plot=True):
        history_nodes = []
        history_edges = []
        history_neutral = []
        
        for step in range(steps):
            n_nodes, n_edges = self.step()
            neutral = self.count_neutral()
            
            history_nodes.append(n_nodes)
            history_edges.append(n_edges)
            history_neutral.append(neutral)
            
            if step % 100 == 0 or step == steps-1:
                print(f"Step {step:3d} | Nodes: {n_nodes:5d} | Edges: {n_edges:5d} | Neutral: {neutral:5d} ({neutral/n_edges*100:.1f}%)")
        
        if plot:
            self.plot_results(history_nodes, history_edges, history_neutral)
        
        return history_nodes, history_edges, history_neutral
    
    def plot_results(self, nodes, edges, neutral):
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))
        
        axs[0,0].plot(nodes, label='Nodes')
        axs[0,0].set_title('Number of Nodes')
        axs[0,0].legend()
        
        axs[0,1].plot(edges, label='Hyperedges', color='orange')
        axs[0,1].set_title('Number of Hyperedges')
        axs[0,1].legend()
        
        axs[1,0].plot(neutral, label='Neutral Clusters', color='green')
        axs[1,0].set_title('Neutral Clusters Growth')
        axs[1,0].legend()
        
        ratio = [n/e if e > 0 else 0 for n,e in zip(neutral, edges)]
        axs[1,1].plot(ratio, label='Neutral Ratio', color='red')
        axs[1,1].set_title('Neutral / Total Hyperedges Ratio')
        axs[1,1].legend()
        
        plt.tight_layout()
        plt.savefig('results/growth_plot.png', dpi=200, bbox_inches='tight')
        print("Graph saved to results/growth_plot.png")
        plt.show()


# Run simulation
if __name__ == "__main__":
    sim = Rule15Simulator()
    sim.run(steps=600)
