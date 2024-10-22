"""
Auxiliary functions for animation.
"""
from numpy import (
    min as np_min,
    max as np_max,
)
from matplotlib.pyplot import figure as plt_figure


def initialize_animation(data=None):
    """
    Initializes a 3D animation plot with specified axis limits.

    Arguments:
        data (np.array, optional): An array specifying movement data.
            The keys should be 'x', 'y', and 'z' and a values should be lists of min and max axis values.

    Returns:
    tuple: A tuple containing:
        - fig (matplotlib.figure.Figure): The created figure.
        - ax (matplotlib.axes._axes.Axes3D): The 3D axis for the plot.
        - scatter (matplotlib.collections.PathCollection): The scatter plot object.
        - line (matplotlib.lines.Line2D): The line plot object.
    """
    col_min = np_min(data, axis=0)
    col_max = np_max(data, axis=0)
    diffs = col_max - col_min
    if data is not None:
        axis_limits = {
            'x': [col_min[0] - diffs[0]*0.1, col_max[0] + diffs[0]*0.1],
            'y': [col_min[1] - diffs[1]*0.1, col_max[1] + diffs[1]*0.1],
            'z': [col_min[1] - diffs[2]*0.1, col_max[2] + diffs[2]*0.1],
        }
        
    else:
        raise Exception('No movement data provided to build axws limits')
        
    fig = plt_figure(dpi=100)
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim(axis_limits.get('x'))
    ax.set_ylim(axis_limits.get('y'))
    ax.set_zlim(axis_limits.get('z'))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    scatter = ax.scatter([], [], [], color='b', s=1)
    line, = ax.plot([], [], [], color='b', linewidth=0.5)

    return fig, ax, scatter, line


def update_location(frame, data, ax, line, scatter):
    """
    Updates the location of a scatter plot and a line plot in a 3D animation.

    Arguments:
        frame (int): The current frame index for the animation.
        data (numpy.ndarray): An array of shape (n, 3) containing the x, y, and z coordinates.
        ax (matplotlib.axes._axes.Axes3D): The 3D axis on which the plots are displayed.
        line (matplotlib.lines.Line2D): The line plot object to be updated.
        scatter (matplotlib.collections.PathCollection): The scatter plot object to be updated.
    """
    x, y, z = data[frame]

    scatter._offsets3d = ([x], [y], [z])

    line.set_data(data[:frame + 1, 0], data[:frame + 1, 1])
    line.set_3d_properties(data[:frame + 1, 2])

    ax.set_title(f"Iteration: {frame}")
