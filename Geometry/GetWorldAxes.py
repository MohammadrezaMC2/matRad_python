import numpy as np

def get_world_axes(grid_struct):
    """
    Generate world coordinate axes for a given grid structure.

    Parameters:
        grid_struct (dict): A dictionary-like structure containing grid dimensions, resolution,
                           and optional DICOM information.

    Returns:
        grid_struct (dict): The updated grid structure with world coordinate axes ('x', 'y', 'z').
    """
    dimensions = None
    resolution_data = None
    update = False

    # Check if grid_struct is valid and determine if it needs updating
    if grid_struct is not None:
        if not ('x' in grid_struct.dtype.names and
                'y' in grid_struct.dtype.names and
                'z' in grid_struct.dtype.names):
            update = True

    # Update conditionally if any axes are missing
    if update:
        # Extract dimensions if available
        if 'cubeDim' in grid_struct.dtype.names:
            dimensions = grid_struct['cubeDim'][0][0][0]

        # Handle DICOM-based first voxel positioning
        if 'dicomInfo' in grid_struct.dtype.names and 'ImagePositionPatient' in grid_struct['dicomInfo']:
            first_vox = grid_struct['dicomInfo']['ImagePositionPatient']
        else:
            # Extract resolution and compute first voxel position
            resolution_data = grid_struct['resolution'][0][0]
            x = resolution_data['x']
            y = resolution_data['y']
            z = resolution_data['z']

            resolution = (x, y, z)
            first_vox = -1 * (dimensions[[1, 0, 2]]) / 2 * resolution

        # Generate world coordinate axes
        grid_struct['x'] = first_vox[0] + x * np.arange(0, dimensions[1])
        grid_struct['y'] = first_vox[1] + y * np.arange(0, dimensions[0])
        grid_struct['z'] = first_vox[2] + z * np.arange(0, dimensions[2])

    return grid_struct