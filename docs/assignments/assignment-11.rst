====================================
Assignment 11 - Numerical Simulation
====================================

.. note::

    Submit your assignment as a single PDF, including plots and source code (if any).
    We expect academic honesty. Collaboration is encouraged, but must be declared. Any use of AI must be declared along with any other sources used.
    
    This is not an exam. Do your best and show that you put in effort and the assignment will be approved.

The objectives of this assignment are:

- To understand how explicit Runge-Kutta (ERK) methods work, and to be able to implement them.
- To understand important concepts of ERK methods, such as accuracy and stability, and the related concepts of local and global error, as well as stability functions.

The theory used here can be found in the Lecture Notes by Sebastien Gros.

Problem 1 - Accuracy and stability of ERKs
------------------------------------------

In this task we will make simulations using the explicit Euler scheme, and two other explicit Runge-Kutta schemes of order 2 and 4, respectively.

The Butcher tables of these three schemes are:

.. math::

    \text{Explicit Euler (RK1):}
    \quad
    &\begin{array}{c|c}
        0 & \\
        \hline
         & 1
    \end{array}
    \\
    \text{Runge-Kutta 2 (RK2):}
    \quad
    &\begin{array}{c|cc}
        0       &         & \\
        \frac12 & \frac12 & \\
        \hline
                &       0 & 1
    \end{array}
    \\
    \text{Runge-Kutta 4 (RK4):}
    \quad
    &\begin{array}{c|cccc}
        0       &         &         &         & \\
        \frac12 & \frac12 &         &         & \\
        \frac12 &         & \frac12 &         & \\
        1       &         &         & 1       & \\
        \hline
                & \frac16 & \frac13 & \frac13 & \frac13
    \end{array}

We will use these methods to simulate the classic test system:

.. math::

    \dot{x} = \lambda x

where :math:`\lambda < 0`.

.. admonition:: Tasks

    a. 
    
        Implement the 3 ERK schemes for a generic scalar ODE :math:`\dot{x} = f(t, x)`.
        Test the implemented codes for :math:`\lambda = -2` in the time interval :math:`[0, 2]`, and compare with the analytical solution.
        Choose a time-step :math:`\Delta t = 0.4` and the initial condition :math:`x(0) = 1`.
        Comment on the results.

    b. 
    
        For what value of :math:`\lambda < 0` will the different schemes become unstable?


Problem 2 - IRK schemes
-----------------------

Here we will consider the Lorenz system

.. math::
    :label: lorentz_system

    \dot{x} &= 5 (y - x) 
    \\
    \dot{y} &= x (20 - z) - y
    \\
    \dot{z} &= x y - 2z

with initial condition :math:`x(0) = 1`, :math:`y(0) = 1`, :math:`z(0) = 1`.

.. admonition:: Tasks

    a. 
    
        The file `irk.py` contains a general RK integrator that can take both ERK and IRK Butcher tables (requiring to use a Newton iteration).
        The Gauss-Legendre collocation method is an IRK scheme with :math:`s = 2` stages and of order :math:`2s = 4`, which has the Butcher table:
        
        .. math::
            \text{IRK4:}
            \quad
            &\begin{array}{c|cccc}
                \frac12 - \frac{\sqrt{3}}6 & \frac14                    & \frac14 - \frac{\sqrt{3}}6 \\
                \frac12 + \frac{\sqrt{3}}6 & \frac14 + \frac{\sqrt{3}}6 & \frac14                    \\
                \hline
                                           & \frac12                    & \frac12
            \end{array}

        Simulate the system :eq:`lorentz_system` with this method, using time interval :math:`[0, 2]`, :math:`N = 200` simulation points.
        Add a code screen shot and a plot of the result to your answer.

    b. 
    
        If we were to use the IRK4 method on the system :math:`\dot{x} = \lambda x`, for what value of :math:`\lambda < 0` will the IRK4 scheme become unstable?

    c. 
    
        Assume that the collocation points :math:`\tau_1 = \frac13`, :math:`\tau_2 = \frac23` are used to construct a Gauss-Legendre collocation method, what is the corresponding Butcher table?
        