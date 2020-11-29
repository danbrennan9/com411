import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np 

fig, ax = plt.subplots()

def animate(frame):
  global ax
  ax.cla() #clears previous axis
  ax.set_xlim(0, 2*np.pi) #same as the np.arange for x
  ax.set_ylim(-1, 1) #sine waves hve lims of -1 and 1 on Y
  x = np.arange(0, 2*np.pi, 0.01)
  y = np.sin(x + frame/50) #moves the y value by x by the divisionof the frame, creating a shifting movement
  ax.plot(x, y)

def run():
  global fig
  simple_animation = animation.FuncAnimation(fig, animate, frames=720, interval=100)
  plt.show()

run()