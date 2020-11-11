import matplotlib.pyplot as plt #import module and function to plot
import random as rnd #importing random module

def data():
  path = {} #create an empty dictionary
  print("What type of line would you like? (:, -- or -")
  style = input()
  print("What type of colour would you like? (r, g or b)")
  colour = input()
  print("What kind of style marker would you like?")
  marker_style = input()
  
  #gain input for specifics of plot
  
  path['style'] = style
  path['colour'] = colour
  path['marker_style'] = marker_style
  #add each input into the dictionary as key value pairs

  return path #return contents

def generate():
  print("How many lines would you like to display?")
  lines_display = int(input()) #gain user input

  for line_display in range(lines_display): #for the input put in by the user, loop that many times
    values = data()

    x = rnd.sample(range(1, 10), 5) #importing 5 random values between 1 and 10, for x
    y = rnd.sample(range(1, 10), 5) #same as

    format = f"{values['style']}{values['colour']}{values['marker_style']}" #return the values of the dictionary, and for each key use the value inside as the format
    plt.plot(x, y, format) #plot the graph

  plt.show()

def run():
  print("Running....")
  generate()
  print("Done!")

run()