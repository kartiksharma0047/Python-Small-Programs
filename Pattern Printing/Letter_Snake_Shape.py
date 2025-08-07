# Print The Pattern

# The Snake length should be dynamic
#   |- Snake Head

#   K A R
#       T
#   S K I
#   H
#   A R M
#       A

#       |- Snake Tail
 
name = input("Enter Name: ").replace(" ", "").upper()
Column = 3

Rows = 0
i = 0
while i < len(name):
    if Rows % 2 == 0:
        i += 3 
    else:
        i += 1 
    Rows += 1

def printLetter(Letter="", is_Letter=False):
    print(Letter + " " if is_Letter else "  ", end="")

index = 0
position_right = True

for row in range(Rows):
    for col in range(Column):
        if row % 2 == 0:
            if index < len(name):
                printLetter(name[index], True)
                index += 1
            else:
                printLetter()
        else:
            if (position_right and col == Column - 1) or (not position_right and col == 0):
                if index < len(name):
                    printLetter(name[index], True)
                    index += 1
                else:
                    printLetter()
            else:
                printLetter()
    print()
    if row % 2 != 0:
        position_right = not position_right
