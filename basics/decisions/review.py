def run():
  print("What is the first part of beep that you will you fix?") #gain user input for variable fix
  fix = input()

  print("What is the second part of beep that you will fix?") # gain user input for variable fix2
  fix2 = input()

  if (fix.lower() == "legs" and fix2.lower() == "arms"): #if both statements are true, runs if statement
    print("what material will you use (iron, steel or diamond)?")
    material = input()
    
    if (material.lower() == "iron" or material.lower() == "steel"): #nested if, if first if is true, expressed with or operator
      print("He's almost as good as new!")
    
    elif (material.lower() == "diamond"): #standard elif
      print("Hes literally shining!")
    
    else: #in case both nested if statements are false, plays else
      print("I'm not sure what material that is.")

  elif (fix.lower() == "head" and fix2.lower() == "hands"): #second if statement
    print("What material will you use (iron, steel or diamond)?")
    material = input()

    if (material.lower() == "iron" or material.lower() == "steel"): #works the same as previous
      print("He's looking quite a bit better!")

    elif (material.lower() == "diamond"):
      print("Look at beep go!")

    else:
      print("I'm not sure what you mean.")

  else: #if both if statement are false, runs else
    print("I'm not sure if thats the best idea.")
