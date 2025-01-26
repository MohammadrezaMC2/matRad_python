import numpy as np
from Geometry import CubeIndex2WorldCoords
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_iso_center(cst, ct, visBool=False):
    """
    Calculate the isocenter of a target region based on given constraints.

    Parameters:
        cst (ndarray): Constraint array where each row represents an object with properties.
                      Assumes columns include at least: [2] type (e.g., "TARGET"),
                      [3] coordinate index, and [5] optional additional constraints.
        ct (ndarray): Coordinate transformation matrix.
        visBool (bool): If True, visualize the target points and the isocenter in 3D.

    Returns:
        iso_center (ndarray): The mean coordinate of the isocenter in world coordinates.
    """
    # Initialize a list to store valid target coordinates
    V = []

    # Determine if the 6th column (index 5) contains no object or constraints
    if cst.shape[1] >= 6:
        no_obj_or_const = all(elem is None or elem is '' for elem in cst[:, 5])
    else:
        no_obj_or_const = True

    # Iterate through constraints to collect target coordinates
    for i in range(cst.shape[0]):
        if cst[i, 2] == "TARGET" and (no_obj_or_const or cst[i, 5] is not None):
            V.append(cst[i, 3][0][0])

    # Remove duplicate coordinates
    V = np.unique(V)

    # Handle case where no valid targets are found
    if V.size == 0:
        # Future versions may add specific handling here
        return None

    # Convert cube indices to world coordinates
    coord = CubeIndex2WorldCoords.cube_index2world_coords(V, ct)

    # Calculate the isocenter as the mean of all valid coordinates
    iso_center = coord.mean(axis=0)

    # Visualization (if enabled)
    if visBool:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot target points (black crosses)
        ax.scatter(coord[:, 1], coord[:, 0], coord[:, 2], color='k', marker='x', label='Target Points')

        # Plot the isocenter (red point)
        ax.scatter(iso_center[1], iso_center[0], iso_center[2], color='r', s=30, label='Isocenter')

        # Set axis labels
        ax.set_xlabel('y [mm]')
        ax.set_ylabel('x [mm]')
        ax.set_zlabel('z [mm]')

        # Add legend
        ax.legend()

        # Show the plot
        plt.show()

    return iso_center
