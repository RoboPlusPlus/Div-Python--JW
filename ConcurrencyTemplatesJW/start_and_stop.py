import time

#Code to execute in independent thread
def countdown(n):
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(1)

#create and launch a thread
from threading import Thread
t = Thread(target=countdown, args=(10,)) # Derssom Daemon = True er satt, så vil funksjonen bare kjøre en gang. Siden main thread er ferdig.
t.start()

