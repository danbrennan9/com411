def run():
  print("What did I hear?") #gain user input for response 1
  response1 = input()

  print("What did I see?") #gain user input for response 2
  response2 = input()

  if (response1.lower() == "grrr" and response2.lower() == "two reds eyes"): #and operator, if both inputs are true plays if statement
    print("There is a scary creature. I should get out of here!")

  else: #if IF statement is false, plays else
    print("I am a little scared but I will continue.")