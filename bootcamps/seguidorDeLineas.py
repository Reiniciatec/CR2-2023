import cyberpi
from cyberpi import mbot2


@cyberpi.event.is_press("b")
def seguir ():
    #si ambos sensores ven la linea
    if cyberpi.quad_rgb_sensor.is_line("L1", 1) == True and cyberpi.quad_rgb_sensor.is_line("R1", 1) == True:
        mbot2.drive_power(30, -30)
           
    #si el izquierdo ve la linea y el derecho no
    if cyberpi.quad_rgb_sensor.is_line("L1", 1) == True and cyberpi.quad_rgb_sensor.is_line("R1", 1) == False:
        mbot2.drive_power(0, -60)
           
    #si el izquierdo no ve la linea y el derecho si
    if cyberpi.quad_rgb_sensor.is_line("L1", 1) == False and cyberpi.quad_rgb_sensor.is_line("R1", 1) == True:
        mbot2.drive_power(60, 0)
           
    #si ni el izquierdo ni el derecho ve la linea
    if cyberpi.quad_rgb_sensor.is_line("L1", 1) == False and cyberpi.quad_rgb_sensor.is_line("R1", 1) == False:
        mbot2.drive_power(0, 0)
        

@cyberpi.event.is_press("a")
def reconoceraaa ():
        mbot2.drive_power(0, -50)
           
@cyberpi.event.is_press("up")
def reconocer ():
    while (True):
        #si ambos sensores ven la linea
        if cyberpi.quad_rgb_sensor.is_line("L1", 1) == True and cyberpi.quad_rgb_sensor.is_line("R1", 1) == True:
            mbot2.drive_power(30, -30)
           
        #si el izquierdo ve la linea y el derecho no
        if cyberpi.quad_rgb_sensor.is_line("L1", 1) == True and cyberpi.quad_rgb_sensor.is_line("R1", 1) == False:
            mbot2.drive_power(0, -60)
           
        #si el izquierdo no ve la linea y el derecho si
        if cyberpi.quad_rgb_sensor.is_line("L1", 1) == False and cyberpi.quad_rgb_sensor.is_line("R1", 1) == True:
            mbot2.drive_power(60, 0)
           
        #si ni el izquierdo ni el derecho ve la linea
        if cyberpi.quad_rgb_sensor.is_line("L1", 1) == False and cyberpi.quad_rgb_sensor.is_line("R1", 1) == False:
            mbot2.drive_power(0, 0)
            break
    
###########################################################################

import cyberpi
from cyberpi import mbot2

@cyberpi.event.is_press("down")
def reconocer_V2 ():
    while (True):
        # L1 Es TRUE si se esta viendo, caso contrario es FALSE
        L1 = cyberpi.quad_rgb_sensor.is_line("L1", 1)
        
        # R1 Es TRUE si se esta viendo, caso contrario es FALSE
        R1 = cyberpi.quad_rgb_sensor.is_line("R1", 1)
        
        #si ambos sensores ven la linea
        if L1 and R1: # L1 TRUE and R1 TRUE
            mbot2.drive_power(50, 50)
           
        #si el izquierdo ve la linea y el derecho no
        if L1 and R1: #L1 TRUE and R1 FALSE
            mbot2.drive_power(50, 25)
           
        #si el izquierdo no ve la linea y el derecho si
        if L1 and R1: # L1 FALSE and R1 TRUE
            mbot2.drive_power(25, 50)
           
        #si ni el izquierdo ni el derecho ve la linea
        if L1 and R1: # L1 FALSE and R1 FALSE
            mbot2.drive_power(0, 0)
