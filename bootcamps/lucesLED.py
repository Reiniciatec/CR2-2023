import cyberpi
import mbot2


rojo = 180
verde = 120
azul = 3

def cambio_color (red, green, blue):
    cyberpi.led.on(red, green, blue, "all")
    
    def cambio_color (red, green, blue):
    cyberpi.led.on(red, green, blue, "all")
    
@cyberpi.event.is_press("a")
def color_ejecutar():
    cambio_color(100, 255, 0) 
    akdas()
    
    
    
    
    
    
    
@cyberpi.event.is_press("up")
def color_rojo():
    cyberpi.led.on(rojo, verde, azul, "all")

@cyberpi.event.is_press("down")
def animacion_arcoiris():
    cyberpi.led.play("rainbow")
