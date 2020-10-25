def run():
  def climb_ladder(steps_remaining, num_steps):
    if num_steps < steps_remaining:
      print("Still some way to go!")
    
    else:
      print("We are almost there!")

  climb_ladder(2,5)