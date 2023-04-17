import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
from matplotlib.animation import FuncAnimation
import threading
import random
import time

G = nx.Graph()
fig, ax = plt.subplots(figsize=(10, 8))

def update_topology(max_nodes, update_interval):
    nodes = set()
    while True:
        node = random.randint(1, max_nodes)
        if node not in nodes:
            G.add_node(node)
            nodes.add(node)
        else:
            G.remove_node(node)
            nodes.remove(node)
        time.sleep(update_interval)

def update(num):
    ax.clear()
    pos = graphviz_layout(G, prog="neato")
    nx.draw(G, pos, with_labels=True, node_color="skyblue", edge_color="gray", node_size=1500, font_size=20, font_weight="bold", ax=ax)
    plt.title("Dynamic Network Topology")

max_nodes = int(input("Enter the maximum number of nodes: "))
update_interval = float(input("Enter the update interval in seconds: "))

threading.Thread(target=update_topology, args=(max_nodes, update_interval), daemon=True).start()
ani = FuncAnimation(fig, update, interval=update_interval * 1000)
plt.show()
