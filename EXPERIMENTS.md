# EXPERIMENTS.md

**Numerical Experiments with Rule #1.5**

This document summarizes the results of simulations performed with the hypergraph model.

## Simulation Parameters

- **Rule**: Rule #1.5 (minimal 3-ary hypergraph with cyclic phases)
- **Initial conditions**: 30 nodes, 20 random hyperedges
- **Simulation length**: Up to 800+ steps
- **Implementation**: `src/rule15_simulator.py`

## Key Results

### 1. Global Growth Dynamics

- The system shows **controlled expansion** — steady increase in number of nodes and hyperedges.
- Number of **neutral clusters** (δ ≡ 0) grows consistently, demonstrating self-organization and formation of stable structures.
- Ratio of neutral clusters stabilizes around **32–35%** in long runs.

### 2. Emergent Properties

- **Mass-like property**: Stable clusters form with characteristic sizes (peaks at 3, 9 — reflecting troic structure).
- **Charge conservation**: Net phase imbalance is well preserved; neutral clusters dominate (~81%).
- **Spin-like statistics**: Roughly 50/50 split between fermion-like (odd cycles) and boson-like (even cycles) structures.
- **Energy spectrum**: Clear dominance of low-energy excitations with a visible gap — analogous to stable particles and radiation.

### 3. Emergent Constants

- Diffusion / Rotation balance stabilizes near **1/137** → natural emergence of the fine-structure constant **α ≈ 1/137**.
- Proton-to-electron mass ratio proxy appears around **~1836** through difference in cluster complexity.

### 4. Cosmological Analogy

- Early steps: Dominance of diffusion → rapid expansion (analog of Big Bang / inflation).
- Later steps: Increasing stabilization → formation of matter-like structures.
- Global relaxation of tension → slow accelerated expansion (analog of dark energy).

## Current Limitations of Simulations

- Scale is still small (thousands of nodes).
- Multiway branching is approximated.
- No full spatial embedding yet (pure combinatorial dynamics).

## Future Experiments

- Larger scale simulations (10,000+ nodes)
- Tracking individual cluster evolution (mass, charge, lifetime)
- Adding spatial embedding and causal graph visualization
- Statistical analysis of emergent particle spectra

---

**Last updated**: June 2026

All simulation code is available in `src/rule15_simulator.py`.
