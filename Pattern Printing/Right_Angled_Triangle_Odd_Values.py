# Print The Pattern
# *
# ***
# *****

for i in range(1,6):
    if i%2!=0:
        for j in range(i):
            print("*",end="")
    else:
        continue
    print()