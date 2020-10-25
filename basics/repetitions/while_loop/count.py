def run():
  print("How many live cables must I avoid?")
  answer = int(input())

  live_cables = 0

  while (live_cables <= answer):
    print("Avoiding....", "...Done! {} live cables avoided!".format(live_cables))
    live_cables += 1

  print("All live cables have been avoided")