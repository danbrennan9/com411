class Human: #class
 
  
  MAX_ENERGY = 100 #constant class attribute

  
  def __init__(self):
    self.name = "Human" #attributes with default values
    self.age = 0
    self.energy = Human.MAX_ENERGY

  
  def grow(self): #method that adds 1 to age
    self.age += 1


  def eat(self, amount=10):#method that takes an amount, namely 10, and adds it to age
    self.amount = amount
    self.age += amount


  def move(self, distance=10):#same as def eat, but removes distance from age
    self.distance=distance
    self.age -= distance

  
  def display(self): #function to display text
    print(f"I am a {self.name}, I am {self.age} years old")

  
  def __repr__(self): #format string representation of object
    return f'robot(name={self.name}, age={self.age})'

  
  def __str__(self): #informal
    return f'My name is {self.name} and I am {self.age} years old.'


if (__name__ == "__main__"): 
  human = Human() #create an object
  human.display() #display it
