from threading import Thread
import time

class CountDownTask:
    def __init__(self):
        self.running = True

    def terminate(self):
        self.running = False

    def run(self, n):
        while self.running and n > 0:
            print("T-minus ", n)
            n -= 1
            time.sleep(1)

c = CountDownTask()
t = Thread(target=c.run, args=(10,))
t.start()

time.sleep(4)
c.terminate() #Signaliserer at threaden skal stoppe inn via method
t.join() # venter til thread har terminert (denne trengs ikke ved bruk av Daemon-threads
