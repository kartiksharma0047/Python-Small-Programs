# Print The Pattern
# 7 rows and 5 Columns
#    * * * *
#    *       *
#    *       *
#    * * * *
#    *       *
#    *       *
#    * * * *
Rows=7
Columns=5
def returnChar(is_star):
    print(" *" if is_star else "  ",end="")

for row in range(Rows):
    for col in range(Columns):
        if row in [0,3,6]:
            returnChar(col!=4)
        else:
            returnChar(col in [0,4])
    print()
        