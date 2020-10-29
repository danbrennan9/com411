def pattern():
  sequences = { #dictionary getting populated
    "Short Sequence":3, "Medium Sequence":2, "Long Sequence":1
  }

  return sequences #returning dictionary to function

def run():
  print(pattern()) #print contents of function

run()