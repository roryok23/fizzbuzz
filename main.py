fruits = ["apple", "pear", "banana"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

#For Loop with Range
for number in range(1,10):
    print(number)

#For Loop with Range and step
for number in range(1,10, 2):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)


total = 0

for number in range(2, 101, 2):
    total += number
print(total)

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
     total2 += number
print(total2)


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

