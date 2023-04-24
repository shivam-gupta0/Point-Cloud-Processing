# Point-Cloud-Processing

**1. Point-cloud-Visualization**

point_cloud_visualization.py is a Python script for visualizing point clouds using Open3D and Matplotlib libraries. The script has a PointCloudVisualization class with methods for generating and displaying point clouds. The numpy_open3d method generates a random 3D numpy array and converts it into an Open3D point cloud object. The rgb_to_pointcloud method takes in a color and depth image and generates an Open3D point cloud object. The display_o3d method displays an Open3D point cloud object using the Open3D visualization window. The display_mpl method displays a numpy array point cloud using a Matplotlib 3D subplot. The run method calls the above methods to create and display point clouds generated from different sources such as uniform sampling from a mesh, RGBD images, and random 3D numpy arrays.
![matlab_vis](https://user-images.githubusercontent.com/85798077/234074025-d48b5a83-99d5-489e-b5dd-b39458b7f032.png)
![bunny_matplot](https://user-images.githubusercontent.com/85798077/234074057-093feca4-f26a-472b-9fa3-5d261243bdd0.png)


https://user-images.githubusercontent.com/85798077/234074068-8391188a-7c70-4790-bc99-2a353234fc69.mp4



https://user-images.githubusercontent.com/85798077/234074084-c640d525-062a-42e0-8327-dd6506036c3c.mp4

