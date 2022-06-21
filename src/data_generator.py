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


def get_momentum(mass, velocity):
    return mass*velocity[0], mass*velocity[1]

def get_square_momentum(mass, velocity):
    x,y = get_momentum(mass, velocity)
    return x*x + y*y

def get_distance(body1, body2):
    return np.sqrt( np.power((body1[0] - body2[0]),2) + np.power((body1[1] - body2[1]),2) )

def get_energy(x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3):
    return - (G*M[0]*M[1] / get_distance([x1,y1], [x2,y2])) - (G*M[1]*M[2] / get_distance([x2,y2], [x3,y3])) - (G*M[2]*M[0] / get_distance([x1,y1], [x3,y3])) + get_square_momentum(M[0], [vx1,vy1]) / (2*M[0]) + get_square_momentum(M[1], [vx2,vy2]) / (2*M[1]) + get_square_momentum(M[2], [vx3,vy3]) / (2*M[2])

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

    print("Total energy of the system: " + str(get_energy(x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3)))

    x,y = euler_method(max_t, step, M, G, x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3)
    plot(x,y)
