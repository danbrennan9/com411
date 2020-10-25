def run():

  print("Please enter a word") #gain inital input needed for all functions
  word = input()

  def option1(): #each "option" function creates code dependent upon the input recieved in run function
      dashes = len(word) + 8
      print("-" * dashes)
      print("|   {}   |".format(word))
      print("-" * dashes)

  def option2():
      print(word.lower())

  def option3():
      print(word.upper())

  def option4():
      reversed = word [::-1] #this is called a slice, the first colon represents where to start, second represents where to end, and the -1 represents in which direction to travel
      print(reversed)

  def option5():
      print("How many times would you like to display the word?")
      repeat = int(input())
      for repeat in range(repeat):
        if (repeat % 2 == 0):
          print(word.lower())
        else:
          print(word.upper())

      

  def run_inner():

    print("""
    Please choose option an option:
    1) Display in a box
    2) Display lower-case
    3) Display upper-case
    4) Display mirrored
    5) Repeat
    6) Quit
    """)
    option = int(input()) #determining option to choose

    if option == 1: #if option 1 is chose, function option 1 will run, etc
        option1()

    elif option == 2:
        option2()

    elif option == 3:
        option3()

    elif option == 4:
        option4()

    elif option == 5:
        option5()
      
    elif option == 6:
        exit

    else:
        print("I'm unsure what you mean, please try again.") #error handling

  run_inner() #run function to begin program once a "word" (global variable) has been determined

