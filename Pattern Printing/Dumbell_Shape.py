# Print The Pattern
# 14 Columns and 6 Rows
#        *                   *
#      * *                   * *
#    * * * * * * * * * * * * * * *
#    * * * * * * * * * * * * * * *
#      * *                   * *
#        *                   *

def printChar(is_star):
    print("* " if is_star else "  ",end="")

# HardCoded Logic
# for row in range(Rows):
#     for col in range(Columns):
#         if row in [0,5]:
#             printChar(col in [2,11])
#         elif row in [1,4]:
#             printChar(col in [1,2,11,12])
#         elif row in [2,3]:
#             printChar(True)
#         else:
#             printChar(False)
#     print()

# Dynamic Logic
# Even Rows and Even Columns
Rows=10
Columns=30
mid=int(Rows/2)
mid_distance=int(Columns-Rows)
for row in range(1,Rows+1):
    if row>=0 and row<=mid:
        if row==mid:
            print("*"*(mid_distance+(mid*2)))
        else:
            print(" "*(mid-row)+"*"*row+" "*mid_distance+"*"*row)
    else:
        if row>mid and row==mid+1:
            print("*"*(mid_distance+(mid*2)))
        else:
            print(" "*(row-mid-1)+"*"*(Rows-row+1)+" "*mid_distance+"*"*(Rows-row+1))