from robot_control_class import RobotControl

rc = RobotControl()

a = rc.get_laser(360)

while a > 1:
    rc.move_straight()
    a = rc.get_laser(360)
    print ("Current distance to wall: {}".format(a))
rc.turn("clockwise",0.28,5.0)# This is an estimate time and velocity in which the robot will rotate 90 degrees
rc.stop_robot()

print ("Wall is at {} meters! Stop the robot!".format(a))