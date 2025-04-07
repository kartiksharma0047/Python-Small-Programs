def fib(num):
    if num <= 0:
        return
    elif num == 1:
        print(0)
    elif num == 2:
        print(0, 1, sep=" ")
    else:
        a, b = 0, 1
        print(a, b, end=" ")
        for _ in range(2, num):
            c = a + b
            print(c, end=" ")
            a, b = b, c
        print()

num = int(input("Enter the number of terms: "))
if num <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series of", num, "terms:")
    fib(num)
