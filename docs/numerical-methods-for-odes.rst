==========================
Numerical Methods for ODEs
==========================


Learning Objectives
===================

After reading this chapter the reader should know:

- What constitutes an initial value problem (IVP)
- Common methods and libraries for solving IVPs
- Implicit and explicit equations
- How to implement explicit and implicit ODE methods
- Challenges and pitfalls that can be encountered in numerical simulations


Introduction
============
The majority of the material presented in this chapter is based on :cite:t:`gros2011`.
The goal of this chapter is therefore to present the contents in a more practical manner. We'll start
by defining the initial value problem and common ways to solve ODEs in Python. We'll then look at the
theory behind numerical methods and its limitations.

Initial Value Problems (IVP)
============================

Throughout your studies you've encountered numerous ordinary differential equations (ODEs) of many shapes and orders.
When we are solving ODEs given a set of initial conditions we are solving an *initial value problem* (IVP). It's solution
often yields equations which specify how a system changes over time. Formally, we can define an initial value problem as a function

.. math::
    y'(t) = f(t, y(t)), \quad f: \Omega \subset \mathbb{R} \times \mathbb{R}^n \to \mathbb{R}^n \quad

where :math:`\Omega` is an open set of :math:`\mathbb{R} \times \mathbb{R}^n` together with a point in the domain :math:`(t_0, y_0) \in \Omega` called the initial condition.
A solution to the initial value problem is a function :math:`y` that solves the differential equation and satisfies :math:`y_0(t_0) = y_0`. We can express a higher order initial value problem by treating
the derivative as an independent function, :math:`y''(t)=f(t,y(t),y'(t))`. In this manner we can represent an N-order
differential equation as a set of N first order differential equations. An example of an initial value problem is the ordinary differential equation

.. math::
    \dot{x} = -ax, \quad x(t_0) = x_0

We recognize the solution to this IVP as the solution :math:`x(t) = x_0\ e^{-at}`. We can show this in many ways, but how might we use python to solve this ODE algebraically?
We can use the SymPy method :code:`dsolve`

.. jupyter-execute::

   import sympy as sm
   sm.init_printing(use_latex='mathjax')
   x = sm.Function('x')
   a, t = sm.symbols('a t')
   lhs = x(t).diff(t) + a*x(t) # Define left-hand side
   result = sm.dsolve(lhs)
   result

We can also specify the the initial conditions with the argument :code:`ics` (initial conditions).

.. jupyter-execute::

   x0 = sm.symbols('x0')
   result = sm.dsolve(lhs, ics={x(t).subs(t, 0): x0})
   result

.. admonition:: Exercise
    :class: dropdown

    Solve the differential equation :math:`\ddot{x} = -\dot{x} -x, \quad \dot{x}(0) = \frac{-x_0}{2}, \quad x(0) = x_0` using SymPy.

    .. hint::
        :class: dropdown

        You can use ``checkodesol`` to check your solution. See SymPy docs.

.. dropdown:: Solution
    :color: success

    .. jupyter-execute::

       import sympy as sm
       sm.init_printing(use_latex='mathjax')
       x = sm.Function('x')
       t, x0= sm.symbols('t x0')
       lhs = sm.Derivative(x(t), t, 2) + x(t).diff(t) + x(t) # Define left-hand side
       result = sm.dsolve(lhs, ics={x(t).diff(t).subs(t,0): -x0/2, x(t).subs(t, 0): x0})
       result = result.simplify() #This is fine, but we can simplify it further
       print(sm.checkodesol(lhs, result))
       result

For a more comprehensive tutorial on solving ODEs algebraically in SymPy, see `the official documentation <https://docs.sympy.org/latest/guides/solving/solve-ode.html>`_.
When working with complex models ODEs can become unpractical or even impossible to solve analytically. In that case we might want to use a numerical method to approximate a solution of the initial value problem.
For many practical applications a numerical approximation is often sufficient. A common solver often used in Python is the SciPy ODE solver :code:`solve_ivp`.

Example: Solving ODEs with SciPy ``solve_ivp``
==============================================

