# MEMORANDUM: Emergent-Hypergraph-Physics

**Rule #1.5**  
**Version**: 0.2 (Updated with Black Holes and Antimatter)  
**Date**: June 2026

## 1. Starting from Zero

We assume nothing from existing physics. Only the most fundamental observation: there exists *something* (experience/information) rather than absolute nothing.

This implies:
- Distinguishable elements (nodes)
- Relations between them (hyperedges)
- Local operations (rewriting rules) as the only mechanism of change

## 2. The Single Minimal Rule — Rule #1.5

**Basic Objects**:
- Indistinguishable nodes
- Only 3-ary hyperedges, each carrying a cyclic phase φ ∈ {0, 1, 2}

**Rewriting Rule**:
For every hyperedge (A, B, C; φ):
- Compute local phase imbalance δ = (sum of all incident phases) mod 3
- If δ ≡ 0 → Cyclic phase rotation (A → B → C)
- If δ ≢ 0 → Diffusion: introduce one new node D and create three new hyperedges with phases chosen to minimize the new δ

**Multiway Dynamics**:
All compatible rewrites occur simultaneously. Physical reality corresponds to branches that **maximize long-term stable neutral clusters** (δ ≡ 0).

## 3. Emergent Physics

- **Quantum Mechanics** — arises from multiway branching and stability selection
- **Space-Time** — emerges from causal structure and density of clusters
- **Particles** — stable neutral clusters
- **Forces** — different regimes of the same rule at different scales
- **Constants** — combinatorial invariants of the base-3 system (especially 137)

## 4. Black Holes

Black holes are a natural and inevitable consequence of Rule #1.5 at high density.

When the local tension τ (average |δ|) in a region becomes extremely high:
- The causal structure (possible future rewrites) bends inward so strongly that no causal influence can escape beyond a certain surface — the **event horizon**.
- Inside the horizon, rewriting continues intensely, but is causally disconnected from the external universe.
- There is **no mathematical singularity** — the discrete nature of the hypergraph prevents infinite compression.
- The interior consists of extremely dense, highly connected neutral clusters undergoing rapid rewriting.
- **Information preservation**: All information remains in the global multiway structure. Hawking radiation emerges naturally as gradual "evaporation" — pairs of virtual clusters appear near the horizon, one falls in, the other escapes, slowly reducing the black hole's mass.
- Very large black holes may have relatively calm interiors for infalling observers until they approach the high-density core.

This resolves the black hole information paradox within the theory.

## 5. Antimatter

Antimatter emerges naturally from the cyclic phase structure of Rule #1.5.

**Mechanism**:
- Each hyperedge has a cyclic phase φ ∈ {0,1,2}. Clusters can form with two opposite "chiralities" (directions of phase rotation).
- **Antiparticle** is a cluster with opposite phase rotation direction relative to normal matter.
- When a particle and its antiparticle meet, their phase imbalances cancel extremely efficiently (δ rapidly goes to 0), causing a cascade of diffusion transitions — this is observed as **annihilation** with release of high-energy photons (pure diffusion waves).
- The slight asymmetry between matter and antimatter (baryon asymmetry) can arise from the fixed preferred direction of cyclic rotation in Rule #1.5 combined with CP-violating effects during the early high-tension phase of the universe.

This provides a unified explanation for both the existence of antimatter and the observed matter-antimatter asymmetry without additional mechanisms.

## 6. Numerical Evidence

Long simulations show controlled growth, self-organization, emergence of charge-like, mass-like and spin-like properties, and stable balance leading to α ≈ 1/137.

## 7. Current Stage and Limitations

This remains an **experimental research project**. See `LIMITATIONS.md` for a honest assessment of current weaknesses.

We welcome rigorous criticism, mathematical derivations, simulation improvements, and collaboration.
