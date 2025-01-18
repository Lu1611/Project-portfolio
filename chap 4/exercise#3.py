
num = int(input("Enter the multiplier: "))
n= int(input("Enter the number of table: "))

for i in range(1, n+1):
    print(f"{num}x{i}={num*i}")

#write a python program to calculate the sum of all the odd numbers within the given range.Range is 20 

sum = 0
for i in range(1, 21, 2):
    sum += i
print("The sum of all odd numbers from 1 to 20 is: ", sum)




