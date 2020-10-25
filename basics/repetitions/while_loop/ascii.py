def run():
  print("How many bars should be charged?")
  response = int(input())

  charged_bars = 0 #variable for tracking charged bars

  while (charged_bars <= response): #while loop to repeat code until variables conditions are true
    print("Charging:", "█" * charged_bars) #prints each loop, while the symbol is printed X amount of times, dependent on the amoutn of charged bars

    charged_bars += 1 #increment on variable

  print("The battery is fully charged.") #end print