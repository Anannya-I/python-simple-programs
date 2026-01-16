x=[]
n = int(input("Enter the size of list: "))
for i in range(n):
    num = int(input("Enter the elements: "))
    x.append(num)
x.sort()
print("List=",x)