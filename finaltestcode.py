import pyrealsense2 as rs
import numpy as np
from pymavlink import mavutil
import time
import os
import subprocess

pipe = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

subprocess.run(['sudo', 'python3', 'pythonMotorTurnFinalInitialize.py'])

pipe.start(config)
count = 0
try:
	while True:
		frames = pipe.wait_for_frames()
		depth_frame = frames.get_depth_frame()

		if not depth_frame:
			continue

		depth_image = np.asanyarray(depth_frame.get_data())

		height, width = depth_image.shape
		center_x, center_y = width//2, height//2
		depth = depth_image[center_y, center_x]

		depth_meters = depth/1000.0
		print(f'Distance to center object is: {depth_meters}m')
		if (depth_meters < 2):
			count += 1
		if (depth_meters > 2):
			count = 0
		if (depth_meters < 2 and count > 15 ):
			print('WARNING: Object closing in')
			subprocess.run(['sudo', 'python3', 'pythonMotorTurnFinal.py'])

except KeyboardInterrupt:
	pass
finally:
	pipe.stop()
