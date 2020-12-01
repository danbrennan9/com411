class Robot: #check human.py for notes

  MAX_ENERGY = 100

  def __init__(self, energy=MAX_ENERGY):
    self.name = "Robot"
    self.age = 0
    self.energy = 0

  def display(self):
    print(f"I am a {self.name}")

  def __repr__(self): 
    return f'robot(name={self.name}, age={self.age})'

  def __str__(self): 
    return f'My name is {self.__name} and I am {self.age} years old.'

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()