import threading,time

def test1():
    time.sleep(5)
    print('5초지났다.')

def test2():
    for i in range(5):
        time.sleep(1)
        print("{0}second".format(i))

t1=threading.Thread(target=test1)
t2=threading.Thread(target=test2)

t1.start()
t2.start()