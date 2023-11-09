# Codeby @1ssb
# sudo pip install keyboard
# To run: sudo python3 this_file.py

import open3d as o3d
import os
import keyboard

def load_point_clouds(directory):
    filenames = sorted([f for f in os.listdir(directory) if f.endswith('.ply') and f.startswith('cloud_')])
    return [os.path.join(directory, filename) for filename in filenames]

def display_point_cloud(file_path):
    pcd = o3d.io.read_point_cloud(file_path)
    coord_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=15.0, origin=[0, 0, 0])

    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(pcd)
    vis.add_geometry(coord_frame)

    print("\nNext input (n, p, q): ", end='', flush=True)
    while True:
        vis.poll_events()
        vis.update_renderer()
        if keyboard.is_pressed('n'):  # Press 'n' to go to the next point cloud
            break
        if keyboard.is_pressed('p'):  # Press 'p' to go to the previous point cloud
            vis.destroy_window()
            return -1
        if keyboard.is_pressed('q'):  # Press 'q' to quit
            vis.destroy_window()
            print("\nQuitting...")
            exit()

    vis.destroy_window()
    return 1

def main():
    directory = "./Point_Clouds-2/"
    point_cloud_filepaths = load_point_clouds(directory)
    total_point_clouds = len(point_cloud_filepaths)
    print(f"Total number of point clouds: {total_point_clouds}")
    print("Instructions: Press 'n' for next, 'p' for previous, 'q' to quit.")
    print("Key: x-axis: Red, y-axis: Green and z-axis: Blue.")
    
    current_index = 0

    while 0 <= current_index < total_point_clouds:
        print(f"Displaying: {point_cloud_filepaths[current_index]}")
        step = display_point_cloud(point_cloud_filepaths[current_index])
        current_index += step

        if current_index >= total_point_clouds:
            print("Reached the end of the point cloud list.")
            break
        
        elif current_index < 0:
            print("No frames before this. Quiting...")
            break

if __name__ == '__main__':
    main()
