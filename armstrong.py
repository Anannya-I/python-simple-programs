n=int(input("enter a number:"))
c=n
s,d=0,0
while(c>0):
    c=c//10
    d+=1
c=n
while(c>0):
    r=c%10
    s=s+(r**d)
    c=c//10
if n==s:
    print("armstrong")
else:
    print("not armstrong")