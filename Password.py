import random
import string

print ("Hello ,Welcome to Password Generator...")

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = num + upper + lower + symbols

length = int(input("\nEnter the length of password: "))
temp = random.sample(all,length)
password = "".join(temp)
print(password)

