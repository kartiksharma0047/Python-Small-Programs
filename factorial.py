def fact(args):
    if (args==0 or args==1):
        return 1
    else:
        return args * fact(args-1)
num=int(input("Enter a number: "))
print (f"Factorial of {num} is: {fact(num)}")
