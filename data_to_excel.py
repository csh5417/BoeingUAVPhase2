import csv
import numpy as np
import pyrealsense2 as rs

def take_ss():
    pipe = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

    pipe.start(config)

    frames = pipe.wait_for_frames()
    depth_frame = frames.get_depth_frame()

    pipe.stop()

    return depth_frame

def to_csv(depth_frame, csv_filename='depth_data.csv'):
    depth_image = np.asanyarray(depth_frame.get_data())

    with open(csv_filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(depth_image)

    print(f"Depth data saved to {csv_filename}")

if __name__ == "__main__":
    depth_frame = take_ss()
    if depth_frame:
        print("Depth snapshot captured successfully.")
    else:
        print("Failed to capture depth snapshot.")
        
    to_csv(depth_frame)