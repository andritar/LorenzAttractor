"""
Lorenz attractor implementation.
"""
from numpy import empty as np_empty
from matplotlib.pyplot import (
    figure as plt_figure,
    show as plt_show,
)

from attractor.derivative import (
    calc_chen_partial_derivatives,
    calc_four_wing_partial_derivatives,
    calc_lorenz_partial_derivatives,
    calc_thomas_partial_derivatives,
)


class StrangeAttractor:
    """
    Lorenz Attractor Numerical methods calculation implementation.
    """

    def __init__(
            self,
            attractor_type='lorenz',
            step=0.01,
            num_iterations=10000,
            method='euler',
            init_coordinates=None,
    ):
        """
        Construct the object.

        Arguments:
            attractor_type (str): type of attractor (`lorenz`, `four_wind` etc.).
            step (float): step size.
            num_iterations (int): number of times to recalculate new location.
            method (str): numerical solving method (`euler` or `runge-kutta`)
            init_coordinates (list[float]): initial location.
        """
        if attractor_type not in ['lorenz', 'four_wing', 'thomas', 'chen']:
            raise Exception('Invalid attractor type provided.')

        if step <= 0:
            raise Exception('Step parameter should be positive.')

        if num_iterations <= 0:
            raise Exception('num_iterations parameter should be positive.')

        if not isinstance(num_iterations, int):
            raise Exception('num_iterations parameter should be integer.')

        self.attractor_type = attractor_type
        self.step = step
        self.num_iterations = num_iterations

        if method in ['euler', 'runge-kutta']:
            self.method = method

        else:
            raise Exception('Not handled method')

        if init_coordinates is None:
            init_coordinates = [1, 1, 1]

        self.init_coordinates = init_coordinates
        self.cached_movement = None

    def set_init_coordinates(self, init_coordinates):
        """
        Provide initial point.

        Arguments:
            init_coordinates (list[float]): initial point location.
        """
        self.init_coordinates = init_coordinates

    def calculate(self, params):
        """
        Calculate movement of Lorenz attractor.

        Arguments:
            params (list[float]): Lorenz attractor parameters.

        Returns:
            movement history as a matrix.
        """
        if self.attractor_type == 'lorenz':
            movement_df = self._calculate(derivative_func=calc_lorenz_partial_derivatives, params=params)

        elif self.attractor_type == 'four_wing':
            movement_df = self._calculate(derivative_func=calc_four_wing_partial_derivatives, params=params)
            
        elif self.attractor_type == 'thomas':
            movement_df = self._calculate(derivative_func=calc_thomas_partial_derivatives, params=params)
            
        elif self.attractor_type == 'chen':
            movement_df = self._calculate(derivative_func=calc_chen_partial_derivatives, params=params)

        else:
            raise Exception(f"Can't handle attractor ty[e '{attractor_type}'.")

        return movement_df

    def _calculate(self, derivative_func, params):
        """
        Internal function to calculate movement of Lorenz attractor.

        Arguments:
            derivative_func (function): function to calculate derivatives.
            params (list[float]): Lorenz attractor parameters.

        Returns:
            movement history as a matrix.
        """
        movement_df = np_empty((self.num_iterations + 1, 3))
        movement_df[0] = self.init_coordinates

        for i in range(self.num_iterations):
            if self.method == 'euler':
                partial_derivatives = derivative_func(coordinates=movement_df[i], params=params)
                movement_df[i + 1] = movement_df[i] + partial_derivatives * self.step

            elif self.method == 'runge-kutta':
                k1 = derivative_func(coordinates=movement_df[i], params=params)
                k2 = derivative_func(coordinates=movement_df[i] + self.step * k1 / 2, params=params)
                k3 = derivative_func(coordinates=movement_df[i] + self.step * k2 / 2, params=params)
                k4 = derivative_func(coordinates=movement_df[i] + self.step * k3, params=params)

                movement_df[i + 1] = movement_df[i] + self.step * (k1 + 2 * k2 + 2 * k3 + k4) / 6

            else:
                raise Exception('Not handled method')

        self.cached_movement = movement_df

        return movement_df

    def plot(self, movement_df):
        """
        Plot attractor.

        Arguments:
            movement_df (np.array): matrix with function movement.
        """
        ax = plt_figure().add_subplot(projection='3d')

        ax.plot(*movement_df.T, lw=0.6)
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        ax.set_zlabel("Z Axis")
        ax.set_title(f"{self.attractor_type.replace('_', ' ').capitalize()} Attractor")

        plt_show()

    def plot_projection(self, movement_df=None, projection='xoy'):
        """
        Plot projection for a provided function.

        Arguments:
            movement_df (np.array): matrix with function movement.
            projection (str): plane to make projection (`xoy`, `xoz` or `yoz`).
        """
        if movement_df is None:
            if self.cached_movement is not None:
                print('Cached movement used')
                movement_df = self.cached_movement

            else:
                raise Exception('No movement to project.')

        projection = projection.lower()
        if projection == 'xoy':
            movement_df = movement_df[:, [0, 1]]

        elif projection == 'xoz':
            movement_df = movement_df[:, [0, 2]]

        elif projection == 'yoz':
            movement_df = movement_df[:, [1, 2]]

        else:
            raise Exception('Unknown projection. Please provide `xoy`, `xoz` or `yoz`.')

        ax = plt_figure().add_subplot()

        ax.plot(*movement_df.T, lw=0.6)
        ax.set_xlabel(f"{projection[0].upper()} Axis")
        ax.set_ylabel(f"{projection[2].upper()} Axis")
        ax.set_title(f"{self.attractor_type.replace('_', ' ').capitalize()} Attractor")

        plt_show()

    def plot_variable_change(self, variable, num_iterations_to_show=None):
        """
        Plot variable change depends on iteration number.

        Arguments:
            variable (str): variable name (`x`, `y`, `z`)
            num_iterations_to_show (int): number of first iterations to display.
        """
        if num_iterations_to_show is None:
            num_iterations_to_show = len(self.cached_movement)
            
        variable_positions = {
            'x': 0,
            'y': 1,
            'z': 2,
        }
        position = variable_positions.get(variable)

        fig = plt_figure(dpi=100)
        ax = fig.add_subplot(1,1,1)
        ax.plot(self.cached_movement[: , position], linewidth=0.5)
        ax.set_title(f'{variable} variable movement')
        ax.set_xlabel('iteration')
        ax.set_ylabel(variable)
        fig.show()

    def build_attractor(self, params):
        """
        Build Lorenz attractor.

        Arguments:
            params (list[float]): Lorenz attractor parameters.
        """
        movement_df = self.calculate(params=params)
        self.plot(movement_df=movement_df)
