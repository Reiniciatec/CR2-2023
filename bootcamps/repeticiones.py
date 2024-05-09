import cyberpi
from cyberpi import mbot2

@cyberpi.event.is_press("up")
def repetimos ():
    repetir = 10
    while(repetir != 0):
        cyberpi.console.println(repetir)
        repetir = repetir - 1
        
        
