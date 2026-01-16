numbers=[]
n=int(input("Enter the size of list: "))
for i in range(n):
	num=int(input("Enter a number: "))
	numbers.append(num)
numbers.sort()
print(numbers)
mid=n//2
print(mid)
if n%2!=0:
	median=numbers[mid]
else:
	median=(numbers[mid]+numbers[mid-1])/2
print("The median is",median)
