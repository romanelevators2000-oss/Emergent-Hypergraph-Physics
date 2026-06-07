# MEMORANDUM: Emergent-Hypergraph-Physics

**Rule #1.5**  
**Version**: 0.4 (Honest Assessment)  
**Date**: June 2026

## 1. Starting Point

This project is an attempt to construct a unified physical theory from minimal assumptions. We begin with almost nothing:

- There exists some form of information (distinguishable elements and relations).
- Change occurs through local rewriting operations.

No assumptions from quantum mechanics, general relativity, or the Standard Model are used as input.

## 2. Rule #1.5

**Objects**:
- Indistinguishable nodes
- 3-ary hyperedges with phase φ ∈ {0, 1, 2}

**Rewriting Rule**:
For each hyperedge (A, B, C; φ):
- Compute local phase imbalance δ = (sum of incident phases) mod 3
- If δ ≡ 0 → cyclic phase rotation
- If δ ≢ 0 → diffusion (add one new node and three new hyperedges minimizing new imbalance)

**Dynamics**: Multiway evolution with selection favoring branches that maximize the number of stable neutral clusters (δ ≡ 0) over long term.

## 3. What We Actually Observe in Simulations

- The system shows **self-organization**: growth of nodes and hyperedges, and formation of relatively stable clusters.
- Neutral clusters (δ ≡ 0) become more common over time.
- A statistical balance between diffusion and rotation transitions appears, stabilizing around ~1/137 in our runs.
- Clusters exhibit rudimentary emergent properties that we can interpret as mass-like, charge-like, and spin-like.

## 4. Correspondence with Known Physics

We observe several **qualitative similarities** with real physics:

- Formation of stable structures analogous to particles
- Different dynamical regimes at different scales
- Global relaxation behavior that can be interpreted as cosmic expansion
- High-density regions that trap causal influence (analogous to black holes)

**Important clarification**: Many of these correspondences are interpretive. We have not yet derived the Standard Model or General Relativity as rigorous limits. The numerical matches (especially 1/137) are encouraging but currently rest on specific choices in the rule and measurement method.

## 5. Current Status

This is an **experimental exploratory model**. 

**Strengths**:
- Extremely minimal ontology and rule
- Clear mechanism of emergence
- Working simulations showing non-trivial self-organization

**Weaknesses** (see LIMITATIONS.md for details):
- No rigorous derivation of known physical laws
- Small simulation scale
- Some numerical matches may result from model choices rather than deep necessity
- Lack of unique testable predictions that clearly distinguish it from existing theories

## 6. Goals

- Improve mathematical understanding of the continuum limit
- Develop larger and more sophisticated simulations
- Find genuinely new, falsifiable predictions
- Subject the model to rigorous criticism

---

This project is a work in progress. We do not claim to have solved fundamental physics. The goal is honest exploration of whether a single minimal rewriting rule can serve as a foundation for physics.

Feedback and criticism are strongly encouraged.
