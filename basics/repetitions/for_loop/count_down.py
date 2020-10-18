print("How far are we from the cave?")
steps = int(input()) #user inputted

for count in range(0, steps, 1): #loop starts on 0, stops looping at steps, and goes up in increments of 1
  print("{} steps remaining.".format(steps))
  steps = steps - 1 #steps loses a number each time, to show the user how far they are from the cave

print("We have reached the cave!")