In this example we'll demonstrate how to numerically solve the IVP :math:`\ddot{x} + 9x, \quad x(0) = 1, \quad \dot{x}(0) = 0`. You're encouraged to code along.
We first have to separate the second order ODE into two first order ODEs.

.. math::

    \dot{x}_1 = x_2, \quad\dot{x}_2 = -9x_1 \newline
    \newline
    \frac{d}{dt} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} x_2 \\ -9x_1 \end{bmatrix}

We can then define the system in python as a 2-dimensional first order ODE in `system`.

.. jupyter-execute::

    import numpy as np
    from scipy.integrate import solve_ivp
    import matplotlib.pyplot as plt

    def system(t, X):
        return [X[1], -9*X[0]]

Initial conditions are set as :math:`x(0) = 1` and :math:`x'(0) = 0`:

.. jupyter-execute::

    x0 = [1, 0]

We specify the time span for the solution from 0 to 10 seconds:

.. jupyter-execute::

    t_span = (0, 10)
    t_eval = np.linspace(0, 10, 100)

Solve the differential equation using SciPy's `solve_ivp`:

.. jupyter-execute::

    solu = solve_ivp(system, t_span, x0, t_eval=t_eval)

Plot the solution to visualize x(t):

.. jupyter-execute::

    plt.figure(figsize=(10, 5))
    plt.plot(solu.t, solu.y[0], label='x(t) - SciPy Solution', color='blue')
    plt.title('Solution of the ODE with SciPy')
    plt.xlabel('Time (t)')
    plt.ylabel('x(t)')
    plt.legend()
    plt.grid()
    plt.show()

By solving this algebraically with SymPy we can examine the error:

.. jupyter-execute::

    z = sm.Function('z')
    k = sm.symbols('k')
    lhs = sm.Derivative(z(k), k,2) + 9*z(k)
    result = sm.dsolve(lhs, ics={z(k).diff(k).subs(k, 0): x0[1], z(k).subs(k, 0): x0[0]})
    result

We can then calculate the error and plot it:

.. jupyter-execute::

    algebraic_solution_func = sm.lambdify(k, result.rhs, 'numpy')
    algebraic_solution = algebraic_solution_func(solu.t)

    error = solu.y[0] - algebraic_solution
    plt.figure(figsize=(10, 5))
    plt.plot(solu.t, error, label='e(t) - SciPy Solution Error', color='blue')
    plt.title('Solution error of the ODE with SciPy')
    plt.xlabel('Time (t)')
    plt.ylabel('e(t)')
    plt.legend()
    plt.grid()
    plt.show()


Although the error is quite small, we can see that it's steadily grows as the integration
errors accumulates. In the next sections we'll look at how numerical methods are implemented
and their limitations. We'll start by looking at Euler's method.


.. admonition:: Exercise
    :class: dropdown

    Simulate the 2-dimensional system of equations :math:`t \in [0, 10]` using SciPy `solve_ivp`.

    .. math::
        \dot{x} = Ax + Bu, \quad A = \begin{bmatrix} -1 & 2 \\ 0 & 1 \end{bmatrix}, \quad B = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad u(t) = \sin(t)


Explicit Euler (ERK)
====================

The explict Euler method, also called the forward Euler method, is really the simplest numerical scheme there is.
We need two ingredients, the initial value problem we defined earlier and the definition of the derivative:

.. math::

    \dot{x} &= f(t, x)

    \dot{x} &= \lim_{h \to 0} \frac{x_{n+1} - x_n}{h}

Armed with these two, we can first say that a good approximation to the derivative :math:`\dot{x}` is the *finite difference*

.. math::

    \dot{x} \approx \frac{x_{n+1} - x_n}{h}

This is a first order approximation to the derivative, which means that the explicit Euler method is a first order method.
If we wanted higher order methods, we could design (and you will do this in the assignments) schemes that are hiigher order approximations to the derivative.
But, at any rate, we need to relate this to the function :math:`f(t, x)` if we are going to be able to solve it.
In this contex, the forward Euler method is defined as:

