import cyberpi
from cyberpi import mbot2

rojo = 20
verde = 100
azul = 30

angle = 90
angle2 = 120
port = 1

@cyberpi.event.is_press("a")
def cambiar_color():
    cyberpi.mbot2.servo_set(angle, port)
    
@cyberpi.event.is_press("b")
def cambiar_color_2():
    cyberpi.mbot2.servo_set(angle2, port)

@cyberpi.event.is_press("right")
def cambiar_color_6():
    cyberpi.led.on(200, 10, 70, "all")
    
@cyberpi.event.is_press("down")
def cambiar_color_4():
    cyberpi.led.play("rainbow")
    

"""
@cyberpi.event.is_press("b")
def cambiar_color_2():
    cyberpi.led.move(1)
    
@cyberpi.event.is_press("up")
def cambiar_color_3():
    cyberpi.led.off("all")
    
@cyberpi.event.is_press("down")
def cambiar_color_4():
    cyberpi.led.play("rainbow")

@cyberpi.event.is_press("left")
def cambiar_color_5():
    cyberpi.led.on(200,80,0, 1)
    cyberpi.led.on(30,200,2, 2)
    cyberpi.led.on(1,50,70, 3)
    cyberpi.led.on(200,2,31, 4)
    cyberpi.led.on(60,1,54, 5)

    
@cyberpi.event.is_press("right")
def cambiar_color_6():
    cyberpi.led.on(200, 10, 70, "all")

cyberpi.led.play(name = "rainbow")

rainbow

spoondrift

meteor_blue

meteor_green

flash_red

flash_orange

firefly

cyberpi.led.off(id = "all")

led.move(step = 1)

"""

    
    
    