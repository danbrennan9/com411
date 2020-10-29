def likelihood(): 
  likelihoods = (50, 38, 27, 99, 4) #tuple populate with values
  return min(likelihoods) #returns the minimum value in the tuple to the function

def run():
  print(f"Minimum likelihood of falling: {likelihood()}%") #calls the result of the function and prints it

run()