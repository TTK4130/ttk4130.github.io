================
Simulation (WIP)
================


Plotting (old)
==============

We'll examine how to plot a simple mass-spring-damper system. We'll first define the system


.. jupyter-execute::

    # System parameters
    m = 1.0  # mass
    c = 0.5  # damping coefficient
    k = 2.0  # spring constant

    # Define the system of ODEs
    def mass_spring_damper(t, y):
        x, v = y
        dxdt = v
        dvdt = (-c * v - k * x) / m
        return [dxdt, dvdt]

We then define our initial conditions, and the range we would like to simulate.

.. jupyter-execute::

    import numpy as np # For storing out solutions in np.arrays

    # Initial conditions
    y0 = [1.0, 0.0]  # initial displacement and velocity
    # Time span
    t_end = 15
    t_span = (0, t_end)
    t_eval = np.linspace(*t_span, 300)  # Increased to 300 for smoother animation

We can then use scipy to solve the initial value problem (IVP) and store the solutions in a pandas dataframe. 

.. jupyter-execute::

    import pandas as pd
    from scipy.integrate import solve_ivp

    # Solve the ODE
    sol = solve_ivp(mass_spring_damper, t_span, y0, t_eval=t_eval)

    # Create a DataFrame
    df = pd.DataFrame({'time': sol.t, 'displacement': sol.y[0]})


Using plotly we can animate the trajectory and display it in a Javascript player.

.. jupyter-execute:: 
    
    import plotly.graph_objects as go
    animation_time = 10

    # Create animation frames
    frames = [
        go.Frame(data=[
            go.Scatter(x=df['time'][:i+1], y=df['displacement'][:i+1], mode='lines', name='trajectory'),  # Line showing trajectory
            go.Scatter(x=[df['time'][i]], y=[df['displacement'][i]], mode='markers', marker=dict(size=10, color='red'), name='current point')  # Marker for current point
        ],
        name=str(df['time'][i]))
        for i in range(len(df))
    ]

    # Create the figure
    fig = go.Figure(
        data=[
            go.Scatter(x=[df['time'][0]], y=[df['displacement'][0]], mode='lines', name='trajectory'),  # Initial empty line
            go.Scatter(x=[df['time'][0]], y=[df['displacement'][0]], mode='markers', marker=dict(size=10, color='red'), name='current point') # Initial marker
        ],
        layout=go.Layout(
            xaxis=dict(range=t_span, autorange=False, title='Time'),
            yaxis=dict(range=[-1,1], autorange=False, title='Displacement'),
            title="Mass-Spring-Damper System Animation",
            updatemenus=[dict(type="buttons",
                            buttons=[dict(label="Play",
                                            method="animate",
                                            args=[None, {"frame": {"duration": animation_time, "redraw": False},
                                                        "fromcurrent": True}])])]),
        frames=frames
    )

    fig.show()




