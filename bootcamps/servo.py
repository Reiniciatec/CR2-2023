import cyberpi
import mbot2

velocidadM1 = 20
velocidadM2 = -20

@cyberpi.event.is_press("up")
def motores ():
    cyberpi.mbot2.drive_power(velocidadM1, velocidadM2)

@cyberpi.event.is_press("down")
def servo_abra ():
    cyberpi.mbot2.servo_set(90, 1)
    
@cyberpi.event.is_press("b")
def servo_cierre ():
    cyberpi.mbot2.servo_set(120, 1)
     


