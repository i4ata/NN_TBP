from .TBP_Solver import *
import numpy as np

step = 0.001
max_t = 5
M = [1,1,1]
G = 1

x1 = -2
y1 = -1

x2 = 1
y2 = 0.5

x3 = 0
y3 = -0.5

vx1 = 0.3471
vy1 = 0.5327

vx2 = vx1
vy2 = vy1

vx3 = -2*vx1
vy3 = -2*vy1

energy_threshold = 1

iterations = 3

def get_random_positions():
    return np.random.uniform(-3,3), np.random.uniform(-3,3), np.random.uniform(-3,3), np.random.uniform(-3,3), np.random.uniform(-3,3), np.random.uniform(-3,3)

def get_random_velocities():
    return np.random.uniform(-1,1), np.random.uniform(-1,1), np.random.uniform(-1,1), np.random.uniform(-1,1), np.random.uniform(-1,1), np.random.uniform(-1,1)

def get_kinetic_energy(mass, v1, v2):
    velocity = np.sqrt(v1*v1 + v2*v2)
    return mass*velocity*velocity/2

def get_potential_energy(x1, y1, m1, x2, y2, m2, G):
    distance = np.sqrt((y2-y1)*(y2-y1) + (x2-x1)*(x2-x1))
    return G*m1*m2/distance

def get_energy(x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3, M, G):
    total_kinetic =  get_kinetic_energy(M[0],vx1,vy1) + get_kinetic_energy(M[1],vx2,vy2) + get_kinetic_energy(M[2],vx3,vy3)
    total_potential = get_potential_energy(x1,y1,M[0],x2,y2,M[1],G) + get_potential_energy(x1,y1,M[0],x3,y3,M[2],G) + get_potential_energy(x2,y2,M[1],x3,y3,M[2],G)
    return total_kinetic - total_potential

if __name__ == '__main__':
    x1, y1, x2, y2, x3, y3 = get_random_positions()
    vx1, vy1, vx2, vy2, vx3, vy3 = get_random_velocities()
    
    print("\nPositions:")
    print("Body 1: " + str(x1) + ", " + str(y1))
    print("Body 2: " + str(x2) + ", " + str(y2))
    print("Body 3: " + str(x3) + ", " + str(y3) + "\n")

    print("Velocities:")
    print("Body 1: " + str(vx1) + ", " + str(vy1))
    print("Body 1: " + str(vx2) + ", " + str(vy2))
    print("Body 1: " + str(vx3) + ", " + str(vy2) + "\n")

    print("Total energy of the system: " + str(get_energy(x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3, M, G)))

    x,y = euler_method(max_t, step, M, G, x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3)
    print("Done")
    plot(x,y)
