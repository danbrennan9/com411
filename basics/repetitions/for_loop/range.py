print("What level of brightness is required?")
brightness = int(input())

print("Adjusting brightness...")

for count in range(2, brightness + 1, 2): #brightness must be +1 of true value, so it shows brightness at its cap, and then loop stops
  print("Beeps brightness level:", "*" * count)
  print("Bops brightness level:", "*" * count)

print("Adjustments complete!")
  