
import spacy
import networkx as nx
import matplotlib.pyplot as plt


def get_dependency_tree(sentence):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(sentence)
    edges = []
    for token in doc:
        edges.append((token.text, token.head.text))
    graph = nx.DiGraph(edges)
    pos = nx.spring_layout(graph)
    labels = {node.text: node.text for node in doc}
    nx.draw(graph, pos, with_labels=True, labels=labels, node_color='lightblue', node_size=1500, arrowsize=20, font_size=10, font_color='black')
    for node in doc:
        if node.dep_ == 'ROOT':
            x, y = pos[node.text]
            plt.text(x, y + 0.05, 'ROOT', horizontalalignment='center', color='red', fontweight='bold', fontsize=8)
        else:
            x, y = pos[node.text]
            head_x, head_y = pos[node.head.text]
            plt.text((x + head_x) / 2, (y + head_y) / 2, node.dep_, horizontalalignment='center', verticalalignment='center', color='red', fontweight='bold', fontsize=8)
    plt.show()
    plt.savefig("C:\\Users\\Public\\dependency_tree.svg")
sentence = "A toy train moves along a winding track at an average speed of 0.25m/s. How far will it travel in 4.00 minutes?"
get_dependency_tree(sentence)