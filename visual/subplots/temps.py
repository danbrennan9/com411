import matplotlib.pyplot as plt

def read_data(file_name): #reads in whatever file name is provided
  with open(file_name) as file: #open file, and close when done
   temps = [] #empty list

   for line in file: #for each line in the file given
     temps.append(int(line.strip())) #add the line as an integer to the empty list, strip any missing chars 
   return temps #returns the contents of the list to the function

def run():
  data = read_data("visual/subplots/temps.txt") #open the first function with a file, and assign it to a local variable
  fig, axs = plt.subplots(1,2) #define subplots, 1 row, 2 collumns

  axs[0].plot(range(1,8), data) #for the first axs (subplot graph), make a line graph, its x axis being 1 up to 7, and its y being the data provided (the temps)
  axs[1].bar(range(1,8), data) #same as before, but with a bar graph
  plt.tight_layout() #format the layout correctly
  plt.show() #show contents

run() #run functions




