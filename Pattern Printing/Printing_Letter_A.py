# Print The Pattern
# 5 Columns and 7 rows
#     * * *  
#   *       *
#   *       *
#   * * * * *
#   *       *
#   *       *
#   *       *
Columns=5
Rows=7
for row in range(Rows):
    for col in range(Columns):
        if row==0 and (col==0 or col==4):
            print("  ",end="")
        elif row==3:
            print("* ",end="")
        else:
            if row!=0 and (col==1 or col==2 or col==3):
                print("  ",end="")
            else:
                print("* ",end="")
    print()
            