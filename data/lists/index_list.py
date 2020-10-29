
#see populate_list.py for more complex demonstration
def movements():
  path = ["Move foward", 10, "Move backward", 5, "Move left", 3, "Move right", 1]
  return path

def run():
  print("Moving...")
  path = movements()
  print(f"{path[0]} for {path[1]} steps")
  print(f"{path[2]} for {path[3]} steps")
  print(f"{path[4]} for {path[5]} steps")
  print(f"{path[6]} for {path[7]} steps")

  

run()