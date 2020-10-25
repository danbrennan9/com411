def run():
  print("Program started!")

  print("Please enter an ASCII code:")
  code = int(input())

  #if code >= 32 and code <= 126:
  if code in range(32, 126):
    character = chr(code)
    print("The character represented by the ASCII code {} is {}".format(code, character))