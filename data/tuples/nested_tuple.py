def steps(): #first function creates a list variable with a list of tuples, and returns it to the steps fuction
  likelihoods = (
    ("step 1", 50),
    ("step 2", 38),
    ("step 3", 27),
    ("step 4", 99),
    ("step 5", 4)
    )
  return likelihoods

def run():
  returned_steps = steps() #this assigns the contents of the steps function toa  local variable
  good_steps = []
  bad_steps = []

  for step in returned_steps: #for each tuple in the local varaible
    
    if step[1] >= 50: #if the tuples contents are equal to or more than 50
      good_steps.append(step) #added the tuple to the good steps list

    else:
      bad_steps.append(step) #if not add the tuple to the bad steps list

  print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}") #prints the amount of contents within each list

run()
