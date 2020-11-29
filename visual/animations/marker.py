import matplotlib.pyplot as plt   
import matplotlib.animation as animation
     
fig, ax = plt.subplots()
    
def animate(frame): 
  global ax
  ax.cla() #clears our axis after each new mapping   
  ax.set_xlim(0, 10) #sets limits
  ax.set_ylim(0, 10)
  plt.plot(frame, frame, 'ro')#plot from frame number to frame number, in red, with circle
     
def run():
  global fig  
  simple_animation = animation.FuncAnimation(fig, animate, frames=10, interval=1000) #animate, with 10 frames at intervals of 1 second
  plt.show()
      
run() 