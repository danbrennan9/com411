class Human: #class
 
  MAX_ENERGY = 100 #constant class attribute

  def __init__(self):
    self.name = "Human" #attributes with default values
    self.age = 0
    self.energy = Human.MAX_ENERGY

  def display(self): #function to display text
    print(f"I am a {self.name}")

if (__name__ == "__main__"): 
  human = Human() #create an object
  human.display() #display it
