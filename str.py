str = input("enter string: ")
ch=input("enter string you want to search: ")
c =0
for i in str:
    if i==ch:
        c+=1
print(c)