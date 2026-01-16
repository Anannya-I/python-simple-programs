n =int(input("Enter a number:"))
print("strong numbers are")
for i in range(n+1):
    copy=i
    sum=0
    while(i>0):
        f=1
        r=i%10
        for j in range(1,r+1):
            f=f*j
        sum=sum+f
        i=i//10
    if copy==sum:
        print(sum)