def short_pattern():
  pattern = { #filling function with dictionary then returning it
    "sequence":"101",
    "occurrences":5
  }

  return pattern

def medium_pattern(): #filling function with dictionary then returning it
  pattern = {
    "sequence":"111000",
    "occurrences": 25
  }

  return pattern

def long_pattern(): #filling function with dictionary then returning it
  pattern = {
    "sequence":"1100110011001100",
    "occurrences":50
  }

  return pattern

def run():
  print("Analysing patterns...")
  patterns = { #creating new dictionary
    "short patterns": short_pattern(), #each dictionary contains the speech I want to apply at the start, and then the contents of the following functions
    "medium patterns": medium_pattern(), #IE, this puts the text medim patterns, then next to it, display the contents of its function, which is the dictionary that was returned within
    "long patternsmm": long_pattern()
  }

 
  print(patterns)

run()