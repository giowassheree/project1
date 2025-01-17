# Names: Giovanni, Nick

nums = [4, 2, 10, 15, 7, 90, 21, 25, 26, 28, 52, 1, 13, 78, 45, 50, 67, 74, 9, 34]

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
for i in nums:
    if isInstance(i, int):
        print(i)
