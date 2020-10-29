def observed():
  observations = [] #creating initial list

  for count in range(7):
    print("Please enter a value")
    observations.append(input()) #whatever user inputs, add to list

  return observations #return list to function

def remove_observations(observations): #stores the list from function 1 for changing
  running = True #sets the bolean to true

  while (running): #while the variables bolean is true

    print("Do you wish to remove an observation?")
    answer = input()

    
    
    if (answer == "yes"):
      print("What observation would you like to remove?")
      removed = input() #input
      observations.remove(removed) #whatever input user types, remove that input from the observations list
    
    else:
      running = False



def run():
  observations = observed() #declaring function in local variable and adds original observations list
  remove_observations(observations) #adds removed observation
  
  
  unique_observed = set() #initalising set
  for observation in observations: #for each 'key'(observations) in observations,do the follow:
    occurences = observations.count(observation) #occurences is equal to the count of how many 'keys' (observations) there are in observations in total
    unique_observed.add( (observation, occurences) ) #for each unique 'key' counted, add the key and its occurences to a tuple

  for key, occurences in unique_observed: #for each key and value of that key (the created tuple) in the list containing the unique keys do the follow
    print(f"{key} observed {occurences} times.") #print what key it is, and how many times it occured

run()