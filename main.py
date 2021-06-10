## License: Apache 2.0. See LICENSE file in root directory.
## Copyright(c) 2015-2017 Intel Corporation. All Rights Reserved.

#####################################################
## librealsense tutorial #1 - Accessing depth data ##
#####################################################

# First import the library
import pyrealsense2 as rs
import numpy as np
import cv2

try:
    # Create a context object. This object owns the handles to all connected realsense devices
    pipeline = rs.pipeline()

    # Configure streams
    config = rs.config()
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

    # Start streaming
    pipeline.start(config)



    # depth_to_disparity = rs.disparity_transform(True)
    # disparity_to_depth = rs.disparity_transform(False)
    # dec_filter = rs.decimation_filter()
    # temp_filter = rs.temporal_filter()
    # spat_filter = rs.spatial_filter()

    while True:
        # This call waits until a new coherent set of frames is available on a device
        # Calls to get_frame_data(...) and get_frame_timestamp(...) on a device will return stable values until wait_for_frames(...) is called
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        if not depth_frame: continue



        # depth_frame = depth_to_disparity.process(depth_frame)
        # depth_frame = dec_filter.process(depth_frame)
        # depth_frame = temp_filter.process(depth_frame)
        # depth_frame = spat_filter.process(depth_frame)
        # depth_frame = disparity_to_depth.process(depth_frame)
        # depth_frame = depth_frame.as_depth_frame()


        depth_data = depth_frame.as_frame().get_data()
        rgb_data = color_frame.as_frame().get_data()

        rgb_image = np.asanyarray(rgb_data)
        depth_image = np.asanyarray(depth_data)
        depth_image = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)


        cv2.imshow('RGB', rgb_image)
        cv2.imshow('depth', depth_image)


        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    exit(0)
except Exception as e:
    print(e)
    pass