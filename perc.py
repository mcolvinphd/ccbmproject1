from random import choice, choices, random
import matplotlib.pyplot as plt
side=35  #Should be an odd number
trials=1000
maxtime=10000 #Number of steps that a particles takes trying to escape
density=0.1
delta_density=0.1
percs=[]
densities=[]
steps = [(1,0),(-1,0),(0,1),(0,-1)]
grid=[[0 for x in range(side)] for y in range(side)]
while density < 0.8:  #Loop over densities
    perc=0
    for trial in range(trials):
        count=0
        #Randomly fill grid with barriers at specified density
        grid=[[choices((0,1),weights=(1-density,density))[0] for x in range(side)] for y in range (side)]
        x,y = side//2,side//2 # Start particle at center
        for time in range(maxtime):
            # Randomly move particle
            sx,sy = choice(steps)
            nx = x+sx
            ny = y+sy
            # if new position is occupied try again
            if grid[nx][ny]==1:
                continue
            if nx==0 or ny==0 or nx==(side-1) or ny==(side-1):
                perc+=1
                break
            x=nx
            y=ny
    print("%4d %5.3f  %5.3f"%(side,density,perc/trials))
    densities.append(density)
    percs.append(perc/trials)
    density+=delta_density
plt.plot(densities,percs)
plt.show()
