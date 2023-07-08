from random import choice
from math import log
import numpy as np
import matplotlib.pyplot as plt
from drawgrid import drawgrid
npart=300
side=75  #Should be an odd number
steps = [(1,0),(-1,0),(0,1),(0,-1)]
grid=[[0 for x in range(side)] for y in range(side)]
grid[side//2][side//2]=1 #Put seed at center of grid
for ipart in range(npart):
    # Start particle in corner of grid
    x,y = 0,0
    # perform the random walk until particle aggregates
    while 1:
        grid[x][y]=0   #Remove particle from current spot
        # Randomly move particle
        sx,sy = choice(steps)
        x += sx
        y += sy
        # Enforce periodic boundaries
        if x < 0: x=side-1
        if y < 0: y=side-1
        if x==side: x=0
        if y==side: y=0
        grid[x][y]=1   #Put particle in new location
        # Stop if you are next to a particle
        if (grid[(x+1)%side][y]+grid[x][(y+1)%side]+
            grid[(x+side-1)%side][y]+grid[x][(y+side-1)%side])>0:
            break
drawgrid(grid, side)
N=0
Ns=[]
Ls=[]
for L in range(1,side//2,2):
    for i in range(side//2-L//2, side//2+L//2+1):
        for j in range(side//2-L//2, side//2+L//2+1):
            if grid[i][j]==1:
                N+=1
    #print(N, L)
    Ns.append(log(N))
    Ls.append(log(L))
    N=0
y=np.array(Ns)
x=np.array(Ls)
## Calculate slope
n=len(x)
slope=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(n*np.sum(x*x)-np.sum(x)**2)
print("slope=",slope)
plt.plot(Ls,Ns)
plt.title("Dimensionality=%5.3f"%(slope))
plt.xlabel("Log(box length)")
plt.ylabel("Log(particles in box)")
plt.show()

