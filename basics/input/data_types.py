def run():
  # Basic interface that gathers intel on person and then measures BMI
  # Questions gather intel
  print("What is your name human?")
  name = str(input())

  print("How old are you (in years)?")
  age = str(input())

  print("How tall are you (in meters)?")
  height = float(input())

  print("How much do you weigh (in kilograms)?")
  weight = float(input())

  BMI = weight / (height ** 2) # This is used to calculate BMI from intel

  print(""+ name +" you are " + age +" years old and your BMI is {:.2f} ".format(BMI)) # Output of information and BMI