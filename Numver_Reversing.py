# Here the question is we have to reverse a number without type conversion and using shortcut methods
# Example :- 123456
# Output :- 654321

input_num=input("Enter a Number: ")
digit=len(input_num)

try:
    num=int(input_num)
    temp=0
    for i in range(digit):
        temp_num=(int(num%(10**(i+1))/10**i))*10**(digit-i-1)
        temp+=temp_num
    print(temp)
except:
    print("Please Provide Integer Value")