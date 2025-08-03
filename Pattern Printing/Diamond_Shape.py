# Print the Pattern
#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *
steps=5
for i in range(1,steps):
    print(" "*(steps-i)+"* "*i)
for i in range(steps-2,0,-1):
    print(" "*(steps-i-1),"* "*i)