def facto(nb):
    f=1
    for i in range(1,nb+1):
        f  *= i
    return f

def factoR(n):
    if n==1:
        return 1 
    else:
        return n*factoR(n-1)

print(facto(5))
print(factoR(5))