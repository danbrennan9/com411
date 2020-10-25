def run():
  print("Please enter the activity to be performed.") #gaining user input on activity 
  activity = input()

  if activity.lower() == "calculate": #if statements check if activity is calculate
    print("Performing calculations...") #performs relative response

  else:
    print("Performing activity...") #if activity is not true for IF statement, aka calculate, performs this code

  print("Activity completed!")