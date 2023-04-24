import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d


class PointCloudVisualization:
    def __init__(self):
        self.title = "Point Cloud Visualization"
        self.width = 1200
        self.height = 900

    def rgb_to_pointcloud(self, color_image_path=str(), depth_image_path=str()):
        # Load the color and depth images
        color_raw = o3d.io.read_image(color_image_path)
        depth_raw = o3d.io.read_image(depth_image_path)

        # Create an RGBD image from the color and depth images
        rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw,
                                                                        convert_rgb_to_intensity=False)

        # Create a pinhole camera intrinsic object with default settings
        pinhole_camera_intrinsic = o3d.camera.PinholeCameraIntrinsic(
            o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault)

        # Create an Open3D point cloud object from the RGBD image and pinhole camera intrinsic
        return o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, pinhole_camera_intrinsic)

    def display_o3d(self, pcd_o3d):
        # Create an Open3D visualizer object
        visualizer = o3d.visualization.Visualizer()

        # Set the size of the visualization window
        visualizer.create_window(width=self.width, height=self.height, window_name=self.title)

        # Add the point cloud geometry to the visualizer
        visualizer.add_geometry(pcd_o3d)

        # Run the visualizer
        visualizer.run()

    def display_mpl(self, pcd_np):
        # Create a new matplotlib figure
        fig = plt.figure()

        # Create a 3D subplot for the point cloud visualization
        ax = fig.add_subplot(111, projection='3d')

        # Plot the point cloud using matplotlib
        ax.scatter(pcd_np[:, 0], pcd_np[:, 1], pcd_np[:, 2])

        # Set the labels for the X, Y, and Z axes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Set the title of the plot
        ax.set_title(self.title)

        # Show the plot
        plt.show()

    def numpy_open3d(self, number_of_points=5, output=str("numpy")):
        # Generate a random 3D numpy array of shape (number_points, 3)
        pcd_rand = np.random.rand(number_of_points, 3)

        # Convert the numpy array to an Open3D point cloud object
        pcd_o3d = o3d.geometry.PointCloud()
        pcd_o3d.points = o3d.utility.Vector3dVector(pcd_rand)

        # Return either the Open3D point cloud object or the numpy array based on the output parameter
        if output == "point_cloud":
            return pcd_o3d
        else:
            return pcd_rand

    def run(self):
        # Create point cloud from random generated 3D numpy array
        pcd_rand = self.numpy_open3d(number_of_points=5, output="numpy")

        # Create a 3D plot with matplotlib
        self.display_mpl(pcd_rand)

        # Uniform Sampling
        # Load the bunny mesh
        bunny = o3d.data.BunnyMesh()
        mesh = o3d.io.read_triangle_mesh(bunny.path)

        # Compute vertex normals for the mesh
        mesh.compute_vertex_normals()

        # Sample 2000 points uniformly from the mesh
        pcd_unisamp = mesh.sample_points_uniformly(number_of_points=2000)

        # Save the point cloud as a ply file
        o3d.io.write_point_cloud("bunny_pcd.ply", pcd_unisamp)

        # Visualize the original mesh and the uniformly sampled point cloud
        self.title = "Uniform Sampling Input"
        self.display_o3d(mesh)
        self.title = "Uniform Sampling Output"
        self.display_o3d(pcd_unisamp)
        self.title = "Point Cloud Visualization"

        # RGBD to Point Cloud
        color_image = "im1.jpg"
        depth_image = "disp1.jpg"

        # Create RGBD image from color and depth images
        pcd_rgbd = self.rgb_to_pointcloud(color_image, depth_image)

        # Visualize the point cloud generated from RGBD image
        self.title = "RGBD to Point Cloud"
        self.display_o3d(pcd_rgbd)
        self.title = "Point Cloud Visualization"

        # Numpy and Open3D
        # Generate a random 3D numpy array of shape (2000, 3)
        pcd_numpy = self.numpy_open3d(number_of_points=2000, output="point_cloud")

        # Visualize the point cloud generated from numpy array using Open3D
        self.title = "Point Cloud from Random 3D Array"
        self.display_o3d(pcd_numpy)
        self.title = "Point Cloud Visualization"

        # Read the bunny point cloud file
        pcd_o3d = o3d.io.read_point_cloud("bunny_pcd.ply")

        # Convert the open3d object to numpy array
        pcd_np = np.asarray(pcd_o3d.points)

        # Display the bunny point cloud using matplotlib
        self.title = "Bunny Point Cloud"
        self.display_mpl(pcd_np)


if __name__ == '__main__':
    pcd = PointCloudVisualization()
    pcd.run()
    

