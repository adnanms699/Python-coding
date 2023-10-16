n=int(input("Enter the value of n"))
s=0
for i in range(1,n+1):
    a=(i**i)/i
    s=s+a
print("sum of series of n is:",s)