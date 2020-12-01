from human import Human
from robot import Robot

class Planet:

  def __init__(self):
    self.humans = []
    self.robots = []

  def add_human(self, Human):
    self.humans.append(Human)

  def add_robot(self, Robot):
    self.robots.append(Robot)

  def remove_human(self, Human):
    self.humans.remove(Human)

  def remove_robot(self, Robot):
    self.robots.remove(Robot)

  def __repr__(self):
    return f"planet(humans={self.humans}, robots={self.robots})"

  def __str__(self):
    return f"This planet has {len(self.humans)} humans and {len(self.robots)} robots"

if (__name__ == "__main__"): 
  planet = Planet()
  print(repr(planet))
  print(planet)
  

