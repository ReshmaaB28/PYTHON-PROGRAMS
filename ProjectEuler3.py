def primefactors(x):
    prime_factors=[]
    divisor=2
    while divisor<=x:
        if(x%divisor==0):
            prime_factors.append(divisor)
            x=x/divisor
        else:
            divisor+=1
    print(prime_factors)
x=int(input("Enter number : "))
primefactors(x)

