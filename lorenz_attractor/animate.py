"""
Auxiliary functions for animation.
"""
from matplotlib.pyplot import figure as plt_figure


def initialize_animation(axis_limits=None):
    """
    Initializes a 3D animation plot with specified axis limits.

    Arguments:
        axis_limits (dict, optional): A dictionary specifying the limits for the axes.
            The keys should be 'x', 'y', and 'z' and a values should be lists of min and max axis values.

    Returns:
    tuple: A tuple containing:
        - fig (matplotlib.figure.Figure): The created figure.
        - ax (matplotlib.axes._axes.Axes3D): The 3D axis for the plot.
        - scatter (matplotlib.collections.PathCollection): The scatter plot object.
        - line (matplotlib.lines.Line2D): The line plot object.
    """
    if axis_limits is None:
        axis_limits = {
            'x': [-25, 25],
            'y': [-25, 25],
            'z': [0, 50],
        }
    fig = plt_figure()
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
