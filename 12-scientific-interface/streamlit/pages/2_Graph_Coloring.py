import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Step generators
def bruteforce_steps(graph, k):
    n = graph.number_of_nodes()
    colors = [0] * n
    def is_valid():
        for u, v in graph.edges():
            if colors[u] == colors[v]:
                return False
        return True
    yield "Start", colors.copy()
    while True:
        if is_valid():
            yield "Valid coloring found", colors.copy()
            return
        i = 0
        while i < n:
            colors[i] += 1
            if colors[i] < k:
                break
            colors[i] = 0
            i += 1
        if i == n:
            yield "All assignments tried", colors.copy()
            return
        yield f"Trying {colors}", colors.copy()

def backtracking_steps(graph, k):
    n = graph.number_of_nodes()
    colors = [-1] * n
    v = 0
    yield "Initialize", colors.copy()
    while 0 <= v < n:
        colors[v] += 1
        while colors[v] < k and any(colors[v] == colors[u] for u in graph.neighbors(v) if colors[u] != -1):
            colors[v] += 1
        if colors[v] < k:
            yield f"Assign color {colors[v]} to v{v}", colors.copy()
            v += 1
            if v < n:
                colors[v] = -1
        else:
            yield f"Backtracking from v{v}", colors.copy()
            colors[v] = -1
            v -= 1
    if v < 0:
        yield "No solution", colors.copy()
    else:
        yield "Solution", colors.copy()

def greedy_steps(graph):
    n = graph.number_of_nodes()
    colors = [-1] * n
    for v in graph.nodes():
        used = {colors[u] for u in graph.neighbors(v) if colors[u] != -1}
        c = 0
        while c in used:
            c += 1
        colors[v] = c
        yield f"Assign color {c} to v{v}", colors.copy()

def welsh_powell_steps(graph):
    order = sorted(graph.nodes(), key=lambda v: graph.degree(v), reverse=True)
    colors = [-1] * graph.number_of_nodes()
    for v in order:
        used = {colors[u] for u in graph.neighbors(v) if colors[u] != -1}
        c = 0
        while c in used:
            c += 1
        colors[v] = c
        yield f"Assign color {c} to v{v}", colors.copy()

# UI
st.title("Graph Coloring Step-by-Step Visualization")
alg = st.sidebar.selectbox("Algorithm", ["Brute Force", "Backtracking", "Greedy", "Welsh-Powell"])

# Graph selection
graph_option = st.sidebar.selectbox("Graph", ["4-cycle", "Custom"])
if graph_option == "4-cycle":
    G = nx.cycle_graph(4)
else:
    adj = st.sidebar.text_area("Enter edges (one per line: u v):", "0 1\n1 2\n2 3\n3 0")
    G = nx.Graph()
    nodes = set()
    for line in adj.splitlines():
        u, v = map(int, line.split())
        nodes.update([u, v])
        G.add_edge(u, v)
    G.add_nodes_from(nodes)

if alg in ["Brute Force", "Backtracking"]:
    k = st.sidebar.number_input("Number of colors", min_value=1, max_value=10, value=3)

# Generate steps
if alg == "Brute Force":
    steps = list(bruteforce_steps(G, k))
elif alg == "Backtracking":
    steps = list(backtracking_steps(G, k))
elif alg == "Greedy":
    steps = list(greedy_steps(G))
else:
    steps = list(welsh_powell_steps(G))

step_idx = st.slider("Step", 0, len(steps)-1, 0)
desc, colors = steps[step_idx]

st.subheader(f"Step {step_idx+1}/{len(steps)}: {desc}")
st.write("Colors:", colors)

# Draw graph
pos = nx.spring_layout(G, seed=42)
palette = ["lightgray","red","green","blue","orange","purple","yellow","pink","brown","cyan"]
node_colors = [palette[c] if 0 <= c < len(palette) else "black" for c in colors]

fig, ax = plt.subplots()
nx.draw(G, pos, with_labels=True, node_color=node_colors, ax=ax)
st.pyplot(fig)
