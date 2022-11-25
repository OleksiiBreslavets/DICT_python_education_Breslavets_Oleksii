"""Chat-Bot project: simple types, input-output, strings, calculations, loops"""

print("Hello! My name is DICT_OleksiiBreslavets_ChatBot.")
print("I was created in 2022.")
print("Please, remind me your name.")
name = input("> ")
print("What a great name you have, " + name + "!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input("> "))
remainder5 = int(input("> "))
remainder7 = int(input("> "))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is " + str(age) + "; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
number = int(input("> "))
for unknown in range(number + 1):
    print(str(unknown) + "!")
print("Let's test your programming knowledge.")
print("Why do we use print() function?")
print("1.To interrupt the execution of a program.")
print("2.To iterate over a sequence.")
print("3.To print the specified message to the screen.")
print("4.To take the input from the user.")
answer = int(input("> "))
while answer != 3:
    print("Please, try again.")
    answer = int(input("> "))
else:
    print("Completed, have a nice day!")
print("Congratulations, have a nice day!")
