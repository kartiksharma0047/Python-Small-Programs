# Here in this program based on the time a message is printed
import time
if(time.strftime("%H") < "12" and time.strftime("%H") > "0"):
    print("Good Morning")
elif(time.strftime("%H") < "18" and time.strftime("%H") > "12"):
    print("Good Afternoon")
else:
    print("Good Evening")
