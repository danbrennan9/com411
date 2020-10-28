def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  return_list = directions()
  count = 0

  for index in range(len(return_list)):
    print("{}: {}".format(count, return_list[index]))
    count += 1

def run():
  menu()

run()