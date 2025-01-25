import numpy as np
from Geometry import CubeCoords2WorldCoords

def get_resolution(grid_struct):
    """
    Extract the resolution of the grid structure along the x, y, and z axes.

    Parameters:
        grid_struct (dict): A dictionary-like structure containing grid resolution information.

    Returns:
        resolution (ndarray): A 3x1 NumPy array containing the resolution for x, y, and z axes.
    """
    # Extract resolution data from the grid structure
    resolution_data = grid_struct['resolution'][0][0]
    x = resolution_data['x']
    y = resolution_data['y']
    z = resolution_data['z']

    # Convert resolution values to float64 and reshape them
    array1 = x.astype(np.float64).reshape(1)
    array2 = y.astype(np.float64).reshape(1)
    array3 = z.astype(np.float64).reshape(1)

    # Combine into a single array
    resolution = np.array([array1, array2, array3])
    return resolution

def cube_index2world_coords(cube_ix, grid_struct):
    """
    Convert cube indices to world coordinates using grid structure and resolution.

    Parameters:
        cube_ix (ndarray): An array of cube indices to be converted.
        grid_struct (dict): A dictionary-like structure containing grid and resolution information.

    Returns:
        coord (ndarray): A NumPy array of world coordinates corresponding to the cube indices.
    """
    # Extract dimensions of the grid if available
    dimensions = None
    if 'cubeDim' in grid_struct.dtype.names:
        dimensions = grid_struct['cubeDim'][0][0][0]

    # Unravel the 1D cube indices into 3D coordinates
    if len(cube_ix.shape) == 1:
        cube_ix1, cube_ix2, cube_ix3 = np.unravel_index(cube_ix, dimensions, order='F')

    # Combine the unraveled indices into a single array
    coordinates = np.column_stack((cube_ix1, cube_ix2 + 1, cube_ix3 + 1))

    # Get the grid resolution and scale the coordinates accordingly
    resolution = get_resolution(grid_struct)
    coord = coordinates[:, [1, 0, 2]] * resolution.T

    # Convert cube coordinates to world coordinates
    coord = CubeCoords2WorldCoords.cube_coords2World_coords(coord, grid_struct, False)

    return coord
