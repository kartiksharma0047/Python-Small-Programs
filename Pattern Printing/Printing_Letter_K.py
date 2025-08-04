# Print The Letter
# 7 Rows and 5 Columns
#  *    * 
#  *   * 
#  *  * 
#  * * 
#  *  * 
#  *   * 
#  *    * 
Rows=7
Columns=5

def printChar(is_Star):
    print("* " if is_Star else "  ",end="")

for row in range(Rows):
    for col in range(Columns):
        if row in [0,6]:
            printChar(col in [0,4])
        elif row in [1,5]:
            printChar(col in [0,3])
        elif row in [2,4]:
            printChar(col in [0,2])
        else:
            printChar(col in [0,1])
    print()