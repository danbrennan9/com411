print("How many mountains should I display?")
mountains_to_display = int(input()) #user input

for count in range(0, mountains_to_display, 1): #the range will start on 0, stop on mountains_to_display, and go up in increments of 1. So for each loop, it will print the text, until it reaches the inputted variables value.
  print("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\
  """)