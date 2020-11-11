import matplotlib.pyplot as plt

def small(): #displays a small plotted square
  x = [3, 3, 4, 4, 3]
  y = [3, 4, 4, 3, 3]

  plt.plot(x, y, 'r:o') #designated parementers for plot to be drawn
  
def medium(): #same as
  x = [2, 2, 5, 5, 2]
  y = [2, 5, 5, 2, 2]

  plt.plot(x, y, 'g--s')

def large(): #same as
  x = [1, 1, 6, 6, 1]
  y = [1, 6, 6, 1, 1]

  plt.plot(x, y, 'b-p')

def run(): #runs the functions
  small()
  medium()
  large()
  plt.show() #displays functions output

run()

