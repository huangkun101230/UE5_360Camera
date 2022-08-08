import cv2
import os
import numpy as np

rgb_folder = 'FinalColor'
depth_folder = 'SceneDepth'
video_name = 'video.avi'

rgb_images = [img for img in os.listdir(rgb_folder) if img.endswith(".png")]
depth_images = [img for img in os.listdir(depth_folder) if img.endswith(".png")]

rgb_frame = cv2.imread(os.path.join(rgb_folder, rgb_images[0]))
depth_frame = cv2.imread(os.path.join(depth_folder, depth_images[0]))

height, width, layers = rgb_frame.shape

print()

video = cv2.VideoWriter(video_name, 0, 1, (width*2,height))

for i in range(len(rgb_images)):
    rgb = cv2.imread(os.path.join(rgb_folder, rgb_images[i]))
    depth = cv2.imread(os.path.join(depth_folder, depth_images[i]))
    video.write(np.hstack((rgb, depth)))
    print(i, "th frame done")
# for image in rgb_images:
#     video.write(cv2.imread(os.path.join(rgb_folder, image)))

cv2.destroyAllWindows()
video.release()