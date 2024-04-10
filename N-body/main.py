#region imports
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from dotenv import load_dotenv, dotenv_values

load_dotenv()
sys.path.insert(0, os.getenv("parent_directory"))
sys.path.insert(0, os.getenv("common_directory"))
from Common import *

#endregion

#initialise variables
#create particles (function)
#calculate acceleration
#evolve states of particles and package the data for plotting
#run simulation (function)

#region Methods
def create_particles(N, pos_array, vel_array, M):
    particles = []
    for i in range(N):
        particle_pos = vector2D.Vect2(pos_array[i, 0], pos_array[i, 1])
        particle_vel = vector2D.Vect2(vel_array[i, 0], vel_array[i, 1])

        particle = Body.Particle(particle_pos, particle_vel, M/N)

        particles.append(particle._pt)
    
    return particles #array of datapoints


def calculate_acceleration_force(pt, pt_array, G):
    for j in range(len(pt_array)):
        if pt_array[j] != pt:
            pt.ax += (pt_array[j].x - pt.x) * pt_array[j].mass * G * (1/(((pt.x - pt_array[j].x) **2 + (pt.y - pt_array[j].y) **2) ** (3/2)))
            pt.ay += (pt_array[j].y - pt.y) * pt_array[j].mass * G * (1/(((pt.x - pt_array[j].x) ** 2 + (pt.y - pt_array[j].y) ** 2) ** (3/2)))
        
        Fx = pt.ax * pt.mass
        Fy = pt.ay * pt.mass

    return vector2D.Vect2(Fx, Fy)


def integrate_and_plot(Nt, dt, pt_array, G, pos, pos_save, plotRealTime):
    #prep figure
    fig = plt.figure(figsize=(4, 5), dpi = 80)
    grid = plt.GridSpec(3, 1, wspace=0.0, hspace=0.3)
    ax1 = plt.subplot() #grid[0:2,0]
    #ax2 = plt.subplot(grid[2,0])
    #main simulation loop
    for i in range(Nt):
        for particle in pt_array:
            F = calculate_acceleration_force(particle, pt_array, G)
            particle.inteqm([F.x, F.y, 0], dt)
            pos[pt_array.index(particle), 0] = particle.x
            pos[pt_array.index(particle), 1] = particle.y

        pos_save[:, :, i+1] = pos

        #plot in real time
        if plotRealTime or (i == Nt-1):
            plt.sca(ax1)
            plt.cla()
            xx = pos_save[:,0,max(i-50, 0):i+1]
            yy = pos_save[:,1,max(i-50, 0):i+1]

            plt.scatter(xx, yy, s=1, color=[.7, .7, 1])
            plt.scatter(pos[:, 0], pos[:, 1], s=10, color='blue')
            ax1.set(xlim=(-2, 2), ylim=(-2, 2))
            ax1.set_aspect('equal', 'box')
            ax1.set_xticks([-2,-1,0,1,2])
            ax1.set_yticks([-2,-1,0,1,2])
            plt.pause(0.001)
    return 0

#endregion       

            



#region main program

def main():
    N = 50                          #number of particles
    t_end = 10.0                    #end time of simulation
    dt = 1e-2                       #time element
    G = 0.1                         #value for simulation scale
    plotRealTime = True             #plot as the simulation runs
    np.random.seed(17)
    M = 20                          #total mass of the system

    pos = np.random.randn(N, 2)     #initialise the positions of the particles at random
    vel = np.random.randn(N, 2)     #initilaise the velocities of the particles at random
    Nt = int(np.ceil(t_end/dt))     #number of timesteps

    pos_save = np.zeros((N, 2, Nt+1))  #Creates an array of dimensions Nx2 and each element contains Nt+1 vals
    pos_save[:, :, 0] = pos          #Added the initial positions of all particles

    particles = create_particles(N, pos, vel, M)

    integrate_and_plot(Nt, dt, particles, G, pos, pos_save, plotRealTime)

if __name__ == "__main__":
    main()

#endregion