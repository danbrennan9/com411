from human import Human
from robot import Robot
from planet import Planet
import random

class Universe:

  def __init__(self):
    self.planets = []

  def generate(self):
    planet = Planet()

    for count in range(random.randint(1,10)):
      human = Human()
      planet.add_human(human)

    for count in range(random.randint(1,10)):
      robot = Robot()
      planet.add_robot(robot)


    self.planets.append(planet)

  def __repr__(self):
    return f"Universe(planets={self.planets})"

  def __str__(self):
    return f"Universe contains {len(self.planets)} planets."

if (__name__ == "__main__"): 
  universe = Universe()
  universe.generate()
  print(universe)

