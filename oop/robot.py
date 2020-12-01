class Robot: #check human.py for notes

  MAX_ENERGY = 100

  def __init__(self, energy=MAX_ENERGY):
    self.name = "Robot"
    self.age = 0
    self.energy = energy

  def display(self):
    print(f"I am a {self.name}")

  def grow(self): #method that adds 1 to age
    self.age += 1

  def eat(self, amount):#method that takes an amount and adds it to energy
    max_energy = self.energy + amount #defining what max energy is
    
    if max_energy > Robot.MAX_ENERGY: #if these values are above the constant attribute then
      self.energy = Robot.MAX_ENERGY #make self.energy equivilent to attribute
      return max_energy - self.energy #return the maximum possible energy, minus the self energy value
    
    else:
      self.energy = max_energy
      return 0
      

  def move(self, distance):#same as def eat, but removes distance from energy
    min_energy = self.energy - distance

    if min_energy < 0: #if min energy is below 0
      self.energy = 0 #turn it to zero
      return self.energy - abs(min_energy) #return self energy minus the min energy

    else:
      self.energy = min_energy
      return 0

  def __repr__(self): 
    return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

  def __str__(self): 
    return f'My name is {self.__name} and I am {self.age} years old.'

if (__name__ == "__main__"):
  robot = Robot()
  print(repr(robot))
  robot.move(10)
  print(repr(robot))
  robot.eat(5)
  print(repr(robot))