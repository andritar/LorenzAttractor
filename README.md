# Lorenz Attractor

This repository provides a Python implementation of the Lorenz Attractor using numerical methods like Euler and Runge-Kutta. The Lorenz Attractor is a system of differential equations that models chaotic behavior in dynamic systems.

## Features

- **Numerical Methods**: Supports both Euler and 4th-order Runge-Kutta methods for solving the Lorenz equations.
- **Customizable Parameters**: Allows customization of initial coordinates, step size, and number of iterations.
- **Visualization**: Provides plotting functionality to visualize the Lorenz Attractor and its projections in different planes.

## Requirements

This implementation depends on the following Python packages:
- `numpy`
- `matplotlib`

You can install the dependencies via pip:
```bash
pip install numpy matplotlib
```

## Usage

### 1. Initializing the Lorenz Attractor
You can initialize the LorenzAttractor class by specifying the step size, number of iterations, numerical method (euler or runge-kutta), and the initial coordinates (optional).

```python
from lorenz_attractor import LorenzAttractor

# Initialize the attractor
lorenz = LorenzAttractor(step=0.01, num_iterations=10000, method='euler', init_coordinates=[1, 1, 1])
```

### 2. Calculating the Movement
To calculate the movement of the Lorenz attractor, use the calculate method. The parameters sigma, rho, and beta of the Lorenz system need to be passed.

```python
params = [10, 28, 8/3]  # sigma, rho, beta
movement = lorenz.calculate(params=params)
```

### 3. Plotting the Lorenz Attractor
After calculating the movement, you can plot the full 3D trajectory of the Lorenz Attractor using the plot method.

```python
lorenz.plot(movement_df=movement)
```

### 4. Plotting Projections
You can also plot 2D projections of the Lorenz Attractor on different planes using the plot_projection method. Valid projections are xoy, xoz, and yoz.

```python
lorenz.plot_projection(movement_df=movement, projection='xoy')
```

### 5. Build and Plot in One Step
For convenience, you can compute and plot the Lorenz Attractor in one step using the build_attractor method.

```python
lorenz.build_attractor(params=params)
```

## Example
```python
from lorenz_attractor import LorenzAttractor

# Initialize the Lorenz Attractor
lorenz = LorenzAttractor(step=0.01, num_iterations=10000, method='runge-kutta')

# Set parameters for the Lorenz system
params = [10, 28, 8/3]

# Calculate and plot the attractor
lorenz.build_attractor(params=params)
```

## Class Overview

`LorenzAttractor`

**init**(step=0.01, num_iterations=10000, method='euler', init_coordinates=None): Initializes the Lorenz Attractor.

**set_init_coordinates**(init_coordinates): Sets the initial coordinates for the system.

**calculate**(params): Calculates the movement of the Lorenz Attractor using the specified numerical method.

**plot**(movement_df): Plots the full 3D trajectory of the Lorenz Attractor.

**plot_projection**(movement_df=None, projection='xoy'): Plots a 2D projection of the Lorenz Attractor on the specified plane.

**build_attractor**(params): Computes and visualizes the Lorenz Attractor in one step.

**plot_variable_change**(variable, num_iterations_to_show=None): Plot how provided variable changes from iteration to iteration.

## License

This project is licensed under the MIT License.
