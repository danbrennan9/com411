print("What type of cover does the book have?") #gain user input
type = input()

if (type == "soft"): #first check, if true moves to nested if statement, if false moves to elif (next check)
  print("Is the book perfect-bound?")
  perfect_bound = input()
  
  if (perfect_bound == "yes"): #nested if statement
    print("Soft cover, perfect bound books are very popular!")
  else: #nested else statement
      print("Soft covers with coils or stitches are great for short books!")

elif (type == "hard"): #if first IF statement is false, moves to this statement
  print("Books with hard covers can be more expensive!")

else: #if all checks are false, runs else statement here
      print("Input not understood!")