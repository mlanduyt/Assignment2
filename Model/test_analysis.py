import numpy as np
import math
from analysis import *


nodes = np.array([[1, 0, 0],[1, 1, 1]])
load = np.array([[0,0,0,0,0,0],[0,0,0,0,0,0]])
nodeType = np.array([1,0])
connections = np.array([[0, 1]])
E = np.array([1])
v = np.array([1])
A = np.array([1])
Iz = np.array([1])
Iy = np.array([1])
Ip = np.array([1])
J = np.array([1])
Nodes = Nodes(nodes=nodes,load=load,nodeType=nodeType)
Elements = Elements(connections,E,v,A,Iz,Iy,Ip,J)
displacement, forces = solver(Nodes,Elements)
def test_static (): 
    assert displacement[1] == 0

def test_size ():
    a = np.size([1,2,3])
    assert a ==3


