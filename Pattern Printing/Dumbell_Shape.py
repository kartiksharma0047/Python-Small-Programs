# Print The Pattern
# 14 Columns and 6 Rows
#        *                   *
#      * *                   * *
#    * * * * * * * * * * * * * * *
#    * * * * * * * * * * * * * * *
#      * *                   * *
#        *                   *
Rows=6
Columns=14

def printChar(is_star):
    print("* " if is_star else "  ",end="")

for row in range(Rows):
    for col in range(Columns):
        if row in [0,5]:
            printChar(col in [2,11])
        elif row in [1,4]:
            printChar(col in [1,2,11,12])
        elif row in [2,3]:
            printChar(True)
        else:
            printChar(False)
    print()