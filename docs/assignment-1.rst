=============
Assignment 1
=============

.. note::

    Submit your delivery as a single PDF.
    We expect academic honesty. Collaboration is encouraged, but must be declared. Any use of AI must be declared along with any other sources used.
    This is not an exam. Do your best and show that you put in effort and the assignment will be approved.

In this assignment we will consider the mass-damper-spring system as shown in the figure below.

.. figure:: figures/mass_damper_spring.svg
  :align: center

  Schematic of the mass-damper-spring system.

The mass :math:`m` is 1kg, the linear spring coefficient :math:`k` is 1 N/m, and the linear damping coefficient is 0.7 Ns/m. To get going, you will also need values for the initial states (i.e. the states at the time step :math:`j=0`). Set the initial position to be 1 meter away from the equilibrium position of the spring (either side is OK), and the initial velocity to be 0.

Problem 1 - Mass-Damper-Spring
==================================

.. hint::
    :class: dropdown

    Have you read the code examples in :ref:`Numerical Methods for ODEs`?

.. admonition:: a)

  Write the system equation of the mass-spring-damper as a second order differential equation. The spring is relaxed when the wagon is at the position :math:`x=0`. You can ignore friction.

.. admonition:: b)

   Transform the second order equation into a set of two first order equations.

.. admonition:: c)

    Solve the initial value problem of the system described in 1b) by hand and verify your answer by using SymPy.

.. admonition:: d)

    Plot the position :math:`x` of the mass from :math:`t=0` to :math:`t=30` seconds. What can you say about the response of the system?

Problem 2 - Numerical Integration
==================================

.. admonition:: a)

    Explain the forward Euler integration method in your own words. How does step size :math:`\Delta t` affect the integration error?


.. admonition:: b)

    Write a code for simulating the system equations from problem 1 using the Euler forward integration method with a step size of :math:`\Delta t = 0.01`.


.. admonition:: c)

    Compare the analytical solution from 1d) with the numerical method in 2d) by plotting the integration error and comment the result. Is the error acceptable? If not, how can we improve our simulation?

.. admonition:: d)

    Test different values of the spring and damper coefficients for at least three different step sizes. Which coefficient affects the integration error the most? Justify your answer.

    .. note::

        Make sure you have the right analytical solution if you choose critical damping, over damped or under damped system


Problem 3 - Limits of Numerical Integration
==============================================

.. admonition:: a)

     Oppgave om stiff systems og at man ikke alltid kan bruke ERK

.. admonition:: b)

     Oppgave om floating point aritmetikk -> også kilde til feil



