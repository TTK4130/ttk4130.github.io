=========================================
Assignment 3 - Implicit Numerical Solvers
=========================================

.. note::

    Submit your assignment as a single PDF, including plots and source code (if any).
    We expect academic honesty. Collaboration is encouraged, but must be declared. Any use of AI must be declared along with any other sources used.
    This is not an exam. Do your best and show that you put in effort and the assignment will be approved.

In this exercise we will look at implicit solvers, which can roughly be identified as solvers where the next step :math:`y_{n+1}` is dependent on *itself*.
The simplest of these is the *backward Euler*, also called the *implicit Euler* method.
We can look at the forward and the backward Euler methods side by side, given as:

.. math::

    \text{Forward Euler: } y_{n+1} = y_n + h f(t_n, y_n)

    \text{Backward Euler: } y_{n+1} = y_n + h f(t_{n+1}, y_{n+1})

Notice that :math:`y_{n+1}` appears on both sides of the equality, this is the essence of what makes it *implicit*.

.. important:: Link to the "Numerical Methods for ODEs" on the website

    Both here and in the previous assignment, we go over things that may already be stated in :ref:`numerical-methods-for-odes`.
    Instead of repeating it here, we should either link to the relevant section on that page, or expand that page to include the general material we need and *then* link it.


Problem 1 - Newton solver
=========================

When dealing with implicit solvers, we have to do something to shake the solution out.
If we have a linear system, this generally means that we have to invert a matrix.
Consider for instance the linear system :math:`\dot{y} = Ay` with the implicit Euler method.
This can be written in the matrix-equation form

.. math::

    (I + hA) y_{n+1} = y_n

which can be solved by finding the inverse of the matrix :math:`I - hA`.
However, for a non-linear system, where we really need to evaluate some right-hand side function :math:`f(t_{n+1}, y_{n+1})`, we're not so lucky.
But all is not lost, Isaac Newton and Joseph Raphson found a nice numerical algorithm that can be used to solve *even* non-linear systems.
There are many other methods that can do this, that is, other fixed point methods and root finding algorithms, but Newton-Raphson is a simple but effective one, and usually sufficient and performant for the systems we investigate.

