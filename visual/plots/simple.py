import matplotlib.pyplot as plt #importing the function and module

def display(x_values, y_values): #first functions takes two lists of values, and supplements them as the arguments
  plt.plot(x_values, y_values) #in this format, print the values
  plt.show() #show values

def run():
  x_values = [1,2,3,4,5] #value x
  y_values = [1,4,9,16,25] #value y
  display(x_values, y_values)

run()