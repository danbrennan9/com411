def run():
  print("Please enter a number:")
  number = int(input()) #gain user input on which number to use in sum

  count = 0 #used to count how many times the count has gone up

  total = 1 #total of sum

  while (count < number): #while counts number is less than number inputted by user, this loop will run
    count = count + 1 #the count will go up, to indicate it has done 1 loop
    total = total * count #the total will take the total sum, and multiply it by the count, for example: Total starts on 1, the loop begins and sees that count is on 0, and the number, say 5, is more than count, so the loop begins and count adds 1 to its number. Total then takes the total number, 1, and divides this by the count, aka 1 * 1 = 1. On the next loop, count will go up by one, and the sum will be 1*2. This loops until count reaches the number inputted.

  print("The factorial is {}".format(total)) #displays answer
