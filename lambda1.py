x=lambda a:a*10
print("sum is :",x(2))

#example 2 multiline  lambda function
x=lambda a,b:(a*b)/(a+b)
print(x)
print("result:",x(2,3))

#example 3
def table(n):
    return lambda a:a*n
n=int(input("enter a number:"))
b=table(n)
for i in range(1,11):
    print(n,"X",i,"=",b(i))