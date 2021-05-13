n = int(input("Enter the number"))

if n > 1:
    for i in range(2,n):
        if (n % i) == 0:
            print(n,"Number is not prime number")
            break
    else:
        print(n,"Number is prime")
else:
    print(n,"is not a prime ")
