import pytest
import numpy as np
from src import *
from math_utils import *
from unittest.mock import patch


@pytest.fixture
def simple_beam():
    nodes = np.array([
        [0.0, 0.0, 0.0, 0],
        [1.0, 0.0, 0.0, 1] 
    ])
    elements = np.array([[0, 1]])  # Element connecting node 0 to 1
    return Beam(nodes, elements, E=200e9, nu=0.3, A=0.01, Iy=1e-4, Iz=1e-4, Irho=1e-4, J=2e-4)

@pytest.fixture
def simple_bc():
    fixed_nodes = {0: (0.0, 0.0, 0.0, 0.0, 0.0, 0.0)}  # Fully fixed at node 0
    return BoundaryCondition(fixed_nodes)

def test_beam_init_valid(simple_beam):
    assert simple_beam.nodes.shape == (2, 4)
    assert simple_beam.elements.shape == (1, 2)
    assert simple_beam.E == 200e9
    assert simple_beam.bc.shape == (2, 6)
    assert np.all(simple_beam.displacements == 0)

def test_beam_invalid_nodes():
    with pytest.raises(ValueError, match=r"Nodes must be a 2D array with shape \(n_nodes, 4\), got \(3,\)\."):
        Beam([1, 2, 3], np.array([[0, 1]]), 200e9, 0.3, 0.01, 1e-4, 1e-4, 1e-4, 2e-4)
    with pytest.raises(ValueError, match=r"Nodes must be a 2D array with shape \(n_nodes, 4\), got \(3,\)\."):
        Beam(np.array([1, 2, 3]), np.array([[0, 1]]), 200e9, 0.3, 0.01, 1e-4, 1e-4, 1e-4, 2e-4)
    with pytest.raises(ValueError, match=r"Nodes must be a 2D array with shape \(n_nodes, 4\), got \(2, 3\)\."):
        Beam(np.array([[0, 0, 0], [1, 0, 0]]), np.array([[0, 1]]), 200e9, 0.3, 0.01, 1e-4, 1e-4, 1e-4, 2e-4)

#def test_beam_invalid_elements():
#    nodes = np.array([[0.0, 0.0, 0.0, 0], [1.0, 0.0, 0.0, 1]])
#    with pytest.raises(ValueError, match=r"Elements must be a 2D array with shape \(n_elements, 2\), got \(2,\)\."):
#        Beam(nodes, [0, 1], 200e9, 0.3, 0.01, 1e-4, 1e-4,1e-4, 2e-4)
#    with pytest.raises(ValueError, match=r"Element 0 has invalid node1_id 2"):
#        Beam(nodes, np.array([[2, 1]]), 200e9, 0.3, 0.01, 1e-4, 1e-4, 1e-4, 2e-4)
#    with pytest.raises(ValueError, match=r"Element 0 has invalid node1_id 1\.5"):
#        Beam(nodes, np.array([[1.5, 1]]), 200e9, 0.3, 0.01, 1e-4, 1e-4,1e-4, 2e-4)
#    with pytest.raises(ValueError, match=r"Element 0 has invalid node2_id 0\.5"):
#        Beam(nodes, np.array([[0, 0.5]]), 200e9, 0.3, 0.01, 1e-4, 1e-4,1e-4, 2e-4)
#    with pytest.raises(ValueError, match=r"invalid literal for int\(\) with base 10: 'a'"):
#       Beam(nodes, np.array([["a", 1]]), 200e9, 0.3, 0.01, 1e-4, 1e-4, 1e-4, 1e-4, 2e-4)

def test_beam_invalid_material_properties():
    nodes = np.array([[0.0, 0.0, 0.0, 0], [1.0, 0.0, 0.0, 1]])
    elements = np.array([[0, 1]])
    with pytest.raises(ValueError, match="Young's Modulus"):
        Beam(nodes, elements, -200e9, 0.3, 0.01, 1e-4, 1e-4, 1e-4, 2e-4)
    with pytest.raises(ValueError, match="Poisson's Ratio"):
        Beam(nodes, elements, 200e9, 1.0, 0.01, 1e-4, 1e-4, 1e-4, 2e-4)
    with pytest.raises(ValueError, match="Cross-sectional area"):
        Beam(nodes, elements, 200e9, 0.3, -0.01, 1e-4, 1e-4, 1e-4, 2e-4)
    with pytest.raises(ValueError, match="Moment of inertia about y-axis"):
        Beam(nodes, elements, 200e9, 0.3, 0.01, -1e-4, 1e-4, 1e-4, 2e-4)
    with pytest.raises(ValueError, match="Moment of inertia about z-axis"):
        Beam(nodes, elements, 200e9, 0.3, 0.01, 1e-4, -1e-4, 1e-4, 2e-4)
    with pytest.raises(ValueError, match="Polar moment of inertia"):
        Beam(nodes, elements, 200e9, 0.3, 0.01, 1e-4, 1e-4, 1e-4, -2e-4)

def test_boundarycondition_init_valid(simple_bc):
    assert 0 in simple_bc.fixed_nodes
    assert len(simple_bc.fixed_nodes[0]) == 6
    assert simple_bc.applied_loads == {}

