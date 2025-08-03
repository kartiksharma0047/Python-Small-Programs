# Print The Pattern
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
steps=5
for i in range(1,steps+1):
    for j in range(steps-i):
        print(" ",end="")
    for j in range(i):
        print("* ",end="")
    print()