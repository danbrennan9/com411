def display_ladder(steps):
  for step in range(steps): #for each step, print the follow statement
    print("|  |")
    print("***")
  print("|  |")


def create_ladder():
  print("Please enter the numbe of steps.") #gaining user input
  steps = int(input) #inputted steps
  display_ladder(steps) #for the steps that the user inputted, play the display_ladder function

create_ladder()