.. math::

    \frac{x_{n+1} - x_n}{h} = f(t_n, x_n)

With some algebra, this can be worked into the form:

.. math::

    x_{n+1} = x_n + h f(t_n, x_n)

This gives a rule as to how we update the *next step* :math:`x_{n+1}` using what we already know, namely the current step :math:`x_n` and the time.
If we apply this method to the model problem :math:`\dot{x} = \lambda x`, we get that

.. math::
    x_{n+1} = x_n + h \lambda x_n = (1 + h\lambda) x_n

This model problem has the familiar solution :math:`x_0 e^{\lambda t}` for some initial condition :math:`x_0` and is not all that interesting in itself.
However, this is a simple problem we can use to test the stability of numerical methods, which we also work with in the assignment on numerical solution.
In the next section we will look at another method that looks very much like the forward Euler method, but is actually slightly different.

Implicit Euler (IRK)
====================

The implicit Euler method, or the backward Euler method, is a close cousin to the forward method.
In fact, the only difference between the two is an index!
Still using the same notation that :math:`\dot{x} = f(t, x)` and that :math:`\dot{x} \approx \frac{x_{n+1} - x_n}{h}`, we define the backward euler method as

.. math::
    :label: backward_euler_general

    x_{n+1} = x_n + h f(t_{n+1}, x_{n+1})

The only difference is that the *next step* :math:`x_{n+1}` features inside the function defining the system dynamics.
In the case of the model problem, this is no issue, since we get that

.. math::

    x_{n+1} = x_n + h\lambda x_{n+1} \Rightarrow x_{n+1} = \frac{x_n}{1 - h\lambda}

However, this becomes much more complicated if the system dynamics is a vector valued function that may depend on the state :math:`x_{n+1}` nonlinearly.
In general, we're stuch with the formulation in :eq:`backward_euler_general`.
We would be albe to find the next step only if we *already had it*, which means that for implicit methods we need additional machinery to wring some answers out of them.
Conveniently, we discuss this in the section below.

Implicit equations
===================

By implicit equation, we mean an equation that describes a relationship, but where the symbols cannot be rearranged to isolate the unknown quantity.
This ties together with the lsat section where we found an equation where the unknown quantity :math:`x{n+1}` featured in an expression that may not have a known inverse.
So we're stuck with the equation on the form

.. math::

    x_{n+1} = x_n + h f(t_{n+1}, x_{n+1})

This equation is on a form known as a *fixed point formulation*, where the defining feature is that if we input the exactly correct :math:`x_{n+1}` into the righthand side, we get that same value back on the lefthand side.
This is good news, as there are many methods to find the solutions to such problems (the so-called *fixed points*)!

Fixed point methods
-------------------

The general form of such problems are

.. admonition:: Fixed point problems

    Given a function :math:`G(x)`, find a point :math:`x^*` such that

    .. math::
        x^* = G(x^*)

If we take :math:`x_n` and :math:`t_{n+1}` as constants for our problem above, we get a problem of this kind if we say that :math:`x^* = x_{n+1}`.
At least the mathematicians are happy with that formualtion (probably).
The iteration in this type of problem comes from the fact that in many cases, we can define the function :math:`G(x)` in such a way that we can set up a chain of guesses to the solution, or that for a sufficient initial guess :math:`x_0`, we can prove that repeatedly applying :math:`G` in the sense that

.. math::
    x_{n+1} = G(x_n)

eventually reaches the (or rather a) fixed point solution :math:`x^*`.
In this situation, we could write that

.. math::
    x^* = \lim_{n \to \infty} x_{n+1} = \lim_{n \to \infty} G^{n}(x_0)

Root-finding problems
---------------------

A closely related method for finding solutions to (nonlinear) implicit equations is the method of root finding.
In this type of approach, we try to identify the zero of a function.
The general form here is

.. admonition:: Root-finding problems

    Given a function :math:`F(x)`, find a point :math:`x^*` such that

    .. math::
        F(x^*) = 0

