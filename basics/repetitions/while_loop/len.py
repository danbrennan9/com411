def run():
  print("Please enter a phrase:")
  phrase = input()

  length = len(phrase)

  repetitions = 0

  while (repetitions < length):
    print(phrase, end=" ")
    repetitions += 1