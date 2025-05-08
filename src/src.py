import numpy as np
import matplotlib.pyplot as plt


def build_up(b, u, v, dx, dy, dt, rho):
    b[1:-1, 1:-1] = (rho * (1 / dt *
        ((u[1:-1, 2:] - u[1:-1, :-2]) / (2 * dx) +
         (v[2:, 1:-1] - v[:-2, 1:-1]) / (2 * dy)) -
        ((u[1:-1, 2:] - u[1:-1, :-2]) / (2 * dx))**2 -
        2 * ((u[2:, 1:-1] - u[:-2, 1:-1]) / (2 * dy) *
             (v[1:-1, 2:] - v[1:-1, :-2]) / (2 * dx)) -
        ((v[2:, 1:-1] - v[:-2, 1:-1]) / (2 * dy))**2))
    return b

def poisson(p, b, dx, dy):
    pn = p.copy()
    for _ in range(50):
        pn = p.copy()
        p[1:-1, 1:-1] = (((pn[1:-1, 2:] + pn[1:-1, :-2]) * dy**2 +
                          (pn[2:, 1:-1] + pn[:-2, 1:-1]) * dx**2) /
                         (2 * (dx**2 + dy**2)) -
                         dx**2 * dy**2 / (2 * (dx**2 + dy**2)) * b[1:-1, 1:-1])

        # Periodic BC in x
        p[:, 0] = p[:, -2]
        p[:, -1] = p[:, 1]
        # Neumann BC in y
        p[0, :] = p[1, :]
        p[-1, :] = p[-2, :]
    return p

# Main solver, used to loop through time steps
def solver(dx, dy, u, v, rho, p, b, dt, nt, nu, dpdx):
    for n in range(nt):
        un = u.copy()
        vn = v.copy()

        b = build_up(b, u, v, dx, dy, dt, rho)
        p = poisson(p, b, dx, dy)

    # Develop the velocity field
        u[1:-1, 1:-1] = (un[1:-1, 1:-1] -
                    un[1:-1, 1:-1] * dt / dx * (un[1:-1, 1:-1] - un[1:-1, :-2]) -
                    vn[1:-1, 1:-1] * dt / dy * (un[1:-1, 1:-1] - un[:-2, 1:-1]) -
                    dt / (2 * rho * dx) * (p[1:-1, 2:] - p[1:-1, :-2]) +
                    nu * (dt / dx**2 * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, :-2]) +
                          dt / dy**2 * (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[:-2, 1:-1])) +
                    dt * dpdx / rho)

        v[1:-1, 1:-1] = (vn[1:-1, 1:-1] -
                    un[1:-1, 1:-1] * dt / dx * (vn[1:-1, 1:-1] - vn[1:-1, :-2]) -
                    vn[1:-1, 1:-1] * dt / dy * (vn[1:-1, 1:-1] - vn[:-2, 1:-1]) -
                    dt / (2 * rho * dy) * (p[2:, 1:-1] - p[:-2, 1:-1]) +
                    nu * (dt / dx**2 * (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, :-2]) +
                          dt / dy**2 * (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[:-2, 1:-1])))
        # Periodic BCs in x for u and v
        u[:, 0] = u[:, -2]
        u[:, -1] = u[:, 1]
        v[:, 0] = v[:, -2]
        v[:, -1] = v[:, 1]
    
    return u
    return v



