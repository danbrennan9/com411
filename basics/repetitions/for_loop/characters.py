
def run():
  print("What strange markings do you see?")
  markings = input()

  count = 0

  for count in range (0, len(markings), 1): #counts starts on 0, continues through each character of markings by increments of 1
    print("index", count, ":", markings[count]) #count represents what index, so starts on index 0, and markings count is the loop that incrementally goes up for each character

  print("Done!")