The name *root-finding* is motivated by polynomials, where we say that the zeros of a polynomial are its roots.
Thus, in the literature, you may find such methods refered to as "root-finding", even though they are concerned with the zeros of a function.
Also, if we spend some time thinking, we can see that it is possible to turn a fixed point problem into a root-finding problem.
If we set :math:`F(x) = x - G(x)`, we obtain that a fixed point :math:`x^*` of :math:`G` is also a root (or zero point) of :math:`F`!
It is also possible to go the other way and converting a root-finding problem into a fixed point problem.
The quickest way to go about it may be to add the input :math:`x` to both sides.
However, this does not always result in a fixed point formualtion which lends itself well to iteration.

Newton's method
---------------

Newton's method is one of several methods one can use to find the zero points of a function.
Some good sources describing the method in greater detail can be found
in LibreTexts :cite:`calculus_openstax_2016` or Wikipedia :cite:`newtons_method_wikipedia_2025`.

The main idea of the method is to use the tangent line as an approximation to the function in question, so that we can successively find better guesses to the root.
For a function :math:`f(x)`, we can use the derivative of the function :math:`f'(x)` to set up the following fixed point scheme:

.. math::
    x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}

As long as :math:`f'(x_n) \neq 0` and the initial guess :math:`x_0` is not too far off, this method will usually converge.
By rearranging the expression slightly, we can say that the update to the point :math:`\Delta x_{n+1}` is equal to

.. math::
    \Delta x_{n+1} = x_{n+1} - x_n = - \frac{f(x_n)}{f'(x_n)}

Thus, if we're close to a fixed point, the update will be small.
This is great news as we can use this as a measure for convergence.
If we set a tolerance level :math:`\text{tol}`, we can say that if

.. math::

    \bigg| - \frac{f(x_n)}{f'(x_n)} \bigg| < \text{tol}

then we accept the point :math:`x_{n+1}` as a solution.
This is starting to sound like an algorithm we could implement for ourselves and use in potential implicit Runge-Kutta solvers.
It's been a while since we talked about those, but in the end, this is why we even need to discuss implicit equations and fixed points and all that.

At any rate, if we say that :math:`f(x_n)` can be a vector-valued function (which often is the case in our dynamical systems), then the derivative will actually be the Jacobi matrix of the function, which we will call :math:`J_f`.
In index-notation we have that

.. math::

    \left[J_f \right]_{i, j} = \frac{\partial f_i}{\partial x_j}

In this case, the division becomes *multiplication by the inverse* or that

.. math::
    x_{n+1} = x_n - J_f^{-1} f(x_n)


While it's not clear from the notation, bear in mind that the Jacobian may also be a function of :math:`x`, and so must be evaluated at the point :math:`x_n`.
Now the time is right for writing the algorithm as a function in Python, and we might get something looking like the following: 

.. jupyter-execute::

    def newtons_method(f, J_f, x_guess, TOL=1e-6, MAX_ITER = 100):
        x = x_guess
        
        for i in range(MAX_ITER):
            delta_x = np.linalg.solve(J_f(x), -f(x))
            x += delta_x
            if np.linalg.norm(delta_x) < TOL:
                break
        
        return x, {"iterations": i, "delta": delta_x}

This function will return either when the update is sufficiently small or when the maximum number of iterations is reached.
If we program a model problem to test this against, we can see whether it works.

.. jupyter-execute::

    def f(x):
        return (x + 1)**3
    
    def J_f(x):
        return np.array([
            [3 * (x[0] + 1)**2, 0, 0],
            [0, 3 * (x[1] + 1)**2, 0],
            [0, 0, 3 * (x[2] + 1)**2]])

    zero_point, diagnostic_data = newtons_method(f, J_f, np.ones((3,)))
    print(f"Zero point: {zero_point}\nNumber of iterations: {diagnostic_data['iterations']}\nDelta: {diagnostic_data['delta']}")

The code shows that the root of the function occurs when :math:`x = y = z = -1`.
It also reached the root using fewer than the allocated iterations and with a final update within the accepted level of tolerance.


Stiff Equations
===============
