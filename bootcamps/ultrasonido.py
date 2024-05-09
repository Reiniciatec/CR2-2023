import cyberpi
import mbot2

@cyberpi.event.is_press("a")
def ultrasonido():
    distancia = cyberpi.ultrasonic2.get()
    cyberpi.console.println(distancia)
    
###########################################################################

velocidad_avanzar = 30

@cyberpi.event.is_press("b")
def ultrasonido_V2():
    while True:
        distancia = cyberpi.ultrasonic2.get()
        if (distancia > 10):
            cyberpi.mbot2.drive_power(velocidad_avanzar, -velocidad_avanzar)
        elif (distancia <= 10):
            cyberpi.mbot2.drive_power(0,0)
        cyberpi.console.println(distancia)   
        
        
hambre = True # Verdadero

if hambre: 
    # AUTO ALIMENTANCION
# NO comer nada :c
