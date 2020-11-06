def cwd(): 
  import os #import a module
  path = os.getcwd() #apply the get current directory command to local variable path
  print(f"The current working directory is {path}") #printing contents, aka variable path
  print("The directory contains the following:")
  for file in os.listdir(path): #for each file in path, print it, listdir is a built in function to list something
    print(file)

def run():
  print("Processing...")
  cwd()

run()