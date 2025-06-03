import networkx as nx
import matplotlib.pyplot as plt

arestas = [
    ('ORIGEM', 'ARVORE 2', 10),
    ('ORIGEM', 'ARVORE 3', 15),
    ('ARVORE 2', 'ARVORE 4', 12),
    ('ARVORE 2', 'ARVORE 5', 15),
    ('ARVORE 3', 'ARVORE 5', 10),
    ('ARVORE 5', 'ARVORE 6', 5),
]

G = nx.Graph()
G.add_weighted_edges_from(arestas)
pos = nx.spring_layout(G)


def mostrar_grafo():
    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color="green", node_size=1000,
            font_size=14, font_weight="bold", edge_color="gray")
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')
    plt.title("Mapa da floresta com caminhos e distâncias")
    plt.axis("off")
    plt.show()


def jogar_grafo():
    mostrar_grafo()
    print("Nós disponíveis:")
    for no in G.nodes:
        print(f" - {no}")

    while True:
        incendio = input("\nQual nó está pegando fogo? ").strip().upper()
        if incendio not in G.nodes:
            print("Nó inválido! Tente novamente.")
            continue
        else:
            break

    origem = 'ORIGEM'
    if incendio == origem:
        print("Você já está no local do incêndio!")
        return

    caminho = nx.dijkstra_path(G, source=origem, target=incendio)
    distancia = nx.dijkstra_path_length(G, source=origem, target=incendio)

    print("\n🔥 Caminho mais curto até o incêndio:")
    print(" -> ".join(caminho))
    print("Distância total:", distancia)
    input("\nPressione [ENTER] para continuar.")

