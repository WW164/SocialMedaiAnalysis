import networkx as nx
import pandas as pd
import random
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
from SRW_RWF_ISRW import SRW_RWF_ISRW
from operator import itemgetter

def gatherData():
    df = pd.read_csv(r'H:\uni\8\Python\HW\02\lastfm_asia\lasftm_asia\lastfm_asia_edges.csv')
    return df


def createGraph(df):
    G = nx.Graph()
    for i in range(int(df.size / 2)):
        G.add_edge(df.at[i, 'node_1'], df.at[i, 'node_2'])

    return G


def adjacencyMatrix(df):
    matrix = np.zeros((7625, 7625), dtype=int)
    for i in range(int(df.size / 2)):
        matrix[df.at[i, 'node_1']][df.at[i, 'node_2']] = 1
        matrix[df.at[i, 'node_2']][df.at[i, 'node_1']] = 1

    return matrix


def samplingNode(G, adjacentMatrix):
    GNode = nx.Graph()

    for i in range(381):
        GNode.add_node(random.choice(list(G.nodes)))

    neighbors = defaultdict(list)
    for i in range(7625):
        for j in range(7625):
            if adjacentMatrix[i][j] == 1:
                neighbors[i].append(j)

    for node in neighbors:
        if GNode.nodes.__contains__(node):
            for neighbor in neighbors[node]:
                if GNode.nodes.__contains__(neighbor):
                    GNode.add_edge(node, neighbor)
                    GNode.add_edge(neighbor, node)
                else:
                    pass
        else:
            pass

    print(nx.info(GNode))
    nx.draw_networkx(GNode)
    plt.show()

    return nx.degree_centrality(GNode)


def samplingEdge(G):
    GEdge = nx.Graph()
    for i in range(381):
        edge = random.choice(list(G.edges))
        GEdge.add_edge(edge[0], edge[1])

    print(nx.info(GEdge))
    nx.draw_networkx(GEdge)
    plt.show()

    return nx.degree_centrality(GEdge)


def compareGraphs(nodeDegreeCentrality, edgeDegreeCentrality, RWDegreeCentrality):
    commonNodes = set(nodeDegreeCentrality).intersection(set(edgeDegreeCentrality), set(RWDegreeCentrality))
    print("Common nodes are: ")
    for commonNode in commonNodes:
        print(commonNode)


def main():
    df = gatherData()
    G = createGraph(df)
    adjacentMatrix = adjacencyMatrix(df)
    nodeDegreeCentrality = samplingNode(G, adjacentMatrix)
    print(sorted(nodeDegreeCentrality.items(), key=itemgetter(1), reverse=True)[:100])
    edgeDegreeCentrality = samplingEdge(G)
    print(sorted(edgeDegreeCentrality.items(), key=itemgetter(1), reverse=True)[:100])
    RW = SRW_RWF_ISRW()
    RWGraph = RW.random_walk_sampling_simple(G, 380)
    RWDegreeCentrality = nx.degree_centrality(RWGraph)
    print(nx.info(RWGraph))
    print(sorted(RWDegreeCentrality.items(), key=itemgetter(1), reverse=True)[:100])
    nx.draw_networkx(RWGraph)
    plt.show()
    
    compareGraphs(nodeDegreeCentrality, edgeDegreeCentrality, RWDegreeCentrality)


if __name__ == '__main__':
    main()
