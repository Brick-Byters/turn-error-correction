from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def turn(db, hub, angle, tolerance=1):
    expected_heading = hub.imu.heading() + angle
    heading_delta = angle

    while abs(heading_delta) > tolerance:
        db.turn(heading_delta)
        heading_delta = expected_heading - hub.imu.heading()


hub = PrimeHub()

left =  Motor(Port.B,Direction.CLOCKWISE)
right = Motor(Port.A,Direction.COUNTERCLOCKWISE)
db = DriveBase(left, right,56,90)

hub.imu.reset_heading(0)

print("\n\nSTART")

turn(db, hub, 90)
turn(db, hub, 45)
turn(db, hub, -45)
turn(db, hub, -90)

print("STOP")