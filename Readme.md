# Readme.md

## Algorithm

Since this problem is single source shortest path, the [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) is implemented.

## Executing the Code

Two sample data files are provided:

1. sample_network.txt: a small graph with 4 nodes
2. network.txt: a graph with 63 nodes

The full code is in the `routing.py` file. It can be run using the command:

`python routing.py <data file> <origin node> <destination node>`

For example: `python routing.py sample_network.txt node1 node2`

## Testing

Elaborate testing is done using the `pytest` framework.

Perform testing by simply typing `pytest` in the terminal. Make sure you are in the same directory and the data files mentioned above are available there!


