#!/usr/bin/env python
# coding: utf-8
from collections import defaultdict
import numpy as np
import sys


def read_graph(filename):
    '''
    Reads the given file and create a graph
    Returns the created graph
    '''
    Graph = defaultdict(list)
    # filename = 'network.txt'
    with open(filename) as f:
        for line in f:
            row = line.strip().split()
            if len(row) != 3:
                continue
            source, target, weight = row[0], row[1], int(row[2])
            Graph[source].append((target, weight))
            # if target is not in Graph, add to it with empty list
            if target not in Graph:
                Graph[target] = []
    return Graph


def get_best_node(D, Q):
    '''
    Inputs:
      D: a dictionary which maps vertices to shortest distances (so far!)
      Q: list of unexplored vertices
    Return the node with the shortest distance which is in Q
    '''
    best_node, shortest_distance = None, np.inf
    for node in Q:
        distance = D[node]
        if distance < shortest_distance:
            best_node = node
            shortest_distance = distance
    return best_node


def back_track(destination, Prev):
    '''
    find the shortest path by back-tracking
    '''
    path = []
    node = destination
    while(node is not None):
        path.append(node)
        node = Prev[node]
    # reverse the node order    
    return path[::-1]


def dijkstras(Graph, origin, destination):
    '''
    Single source shortest path using the Dijkstra's algorithm
    Returns the shortest distance as well as the shortest path
    '''
    # list of all vertices
    V = Graph.keys()
    if origin not in V:
        print('Error! The origin is not in the Graph')
        return (np.inf, None)
    if destination not in V:
        print('Error! The destination is not in the Graph')
        return (np.inf, None)

    # initialize all distances to infinity
    D = {k: np.inf for k in V}
    # distance to origin from origin is zero
    D[origin] = 0
    # Previous node to back-track shortest distance
    Prev = {k: None for k in V}
    # Add all nodes to the queue 
    # (Q is not an actual queue abstract data structure, but a list)
    Q = list(V)
    curr_node = origin
    while(len(Q) > 0):
        # if curr_node is the destination, stop
        if curr_node == destination:
            # print('Shortest distance = %d' % (D[destination]))
            shortest_path = back_track(destination, Prev)
            return(D[destination], shortest_path)
        # otherwise continue
        Q.remove(curr_node)
        # Find all neighbours of curr_node
        neighbours = Graph[curr_node]
        for node, weight in neighbours:
            # Relaxation
            if D[curr_node] + weight < D[node]:
                D[node] = D[curr_node] + weight
                # mark the shortest path
                Prev[node] = curr_node

        # pick the node with the smallest distance
        curr_node = get_best_node(D, Q)
        if curr_node is None:
            print('The destination: %s is not reachable from the origin: %s'%(destination, origin))
            return (np.inf, None)

    # The control should never reach here
    return (-1, None)


def main():
    # read the command line arguments
    if len(sys.argv) != 4:
        print('Correct format is: python routing.py <network-filename> <origin> <destination>')
        sys.exit(1)

    filename = sys.argv[1]
    origin = sys.argv[2]
    destination = sys.argv[3]

    # Read the file & create the graph
    Graph = read_graph(filename)
    shortest_dist, shortest_path = dijkstras(Graph, origin, destination)
    if shortest_path is not None:
        print('Shortest path')
        for node in shortest_path:
            print(node)
        print('Shortest distance: %d'%(shortest_dist))


if __name__ == '__main__':
    main()

# Test
# origin = 'J1001'
# destination = 'X1058'
# destination = 'J1055'
