import random

pass_array = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '1', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'p', 'r', '_', '#', '@', '!', '&', '^', '$', '~', '+']

print("Enter the length of the password:")
length = int(input())

password = ''.join(random.choice(pass_array) for _ in range(length))

print("Your Password is : "+password)