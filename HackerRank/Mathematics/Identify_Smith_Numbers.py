def SumOfDigits(n):
    return n if n<10 else n%10+SumOfDigits(n//10)
def isSmith(n):
    Digits=SumOfDigits(n)
    Factors,i=0,2
    while i*i<=n:
        if n%i:i+=1
        else:
            n//=i
            Factors+=SumOfDigits(i)
    return int(Digits==Factors+SumOfDigits(n))
n=int(input())
print(isSmith(n) if n>1 else 0)
