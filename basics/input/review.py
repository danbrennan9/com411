def run():
  #Calculator

  #Gets first number for variable answer
  print("Please enter a number")
  firstnumber = int(input())

  #Gets second number for variable answer
  print("Please enter another number")
  secondnumber = int(input())

  answer = firstnumber + secondnumber #Adds the inputs together

  print("Those two numbers add too {}".format(answer))#Outputs the answer of the two inputs

  print("Now please enter a number you liked the multiply this answer by")
  newnumber = int(input())

  newanswer = answer * newnumber

  print("The final answer is {}".format(newanswer))