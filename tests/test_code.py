import numpy as np
import pytest
from src import *

# Setup grid for use in further tests
def setup_grid():
    nx, ny = 5, 5
    dx = dy = 1.0
    rho = 1.0
    dt = 0.01
    nu = 0.1
    nt = 1
    dpdx = 1.0
    u = np.zeros((ny, nx))
    v = np.zeros((ny, nx))
    p = np.zeros((ny, nx))
    b = np.zeros((ny, nx))
    return dx, dy, u, v, rho, p, b, dt, nt, nu, dpdx

# Test the build up function
def test_build_up():
    dx, dy, u, v, rho, p, b, dt, nt, nu, dpdx = setup_grid()
    b_new = build_up(b.copy(), u.copy(), v.copy(), dx, dy, dt, rho)
    assert b_new.shape == b.shape

# Test the poisson function
def test_poisson():
    dx, dy, u, v, rho, p, b, dt, nt, nu, dpdx = setup_grid()
    b_rand = np.random.rand(*p.shape)
    p_out = poisson(p.copy(), b_rand, dx, dy)
    assert not np.any(np.isnan(p_out))
    assert p_out.shape == p.shape

# Test solver against expected velocity(expected velocity field)
def test_solver_velocity_field():
    dx, dy, u, v, rho, p, b, dt, nt, nu, dpdx = setup_grid()
    u_out = solver(dx, dy, u.copy(), v.copy(), rho, p.copy(), b.copy(), dt, nt, nu, dpdx)
    assert u_out.shape == u.shape
    assert np.all(np.isfinite(u_out))

$ Test solver against expected velocity change based on known dpdx
def test_velocity_change():
    dx, dy, u, v, rho, p, b, dt, nt, nu, dpdx = setup_grid()
    u_before = u.copy()
    u_after = solver(dx, dy, u.copy(), v.copy(), rho, p.copy(), b.copy(), dt, 10, nu, dpdx)
    assert not np.allclose(u_before, u_after)

# Test symmetrical results based on centralized flow 'source'
def test_pressure_symmetry():
    dx, dy, u, v, rho, p, b, dt, nt, nu, dpdx = setup_grid()
    b_test = np.zeros_like(p)
    b_test[2, 2] = 100
    p_out = poisson(p.copy(), b_test, dx, dy)
    assert np.isclose(p_out[2, 1], p_out[2, 3], atol=1e-2)
    assert np.isclose(p_out[1, 2], p_out[3, 2], atol=1e-2)
