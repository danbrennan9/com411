def run():
  print("Where should I look?") #gain user input
  response = input()

  if (response.lower() == "in the bedroom"): #first if statement
    print("Where in the bedroom should I look?")
    bedroom_response = input()
    if (bedroom_response.lower() == "under the bed"): #if first if statement is true, moves to this if statement
      print("Found some shoes but no battery")
    else: #if nested if statement is false, goes to else statement
      print("Found some mess but no battery")

  elif (response.lower() == "in the bathroom"): #if first if statement is false, moves to this elif
    print("Where in the bathroom should I look?")
    bathroom_response = input()
    if (bathroom_response.lower() == "in the bathtub"): #nested if
      print("Found a rubber duck but no battery")
    else: #if nested if is false
      print("Found a wet surface but no battery")

  elif (response.lower() == "in the lab"):
    print("Where in the lab should I look?")
    lab_response = input()
    if (lab_response.lower() == "on the table"): #This section functions the same as the first two
      print("Yes! I found my battery!")
    else:
      print("Found some tools but no battery")

  else: #if all if and elif statements are false, this else statement runs
    print("I do not know where that is but I will keep looking.")