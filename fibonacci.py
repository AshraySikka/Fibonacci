x=int(input("Enter the number of terms you want of the series: "))
a=0
b=1
for i in range (x):
    print(a)
    c=a+b
    a=b
    b=c
