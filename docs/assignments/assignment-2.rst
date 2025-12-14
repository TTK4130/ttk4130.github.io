=========================================
Assignment 2 - Explicit Numerical Solvers
=========================================

.. note::

    Submit your assignment as a single PDF, including plots and source code (if any).
    We expect academic honesty. Collaboration is encouraged, but must be declared. Any use of AI must be declared along with any other sources used.
    This is not an exam. Do your best and show that you put in effort and the assignment will be approved.

In the last exercise, we looked at the forward/explicit Euler method, which is a first order method.
It is perhaps the simplest numerical integrator or solver one can come up with and it is quite effective in its own right.
However, for complicated systems one may need to break out heavier machinery to perform calculations accurately enough.
The forward Euler method is a first-order-in-time method, meaning that the local error it commits in each step is linear in the timestep.
When numerically solving systems in Matlab, one often uses `ode45`, which is an adaptive method combining a fourth and fifth order method.
This means that if one halves the length of the timestep, the error typically decreases with a factor 16.
With the right mathematical framework, one can develop methods that have any convergence order one could wish for, but the trade-off is that more accurate methods typically require more computation per timestep.
In this exercise, we will work with second order methods and use tools that can at least in principle be extended to work with even higher order methods.


Problem 1 - Derivation of the consistency and order conditions
==============================================================

In this problem, we will compute the conditions that a second order numerical method must satisfy for the method to actually be second order.
This is essentially done through a Taylor expansion of the dynamical system.

Consider the system

.. math::

    \dot{y} = f(t, y)

A general two-stage explicit Runge-Kutta method can be compactly described with the Butcher table

.. math::

    \begin{array}{c|cc}
        0 & &\\
        c_2 & a_{21} & \\
        \hline
          & b_1 & b_2
    \end{array}

This can also be written for a step from :math:`y_n = y(t_n)` to :math:`y_{n+1} = y(t_n + h)` in the equation form

.. math::

    k_1 &= f(t_n, y_n)

    k_2 &= f(t_n + c_2 h, y_n + h a_{21} k_1)

    y_{n+1} &= y_n + h \left( b_1 k_1 + b_2 k_2 \right)


