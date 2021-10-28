def largest(a):
    n=len(a)
    max=a[0]
    for i in range(1,n):
        if a[i]>max:
            max=a[i]
    return max
def smallest(a):
    n=len(a)
    min=a[0]
    for i in range(1,n):
        if a[i]<min:
            min=a[i]
    return min
b=[1,5,9,96,78,90,45,63,87,98,64,98]
j=largest(b)   
h=smallest(b)
print(j)
print(h)               