.. admonition:: Tasks

    a. 
    
        Implement the Newton-Raphson method (also simply known as Newton's method) for an arbitrary function :math:`f(t, y)`. The inputs to the function should include the initial guess :math:`(t_0, x_0)`, the function :math:`f(t, x)` and its Jacobian :math:`J_f(t, x)`.

        .. hint::
            :class: dropdown

            In order to verify that you have implemented the method correctly, you can try to find the roots of a polynomial you know the answer to. For instance, the polynomial

            .. math::

                (x_1 + 1)^3 + (x_2 + 1)^3 + (x_3 + 1)^3

            should have all its roots at :math:`x_1 = x_2 = x_3 = -1`. Since it is a polynomial, the analytical evaluation of the Jacobian should be straightforward to compute.


Problem 2 - Implicit Euler and Midpoint
=======================================

With a working Newton solver, we can continue with implementing implicit solvers.
The two we are going to take a look at are the implicit Euler method and the implicit Midpoint method.
These methods have Butcher tables

.. math::

    \text{Implicit Euler:}\quad
    \begin{array}{c|c}
        1 & 1 \\
        \hline
        & 1
    \end{array}
    \\
    \text{Implicit Midpoint:}\quad
    \begin{array}{c|c}
        \frac12 & \frac12\\
        \hline
         & 1
    \end{array}

When you test your implementation of these solvers, use the harmonic oscillator as a test-case.
The harmonic oscillator is a simplification of the damped non-linear oscillator from the previous assignment, where we remove the damping term and use the small-angle approximation (:math:`\sin(\theta) = \theta`) to remove the non-linearity.
This leaves us with the equation

.. math::

    \ddot{\theta} + \omega^2 \theta = 0

With initial conditions :math:`\theta(0) = 1, \dot{\theta}(0) = 0`, we get that the analytical solution is simply

.. math::

    y(t) = \cos(\omega t)

This allows us to use the analytical solution directly when determining the error and convergence order of the implemented methods, even when the simulation time is very long.
To make things even simpler, we will set :math:`\omega = 1`.

.. note::
    :class: dropdown

    You may have observed that this is actually a linear system, and thus we could "just invert the matrix" to get the answer and not bother with the non-linear solver. 
    This is correct, but developing a general non-linear solver will be useful for future assignments where things may not longer be the case.


.. admonition:: Tasks

    a. 
    
        Implement implicit Euler using the Newton solver you programmed in the previous problem.

    b. 
    
        Implement implicit Midpoint using the Newton solver you programmed in the previous problem.

        .. hint::
            :class: dropdown

            The half-step in the implicit Midpoint can be a bit tricky to figure out. It turns out it is possible to think of the implicit midpoint as an implicit Euler half-step from :math:`y_n` to :math:`y_{n+\frac12}`, and then an *explicit* Euler half-step from :math:`y_{n+\frac12}` to :math:`y_{n+1}`. This is really where the midpoint method gets its name, since :math:`y_{n+\frac12}` *is* the midpoint.
    
    c. 
    
        (Optional? Or even remove?) Find the experimental order of convergence for both methods. Is this unexpected considering that both methods are one-stage methods?

    d. 
    
        Simulate the harmonic oscillator with a fairly large timestep (maybe :math:`h = 0.1`) and for a "long" time (maybe :math:`t_f = 10`). Do this for both the explicit Euler, the implicit Euler and the implicit Midpoint method, then compare each solution with the analytical solution. What do the different methods do? Are they able to simulate the system for those solver parameters?
        
        .. The behavior of the implicit Midpoint method is qualitatively different as it is a collocation method and thus a symplectic integrator. This means that it numerically preserves the energy of a perturbed Hamiltonian and since the harmonic oscillator admits a Hamiltonian formulation (or equivalently an unconstrained Lagrangian formulation due to the Legendre transform) and thus its long term behavior is quite different. We could expand slightly on this if we want to, but I suspect that control engineers more often work with constrained Lagrangians, hence their systems do not *have* a symplectic geometry, rendering this point irrelevant. Though it is quite nice. 


Problem 3 - Stability and stiff systems
=======================================

In the previous assignment, we looked at the stability of explicit methods.
With a similar treatment of implicit methods, we hope it will be clear why one might be interested in implicit methods.
Not only that, but maybe you will get an intuition for what separates A- and L-stability.

In this problem, we will look at a known stiff system described by

.. math::
    \dot{x}_1 = - 0.5 x_1 + 20 x_2
    \\
    \dot{x}_2 = - 20 x_2

with initial conditions :math:`x_1(0) = 0, x_2(0) = 1`.

One way to observe that it is stiff is that the behavior of the system will be very different when :math:`x_2` is large and when it is small.
It is the case that :math:`x_2` will decay very quickly due to the coefficient :math:`-20`, but during the decay :math:`x_1` will increase roughly as fast as :math:`x_2` decays.
When :math:`x_2` no longer contributes much, when it has become small, :math:`x_1` will also decay, but much slower due to the coefficient :math:`-0.5`.


.. admonition:: Tasks

    a. 
    
        Define stiff systems in your own words.

        .. hint::
            :class: dropdown

            There is no precise mathematical definition of stiffness, and most attempts at defining it defer to general statements about when the "phenomenon of stiffness" appears in a numerical solution.
            Reflect over what you think it means for a system to "be stiff".
    
    b. 
    
        Find the stability functions for the implicit Euler and the implicit Midpoint method.

    c. 
    
        Plot the stability functions for both methods and conclude whether they are A-stable. Also, are any of the methods L-stable?

    d. 
    
        Use both the explicit Euler, implicit Euler and the implicit Midpoint methods to numerically solve the stiff system
        Increase the stepsize from :math:`h = 0.01` to :math:`h = 0.1` and describe what you observe.
        Include a plot of :math:`x_1` over time for each of the methods for :math:`h = 0.1`.
    
    e. 
    
        What do you think is the main concerns one should address when choosing a numerical solver?

        .. hint::
            :class: dropdown

            Some keywords may be *accuracy*, *stability*, *computational cost* and *solver properties*.
    
    f.

        (Optional) If you implemented an adaptive controller for the timestep in the previous assignment, try to use it to simulate the system and see what timesteps it selects. Are the selected timesteps reasonable?


.. Problem 4 (optional) - Collocation methods and symplectic integrators
.. =====================================================================

.. Note: I abandoned this task since it became clear that it was less applicable to control problems than I thought.
.. It is most useful for unconstrained Lagrangian/Hamiltonian systems, but in reality we often constrain our systems.
.. The text is left here as a WIP so that the problem may be posed at some point, if someone thinks hard enough about it.

.. There are two main reasons to care about collocation methods.
.. The first is that if the collocation points are well chosen, the order to the method can be much higher than anticipated.
.. Generally for an :math:`s`-stage Runge-Kutta method, we expect the accuracy or convergence to be of order :math:`s`.
.. However, with the Gauss-Legendre collocation points, this increases to :math:`2s`.
.. This is phenomenal, as we can get with two stages what an explicit method would require *four* stages to accomplish.
.. Of course, we still have to sovle a possibly non-linear system, so the computational cost may still be much higher than an explicit method.
.. Typically it will be.

.. The second reason to care about collocation methods is that they are also *symplectic integrators*, which means that they will approximately conserve the energy of a Hamiltonian system, if you were to use the method for simulating a Hamiltonian system.
.. Hamiltonian dynamics is not something we will go into in this course, but it is a general result that all Lagrangian systems admit a Hamiltonian formulation.
.. And we *will* go into Lagrangians in this course!


.. .. admonition:: Tasks (I of II)

..     a.

..         If you have done the previous problems, you will have an implementation of the implicit Midpoint method, which is the one-stage Gauss-Legendre collocation method. Now, implement the two-stage Gauss-Legendre collocation method given in the Butcher table above.

..     b.

..         Verify that the orders of convergence actually are what we say it will be; that is second order for the implicit Midpoint method and fourth order for the two-stage Gauss-Legendre method.


.. Both of these methods are implicit, but it would be nice to have an explicit symplectic integrator as well. Such methods do exist, and the simplest one is called the Størmer-Verlet method in reference to the french physicist Loup Verlet who used it for molecular dynamics in the 1960s and the Norwegian astrophysicist Carl Størmer who used it to study the trajectory of electrical particles in a magnetic field in 1907.

.. Anyways, the Størmer-Verlet integrator (often also simply called the Verlet integrator) is meant for applciation to second order ODEs, for example those that arise from Newton's equations of motion. Explicit symplectic integrators can be developed for other systems, but we often find ourselves tinkering with Newton's laws, so it may make a fine addition to a cyberneticist's or control engineer's collection.

.. One slight issue is that the scheme requires that we can write our system as a "decoupled" one, in the sense that

.. .. math::

..     \dot{x} = f(t, v),
..     \quad
..     \dot{v} = g(t, x).

.. This rules out systems like the damped non-linear oscillator from the previous assignment specifically due to the damping term.
.. However, the harmonic oscillator *does* admit such a formulation since

.. .. math::

..     \dot{x} = v,
..     \quad
..     \dot{v} = -\omega^2 x.

.. .. important:: Semi-implicit Euler

..     This is not the Størmer-Verlet integrator, but the Semi-implicit Euler scheme.

..     The point with this problem should be to give some indication that splitting the update steps and generally doing clever things in the scheme may actually lead to useful additional properties.


.. If we have a system with :math:`f` and :math:`g` as above, then the semi-implicit Euler scheme can be written as

.. .. math::

..     v_{n+1} = v_n + h \cdot g(t_n, x_n)
..     \\
..     x_{n+1} = x_n + h \cdot f(t_n, v_{n+1})



.. .. admonition:: Tasks (II of II)

..     c.

..         Implement the Størmer-Verlet integrator and verify its order of convergence.

..     d.

..         Numerically verify that it is indeed symplectic by simulating the harmonic oscillator for a long time.


Problem 4 (optional) - General IRK methods
==========================================

By now, we have dealt with a large number of Runge-Kutta methods, all of which can be represented with a Butcher table.
Maybe the time is right to implement a general routine that can take any Butcher table and perform the corresponding RK method?
In general, an RK method will then look like

.. math::

    \begin{array}{c|c}
    \vec{c} & A \\
    \hline
     & \vec{b}
    \end{array}

where :math:`A` defines the linear combination of the stages inside the ODE right-hand side evaluations, :math:`b` is the final linear combination of stages to get the next step and :math:`c` is the vector of appropriate time offsets.
Until now, the time offsets have not been very important, since our systems have been *autonomous*, but often in real life, the forces we're subjected to change not only in space, but also time, so it *is* important.

Let us consider the system

.. math::

    \dot{x}_1 = -\lambda_1 x_1 + A_1 \cos(\omega_1 t),
    \\
    \dot{x_2} = -\lambda_2 x_2 + A_2 \cos(\omega_2 t).

It is not a system of homogeneous ODEs since it has the cosine driving term, which makes it non-autonomous.
The ODEs are decoupled, so they can be solved one at a time using an integrating factor, which gives the solution

.. math::

    x_i(t) = \frac{A_i (\lambda_i \cos(\omega_i t) + \omega_i \sin(\omega_i t))}{\lambda_i^2 + \omega_i^2} + e^{-\lambda_i t} \left( y_0 - \frac{A_i\lambda_i}{\lambda_i^2 + \omega_i^2} \right)

To test that the general IRK implementation is correct, you may of course compare the performance between your hard-coded previous implementations to the general scheme, but you may also test it on an RK method you haven't implemented yet: the two-stage Gauss-Legendre collocation method.
This method is given by the vectors and matrices:

.. math::

    A = \begin{pmatrix}
    \frac14 & \frac14 - \frac{\sqrt3}{6} \\
    \frac14 + \frac{\sqrt3}{6} & \frac 14
    \end{pmatrix},
    \quad
    \vec{b} = \begin{pmatrix}
    \frac12 \\ \frac12
    \end{pmatrix},
    \quad
    \vec{c} = \begin{pmatrix}
    \frac12 - \frac{\sqrt3}{6} \\ \frac12 + \frac{\sqrt3}{6}
    \end{pmatrix}.

Since it is a collocation method, it should have twice the convergence order one would expect.
As a two-stage method, it should then be a fourth order accurate method, which you can numerically verify by computing the experimental order of convergence.

.. admonition:: Tasks

    a.

        Implement a function that applies a general IRK method to a system defined by its right-hand side function :math:`f(t, x)` and the Jacobian of this function :math:`J_f(t, x)`. The general IRK function should handle state vectors of arbitrary dimensions and an arbitrary number of implicit or explicit stages.
    
    b.

        Both explicit and implicit RK methods can be described by Butcher tables. Hoever, it is wasteful to use the Newton on a known explicit scheme, since it can be sovled with a forward pass through the stages. Extend your general code to detect whether the Newton solver is required or not.

        .. hint::
            :class: dropdown

            One only needs to investigate the :math:`A`-matrix do determine whether the RK method is implicit or explicit. What is the condition :math:`A` must satisfy? 

    c.

        There is a third "type" of Runge-Kutta methods hidden in this general approach, the so-called *diagonally-implicit Runge-Kutta* methods, or DIRK among friends. The major innovation here is that while the DIRK is implicit, any stage :math:`p` is only dependent on the :math:`p-1` stages *before* it. This means that we do not need to solve for all stages simultaneous, but can solve one at a time, until we get to the last one. Extend your general IRK function to handle this case, as well, possibly saving some precious computational time.

        .. hint::
            :class: dropdown

            There is also a special condition the :math:`A`-matrix must satisfy here if the scheme is to be a DIRK. What is it?