.. admonition:: Tasks

    a) Find the Taylor expansion of :math:`y(t_n + h)` to the second order in :math:`h`.

    .. hint::
        :class: dropdown

        You may use that

        .. math::

            \ddot{y} = \frac{\partial f}{\partial t} + \frac{\partial f}{\partial y} f = f_t + f_y f

    b) Find the Taylor expansion of the 2-stage RK expression for :math:`y_{n+1}`.

    c) Find what the coefficients :math:`a_{21}, b_1, b_2` and :math:`c_2` must be for the Taylor expansions to agree to the second order.

    .. hint::
        :class: dropdown

        By "agree" we mean that the :math:`h`- and :math:`h^2`-terms in both Taylor expansions should have the same values.
    
    d) Verify that Heun's method (also called modified/improved Euler) and the Midpoint method satisfy the conditions in task c.

    .. note::
        :class: dropdown

        .. math::

            \text{Heun's method:}\quad
            \begin{array}{c|cc}
                0 & \\
                1 & 1 & \\
                \hline
                & \frac12 & \frac12
            \end{array}
            \\
            \text{Midpoint method:}\quad
            \begin{array}{c|cc}
                0 & \\
                \frac12 & \frac12 & \\
                \hline
                & 0 & 1
            \end{array}

.. note::

    There is a lot of algebra involved with developing these expressions, so we will not try to do this by hand for higher order methods.
    However, if we wanted to, we could compute higher order terms in the Taylor expansions and get more accurate methods.
    Typically, we would need to calculate more stages, since we need additional terms to match the coefficients in the Taylor series of :math:`y(t_n + h)`.



Problem 2 - Stability of explicit methods
=========================================

An important concept in numerical simulations is the stability of the methods.
A shorter timestep :math:`h` yields more accurate simulations, but are there any limits to how large we can take the timestep to be?
Phrased differently: when do our models break down?
In order to analyze this, people developed A-stability, which tests the "absolute stability" of the method.
To analyze this, we use the prototypical linear ordinary differential equation

.. math::

    \dot{y} = \lambda y, \quad \lambda \in \mathbb{C}

and see what conditions we must put on our timestep for any given :math:`\lambda`.

An explicit RK method will always define an update to get the next timestep, called the stability function, on the form

.. math::

    y_{n+1} = R(z) y_n, \quad z = h\lambda

and we way that the method is stable for :math:`z` if it is the case that :math:`|R(z)| \leq 1`.

.. admonition:: Tasks

    a.

        Find the stability function :math:`R(z)` for explicit Euler, Heun's method and the Midpoint method.

    b.
    
        Restrict :math:`\lambda` to being only real, that is :math:`\lambda = a + 0i`. For which values of :math:`a` is :math:`\lambda` in the stability region for each method? Compute :math:`\lambda` as a function of :math:`h`.

        .. hint::
            :class: dropdown

            The timestep :math:`h` has to feature since the input to the stability function should be :math:`z = h\lambda`.
        
    c.
    
        (Optional?) Plot the stability functions for each method. Also plot the stability function for the fourth order classical Runge-Kutta method given in the note below. The plot should distinguish between inputs where :math:`|R(z)| \leq 1` and :math:`|R(z)| > 1`.

        .. note::
            :class: dropdown

            The Runge-Kutta 4 scheme has the Butcher table:

            .. math::

                    \begin{array}{c|cccc}
                        0 & \\
                        \frac12 & \frac 12 & \\
                        \frac12 & & \frac12 & \\
                        1 & & & 1 & \\
                        \hline
                        & \frac16 & \frac 13 & \frac13 & \frac13
                    \end{array}

            You could calculate the stability function, but you may simply use the result that it would be:

            .. math::

                R_{RK4}(z) = 1 + z + \frac{z^2}{2!} + \frac{z^3}{3!} + \frac{z^4}{4!}


Problem 3 - Simulating the damped nonlinear oscillator
======================================================

.. math::

    \ddot{\theta} + 2 \xi \omega_0 \dot{\theta} + \omega_0^2 \sin(\theta) = 0

We will use the parameters :math:`\omega_0 = 10` and :math:`\xi = 0.02`, as well as the initial conditions :math:`\theta(0) = 1` and :math:`\dot{\theta}(0) = 0`.

Also, note that we can transform a second order ODE to a system of first order ODEs.
By setting :math:`y_1 = \theta` and :math:`y_2 = \dot{\theta}`, we get the transformed system as

.. math::

    \dot{y_1} &= y_2

    \dot{y_2} &= -2\xi \omega_0 y_2 + \omega_0^2 \sin(y_1)

with the initial conditions :math:`y_1(0) = \theta(0), y_2(0) = \dot{\theta}(0)`.

.. admonition:: Tasks

    a.

        Implement Heun's method and the Midpoint method.
    
    b.

        Obtain a reference solution.

        .. hint::
            :class: dropdown

            If we had a problem for which we knew the analytical solution, we could set :math:`y_{ref} = y_{analytical}`.
            This would be the case for the simpler non-damped linear (harmonic) oscillator defined by :math:`\ddot{\theta} + \omega^2 \theta = 0`.
            Its solution for the same initial conditions as above would simply be :math:`\theta(t) = \cos(\omega t)`.

            We have a more complicated problem, so we would need to do something else if we wanted a reference solution.
            One way is to use another (more expensive) simulator to get a high-fidelity numerical solution that we expect to be so accurate that the difference between it and the actual true solution is negligible compared to how our own numerical approximation fares.
            You may for instance use SciPy's ``solve_ivp`` or Matlab's ``ode45``.
            
            Remember to force evaluation at the same times as your fixed-step solvers evaluate.
            Also, if the methods for generating the reference solution requires a timestep, use a very small timestep.
            This will be important for the next task.

    c.

        Compute solutions for :math:`h = 2^{-i}` for some integers :math:`i`, with both explicit Euler, Heun's and Midpoint.
        Typically, we want .5, .25, .125, .0625 and so on...
        Compute also the error :math:`E(h) = \|y_{num}(T) - y_{ref}(T)\|` in the :math:`\infty`-norm and 2-norm.
        Plot the errors for each method on a  log-log plot, observe roughly what convergence rate the methods have.

        .. hint::
            :class: dropdown

            For a :math:`p`-th order method, the error should follow the relation :math:`E(h) \approx C h^p`, where :math:`C` is some constant that only depends on which exact method is being used (but not on the stepsize itself).
            If this is the case, then one can compute the `empirical convergence order` with the formula

            .. math::

                p \approx \frac{\log(E(h_1) / E(h_2))}{\log(h_1 / h_2)} 








Problem 4 (optional) - Adaptive timestep control
================================================

All the methods we have seen so far have been so-called "fixed step methods".
That is, the methods use just one timestep length over the entire simulation.
However, with both a low-order and a high-order method (first and second order in our case), we can set up a simple predictor-corrector scheme to adaptively resize the simulation timestep during simulation.

Let :math:`y_{n+1}^{(1)}` be the first order numerical approximation and :math:`y_{n+1}^{(2)}` be the second order approximation.
These can be computed, for instance, with explicit Euler and Heun's method, but you are free to select the second order method.
The crucial part is figuring out that if the two approximations are close, then we don't gain much from using the second order method over the first order one.
That, in turn, means that we can increase the timestep so that the second order method actually does some useful work for us.
For this we need the relative error between the methods, given by

.. math::

    e = \frac{\|y_{n+1}^{(2)} - y_{n+1}^{(1)}\|}{\|y_{n+1}^{(2)}\|}

After this, we need a control law for adjusting the timestep.
You may come up with your own, or you may use this one:

.. math::

    h_{new} = \alpha \cdot h \cdot \sqrt{\frac{\text{tol}}{e}}

Here, :math:`\alpha` is a safety factor so that our resizing is not too wild, and :math:`\text{tol}` is the tolerance level we set for when we accept a timestep.
So if :math:`e \leq \text{tol}` we accept the step, adjust the timestep for the next iteration with the formula above and move on.
If not, we reduce the stepsize using the same formula and try the current step again.
You may also want to limit the growth or shrinkage of the timestep, and maybe also the minimum and maximum allowed timestep.

.. admonition:: Tasks

    a.
        
        Implement the predictor-corrector scheme and simulate the oscillator from problem 3.

    b. 
    
        Make a plot showing the stepsize over time.

    c.
    
        Compare the total number of function evaluations between the adaptive scheme and the fixed step method you choose. Make sure that the comparison is fair, meaning that both methods should have a comparable final error.