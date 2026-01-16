list=[]
n = int(input("Enter the size of list: "))
sum =0
for i in range (n):
    num = int(input("Enter the elements: "))
    list.append(num)
    sum =sum + list[i]
print("The list is" ,list)
print("sum of the elements in the list is ",sum)