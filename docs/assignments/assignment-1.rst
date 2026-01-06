==========================================================
Assignment 1 - Modelling and Simulation Basics
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
To get going, you will also need values for the initial states (i.e. the states at the time step :math:`j=0`).
Set the initial position to be 1 meter away from the equilibrium position of the spring (either side is OK), and the initial velocity to be 0.

Problem 1 - Mass-Damper-Spring
==================================

.. hint::
    :class: dropdown

    Have you read the code examples in :ref:`Numerical Methods for ODEs`?

.. admonition:: Tasks

    a) Write down the expressions for the forces of a spring and a damper.

    b) Using the expression in 1a), find the second order differential equation describing the position of the mass :math:`x`. The spring is relaxed when the wagon is at the position :math:`x=0`.

    c) Transform the expression from 1b) into a set of first order ordinary differential equations.


Problem 2 - Integrator
==================================

Most ODE systems it is not practical or possible to find analytical solutions.
Therefore, in ordre to find its solution/trajectory we rely on numerical integrators
to approximate a solution for us. The simplest method for numerical integration is the
Explicit Euler method, also known as forward Euler. In this task, we develop such an
integrator, and use it to solve the system defined in Problem 1.

.. admonition:: Tasks

    a) Explain, in your own words, how the forward Euler integration method works.
    In particular, describe how information from the differential equation is used to advance the solution in time.

    b) Write a Python function of the system of ordinary differential equations derived for the mass-damper-spring system in problem 1. The function must have the following canonical form

        .. code:: python

            def y_dot(t, y, params):
                y_1, y_2 = y # Extract state variables
                dydt_1 = function_of(y_1, y_2, t) # Your system of 1st order ODEs
                dydt_2 = function_of(y_1, y_2, t)
                return [dydt_1, dydt_2] # Must have same shape as y

    c) Write a code for simulating the system equations from Problem 1 using the Euler forward integration method with a step size of :math:`\Delta t = 0.01` and plot the results. Let the friction coefficient remain zero.




Problem 3 – Analytical solution and comparison
===============================================

In Problem 2, you implemented a numerical simulator for the mass–damper–spring system
based on the system of first-order ordinary differential equations derived in Problem 1.
In this problem, you will compare your numerical results with the analytical
(closed-form) solution of the same system.

Analytical solution
-------------------

The analytical solution of the mass–damper–spring system depends on the amount of damping.
To describe this, we introduce the following quantities, defined in terms of the physical
parameters :math:`m`, :math:`d` and :math:`k`:

.. math::

   \omega_n = \sqrt{\frac{k}{m}}, \qquad
   \zeta = \frac{d}{2\sqrt{km}}.

Here, :math:`\omega_n` is the undamped natural frequency and :math:`\zeta` is the damping ratio.

Depending on the value of :math:`\zeta`, the system is classified as

- *underdamped* (:math:`0 \le \zeta < 1`),
- *critically damped* (:math:`\zeta = 1`),
- *overdamped* (:math:`\zeta > 1`).

The analytical solution for the position of the mass differs between these cases.

Underdamped case
^^^^^^^^^^^^^^^^

For the underdamped case (:math:`0 \le \zeta < 1`), define the damped natural frequency

.. math::

   \omega_d = \omega_n \sqrt{1 - \zeta^2}.

The analytical solution for the position is

.. math::

   x(t) = e^{-\zeta \omega_n t}
   \left[
   x_0 \cos(\omega_d t) +
   \frac{v_0 + \zeta \omega_n x_0}{\omega_d} \sin(\omega_d t)
   \right].

Critically damped case
^^^^^^^^^^^^^^^^^^^^^^

For the critically damped case (:math:`\zeta = 1`), the solution is given by

.. math::

   x(t) = \left(x_0 + (v_0 + \omega_n x_0)t\right)e^{-\omega_n t}.

Overdamped case
^^^^^^^^^^^^^^^

For the overdamped case (:math:`\zeta > 1`), define the characteristic exponents

.. math::

   r_{1,2} = -\zeta\omega_n \pm \omega_n\sqrt{\zeta^2 - 1}.

The analytical solution is

.. math::

   x(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t},

where the constants are determined from the initial conditions as

.. math::

   C_1 = \frac{v_0 - r_2 x_0}{r_1 - r_2}, \qquad
   C_2 = x_0 - C_1.

.. admonition:: Tasks

    a) Write a Python function that computes the analytical solution :math:`x(t)` for the
       mass–damper–spring system. The function shall:

       - take the time vector :math:`t`, initial conditions :math:`x_0` and :math:`v_0`,
         and the parameter dictionary ``params`` as input,
       - compute :math:`\omega_n` and :math:`\zeta` from ``params``,
       - select and apply the correct analytical expression based on the damping regime.

       Use a small numerical tolerance when checking whether :math:`\zeta \approx 1` to avoid
       misclassification due to floating-point round-off errors and to prevent division by
       zero in expressions involving :math:`\omega_d`.


    b) Write a simulation script where the parameters :math:`m`, :math:`d` and :math:`k`
       are defined once in ``params`` and used consistently in both:

       - the numerical simulator (via your ``y_dot`` function from Problem 2), and
       - the analytical solution from Task a).

    c) Using your Euler forward integrator from Problem 2, simulate the system and plot
       the numerical solution and analytical solution for the position :math:`x(t)` in
       the same figure.

    d) Compute and plot the error between the numerical and analytical solutions as a
       function of time.

    e) Repeat the comparison for at least two different values of the damping coefficient
       :math:`d`. Comment briefly on how the damping influences the numerical error.
