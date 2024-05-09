import cyberpi
import time

velocidad_avanzar = 30

cyberpi.mbot2.drive_power(velocidad_avanzar, -velocidad_avanzar)
time.sleep(3)
cyberpi.mbot2.drive_power(0,0)