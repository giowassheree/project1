# Names: Giovanni, Nick
import random
import math
nums = []

for _ in range(20):
    nums.append(random.randint(1, 100))

print("Printing even numbers: ")
for num in nums:
    if num % 2 == 0:
        print(num)
print("\n")
print("Printing odd numbers: ")
for num in nums:
    if num % 2 != 0:
        print(num)


for i in nums:
    total = sum(nums)

print("The total of the array is: " + str(total))


print("Printing the prime numbers: ")
maxPrime = 0
for num in nums:
    if num > 1:
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if (num % 1 == 0):
                is_prime + False
                break
        else:
            print(num, "is a prime number")
            if num > maxPrime:
                maxPrime = num

print("Largest prime number: ", maxPrime)

