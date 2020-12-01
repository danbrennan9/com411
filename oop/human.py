class Human: #class
 
  MAX_ENERGY = 100 #constant class attribute

  def __init__(self):
    self.name = "Human" #attributes with default values
    self.age = 0
    self.energy = Human.MAX_ENERGY

  def display(self): #function to display text
    print(f"I am a {self.name}")

  def __repr__(self): #format string representation of object
    return f'robot(name={self.name}, age={self.age})'

  def __str__(self): #informal
    return f'My name is {self.name} and I am {self.age} years old.'

if (__name__ == "__main__"): 
  human = Human() #create an object
  human.display() #display it
