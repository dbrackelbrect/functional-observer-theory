import networkx as nx
import numpy as np

# === CONFIGURATION ===
N = 100
k = 5
alpha = 0.7
noise = 0.05
iterations = 3000
seed_neighbors = 40

# === INIT SYSTEM ===
G = nx.DiGraph()
latent = np.random.randn(k)
nodes = {
    i: {'state': np.zeros(k), 'estimate': np.zeros(k), 'active': False}
    for i in range(N)
}
G.add_nodes_from((i, attr) for i, attr in nodes.items())
G.add_edges_from([(i, j) for i in range(N) for j in np.random.choice(N, 10, replace=False)])

# === FUNCTIONS ===
def observe(n):
    if not G.nodes[n]['active']: return np.zeros(k)
    neighbors = [G.nodes[j]['state'] + np.random.randn(k) * noise
                 for j in G.neighbors(n) if G.nodes[j]['active']]
    return np.mean(neighbors, axis=0) if neighbors else np.zeros(k)

def update(n):
    o = observe(n)
    est = G.nodes[n]['estimate']
    G.nodes[n]['estimate'] = alpha * o + (1 - alpha) * est
    G.nodes[n]['state'] = G.nodes[n]['estimate']
    G.nodes[n]['active'] = True

def invoked(thresh=0.01, min_active=10):
    vals = [G.nodes[n]['estimate'] for n in G.nodes if G.nodes[n]['active']]
    if len(vals) < min_active: return False
    return np.var(vals, axis=0).mean() < thresh

# === SEEDING ===
seed = np.random.randint(N)
G.nodes[seed]['state'] = latent + np.random.randn(k) * noise
G.nodes[seed]['active'] = True
for j in list(G.neighbors(seed))[:seed_neighbors]:
    G.nodes[j]['state'] = G.nodes[seed]['state'] + np.random.randn(k) * noise
    G.nodes[j]['active'] = True

# === LOOP ===
invoked_time = None
for t in range(iterations):
    for n in G.nodes:
        if G.nodes[n]['active']:
            update(n)
    if invoked_time is None and invoked():
        invoked_time = t
        break

# === OUTPUT ===
estimates = [G.nodes[n]['estimate'] for n in G.nodes if G.nodes[n]['active']]
invoked_state = np.mean(estimates, axis=0)
error = np.linalg.norm(invoked_state - latent)

print(f"\nInvocation at t={invoked_time}: Reality answers!\n")
print("Invoked state:\n", invoked_state)
print("Latent state:\n", latent)
print(f"Invocation error (L2 norm): {error:.4f}")
