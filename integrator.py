# Imports for the integration and visualization
import numpy as np
import matplotlib.pyplot as plt

def solver(f, dx, psii, psio):

    # Creating initial conditions
    psi = [psii, psio]

    # Simulating Verlet algorithm
    for idx, value in enumerate(x):
        psi.append(2 * psi[idx + 1] - psi[idx] + (dx ** 2) * f[idx] *
psi[idx + 1])

    # Adjusting for different dimensions in the graph
    psi.pop()
    psi.pop()

    # Normalizing the wavefunction and finding creating the probability function
    norm = 0
    p = []
    full_psi = []
    for i, e in enumerate(psi):
        norm += ((e ** 2) * dx)
    A = (1/norm) ** 0.5
    for i, e in enumerate(psi):
        full_psi.append(A * e)
        p.append((A * e) ** 2)

    return full_psi, p, x



m = 1 # Mass
hbar = 1 # Reduced Planck constant (Using one for simplicity)
E = 1 # Energy
x0 = 0 # Starting point for position
h = 0.01 # Position step distance
xf = 10 # Final point for position
psi0 = 0 # Initial value for the wave function
psi1 = 0.001 # Second value for the wav function (needed since the Schrödinger equation is second order)
N = int(((xf-x0)/h) + 1) # Number of position steps
x = np.linspace(x0, xf, N) # Creating position vector
v = 0.5 * m * x ** 2 # Potential energy function
func = ((2*m)/(hbar ** 2))*(E - v) # Linear function that multiplies the wave function to equal the second derivative of the wave function

wave_function, probability, position = solver(func, h, psi0, psi1)

# Plotting wave function vs position
plt.plot(position, wave_function)
plt.title("Wave Function vs Position")
plt.xlabel("Position")
plt.ylabel("Wave Function")
plt.show()

# Plotting probabilities vs position
plt.plot(position, probability)
plt.title("Probability vs Position")
plt.xlabel("Position")
plt.ylabel("Probability")
plt.show()