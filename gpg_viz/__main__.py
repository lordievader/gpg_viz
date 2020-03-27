#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <o.i.vandertoorn@utwente.nl>
Description:    Parses json files from https://pgp.cs.uu.nl/ into a graph.
"""
import sys
import re
import json
import matplotlib.pyplot as plt
import networkx
from networkx.drawing.nx_agraph import graphviz_layout


def main():
    """Main function.
    """
    json_path = sys.argv[1]
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)

    graph = build_graph(data)
    plot(graph)


def build_graph(data):
    """Builds the graph based on given data.

    :param data: json data as a dictionary
    :type data: dictionary
    :returns: networkx graph.
    """
    graph = networkx.DiGraph()
    for chain in data['xpaths']:
        previous = None
        length = len(chain)
        for index, key in enumerate(reversed(chain)):
            uid = key['uid']
            label = re.sub(r'\s.*$', '', uid)
            if index == 0:
                color = 'green'

            elif index == length - 1:
                color = 'red'

            else:
                color = 'blue'

            graph.add_node(uid, value=label, color=color)
            if previous is not None:
                graph.add_edge(uid, previous)

            previous = uid

    return graph


def plot(graph):
    """Plots the graph.

    :param graph: graph to plot
    :type graph: networkx graph
    """
    fig, axis = plt.subplots(1, 1, figsize=(10, 10))
    pos = graphviz_layout(graph)
    values = networkx.get_node_attributes(graph, 'value')
    node_labels = {}
    for name, value in values.items():
        node_labels[name] = f'{value}'

    colors = []
    for name in pos:
        color = networkx.get_node_attributes(graph, 'color')[name]
        colors.append(color)

    networkx.draw(
        graph, pos, ax=axis, node_shape='o',
        node_size=200,
        node_color=colors,
        alpha=0.5,
        style='dotted'
    )
    networkx.draw_networkx_labels(
        graph, pos, ax=axis, labels=node_labels,
        font_size=25,
    )

    fig.tight_layout()
    fig.savefig('graph.png')


if __name__ == '__main__':
    main()
