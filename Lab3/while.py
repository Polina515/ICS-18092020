a=[34,78,350]
## yes - всі числа парні
## no - є непарні
while len(a)>0:
    last=a.pop()
    if last%2!=0:
        print('No')
        break
else:
    print('yes')
    
