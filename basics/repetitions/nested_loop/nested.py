def run():
  print("How many rows should I have?")
  rows = int(input())

  print("How many columns should I have?")
  columns = int(input())

  print("Here I go:")


  for count in range(0, columns, 1):
    print("")
    for count in range(0, rows, 1):
      print(":=)", end="")
  