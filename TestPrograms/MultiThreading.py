import threading
import time

def func(sec):
    print(f"Part completed in {sec}s")
    time.sleep(sec)

# Time is recorded for start time 
time1=time.perf_counter()

t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[2])
t3=threading.Thread(target=func,args=[1])

# Threads Started
t1.start()
t2.start()
t3.start()

# Threads Ended
t1.join()
t2.join()
t3.join()

# Time is recorded for end time
time2=time.perf_counter()
print(time2-time1)
