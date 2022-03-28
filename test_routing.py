import pytest
from routing import *
import numpy as np

@pytest.fixture
def sample_graph():
    return read_graph('sample_network.txt')


def test_data_reading_nodes(sample_graph):
    assert len(sample_graph.keys()) == 4, "number of nodes in sample data is 4"


def test_data_reading_edges(sample_graph):
    assert sample_graph['node1'] == [('node2', 6), ('node3', 4), ('node4', 5)], "The adjacent nodes of node1 are node2 and node3"


def test_sample_shortest_path1(sample_graph):
    origin = 'node1'
    destination = 'node2'
    shortest_dist, shortest_path = dijkstras(sample_graph, origin, destination)
    assert shortest_dist == 5, "shortest distance should be 5"


def test_sample_shortest_path2(sample_graph):
    origin = 'node1'
    destination = 'node2'
    shortest_dist, shortest_path = dijkstras(sample_graph, origin, destination)
    assert shortest_path == ['node1', 'node3', 'node2'], "shortest path should be through node3"
    # assert len(shortest_path) == 3, 'shortest path length is 3'


def test_sample_shortest_path_source_to_source(sample_graph):
    origin = 'node1'
    destination = 'node1'
    shortest_dist, shortest_path = dijkstras(sample_graph, origin, destination)
    assert shortest_dist == 0, "shortest distance from node1 to itself is zero"


def test_origin_not_in_graph(sample_graph):
    origin = 'node5'
    destination = 'node1'
    shortest_dist, shortest_path = dijkstras(sample_graph, origin, destination)
    assert shortest_dist == np.inf, "shortest distance should be infinity"


def test_unreachable_path(sample_graph):
    origin = 'node4'
    destination = 'node1'
    shortest_dist, shortest_path = dijkstras(sample_graph, origin, destination)
    assert shortest_dist == np.inf, "node4 is unreachable from node1"


# Testing the larger file

@pytest.fixture
def big_graph():
    return read_graph('network.txt')


def test_reading_graph(big_graph):
    assert len(big_graph.keys()) == 63, "number of nodes in the data is 63"


def test_given_example_distance(big_graph):
    origin = 'J1053'
    destination = 'J1037'
    shortest_dist, shortest_path = dijkstras(big_graph, origin, destination)
    assert shortest_dist == 4458, 'shortest distance is 4458'


def test_given_example_path(big_graph):
    origin = 'J1053'
    destination = 'J1037'
    shortest_dist, shortest_path = dijkstras(big_graph, origin, destination)
    assert shortest_path == ['J1053', 'J1035', 'J1036', 'J1037'], 'shortest distance path in incorrect'
