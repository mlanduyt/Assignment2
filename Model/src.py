import numpy as np
from math_utils import *

# Establish Node Class
class node:
    def __init__(self, x, y, z, F=None, disp=None):
        self.x = x
        self.y = y
        self.z = z
        self.F = np.zeros(6) if F is None else np.array(F)
        self.disp = np.zeros(6) if disp is None else np.array(disp)
        self.supported_dofs = []

    def set_support(self, support):
        self.supported_dofs = [i for i, val in enumerate(support) if val]

# Establish Element Class
class element:
    def __init__(self, node1, node2, E, nu, A, Iz, Iy, Ip, J, z_axis):
        self.node1 = node1 
        self.x1 = node1.x
        self.y1 = node1.y
        self.z1 = node1.z
        self.node2 = node2
        self.x2 = node2.x
        self.y2 = node2.y
        self.z2 = node2.z    
        self.E = E # Modulus of elasticity
        self.nu = nu # Poisson's Ratio
        self.A = A # Cross-sectional area
        self.Iz = Iz # Moment of inertia
        self.Iy = Iy # Moment of inertia
        self.Ip = Ip # Polar moment of inertia
        self.J = J 
        self.z = z_axis # Local z axis
        self.L = np.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2 + (node1.z - node2.z)**2)
        if self.L == 0:
            raise ValueError("Duplicate nodes, review node input")

        # Calculates element properties
        self.k_e = local_elastic_stiffness_matrix_3D_beam(self.E, self.nu, self.A, self.L, self.Iy, self.Iz, self.J) # Obtains local elastic stiffness matrix    
        self.gamma = rotation_matrix_3D(self.x1, self.y1, self.z1, self.x2, self.y2, self.z2, self.z) # Rotation Matrix
        self.Gamma = transformation_matrix_3D(self.gamma) # Transformation Matrix
        self.k_global = self.Gamma.T @ self.k_e @ self.Gamma # Global Stiffness Matrix


def structure(nodes, element_connect, force_applied, supports):

    # nodes
    Nodes = [node(nodes[i][0], nodes[i][1], nodes[i][2], force_applied[i]) for i in range(len(nodes))]
    for support in supports:
        node_index = support[0]
        Nodes[node_index].set_support(support[1:])
    
    # elements
    Elements = [element(Nodes[element_connect[i][0]], Nodes[element_connect[i][1]], element_connect[i][2], 
                          element_connect[i][3], element_connect[i][4], element_connect[i][5], element_connect[i][6], 
                          element_connect[i][7], element_connect[i][8], element_connect[i][9]) for i in range(len(element_connect))]

    #develop local stiffness matrix
    lmat_local = [Elements[i].k_e for i in range(len(Elements))]

    # convert local to global
    gamma = [Elements[i].gamma for i in range(len(Elements))]
    Gamma = [Elements[i].Gamma for i in range(len(Elements))]
    lmat_global = [Elements[i].k_global for i in range(len(Elements))]

    # Create global stiffness matrix
    n_squares = int(6*len(Nodes))
    k_global = np.zeros((n_squares, n_squares))
    for i, elem in enumerate(Elements):
        node1_index, node2_index = element_connect[i][0], element_connect[i][1]
        dof_indices = np.array([node1_index * 6 + j for j in range(6)] + [node2_index * 6 + j for j in range(6)])
        for row_local, row_global in enumerate(dof_indices):
            for col_local, col_global in enumerate(dof_indices):
                k_global[row_global, col_global] += lmat_global[i][row_local, col_local]

    # Boundary conditions
    supported_dofs = []
    unsupported_dofs = [i for i in range(len(Nodes) * 6)]

    for support in supports:
        node_index = support[0]
        dof_indices = np.array([node_index * 6 + j for j in range(6)])
        for i, is_restricted in enumerate(support[1:]):
            if is_restricted:
                supported_dofs.append(dof_indices[i])

    unsupported_dofs = [dof for dof in unsupported_dofs if dof not in supported_dofs]

    # Partition matrices
    k_uu = k_global[np.ix_(unsupported_dofs, unsupported_dofs)]
    f_u = np.concatenate([np.array(node.F).flatten() for node in Nodes])[unsupported_dofs]
    check_singular(k_uu)
    
    # Solve for displacements
    del_u = np.linalg.solve(k_uu, f_u)
    del_f = np.zeros(len(Nodes) * 6)
    del_f[unsupported_dofs] = del_u

    # Calculate forces
    f_all = k_global @ del_f

    return del_f, f_all

def check_singular(matrix: np.ndarray):
    if np.linalg.cond(matrix) > 1e10:
        raise ValueError("Singular stiffness matrix detected. Check supports.")

