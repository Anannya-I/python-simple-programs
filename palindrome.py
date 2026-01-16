"""s=input("Enter a string: ")
r = ""
i = len(s)-1
while i>=0:
    r =r+s[i]
    i-=1
if s==r:
    print("palindrome")
else:
    print(" not palindrome")"""

#OR

s=input("Enter a string: ")
r = s[::-1]
print("reverse of string is",r)
if s==r:
    print("palindrome")
else:
    print(" not palindrome")


