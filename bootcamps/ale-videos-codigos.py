import cyberpi
import mbot2

def ultrasonido():
    distancia = cyberpi.ultrasonic2.get()
    return distancia

def the_rial_cambio_color (red, green, blue):
    cyberpi.led.on(red, green, blue, "all")  
   
def seguidor_de_lineas ():
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
def principal ():
    while (True):
        distancia = ultrasonido()
        if (distancia > 15):
            seguidor_de_lineas()
        elif (distancia < 15):
            if (distancia > 7.5):
                mbot2.drive_power(15, -15)
            elif (distancia < 7.5):
                mbot2.drive_power(0, 0)
               
               
               
   
   
   
   
    # while (True):
    #     distancia = ultrasonido()
    #     if (distancia > 30):
    #         seguidor_de_lineas()
    #     elif (distancia < 30):
    #         if (distancia > 15):
    #             mbot2.drive_power(15, -15)
    #         elif (distancia < 15):
    #             mbot2.drive_power(0, 0)
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    # while (True):
    #     distancia = ultrasonido()
    #     if(distancia < 15):
    #         if (distancia > 10):
    #             the_rial_cambio_color(200, 0, 0)
    #         if (distancia < 10):
    #             the_rial_cambio_color(0, 200, 0)
               
    #     if (distancia > 15):
    #         the_rial_cambio_color(0, 0, 200)  





import cyberpi
from cyberpi import mbot2

def ultrasonido():
    distancia = cyberpi.ultrasonic2.get()
    return distancia

def seguidor_de_lineas ():
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

@cyberpi.event.is_press("b")
def principal ():
    # PREVIO AL CICLO
    distancia = ultrasonido()
   
    # EL CICLO
    # distancia > 10 = TRUE, y por lo tanto se ejecutra
    while (distancia > 10):
        distancia = ultrasonido()
        cyberpi.console.println(distancia) # DEBUGGEO: imprimimos una variable, para ver como cambia en el tiempo y ver asi errores
        seguidor_de_lineas()
   
    # FUERA DE CICLO
     
    mbot2.drive_power(0, 0)
    cyberpi.console.println("termino")
