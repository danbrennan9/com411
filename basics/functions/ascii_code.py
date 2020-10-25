
def run():
  print("Program started!")

  print("Please enter a standard character.")
  character = input()

  if len(character) == 1:
    value = ord(character)
    print("The ASCII code for {} is {}".format(character, value))

  else:
    print("That is an unknown character.")

  print("Program ended!")


