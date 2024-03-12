import networkx as nx
import matplotlib.pyplot as plt

# Створення пустого графу
G = nx.Graph()

# Додавання вершин та ребер
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (4, 6)])

# Візуалізація графу
nx.draw(G, with_labels=True)
plt.show()

# Аналіз основних характеристик графу
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступінь вершин:", dict(G.degree()))
