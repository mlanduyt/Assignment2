import numpy as np
import matplotlib.pyplot as plt

# Domain size
nx = 50
ny = 50
Lx = 2.0
Ly = 1.0

dx = Lx / (nx - 1)
dy = Ly / (ny - 1)

# Fluid properties
rho = 1.0
nu = 0.1  # kinematic viscosity

# Time-stepping
dt = 0.001
nt = 500

# Pressure gradient
dpdx = 0.0  # drives the flow in x

# Initialization
u = np.zeros((ny, nx))  # x-velocity
v = np.zeros((ny, nx))  # y-velocity
p = np.zeros((ny, nx))  # pressure
b = np.zeros((ny, nx))  # RHS of pressure Poisson

def build_up_b(b, u, v, dx, dy, dt):
    b[1:-1, 1:-1] = (rho * (1 / dt *
        ((u[1:-1, 2:] - u[1:-1, :-2]) / (2 * dx) +
         (v[2:, 1:-1] - v[:-2, 1:-1]) / (2 * dy)) -
        ((u[1:-1, 2:] - u[1:-1, :-2]) / (2 * dx))**2 -
        2 * ((u[2:, 1:-1] - u[:-2, 1:-1]) / (2 * dy) *
             (v[1:-1, 2:] - v[1:-1, :-2]) / (2 * dx)) -
        ((v[2:, 1:-1] - v[:-2, 1:-1]) / (2 * dy))**2))
    return b

def pressure_poisson(p, b, dx, dy):
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

# Main loop
for n in range(nt):
    un = u.copy()
    vn = v.copy()

    b = build_up_b(b, u, v, dx, dy, dt)
    p = pressure_poisson(p, b, dx, dy)

    # Velocity field update
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

    # Boundary Conditions
    u[0, :] = 0
    u[-1, :] = 1
    v[0, :] = 0
    v[-1, :] = 0

    # Periodic BCs in x for u and v
    u[:, 0] = u[:, -2]
    u[:, -1] = u[:, 1]
    v[:, 0] = v[:, -2]
    v[:, -1] = v[:, 1]

# Plotting
X, Y = np.meshgrid(np.linspace(0, Lx, nx), np.linspace(0, Ly, ny))

#
#plt.figure(figsize=(10, 4))
#plt.contourf(X, Y, u, 20, cmap='jet')
#plt.colorbar(label='Velocity u')
#plt.title('Channel Flow: Velocity Profile u(x,y)')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.tight_layout()
#plt.savefig('flow.png')
#plt.show()

fig = plt.figure(figsize = (11,7), dpi=100)
plt.quiver(X[::3, ::3], Y[::3, ::3], u[::3, ::3], v[::3, ::3]);
plt.savefig('flow.png')
plt.show()

print(Y)
