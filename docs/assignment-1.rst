=============
Assignment 1
=============

We consider here a mass-damper-spring system as shown in the figure below.

.. figure:: figures/mass_damper_spring.svg
  :align: center

  Schematic of the mass-damper-spring system.

.. admonition:: Exercise a)

  Write the system equation as a second order differential equation. The spring is relaxed when the wagon is at the position :math:`x=0`.


.. hint::
   :class: dropdown
   
   Have you watched lecture 2?

.. admonition:: Exercise b)

   Transform the second order equation into a set of two first order equations.

.. admonition:: Exercise c)

   Write a code for simulating the system equations from b), using the Euler forward integration method a step size of :math:`0.01` seconds. The mass :math:`m` is 1kg, the linear spring coefficient :math:`k` is 1 N/m, and the linear damping coefficient is 0.7 Ns/m. To get going, you will also need values for the initial states (i.e. the states at the time step :math:`j=0`). Set the initial position to be 1 meter away from the equilibrium position of the spring (either side is OK), and the initial velocity to be 0.

.. math::

   \begin{bmatrix}
     a & b
   \end{bmatrix}
