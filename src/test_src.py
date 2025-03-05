import sys
import os
import numpy as np
import pytest
from src.src import *
from math_utils import *

def test_tutorial():
    node0 = [0, 0, 10]  # Fixed
    node1 = [15, 0, 10]  # Midpoint (force applied)
    node2 = [15, 0, 0]  # Pin
    nodes = np.array([node0, node1, node2])

    element1 = [0, 1, 1000, 0.3, 0.5, 0.041667, 0.010416, 0.16667, 0.02861, None]
    element2 = [1, 2, 1000, 0.3, 0.5, 0.041667, 0.010416, 0.16667, 0.02861, [1, 0, 0]]
    element_connect = np.array([element1, element2], dtype=object)

    f_appl = np.array([[0,0,0,0,0,0],   
                   [0.1,0.05,-0.07,0.05,-0.1,0.25],  
                   [0,0,0,0,0,0]]) 
    
    support_0 = [0, 1, 1, 1, 1, 1, 1]  # Fixed: Restraints all DOF
    support_1 = [1, 0, 0, 0, 0, 0, 0]  # Free: No restraints
    support_2 = [2, 1, 1, 1, 0, 0, 0]  # Pinned: Restraints all translation (x, y, z)
    supports = np.array([support_0, support_1, support_2])

    displacement, forces = structure(nodes, element_connect, f_appl, supports)
    
    known = np.array([0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
                      0.00000000e+00,  0.00000000e+00,  2.84049957e-03,  1.59842256e+00,
                      -1.30609177e-03, -1.47203405e-01, -1.67304182e-02,  1.82342076e-01, 
                      0.00000000e+00,  0.00000000e+00,  0.00000000e+00, -1.66161682e-01,
                      8.79128406e-03,  1.82342076e-01])

    assert np.allclose(displacement, known, atol=1e-6)

def test_zeros():
    node0 = [0, 0, 10]  # Fixed
    node1 = [15, 0, 10]  # Midpoint (force applied)
    node2 = [15, 0, 0]  # Pin
    nodes = np.array([node0, node1, node2])

    element1 = [0, 1, 1000, 0.3, 0.5, 0.041667, 0.010416, 0.16667, 0.02861, None]
    element2 = [1, 2, 1000, 0.3, 0.5, 0.041667, 0.010416, 0.16667, 0.02861, [1, 0, 0]]
    element_connect = np.array([element1, element2], dtype=object)

    f_appl = np.array([[0,0,0,0,0,0],   
                   [0.0,0.0,0.0,0.0,0.0,0.0],  
                   [0,0,0,0,0,0]]) 
    
    support_0 = [0, 1, 1, 1, 1, 1, 1]  
    support_1 = [1, 0, 0, 0, 0, 0, 0]  
    support_2 = [2, 1, 1, 1, 0, 0, 0]
    supports = np.array([support_0, support_1, support_2])

    displacement, forces = structure(nodes, element_connect, f_appl, supports)
    
    known = np.array([0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
                      0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
                      0.00000000e+00, 0.00000000e+00, 0.00000000e+00,  0.00000000e+00, 
                      0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,
                      0.00000000e+00,  0.00000000e+00])

    assert np.allclose(displacement, known, atol=1e-6)

def test_vector():
    test_vector = [0, 1, 1]
    with pytest.raises(ValueError):
        check_unit_vector(test_vector)

def test_math():
    a = 1
    b = 2
    c = a + b
    d = c/a
    assert d == 3

def test_parallel():
    vector1 = np.array([1, 0, 0])
    vector2 = np.array([1, 0, 0])
    with pytest.raises(ValueError):
        check_parallel(vector1, vector2)

def test_duplicate_nodes():
    nodes = np.array([[0, 0, 0], [0, 0, 0]])
    node_1 = node(nodes[0][0], nodes[0][1], nodes[0][2])
    node_2 = node(nodes[1][0], nodes[1][1], nodes[1][2])
    with pytest.raises(ValueError):
        element(node_1, node_2, 1, 1, 1, 1, 1, 1, 1, None)

def test_singular():
    mat = [[0, 0], [0, 0]]
    with pytest.raises(ValueError):
        check_singular(mat)

