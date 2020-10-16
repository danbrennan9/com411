# Ask user to enter their name
print("What is your name human?")
name = input()
print("Nice to meet you", name)

# Alternative 1

print("What is your name human?")
name = input()
print("Nice to meet you {}".format(name))

# Alternative 2
name = input("What is your name human?\n")
print("Nice to meet you", name)