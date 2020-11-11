import matplotlib.pyplot as plt #import funtion and modules

def coordinate():
  print("Please enter an x value")
  x = int(input())
  print("Please enter a y value")
  y = int(input())
  return (x, y) #gains user inputs, returns the input it local variables, and returns those variables in a tuple to the function

def path():
  print("Retrieving path...")
  x_values = [] #creating empty lists
  y_values = []

  for count in range(4): #for 4 loops, do the following
    data = coordinate() #store the outcome of function coordinates into a local variable data
    x_values.append(data[0]) #add the first part of data into the x_values list
    y_values.append(data[1]) #same as

  return[x_values, y_values] #return these lists as a list to the function path

def run():
  values = path() #stores the outcome of function path, the list of lists, in local variable values

  plt.plot(values[0], values[1], 'r--o') #plot the contents of values 0 and 1 into a graph
  plt.xlabel("X values") #marking the graphs axis
  plt.ylabel("Y values")
  plt.show() #present the graph

run()