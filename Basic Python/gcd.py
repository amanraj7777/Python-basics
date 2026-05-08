m = int(input("enter 1st Number : "))
n = int(input("enter 2nd Number : "))

def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if m % i == 0 and n % i ==0 :
            s = i
    print(s)
gcd(m,n)