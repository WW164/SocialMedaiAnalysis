import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

def gatherData():
    df = pd.read_csv(r'H:\uni\8\Python\HW\02\lastfm_asia\lasftm_asia\lastfm_asia_edges.csv')
    print(df)
    return df


def adjacencyMatrix(df):
    matrix = np.zeros((7625, 7625), dtype=int)
    for i in range(int(df.size / 2)):
        matrix[df.at[i, 'node_1']][df.at[i, 'node_2']] = 1
        matrix[df.at[i, 'node_2']][df.at[i, 'node_1']] = 1

    return matrix


def calculateDegree(adjacentMatrix):
    degree = np.zeros(7625, dtype=int)
    for i in range(7625):
        for j in range(7625):
            if adjacentMatrix[i][j] == 1:
                degree[i] = degree[i] + 1
    return degree


def calculateAverageNeighborDegree(adjacentMatrix, degree):
    averageNeighborDegree = np.zeros(7625, dtype=float)

    for i in range(7625):
        sumDegree = 0
        number = 0
        for j in range(7625):
            if adjacentMatrix[i][j] == 1:
                sumDegree = sumDegree + degree[j]
                number = number + 1
        if number != 0:
            averageNeighborDegree[i] = sumDegree / number

    return averageNeighborDegree


def calculateAverageCommonNeighbor(adjacentMatrix):
    neighbors = defaultdict(list)
    commonNeighbors = {}
    averageCommonNumber = {}

    for i in range(7625):
        for j in range(7625):
            if adjacentMatrix[i][j] == 1:
                neighbors[i].append(j)

    for neighbor in neighbors:
        sumDegree = 0
        number = 0
        commonNeighbors.clear()
        for value in neighbors[neighbor]:
            commonNeighbors[value] = set(neighbors[neighbor]).intersection(set(neighbors[value]))
        for commonNeighbor in commonNeighbors:
            for value in commonNeighbors[commonNeighbor]:
                sumDegree = sumDegree + value
                number = number + 1
        if number != 0:
            averageCommonNumber[neighbor] = sumDegree / number

    return averageCommonNumber


def main():
    df = gatherData()
    adjacentMatrix = adjacencyMatrix(df)
    degree = calculateDegree(adjacentMatrix)
    print(degree)
    plt.plot(degree)
    plt.show()
    averageNeighborDegree = calculateAverageNeighborDegree(adjacentMatrix, degree)
    print(averageNeighborDegree)
    plt.plot(averageNeighborDegree)
    plt.show()
    averageCommonNeighbor = calculateAverageCommonNeighbor(adjacentMatrix)
    print(averageCommonNeighbor)
    plt.plot(list(averageCommonNeighbor))
    plt.show()


if __name__ == '__main__':
    main()
