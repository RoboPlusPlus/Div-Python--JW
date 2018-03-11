# main.py -- put your code here!
import pyb
accel = pyb.Accel()
LedX = pyb.LED(1)
LedY = pyb.LED(2)
LedZ = pyb.LED(3)
sample_timeMS = 200

def init():
   
    for i in range(5):
        LedX.on()
        LedY.on()
        LedZ.on()
        pyb.delay(100)
        LedX.off()
        LedY.off()
        LedZ.off()
        pyb.delay(100)
        LedX.on()
        LedY.on()
        LedZ.on()
        pyb.delay(100)
        LedX.off()
        #LedY.off()
        LedZ.off()
        pyb.delay(100)
        LedX.on()
        LedY.on()
        LedZ.on()
        pyb.delay(100)
        LedX.off()
        LedY.off()
        #LedZ.off()
        pyb.delay(100)

def run():
    t=0
    while t<100:
        print(accel.x(), accel.y(), accel.z())
        LedX.intensity(accel.x())
        LedY.intensity(accel.y())
        LedZ.intensity(accel.z())
        pyb.delay(100)
        t+=1
init()
run()


    
