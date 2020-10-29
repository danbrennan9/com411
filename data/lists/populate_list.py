def directions(): #function with content of available directions
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu(): #menu function
  print("Please select a direction:")
  return_list = directions()
  count = 0

  for index in range(len(return_list)):
    print("{}: {}".format(count, return_list[index])) #returns the list with correct formatting
    count += 1
    

  direction = int(input()) #gain user input
  return return_list[direction] #return list

  
def run():
  route = []
  print("Working out escape route...")

  for count in range(5): #max iterations
    route.append(menu()) #updating the list in menu due to input
    
  print("Escape route: {}".format(route))


run()