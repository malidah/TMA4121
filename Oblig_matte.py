import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Løser varmeligningen med randkrav u(0,y,t)=u(Lx,y,t)=u(x,0,t)=u(x,Ly,t)=0
# Parametre
Lx, Ly = 1.0, 1.0 #område
Nx, Ny = 50, 50 #antall punkter
dx, dy = Lx / (Nx - 1), Ly / (Ny - 1) #avstand mellom punktene i x og y retning
alpha = 0.01  # Termisk diffusivitet
dt = 0.001  # Tidssteg
Nt = 10000  # Antall tidssteg

# Initialisere temperaturen
# u = np.zeros((Nx, Ny)) #Her er for temperatur null på hele flaten
np.random.seed(0)  # Ellers kan vi ta noe random
u = np.random.rand(Nx, Ny) *40 

# Initialbetingelse, altså plassere en varme et sted på området for t=0
u[Nx//2, Ny//2] = 1000

# plotting
fig, ax = plt.subplots()
im = ax.imshow(u, cmap='hot', interpolation='bilinear', origin='lower', extent=[0, Lx, 0, Ly], vmin=0, vmax=100)
ax.set_title("Temperature Distribution")
colorbar = fig.colorbar(im)

# funksjon som løser varmelikningen
def update(frame):
    global u
    u_new = u.copy()
    for i in range(1, Nx-1):
        for j in range(1, Ny-1):
            u_new[i, j] = u[i, j] + dt * alpha * (
                (u[i+1, j] - 2*u[i, j] + u[i-1, j]) / dx**2 +
                (u[i, j+1] - 2*u[i, j] + u[i, j-1]) / dy**2)
    u = u_new
    im.set_data(u)
    return im,

# animasjon
ani = FuncAnimation(fig, update, frames=Nt, blit=True)
plt.show()