list=[1,2,3,4,5,6,7,8]
a=0
x = int(input("Enter the element to search: "))
for i in range (len(list)):
    if list[i]==x:
        a=1
if(a==1):
    print("item found")
else:
    print("item not found")
        
