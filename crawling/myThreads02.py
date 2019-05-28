import threading, time
 
class thrSum (threading.Thread):
    def __init__(self, trMin, trMax):
         threading.Thread.__init__(self)
         self.trMin = trMin
         self.trMax = trMax
    
    def run(self):
        total = 0
        for i in range(self.trMin, self.trMax):
            total += i
            time.sleep(1)
            print("Subthread", total)
 
t = thrSum(1, 10)
#t.daemon = True
t.start()
 
print("Main Thread")

