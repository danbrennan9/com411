def run():
  print("What type of adventure should I have?") #gains user input
  type = input()

  if (type.lower() == "scary" or type.lower() == "short"): #logical or operator, if either inputs are true, prints statement 
    print("Entering the dark forest!")
    
  elif (type.lower() == "safe" or type.lower() == "long"): #if first IF statement is false, plays this elif statement (works same)
    print("Taking the safe route!")

  else: #if all statements are false, plays else statement
    print("Not sure which route to take.")