import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
monuments = ['Исаакиевский собор', 'Сенатская площадь(Медный всадник)', 'Адмиралтейство', 'Главный штаб', 'Дворцовая площадь', 'Эрмитаж', 'Дворцовый мост']
G.add_nodes_from(monuments)
G.add_edge('Исаакиевский собор', 'Сенатская площадь(Медный всадник)', weight=325)
G.add_edge('Исаакиевский собор', 'Александровский сад', weight=400)
G.add_edge('Адмиралтейство', 'Александровский сад', weight=30)
G.add_edge('Главный штаб', 'Александровский сад', weight=350)
G.add_edge('Главный штаб', 'Дворцовая площадь(Александровская колонна)', weight=125)
G.add_edge('Эрмитаж', 'Дворцовая площадь(Александровская колонна)', weight=80)
G.add_edge('Эрмитаж', 'Дворцовый мост', weight=550)
shortest_path = nx.approximation.traveling_salesman_problem(G)
print("Самый короткий маршрут через все памятники:", shortest_path)
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
def add_nodes(nodes):
    for i in nodes:
        graph.add_node(i, image=img)
