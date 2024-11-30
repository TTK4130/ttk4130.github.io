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




Implicit Euler (IRK)
====================

Implicit equations
===================

Stiff Equations
===============
