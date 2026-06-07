# MEMORANDUM: Emergent-Hypergraph-Physics

**Rule #1.5**  
**Version**: 0.5 (Honest Version)  
**Date**: June 2026

## 1. Starting Assumptions

We start with minimal ontological commitments:
- There exists information in the form of distinguishable elements (nodes) and relations between them (hyperedges).
- Change occurs exclusively through local rewriting operations.

No concepts from quantum mechanics, relativity, or particle physics are assumed a priori.

## 2. Rule #1.5

**Objects**:
- Nodes (indistinguishable)
- 3-ary hyperedges with discrete phase φ ∈ {0, 1, 2}

**Rewriting Rule**:
For each hyperedge (A, B, C; φ):
- Compute local phase imbalance δ = (sum of incident phases) mod 3
- If δ ≡ 0: perform cyclic phase rotation
- If δ ≢ 0: perform diffusion (introduce one new node and three new hyperedges chosen to reduce imbalance)

**Evolution**: Multiway system where all compatible rewrites occur, with branches selected according to a stability principle (maximizing neutral clusters δ ≡ 0 over time).

## 3. Observed Behavior in Simulations

Numerical experiments (up to ~800–1000 steps) show:
- Steady growth in the number of nodes and hyperedges
- Formation and increasing prevalence of neutral clusters (δ ≡ 0)
- A statistical balance between diffusion and rotation steps that stabilizes near 1/137 in our implementation
- Emergence of rudimentary cluster properties that can be interpreted as mass-like, charge-like, and spin-like

## 4. Relation to Known Physics

We observe several **qualitative analogies**:
- High-density regions that trap causal influence (resembling black holes)
- Global relaxation processes (resembling cosmic expansion)
- Stable clusters (resembling particles)
- Phase-based distinctions (resembling charge and antimatter)

**Important note**: These are interpretive analogies. We have not derived the Standard Model, General Relativity, or precise experimental values as rigorous limiting cases. Some numerical coincidences (particularly 1/137) depend on the specific choice of troic phases and stability metric.

## 5. Current Status

This is an **early-stage experimental research project**. 

The model demonstrates interesting self-organizing behavior, but significant work remains to establish whether it can reproduce known physics in a non-ad-hoc way.

See `LIMITATIONS.md` for a detailed list of weaknesses.

---

We invite critical analysis and collaboration.
