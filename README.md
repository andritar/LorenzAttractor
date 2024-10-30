# Lorenz Attractor

This repository provides a Python implementation of various chaotic attractors, including the Lorenz, Chen, 
Four-Wing, and Thomas attractors, using numerical methods like Euler and 4th-order Runge-Kutta. These attractors 
are modeled with differential equations that demonstrate chaotic behavior in dynamic systems.
## Features

- **Attractor Types**: Includes Lorenz, Chen, Four-Wing, and Thomas attractors.
- **Numerical Methods**: Supports both Euler and 4th-order Runge-Kutta methods for solving the Lorenz equations.
- **Customizable Parameters**: Allows customization of initial coordinates, step size, and number of iterations.
- **Visualization**: Provides options to visualize the attractor’s animated 3D trajectory, projections in different planes, and variable evolution over iterations.

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
Initialize the `StrangeAttractor` class by specifying the attractor type (`lorenz`, `chen`, `four_wing`, `thomas`),
step size, number of iterations, numerical method (`euler` or `runge-kutta`), and optional initial coordinates.

```python
from strange_attractor import StrangeAttractor

# Initialize the attractor
attractor = StrangeAttractor(attractor_type='lorenz', step=0.01, num_iterations=10000, method='euler', init_coordinates=[1, 1, 1])
```

### 2. Calculating the Movement
To calculate the movement, use the calculate method with attractor-specific parameters. For the Lorenz system, 
these include sigma, rho, and beta.

```python
params = [10, 28, 8/3]  # Lorenz system parameters
movement = attractor.calculate(params=params)
```

### 3. Plotting the Lorenz Attractor
After calculating the movement, you can plot the full 3D trajectory of the Lorenz Attractor using the plot method.

```python
attractor.plot(movement_df=movement)
```

### 4. Plotting Projections
Plot 2D projections of the attractor on specified planes (options: `xoy`, `xoz`, `yoz`) using plot_projection.

```python
attractor.plot_projection(movement_df=movement, projection='xoy')
```

### 5. Variable Change Plot
To visualize how a specific variable (e.g., `x`, `y`, or `z`) changes over iterations, use plot_variable_change.

```python
attractor.plot_variable_change(variable='x', num_iterations_to_show=5000)
```

### 6. Build and Plot in One Step
For convenience, you can compute and plot the Lorenz Attractor in one step using the build_attractor method.

```python
attractor.build_attractor(params=params)
```

### Run animation

To animate strange attractor movement use `initialize_animation` and `update_location` methods:

```python
fig, ax, scatter, line = initialize_animation(data=attractor.cached_movement)
ani = FuncAnimation(
    fig, 
    partial(
        update_location, 
        data=attractor.cached_movement, 
        ax=ax, 
        line=line, 
        scatter=scatter,
    ), 
    frames=len(attractor.cached_movement), 
    interval=2,
)
plt_show()

```

## Example
```python
from strange_attractor import StrangeAttractor

# Initialize the Lorenz Attractor
attractor = StrangeAttractor(attractor_type='lorenz', step=0.01, num_iterations=10000, method='runge-kutta')

# Set parameters for the Lorenz system
params = [10, 28, 8/3]

# Calculate and plot the attractor
attractor.build_attractor(params=params)
```

## Class Overview

`StrangeAttractor`

**init**(attractor_type='lorenz', step=0.01, num_iterations=10000, method='euler', init_coordinates=None): Initializes the Strange Attractor.

**set_init_coordinates**(init_coordinates): Sets the initial coordinates for the system.

**calculate**(params): Calculates the movement of the Lorenz Attractor using the specified numerical method.

**plot**(movement_df): Plots the full 3D trajectory of the Lorenz Attractor.

**plot_projection**(movement_df=None, projection='xoy'): Plots a 2D projection of the Lorenz Attractor on the specified plane.

**build_attractor**(params): Computes and visualizes the Lorenz Attractor in one step.

**plot_variable_change**(variable, num_iterations_to_show=None): Plot how provided variable changes from iteration to iteration.

## License

This project is licensed under the MIT License.
