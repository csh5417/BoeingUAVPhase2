from pymavlink import mavutil
import time

the_connection = mavutil.mavlink_connection('/dev/ttyTHS1', 115200)
the_connection.mav.send(the_connection.mav.command_long_encode(
    the_connection.target_system, 
    the_connection.target_component, 
    mavutil.mavlink.MAV_CMD_DO_SET_SERVO, 0, 9,
1500, 0, 0, 0, 0, 0
))


time.sleep(2)
print("Motor Activate")
the_connection.mav.send(the_connection.mav.command_long_encode(
    the_connection.target_system, 
    the_connection.target_component, 
    mavutil.mavlink.MAV_CMD_DO_SET_SERVO, 0, 9,
1100, 0, 0, 0, 0, 0
))
print("Done")
