from human import Human
from robot import Robot

class Planet:

  def __init__(self): #dictionary containing two attributes
    self.inhabitants = {
      'humans':[],
      'robots':[]
    }


  def add_human(self, Human):
    self.inhabitants['humans'].append(Human) #add a human to humans list in dict

  def add_robot(self, Robot):
    self.inhabitants['robots'].append(Robot)

  def remove_human(self, Human):
    self.inhabitants['humans'].remove(Human)

  def remove_robot(self, Robot):
    self.inhabitants['robots'].remove(Robot)

  def __repr__(self):
    return f"planet(humans={self.inhabitants['humans']}, robots={self.inhabitants['robots']})"

  def __str__(self):
    return f"This planet has {len(self.inhabitants['humans'])} humans and {len(self.inhabitants['robots'])}"

if (__name__ == "__main__"): 
  planet = Planet()
  print(repr(planet))
  print(planet)
  

