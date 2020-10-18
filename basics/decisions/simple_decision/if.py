
print("What type of book is this (adventure or horror?)?") #gaining input from user on what statement to run
type = input()


if type.lower() == "adventure": #first check to see if book is adventure
  print("I like adventure books!")

elif type.lower() == "horror": #if the first check is false, moves to elif check
  print("I like horror books!")

else:
  print("I'm not sure what type of book you mean.") #to account for errors, if the response is not recognised

print("Finished reading book!") #prints at the end of the program regardless of control flow