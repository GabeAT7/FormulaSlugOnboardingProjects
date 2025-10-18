import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass
class State:
    xpos : float
    ypos : float
    xvel : float
    yvel : float 

deltaT = 0.7
bounceCoeff = 0.9


def step (state:State) -> State:
    new_xpos = state.xpos + state.xvel * deltaT
    new_ypos = state.ypos + state.yvel * deltaT
    new_yvel = state.yvel -9.81 * deltaT
    if new_ypos < 0:
        new_yvel = new_yvel * -1 * bounceCoeff
    sNew = State(
        xpos = new_xpos,
        ypos = new_ypos,
        xvel = state.xvel,
        yvel = new_yvel

    )

    return sNew


def step2 (state:State) -> State:
    new_xpos = state.xpos + state.xvel * deltaT
    new_ypos = state.ypos + state.yvel * deltaT
    new_yvel = state.yvel -9.81 * deltaT
    if new_ypos < 0:
        new_yvel = new_yvel * -1 * 1.01
    sNew = State(
        xpos = new_xpos,
        ypos = new_ypos,
        xvel = state.xvel,
        yvel = new_yvel

    )

    return sNew




def animate (i):
    global s0, s1
    
    s0 = step(s0)
    s1 = step2(s1)

    ax.clear()

    ax.scatter([s0.xpos],[s0.ypos],s=200)

    ax.scatter([s1.xpos],[s1.ypos],s=200)

    ax.set_xlim(-2,2)

    ax.set_ylim(0,1000)

    return ax
    

s0 = State(
    xpos = 0,
    ypos = 500,
    xvel = 0,
    yvel = 0,

)


s1 = State(
    xpos = 1,
    ypos = 500,
    xvel = 0,
    yvel = 0,

)




fig = plt.figure(figsize=(3,3), dpi=150)
ax = fig.add_subplot(111)

ax.grid()

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

plt.pause(5)
ani = animation.FuncAnimation(fig, animate, interval=0)
plt.show()