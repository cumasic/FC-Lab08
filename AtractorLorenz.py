import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Función que define el sistema de Lorenz
def lorenz(xyz0,t):
    s=10
    r=28
    b=8.0/3.0
    x,y,z = xyz0
    dxdt = s * (y - x)
    dydt = x * (r - z) - y
    dzdt = x * y - b * z
    return [dxdt, dydt, dzdt]

#Condiciones iniciales
xyz0 = [1.0, 1.0, 1.0]

#Tiempo
t = np.linspace(0,100,1000)

#Solucion de las ecuaciones diferenciales
sol = solve_event_equation = odeint(lorenz,xyz0,t)

#Gráfica
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot(sol[:,0], sol[:,1], sol[:,2], lw=0.5)
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")
ax.set_title("Atractor de Lorenz")
plt.show()