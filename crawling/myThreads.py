import threading, time
 
def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
        time.sleep(1)
    print("Subthread", total)
 
t = threading.Thread(target=sum, args=(1, 10))
t.start()
 
print("Main Thread")

