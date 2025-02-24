import numpy as np
import math
from math_utils import *

class Nodes:
    def __init__(self,nodes,nodeType,load):
        self.nodes = nodes
        self.nodeType = nodeType
        self.load = load
        self.numNodes = np.size(nodes,0)
        self.numDOF = 6
        self.forces = np.reshape(load,(self.numNodes*6,1))

class Elements:
    def __init__(self,connections,E,v,A,Iz,Iy,Ip,J):
        self.connections = connections
        self.E = E
        self.v = v
        self.A = A
        self.Iz = Iz
        self.Iy = Iy
        self.Ip = Ip
        self.J = J
        self.numElements = np.size(self.connections,0)
        self.elem_load = np.zeros((12,self.numElements))
        self.L = np.zeros(self.numElements)+1  

def find_global_frame_stiffness(Nodes,Elements):
    K_global=np.zeros((Nodes.numNodes*6,Nodes.numNodes*6))
    for elm_ind in range(Elements.numElements):

        node0 = Elements.connections[elm_ind][0]
        node1 = Elements.connections[elm_ind][1]
        x1 = Nodes.nodes[node0][0]
        y1 = Nodes.nodes[node0][1]
        z1 = Nodes.nodes[node0][2]
        x2 = Nodes.nodes[node1][0]
        y2 = Nodes.nodes[node1][1]
        z2 = Nodes.nodes[node1][2]

        # length of element
        Elements.L[elm_ind] = math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2 )

        # DOF indices
        node1_dof_ind1 = 6 * node0
        node1_dof_ind2 = 6 * (node0 + 1)
        node2_dof_ind1 = 6 * node1
        node2_dof_ind2 = 6 * (node1 + 1)

        # material
        mats = np.array([Elements.E[elm_ind], Elements.v[elm_ind], Elements.A[elm_ind], Elements.L[elm_ind], Elements.Iy[elm_ind], Elements.Iz[elm_ind], Elements.J[elm_ind]])
        ke = local_elastic_stiffness_matrix_3D_beam(*mats)
        gamma = rotation_matrix_3D(x1,y1,z1,x2,y2,z2)
        Gamma = transformation_matrix_3D(gamma)
        k_eg = np.transpose(Gamma) @ ke @ Gamma
        
        # assemble frame stiffness matrix

        K_global[node1_dof_ind1:node1_dof_ind2,node1_dof_ind1:node1_dof_ind2] += k_eg[0:6,0:6]
        K_global[node1_dof_ind1:node1_dof_ind2,node2_dof_ind1:node2_dof_ind2] += k_eg[0:6,6:12]
        K_global[node2_dof_ind1:node2_dof_ind2,node1_dof_ind1:node1_dof_ind2] += k_eg[6:12,0:6]
        K_global[node2_dof_ind1:node2_dof_ind2,node2_dof_ind1:node2_dof_ind2] += k_eg[6:12,6:12]

    return K_global

def partition_matrices(Nodes,Elements,K_global):
    DOF = np.zeros((Nodes.numNodes,Nodes.numDOF))
    for node_ind in range(Nodes.numNodes):
        if Nodes.nodeType[node_ind] == 0:
            DOF[node_ind][:] = 1 
        elif Nodes.nodeType[node_ind] == 2:
            DOF[node_ind][3:6] = 1
    
    DOF = np.reshape(DOF,(Nodes.numNodes*6,1))
    unknown_disp = np.where(DOF != 0)[0]
    known_disp = np.where(DOF == 0)[0]

    known_forces = np.array(Nodes.forces[unknown_disp])
    unknown_forces = np.array(Nodes.forces[known_disp])

    partition_forces = np.vstack((Nodes.forces[unknown_disp],Nodes.forces[known_disp]))
    partition_K_global = np.vstack((K_global[unknown_disp],K_global[known_disp]))
    num_unknown_disp = np.size(unknown_disp)
    return partition_K_global, partition_forces, num_unknown_disp

def solver(Nodes,Elements):
    
    K_global = find_global_frame_stiffness(Nodes,Elements)
    partition_K_global, partition_forces, num_unknown_disp = partition_matrices(Nodes,Elements,K_global)

    known_forces = partition_forces[0:num_unknown_disp]
    K_known_forces = partition_K_global[0:num_unknown_disp,0:num_unknown_disp]

    Delta_f = np.linalg.solve(K_known_forces,known_forces)
    K_unknown_forces = partition_K_global[0:num_unknown_disp,num_unknown_disp:]
    F_reaction = K_unknown_forces @ Delta_f
    return Delta_f, F_reaction