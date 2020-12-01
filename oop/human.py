class Human: #class
 
  
  MAX_ENERGY = 100 #constant class attribute

  
  def __init__(self, name="Human"):
    self.name = name #attributes with default values
    self.age = 0
    self.energy = Human.MAX_ENERGY #set the energy to the constant attributre

  
  def grow(self): #method that adds 1 to age
    self.age += 1


  def eat(self, amount):#method that takes an amount and adds it to energy
    max_energy = self.energy + amount #defining what max energy is
    
    if max_energy > Human.MAX_ENERGY: #if these values are above the constant attribute then
      self.energy = Human.MAX_ENERGY #make self.energy equivilent to attribute
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

  
  def display(self): #function to display text
    print(f"I am a {self.name}, I am {self.age} years old, my energy is {self.energy}")

  
  def __repr__(self): #format string representation of object
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'

  
  def __str__(self): #informal
    return f'My name is {self.name} and I am {self.age} years old.'


if (__name__ == "__main__"): 
  human = Human() #create an object
  print(repr(human))
  human.move(10)
  print(repr(human))
  human.eat(5)
  print(repr(human))