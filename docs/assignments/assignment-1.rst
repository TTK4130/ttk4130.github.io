==================================================
Assignment 1 - Modelling and Simulation Overview
==================================================

.. note::

    Submit your assignment as a single PDF.
    We expect academic honesty. Collaboration is encouraged, but must be declared. Any use of AI must be declared along with any other sources used.
    This is not an exam. Do your best and show that you put in effort and the assignment will be approved.

In this assignment we will consider the mass-damper-spring system as shown in the figure below.

.. figure:: ../figures/mass_damper_spring.svg
  :align: center

  Schematic of the mass-damper-spring system.

The mass :math:`m` is 1kg, the linear spring coefficient :math:`k` is 1 N/m, and the linear damping coefficient is 0.7 Ns/m. To get going, you will also need values for the initial states (i.e. the states at the time step :math:`j=0`). Set the initial position to be 1 meter away from the equilibrium position of the spring (either side is OK), and the initial velocity to be 0.

Problem 1 - Mass-Damper-Spring
==================================

.. hint::
    :class: dropdown

    Have you read the code examples in :ref:`Numerical Methods for ODEs`?

.. admonition:: a)

  Write the system equation of the mass-spring-damper as a second order differential equation. The spring is relaxed when the wagon is at the position :math:`x=0`.

.. admonition:: b)

   Transform the second order equation into a set of two first order equations.

.. admonition:: c)

    Solve the initial value problem of the system described in 1b) by hand and verify your answer by using SymPy. For this task set the friction coefficient to zero.

.. admonition:: d)

    Plot the position :math:`x` of the mass from :math:`t=0` to :math:`t=30` seconds. What can you say about the response of the system?

Problem 2 - Numerical Integration
==================================

.. admonition:: a)

    Explain the forward Euler integration method in your own words. How does step size :math:`\Delta t` affect the integration error?


.. admonition:: b)

    Write a code for simulating the system equations from Problem 1 using the Euler forward integration method with a step size of :math:`\Delta t = 0.01` and plot the results. Let the friction coefficient remain zero. Compare the analytical solution from 1d) with the numerical method in 2d) by plotting the integration error and comment the result. Is the error acceptable?


.. admonition:: c)

    Investigate the impact of the spring and damper coefficients on the integration error. Determine which coefficient has the greatest influence. To estimate the error in cases where the damper coefficient is non-zero, you can either derive the analytical solution or use a very small time step as the baseline for comparison. Test various combinations of spring and damper coefficient values across three different step sizes, and justify your conclusions.

    .. note::

        If you use the analytical solution for calculating the integration error also in the cases with non-zero damping coefficient, make sure you have the right analytical solution (as there are different solutions for critically damped, overdamped and underdamped system)



