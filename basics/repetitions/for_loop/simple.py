print("How many mountains should I display?")
mountains_to_display = int(input()) #user input

for count in range(0, mountains_to_display, 1): #the range starts on 0, goes up to a total of the variable (user inputted), in increments of 1. So if mountains_to_display is 3, it will start on 0, loop, print the mountain once, check what numbers its currently on, if its not 3, it will print another mountain, until it reaches 3 loops. Aka, it will loop until its looped the specified amount of times that the user inputted variable says.
  print("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\
  """)