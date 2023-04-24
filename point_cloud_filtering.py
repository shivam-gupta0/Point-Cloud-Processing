import open3d as o3d
import numpy as np


class Pcfiltering():
    def __init__(self):
        self.title = "Point Cloud Filtering"
        self.pcd_path = "depth_2_pcd.ply"

    def pointcloud_sampling(self):
        # Read point cloud:
        pcd = o3d.io.read_point_cloud(self.pcd_path)

        # Random down-sampling:
        random_pcd = pcd.random_down_sample(sampling_ratio=0.005)

        # Uniform down-sampling:
        uniform_pcd = pcd.uniform_down_sample(every_k_points=200)

        # Voxel down-sampling:
        voxel_pcd = pcd.voxel_down_sample(voxel_size=0.4)

        # Translating point clouds:
        points = np.asarray(random_pcd.points)
        points += [-3, 3, 0]
        random_pcd.points = o3d.utility.Vector3dVector(points)

        points = np.asarray(uniform_pcd.points)
        points += [0, 3, 0]
        uniform_pcd.points = o3d.utility.Vector3dVector(points)

        points = np.asarray(voxel_pcd.points)
        points += [3, 3, 0]
        voxel_pcd.points = o3d.utility.Vector3dVector(points)

        # Display:
        o3d.visualization.draw_geometries([pcd, random_pcd, uniform_pcd, voxel_pcd])

    def outlier_removal(self):

        # Read point cloud:
        pcd = o3d.io.read_point_cloud(self.pcd_path)
        # Down sampling to reduce the running time:
        pcd = pcd.voxel_down_sample(voxel_size=0.02)

        # Radius outlier removal:
        pcd_rad, ind_rad = pcd.remove_radius_outlier(nb_points=16, radius=0.05)
        outlier_rad_pcd = pcd.select_by_index(ind_rad, invert=True)
        outlier_rad_pcd.paint_uniform_color([1., 0., 1.])

        # Statistical outlier removal:
        pcd_stat, ind_stat = pcd.remove_statistical_outlier(nb_neighbors=20,
                                                     std_ratio=2.0)
        outlier_stat_pcd = pcd.select_by_index(ind_stat, invert=True)
        outlier_stat_pcd.paint_uniform_color([0., 0., 1.])

        # Translate to visualize:
        points = np.asarray(pcd_stat.points)
        points += [3, 0, 0]
        pcd_stat.points = o3d.utility.Vector3dVector(points)

        points = np.asarray(outlier_stat_pcd.points)
        points += [3, 0, 0]
        outlier_stat_pcd.points = o3d.utility.Vector3dVector(points)

        # Display:
        o3d.visualization.draw_geometries([pcd_stat, pcd_rad, outlier_stat_pcd, outlier_rad_pcd])


if __name__ == '__main__':
    pc_sampling = Pcfiltering()
    pc_sampling.pointcloud_sampling()
    pc_sampling.outlier_removal()


