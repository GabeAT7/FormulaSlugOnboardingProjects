import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass



class State:
    xpos : float
    ypos : float
    xvel : float
    xacel : float
    time : float

deltaT = 1


def step (state:State) -> State:
    new_xpos = state.xpos + state.xvel * deltaT
    new_xvel = state.xvel + state.xacel * deltaT
    new_xacel = state.xacel
    new_time = state.time + 1
    print(new_time,new_xvel)


    if new_time > 9:
        if new_xvel > 0:
            new_xacel = -4
        elif new_xvel < 0:
            new_xvel = 0

    sNew = State(
        xpos = new_xpos,
        ypos = state.ypos,
        xvel = new_xvel,
        xacel = new_xacel,
        time = new_time

    )

    return sNew

def animate (i):
    global s0
    s0 = step(s0)
    ax.clear()
    ax.scatter([s0.xpos],[s0.ypos],s=200)
    ax.set_xlim(-500,1000)
    ax.set_ylim(0,5)
    return ax

s0 = State(
    xpos = 0,
    ypos = 0,
    xvel = 0,
    xacel = 0.9,
    time = 0
)

fig = plt.figure(figsize=(3,3), dpi=150)
ax = fig.add_subplot(111)
ax.grid()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
plt.pause(5)
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()