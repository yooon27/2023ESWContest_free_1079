#main
import robotState
import carControl
import tracking

state = "stop"
i=10

while True:
    if i == 10:
        state =  robotState.robotState()
        i = 0
    i += 1

    if state == "tracking":
        tracking.tracking()
        
    elif state == "stop":
        carControl.carState("stop")

    elif state == "forward":
        carControl.carState("forward")

    elif state == "left":
        carControl.carState("left")
    
    elif state == "right":
        carControl.carState("right")

