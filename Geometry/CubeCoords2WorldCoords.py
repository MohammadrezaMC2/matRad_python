import numpy as np
from Geometry import GetWorldAxes

def get_resolution(grid_struct):
    """
    Extract the resolution of the grid structure along the x, y, and z axes.

    Parameters:
        grid_struct (dict): A dictionary-like structure containing grid resolution information.

    Returns:
        resolution (ndarray): A 3x1 NumPy array containing the resolution for x, y, and z axes.
    """
    resolution_data = grid_struct['resolution'][0][0]
    x = resolution_data['x']
    y = resolution_data['y']
    z = resolution_data['z']

    array1 = x.astype(np.float64).reshape(1)
    array2 = y.astype(np.float64).reshape(1)
    array3 = z.astype(np.float64).reshape(1)

    resolution = np.array([array1, array2, array3])
    return resolution

def cube_coords2World_coords(cCoord=None, grid_struct=None, allow_outside=False):
    """
    Convert cube coordinates to world coordinates.

    Parameters:
        cCoord (ndarray): Cube coordinates to be converted.
        grid_struct (dict): A dictionary-like structure containing grid resolution and axes information.
        allow_outside (bool): If False, restrict the coordinates within grid bounds.

    Returns:
        coord (ndarray): World coordinates corresponding to the input cube coordinates.

    Raises:
        AssertionError: If queried coordinates are outside the grid bounds and allow_outside is False.
    """
    if cCoord is None and grid_struct is None:
        allow_outside = True

    # Get world axes and resolution from grid structure
    grid_struct = GetWorldAxes.get_world_axes(grid_struct=grid_struct)
    resolution = get_resolution(grid_struct)

    # Compute translation from cube coordinates to world coordinates
    first_vox_world = np.array([
        np.min(grid_struct['x'][0][0]),
        np.min(grid_struct['y'][0][0]),
        np.min(grid_struct['z'][0][0])
    ])
    first_vox_world = first_vox_world.reshape((1, 3))
    first_vox_cube = resolution.reshape((1, 3))
    translation = first_vox_world - first_vox_cube

    # Extract grid dimensions
    dimensions = grid_struct['cubeDim'][0][0][0]

    # Check bounds if allow_outside is False
    if not allow_outside:
        min_bound_cube = first_vox_cube / 2
        max_bound_cube = first_vox_cube.reshape((3, 1)) / 2 + dimensions[[1, 0, 2]].reshape(3, 1) * resolution.reshape(3, 1)
        min_bound_cube = min_bound_cube.reshape(1, 3)
        max_bound_cube = max_bound_cube.reshape(1, 3)

        # Check if any coordinates violate bounds
        violate_bounds = np.any(
            np.any((cCoord < min_bound_cube) | (cCoord > max_bound_cube), axis=1)
        )

        if violate_bounds:
            raise AssertionError("Queried world coordinate is outside the CT bounds.")

    # Apply translation to get world coordinates
    coord = cCoord + translation

    return coord
