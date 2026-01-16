list = [5,4,67,2,[6,7,12],1]
alias=list[:] #cloning

alias[2]=29
print(alias)

alias=list[:] #clonin
alias.insert(3,8)
print(alias)

alias=list[:] #clonin
alias.pop(1)
print(alias)
print(list)