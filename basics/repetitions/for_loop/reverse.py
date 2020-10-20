print("What phrase do you see?")
phrase = input()

print("Reversing...\nThe phrase is ", end="")

for position in range (len(phrase) - 1, -1, -1): #for loop starts on end character of phrase, loops until it reaches the last character, and goes down in increments of 1
  print(phrase[position], end="") 
