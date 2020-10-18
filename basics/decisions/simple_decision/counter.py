print("Please enter the first whole number.")
first_num = int(input())

print("Please enter the second whole number.")
second_num = int(input())

print("Please enter the the third whole number.")
third_num = int(input())

odd_num = 0
even_num = 0

if (first_num % 2 == 0):
  even_num += 1
else:
    odd_num += 1

if (second_num % 2 == 0):
  even_num += 1
else:
    odd_num += 1

if (third_num % 2 == 0):
  even_num += 1
else:
    odd_num += 1

print("There was {} even and {} odd numbers.".format(even_num, odd_num))



