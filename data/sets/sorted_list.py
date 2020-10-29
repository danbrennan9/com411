def observed():
  observations = [] #creating initial list

  for count in range(7):
    print("Please enter a value")
    observations.append(input()) #whatever user inputs, add to list

  return observations #return list to function

def remove_observations(observation):
  print("Do you wish to remove any observations?")
  answer = input()

  remove_observations = True

  while remove_observations = True
    if answer = "yes".lower
    print("What observation would you like to remove?")
    removed_observation = input()
    removed_observations.remove(removed_observation) 
    else:
      remove_observations = False



def run():
  print("Counting observations...")
  observations = observed() #declaring function in local variable
  unique_observed = set() #initalising set
  
  for observation in observations: #for each 'key'(observations) in observations,do the follow:
    occurences = observations.count(observation) #occurences is equal to the count of how many 'keys' (observations) there are in observations in total
    unique_observed.add( (observation, occurences) ) #for each unique 'key' counted, add the key and its occurences to a tuple

  for key, occurences in unique_observed: #for each key and value of that key (the created tuple) in the list containing the unique keys do the follow
    print(f"{key} observed {occurences} times.") #print what key it is, and how many times it occured

run()