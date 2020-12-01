import matplotlib.pyplot as plt   
import matplotlib.animation as animation
     
fig, ax = plt.subplots()
data = [] #global list

def init():
  data.append({'x':[3,3,4,4,3], 'y':[3,4,4,3,3]}) #add these dictionaries, with their key (x or y) and their index being the list of values to assign it
  data.append({'x':[2,2,5,5,2], 'y':[2,5,5,2,2]})
  data.append({'x':[1,1,6,6,1], 'y':[1,6,6,1,1]})
    
def animate(frame): 
  global ax
  ax.cla()
  index = frame % len(data) #to work out the index, take the frame and divide it by the length of the list data
  ax.set_xlim(0, 7) #sets limits
  ax.set_ylim(0, 7)
  plt.plot(data[index]['x'], data[index]['y']) #plot datas index, pointing to the key within the dictionary and as a result what list of values to use
     
def run():
  global fig  
  simple_animation = animation.FuncAnimation(fig, animate, frames=3, interval=1000, init_func=init) #animate, with 10 frames at intervals of 1 second
  plt.show()
      
run() 