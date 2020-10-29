def likelihood(): #function that returns min and max values in nested tuple
  likelihoods = (50, 38, 27, 99, 4) #tuple populate with values
  return min(likelihoods), max(likelihoods) #returns the minimum value in the tuple to the function

def run():
  likelihood() #gets contents of first function, then print the min and max values of the tuple within
  print(f"Maximum likelihood of falling: {max(likelihood())}%") #calls the result of the function and prints it 
  print(f"Minimum likelihood of falling: {min(likelihood())}%") #calls the result of the function and prints it

run()