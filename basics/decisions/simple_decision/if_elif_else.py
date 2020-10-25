def run():
  print("Towards which direction should I paint (up, down, left or right)?") #gains user input
  direction = input()

  if direction.lower() == "up": #first check, followed by suitable checks until it finds true response
    print("I am painting in the upward direction!")

  elif direction.lower() == "down":
    print("I am painting in the downward direction!")

  elif direction.lower() == "left":
    print("I am painting in the leftward direction!")

  elif direction.lower() == "right":
    print("I am painting in the rightward direction!")
  
  else:
    print("I'm not sure what you mean.") #in case of human error, this will tell the user their input was wrong