def test_boundarycondition_invalid_fixed_nodes():
    with pytest.raises(ValueError, match="Node ID -1 must be a non-negative integer"):
        BoundaryCondition({-1: (0.0, 0.0, 0.0, 0.0, 0.0, 0.0)})
    with pytest.raises(ValueError, match="Constraints for node 0 must be a tuple of 6 DOFs"):
        BoundaryCondition({0: (0.0, 0.0)})
    with pytest.raises(ValueError, match="Constraint invalid at DOF 0 for node 0 must be a number or None"):
        BoundaryCondition({0: ('invalid', 0.0, 0.0, 0.0, 0.0, 0.0)})

def test_boundarycondition_apply_load(simple_bc):
    simple_bc.apply_load(1, (100.0, 0.0, 0.0, 0.0, 0.0, 0.0))
    assert 1 in simple_bc.applied_loads
    assert simple_bc.applied_loads[1] == (100.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    with pytest.raises(ValueError, match="Loads for node 1 must be a tuple of 6 values"):
        simple_bc.apply_load(1, (100.0, 0.0))
    with pytest.raises(ValueError, match="Loads for node 1 must be a tuple of 6 values"):
        simple_bc.apply_load(1, (1.0, 2.0, 3.0, 4.0, 5.0))  # Line 86
    with pytest.raises(ValueError, match="Load a at DOF 0 for node 1 must be a number"):
        simple_bc.apply_load(1, ("a", 0.0, 0.0, 0.0, 0.0, 0.0))  # Extra coverage for _check_loads

def test_boundarycondition_supports(simple_bc):
    simple_bc.add_fixed_support(1)
    assert simple_bc.fixed_nodes[1] == (0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    simple_bc.add_pinned_support(2)
    assert simple_bc.fixed_nodes[2] == (0.0, 0.0, 0.0, None, None, None)

def test_boundarycondition_get_dof_constraints(simple_bc):
    constraints = simple_bc.get_dof_constraints()
    assert constraints[0] == [True, True, True, True, True, True]

def test_beamsolver_init(simple_beam, simple_bc):
    solver = BeamSolver(simple_beam, simple_bc)
    assert solver.beam is simple_beam
    assert solver.bc is simple_bc
    assert solver.internal_forces is None

@pytest.fixture
def test_build_stiffness_matrix(mock_trans, mock_rot, mock_local, simple_beam, simple_bc):
    mock_local.return_value = np.eye(12) * 1e9
    mock_rot.return_value = np.eye(3)
    mock_trans.return_value = np.eye(12)
    solver = BeamSolver(simple_beam, simple_bc)
    K = solver.build_stiffness_matrix()
    assert K.shape == (12, 12)
    assert np.any(K != 0)

def test_solve(simple_beam, simple_bc):
    solver = BeamSolver(simple_beam, simple_bc)
    simple_bc.apply_load(1, (1000.0, 0.0, 0.0, 0.0, 0.0, 0.0))
    displacements, reactions = solver.solve()
    assert displacements.shape == (2, 6)
    assert reactions.shape == (2, 6)
    assert np.any(displacements != 0)
    assert np.allclose(reactions[0], [-1000.0, 0, 0, 0, 0, 0], atol=1e-5)

def test_compute_element_forces(simple_beam, simple_bc):
    solver = BeamSolver(simple_beam, simple_bc)
    displacements = np.zeros((2, 6))
    displacements[1, 0] = 0.001
    forces = solver.compute_element_forces(displacements)
    assert 0 in forces
    assert forces[0].shape == (12,)
    assert np.any(forces[0] != 0)

def test_build_geometric_stiffness_matrix_raises(simple_beam, simple_bc):
    solver = BeamSolver(simple_beam, simple_bc)
    with pytest.raises(ValueError, match=r"Must run solve\(\) first to compute internal forces for buckling analysis\."):
        solver.build_geometric_stiffness_matrix()

def test_build_geometric_stiffness_matrix_after_solve(simple_beam, simple_bc):
    solver = BeamSolver(simple_beam, simple_bc)
    simple_bc.apply_load(1, (1000.0, 0.0, 0.0, 0.0, 0.0, 0.0))
    solver.solve()
    K_geo = solver.build_geometric_stiffness_matrix()
    assert K_geo.shape == (12, 12)
    assert np.any(K_geo != 0)

def test_display_results(simple_beam, simple_bc, capsys):
    solver = BeamSolver(simple_beam, simple_bc)
    simple_bc.apply_load(1, (1000.0, 0.0, 0.0, 0.0, 0.0, 0.0))
    displacements, reactions = solver.solve()
    solver.display_results(displacements, reactions)
    captured = capsys.readouterr()
    assert "Node 0 Displacements" in captured.out
    assert "Node 1 Reactions" in captured.out

def test_solve_buckling(simple_beam, simple_bc):
    solver = BeamSolver(simple_beam, simple_bc)
    simple_bc.apply_load(1, (-1000.0, 0.0, 0.0, 0.0, 0.0, 0.0))
    solver.solve()
    eigvals, eigvecs, buckling_forces = solver.solve_buckling()
    assert isinstance(eigvals, np.ndarray)
    assert eigvecs.shape[0] == 12
    assert isinstance(buckling_forces, dict)
    if len(eigvals) > 0:
        assert 0 in buckling_forces

def test_add ():
    z = 2+2
    assert z == 4

def test_subtract():
    z = 3-2
    assert z == 1

def test_multiply ():
    z = 2*2
    assert z == 4

def test_divide ():
    z = 4/2
    assert z == 2

def test_eig ():
    A = np.array([[1, 3, 2],[2, 2, 1],[3, 1, 3]])
    e_vals, e_vecs = np.linalg.eig(A)
    z = e_vals[0] - 6
    assert z < 0.05

