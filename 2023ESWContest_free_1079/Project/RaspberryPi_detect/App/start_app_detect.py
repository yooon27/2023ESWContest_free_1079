#main
import robotState
import brushServo

box = False
brush = False
i=10

while True:
    state =  robotState.robotState()
    box =robotState.boxState()
    brush = robotState.brushState()
    print(brush)
    print(box)
    brushServo.servoMotor(box)
    brushServo.brushMotor(brush)

