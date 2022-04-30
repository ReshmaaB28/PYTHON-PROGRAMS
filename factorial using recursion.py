def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)
n=eval(input("Enter a positive number : "))
print("Factorial of",n,"is",fact(n))
