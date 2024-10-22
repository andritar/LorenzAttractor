"""
Functionality to calculate derivatives and partial derivatives.
"""
from numpy import (
    array as np_array,
    sin as np_sin,
)


def calc_chen_partial_derivatives(coordinates, params):
    """
    Calculate partial derivatives for Chen attractor.

    Arguments:
        coordinates (numpy.array): function point.
        params (list[float]): Chen attractor parameters.

    Returns:
        Chen attractor partial derivatives as a list.
    """
    x, y, z = coordinates
    a, b, c = params
    derivative_x = a*x - y*z
    derivative_y = b*y + x*z
    derivative_z = c*z + x*y/3

    partial_derivatives = np_array([derivative_x, derivative_y, derivative_z])

    return partial_derivatives


def calc_four_wing_partial_derivatives(coordinates, params):
    """
    Calculate partial derivatives for four wing attractor.

    Arguments:
        coordinates (numpy.array): function point.
        params (list[float]): Four wing attractor parameters.

    Returns:
        Four wing attractor partial derivatives as a list.
    """
    x, y, z = coordinates
    a, b, c = params
    derivative_x = a * x + y * z
    derivative_y = b * x + c * y - x * z
    derivative_z = -z - x * y

    partial_derivatives = np_array([derivative_x, derivative_y, derivative_z])

    return partial_derivatives


def calc_lorenz_partial_derivatives(coordinates, params):
    """
    Calculate partial derivatives for Lorenz attractor.

    Arguments:
        coordinates (numpy.array): function point.
        params (list[float]): Lorenz attractor parameters.

    Returns:
        Lorenz attractor partial derivatives as a list.
    """
    x, y, z = coordinates
    s, r, b = params
    derivative_x = s * (y - x)
    derivative_y = r * x - y - x * z
    derivative_z = x * y - b * z

    partial_derivatives = np_array([derivative_x, derivative_y, derivative_z])

    return partial_derivatives


def calc_thomas_partial_derivatives(coordinates, params):
    """
    Calculate partial derivatives for Thomas attractor.

    Arguments:
        coordinates (numpy.array): function point.
        params (list[float]): Lorenz attractor parameters.

    Returns:
        Thomas attractor partial derivatives as a list.
    """
    if len(params) > 1:
        raise Exception('Only one parametershould be provided for Thomas attractor.')
        
    x, y, z = coordinates
    b = params[0]
    derivative_x = np_sin(y) - b*x
    derivative_y = np_sin(z) - b*y
    derivative_z = np_sin(x) - b*z

    partial_derivatives = np_array([derivative_x, derivative_y, derivative_z])

    return partial_derivatives
