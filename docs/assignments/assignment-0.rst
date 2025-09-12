==========================================================
Assignment 0 - Modelling and Simulation Basics (Optional)
==========================================================


This assignment is meant as a refresher to modelling systems as Ordinary Differential Equations (ODEs), as well as
an intro to simple numerical integration. We will consider the mass-damper-spring system as shown in the figure below.

.. figure:: ../figures/mass_damper_spring.svg
  :align: center

  Schematic of the mass-damper-spring system.


Such a system can be divided into three basic elements:

- The mass [kg] - resists any change in motion according to Newton's second law
- The spring [N/m] - stores energy and creates a restoring force directly proportional to its extension or compression according to Hooke's law
- The damper [Ns/m] - dissipates energy by generating a force directly proportional to the speed, opposing motion

The mass :math:`m` is 1kg, the linear spring coefficient :math:`k` is 1 N/m, and the linear damping coefficient is 0.7 Ns/m.
You are free to play around with these parameters, but make sure they are feasible. For example, it does not make sense
to have a damper with negative damping coefficient. To get going, you will also need values for the initial states (i.e. the states at the time step :math:`j=0`).
Set the initial position to be 1 meter away from the equilibrium position of the spring (either side is OK), and the initial velocity to be 0.

Problem 1 - Mass-Damper-Spring
==================================

.. hint::
    :class: dropdown

    Have you read the code examples in :ref:`Numerical Methods for ODEs`?

.. admonition:: Tasks

    a) Write down the expressions for the forces of a spring and a damper.

    b) Using Newton's second and third law, find an expression for all the forces acting on the mass

    c) Using the expression in 1b), find the system of equations as a function of the position of the mass :math:`x`. The spring is relaxed when the wagon is at the position :math:`x=0`. What kind of equation is this?

    d) Transform the expression from 1c) into a set of first order ordinary differential equations.

    e) What is the definition of an initial value problem (IVP)?

    f) Solve the initial value problem of the system described in 1c) by hand and verify your answer by using SymPy. For this task set the friction coefficient to zero.

    g) Plot the position :math:`x` of the mass from :math:`t=0` to :math:`t=30` seconds using Python and Matplotlib. What can you say about the response of the system?

Problem 2 - Numerical Integration
==================================

Most systems won't have an analytical solution. To find its solution/trajectory we rely on numerical integrators to approximate
a solution for us. The simplest method for numerical integration is the Explicit Euler or Forward Euler method. Please revise your knowledge of
Explicit Euler and do the following tasks.

.. admonition:: Tasks

    a) Explain the forward Euler integration method in your own words. How does step size :math:`\Delta t` affect the integration error?

    b) Write a Python function of the system of ordinary differential equations derived for the mass-damper-spring system in problem 1. The function must have the following canonical form

        .. code:: python

            def y_dot(t, y):
                y_1, y_2 = y # Extract state variables
                dydt_1 = function_of(y_1, y_2, t) # Your system of 1st order ODEs
                dydt_2 = function_of(y_1, y_2, t)
                return [dydt_1, dydt_2] # Must have same shape as y

    c) Write a code for simulating the system equations from Problem 1 using the Euler forward integration method with a step size of :math:`\Delta t = 0.01` and plot the results. Let the friction coefficient remain zero.

    d) Compare the analytical solution from problem 1 with the numerical method in 2c) by plotting the integration error and comment the result. Is the error acceptable?

    e) Investigate the impact of the spring and damper coefficients on the integration error. Determine which coefficient has the greatest influence. To estimate the error in cases where the damper coefficient is non-zero, you can either derive the analytical solution or use a very small time step as the baseline for comparison. Test various combinations of spring and damper coefficient values across three different step sizes, and justify your conclusions.

    .. note::

        If you use the analytical solution for calculating the integration error also in the cases with non-zero damping coefficient, make sure you have the right analytical solution (as there are different solutions for critically damped, overdamped and underdamped system)



