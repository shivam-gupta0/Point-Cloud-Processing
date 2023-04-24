# Depth Image Processing and Point Cloud Analysis

This repository contains Python scripts for processing depth images and analyzing point clouds. The scripts use various libraries, including OpenCV, NumPy, Matplotlib, and Open3D.

# Prerequisites
Python 3.6 or higher

numpy

open3d

scikit-learn

matplotlib



# Files
The repository contains the following files:

**point_cloud_visualization.py:** This is a Python script for visualizing point clouds using Open3D and Matplotlib libraries. The script has a PointCloudVisualization class with methods for generating and displaying point clouds. The numpy_open3d method generates a random 3D numpy array and converts it into an Open3D point cloud object. The rgb_to_pointcloud method takes in a color and depth image and generates an Open3D point cloud object. The display_o3d method displays an Open3D point cloud object using the Open3D visualization window. The display_mpl method displays a numpy array point cloud using a Matplotlib 3D subplot. The run method calls the above methods to create and display point clouds generated from different sources such as uniform sampling from a mesh, RGBD images, and random 3D numpy arrays.
![matlab_vis](https://user-images.githubusercontent.com/85798077/234074025-d48b5a83-99d5-489e-b5dd-b39458b7f032.png)
![bunny_matplot](https://user-images.githubusercontent.com/85798077/234074057-093feca4-f26a-472b-9fa3-5d261243bdd0.png)


https://user-images.githubusercontent.com/85798077/234074068-8391188a-7c70-4790-bc99-2a353234fc69.mp4



https://user-images.githubusercontent.com/85798077/234074084-c640d525-062a-42e0-8327-dd6506036c3c.mp4


**point_cloud_filtering.py:**
This is a Python script that demonstrates point cloud filtering using the Open3D library. The script defines a class called Pcfiltering that has two methods: pointcloud_sampling and outlier_removal.

The pointcloud_sampling method reads a point cloud from a PLY file, and then demonstrates three types of point cloud downsampling: random down-sampling, uniform down-sampling, and voxel down-sampling. The method then translates each down-sampled point cloud to a different location, and displays all four point clouds using Open3D's visualization functionality.

The outlier_removal method reads a point cloud from a PLY file, and applies two types of outlier removal: radius outlier removal and statistical outlier removal. The method then translates each outlier-removed point cloud to a different location, and displays all four point clouds using Open3D's visualization functionality.




**ground_detection.py:** This script reads a depth image and performs ground detection using a threshold. It then sets the ground pixels to green and displays the result.

The script first defines camera parameters for a depth image. It then reads the depth image and computes a grayscale image from it. The grayscale image is converted to a 3-channel image and the height and width of the depth image are extracted. The script then computes the indices for the image and reshapes them to have the same shape as the depth image. It computes constants using the camera parameters and computes an organized point cloud from the indices and depth values.

The script then sets a threshold for ground detection and finds the maximum y-value in the organized point cloud. It then iterates over the organized point cloud and sets the depth image pixel to green if the y-value is above the threshold.

Finally, the script displays the depth image with the ground pixels set to green.


![Ground_Detection](https://user-images.githubusercontent.com/85798077/234078206-755ecb78-4828-47a0-9a3e-0a3b9e26f39b.png)

**point_cloud_segmentation.py:** This script reads a downsampled point cloud from a PLY file and performs clustering on the points using the DBSCAN algorithm. The resulting clusters are then visualized using different colors. 


# Usage

To run the scripts, you need to install the required libraries first. You can use pip to install them:


pip install imageio numpy matplotlib open3d scikit-learn


The scripts use some input files that are included in the repository. You can modify the files or use your own files instead.
