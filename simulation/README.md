# Functional Observer Simulation

This script simulates a minimal model of recursive observer invocation over a directed graph, illustrating the core mechanism behind the **Functional Observer Theory (FOT)**.

It demonstrates how a distributed network of nodes — each with incomplete information — can recursively converge on a hidden **latent state** through local observation, noisy estimation, and a cascading activation process.

## 🔧 How It Works

- A random **latent vector** is generated as ground truth.
- A sparse directed graph of observer nodes is created.
- A single node is seeded with a noisy version of the latent vector.
- Each node recursively updates its internal state by observing its active neighbors.
- When the network-wide estimates converge below a threshold, **invocation is triggered** — the latent structure has been recovered.

## 🌀 Why It Matters

This system models **emergent time, shared state, and latent coherence** — the core mechanics of recursive functional invocation. It offers a tiny but profound demonstration: that distributed observers can generate structure through mutual recursion without a central clock or coordinator.

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
