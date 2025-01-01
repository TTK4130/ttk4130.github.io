==============
SymPy and CAS
==============

.. note::

    If you don't have SymPy installed you can try it in your browser with the :ref:`SymPy Live` page

SymPy Introduction
==================

This page aims to introduce you to the wonderful world of SymPy and CAS (Computer Algebra System). The code examples are based on the SciPy 2016 Conference SymPy tutorial (see :ref:`More resources on SymPy`) and the `official documentation for SymPy <https://docs.sympy.org/latest/index.html>`_. The page partly written as an interactive tutorial and you're encouraged to code along with the provide examples.


SymPy is a Python library for symbolic mathematics :cite:`Sympy2017`. Some of you may have worked with similar programs such as GeoGebra CAS, Maple, Matlab Symbolic Math Toolbox, Mathematica etc.. These type of programs are often categorized as Computer Algebra Systems or CAS. In general terms, a Computer Algebra System is any software that can manipulate mathematical expressions symbolically. This means that it manipulates expressions similar to how we do.
One of the main benefits of this is that there is no loss of precision. An example of this is irrational numbers. Any computer can evaluate the square root of two, but only with limited precision due to hardware constraints. A CAS would express the square root of two as the relationship between the operation "square root" and the integer two. By representing a mathematical expressions as the relationship between operators and numbers we don't sacrifice any precision.

SymPy Basics
=============

Importing SymPy
----------------

We can import SymPy using the following convention

.. jupyter-execute::

    import sympy as sm

Since SymPy objects are a bit difficult to interpret, we have methods of printing out mathematical expressions similar to math in a textbook.
SymPy supports several printers to output expressions. Using  :external:py:func:`~sympy.interactive.printing.init_printing` will automatically enable the best printer
in your environment. This will usually generate an image of the expression you are printing. This webpage, which uses Jupyter notebooks, uses MathJax (a JavaScript library for rendering mathematical notation) to print SymPy expressions.

.. jupyter-execute::

    sm.init_printing(use_latex='mathjax')
    x = sm.symbols('x')
    x**2

SymPy Symbols
---------------

Demonstrating the example above, we see that the square root of two has limited precision when using the :code:`math.sqrt`.

.. jupyter-execute::

    import math
    math.sqrt(2)

Using SymPy we see that the square root of two is expressed symbolically

.. jupyter-execute::

    sm.sqrt(2)

Computing the square root of 8 demonstrates the real power of SymPy, namely simplification.

.. jupyter-execute::

    sm.sqrt(8)

Mathematical symbols are created with the :external:py:func:`~sympy.core.symbol.symbols` function

.. jupyter-execute::

    x = sm.symbols('x')
    x

which creates a symbols object of the :external:py:class:`~sympy.core.symbol.Symbol` type

.. jupyter-execute::

    type(x)

We can create multiple symbols in one go with ``symbols()``, and Greek symbols spelled out are automatically recognized

.. jupyter-execute::

    alpha, beta, Alpha, Beta = sm.symbols('alpha beta Alpha Beta')
    alpha, beta, Alpha, Beta

The argument in ``symbols()`` doesn't need to match the Python variable name. We can use this to make out Python code more (or less) readable

.. jupyter-execute::

    unrelated = sm.symbols('nonsense')
    flywheel_ang_vel, flywheel_inertia = sm.symbols('omega1, I1')
    unrelated, flywheel_ang_vel, flywheel_inertia

SymPy has a compact function call to create many similar symbols

.. jupyter-execute::

    sm.symbols('x1:21')


Functions
------------

We can also define functions in addition to symbols. These are vital when setting up differential equations, where you don't know the definition of a function, but only its derivative.
Using ``Function()`` will create a function of the type ``UndefinedFunction``

.. jupyter-execute::

    x = sm.Function('x')
    type(x)

We can create a function of one of many variables

.. jupyter-execute::

    t = sm.symbols('t')
    x(t)

Using the same function...

.. jupyter-execute::

    x(t, alpha, beta)


.. admonition:: Exercise

    Create a function :math:`F(t, u)`

.. dropdown:: Solution
    :color: success

    .. jupyter-execute::

        t, u = sm.symbols('t, u')
        F = sm.Function('F')
        F(t, u)



Symbolic Expressions and Expression Trees
-----------------------------------------

Using symbolic functions and variables we can construct expressions using mathematical operators.

.. jupyter-execute::

    t, theta = sm.symbols('t, Theta')
    x = sm.Function('x')
    expr = x(t) - (t**2)/theta
    expr

Expressions will have a type ``Add, Mul or Pow``. This is because expressions are represented as trees in SymPy. This is important to know
when working with SymPy. The internal tree-structure is the reason that SymPy sometimes prints expressions in unusual ways. By using
:code:`srepr` we can see what an expression looks like internally and verify our expressions.

.. jupyter-execute::

    x, y, z = sm.symbols('x, y, z')
    expr = x**2  - 2*x*y
    expr

Internal representation:

.. jupyter-execute::

    print(sm.srepr(expr))


We can also draw a diagram of the expression tree

.. graphviz::
    :align: center

    digraph{

    # Graph style
    "ordering"="out"
    "rankdir"="TD"

    #########
    # Nodes #
    #########

    "Add(Pow(Symbol('x'), Integer(2)), Mul(Integer(-2), Symbol('x'), Symbol('y')))_()" ["color"="black", "label"="Add", "shape"="ellipse"];
    "Pow(Symbol('x'), Integer(2))_(0,)" ["color"="black", "label"="Pow", "shape"="ellipse"];
    "Symbol('x')_(0, 0)" ["color"="black", "label"="x", "shape"="ellipse"];
    "Integer(2)_(0, 1)" ["color"="black", "label"="2", "shape"="ellipse"];
    "Mul(Integer(-2), Symbol('x'), Symbol('y'))_(1,)" ["color"="black", "label"="Mul", "shape"="ellipse"];
    "Integer(-2)_(1, 0)" ["color"="black", "label"="-2", "shape"="ellipse"];
    "Symbol('x')_(1, 1)" ["color"="black", "label"="x", "shape"="ellipse"];
    "Symbol('y')_(1, 2)" ["color"="black", "label"="y", "shape"="ellipse"];

    #########
    # Edges #
    #########

    "Add(Pow(Symbol('x'), Integer(2)), Mul(Integer(-2), Symbol('x'), Symbol('y')))_()" -> "Pow(Symbol('x'), Integer(2))_(0,)";
    "Add(Pow(Symbol('x'), Integer(2)), Mul(Integer(-2), Symbol('x'), Symbol('y')))_()" -> "Mul(Integer(-2), Symbol('x'), Symbol('y'))_(1,)";
    "Pow(Symbol('x'), Integer(2))_(0,)" -> "Symbol('x')_(0, 0)";
    "Pow(Symbol('x'), Integer(2))_(0,)" -> "Integer(2)_(0, 1)";
    "Mul(Integer(-2), Symbol('x'), Symbol('y'))_(1,)" -> "Integer(-2)_(1, 0)";
    "Mul(Integer(-2), Symbol('x'), Symbol('y'))_(1,)" -> "Symbol('x')_(1, 1)";
    "Mul(Integer(-2), Symbol('x'), Symbol('y'))_(1,)" -> "Symbol('y')_(1, 2)";
    }

.. note::

    The diagram above was generated by using Graphviz and ``dotprint``

Notice how the nodes in the tree are structured according to the order of operations. The operations are defined as classes in SymPy, and we could just as easily
define our expressions using ``Add, Mul, Pow, Symbol`` (Add, Multipy, Power, Symbol). Let's look at a simpler expression: :math:`x^2`

.. jupyter-execute::

    x = sm.symbols('x')
    expr = x**2
    sm.srepr(expr)

.. graphviz::
    :align: center

    digraph{

    # Graph style
    "ordering"="out"
    "rankdir"="TD"

    #########
    # Nodes #
    #########

    "Pow(Symbol('x'), Integer(2))_()" ["color"="black", "label"="Pow", "shape"="ellipse"];
    "Symbol('x')_(0,)" ["color"="black", "label"="x", "shape"="ellipse"];
    "Integer(2)_(1,)" ["color"="black", "label"="2", "shape"="ellipse"];

    #########
    # Edges #
    #########

    "Pow(Symbol('x'), Integer(2))_()" -> "Symbol('x')_(0,)";
    "Pow(Symbol('x'), Integer(2))_()" -> "Integer(2)_(1,)";
    }

By using the same operators in the graph we can create the same object.

.. jupyter-execute::

    expr = sm.Pow(sm.Symbol('x'), sm.Integer(2))
    expr

See the manipulation section of the `official SymPy tutorial <https://docs.sympy.org/latest/tutorials/intro-tutorial/manipulation.html>`_ for more information on this topic.

SymPy has a comprehensive library of functions, all of which are documented in the official documentation.

.. jupyter-execute::

    expr2 = sm.sqrt(x)*sm.sin(x) + sm.Abs(z)/y
    expr2


When working with fractions, keep in mind that SymPy may evaluate the expression. We can get around this by using ``S()``
to sympify numbers. This is especially useful when working with irrational numbers

.. jupyter-execute::

    1/3 * x

.. jupyter-execute::

    sm.S(1)/3 * x

.. admonition:: Exercise

    Create a SymPy expression for the normal distribution function

    .. math::

        \frac{1}{\sqrt{2\pi\sigma}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}

.. dropdown:: Solution
    :color: success

    .. jupyter-execute::

        x, mu, sigma = sm.symbols('x mu sigma')
        normal = 1/sm.sqrt(2 * sm.pi * sigma**2)* sm.exp(-(x - mu)**2/(2*sigma**2))
        normal



Printing and Sympification
--------------------------

As illustrated with ``srepr()`` above, expressions in SymPy can have many representations. The most standard representation
is ``str()``, which gives a representation similar to what you would code

.. jupyter-execute::

    expr3 = x*sm.cos(x)**2/sm.Abs(sm.Symbol('omega'))
    str(expr3)

SymPy also has a pretty printer :external:py:func:`pprint() <sympy.printing.pretty.pretty.pretty_print>` that prints unicode symbols more similar to the typesetting we are used to

.. jupyter-execute::

    sm.pprint(expr3)

Additionally, SymPy can also generate LaTeX representations of SymPy expressions using the :external:py:func:`sympy.printing.latex.latex` function

.. jupyter-execute::

    print(sm.latex(expr3))


SymPy can also interpret and convert strings into SymPy expressions

.. jupyter-execute::

    s = sm.sympify('x*cos(x)/omega')
    s

It's also worth noting that SymPy can generate expressions in many different programming languages. This allows us to use SymPy to solve/find the expressions we want,
which we then implement in our programs

.. jupyter-execute::

    print(sm.ccode(expr3))          # C
    print(sm.fcode(expr3))          # Fortran
    print(sm.rust_code(expr3))      # Rust
    print(sm.octave_code(expr3))    # Matlab / Octave
    print(sm.julia_code(expr3))     # Julia
    # LLVM etc ...

.. admonition:: Exercise

    Use the :code:`latex` method demonstrated in the `SymPy documentation <https://docs.sympy.org/latest/tutorials/intro-tutorial/printing.html>`_ to generate a LaTex expression for the normal distribution.

.. dropdown:: Solution
    :color: success

    .. jupyter-execute::

        print(sm.latex(normal))


Differentiation
-----------------

.. note::

    SymPy has several methods for computing an integral. Since most of the systems we'll work with in the course don't have analytical solutions, we won't
    introduce them here. See the the `calculus section of the official SymPy tutorial <https://docs.sympy.org/latest/tutorials/intro-tutorial/calculus.html#integrals>`_ if you want to learn more.

Computing derivatives of complex expressions by hand can be very tedious process prone to errors. With SymPy we can calculate derivatives with ease.
All functions and expressions have a ``.diff()`` method which can be used to differentiate. There is also a standalone function :external:py:func:`~sympy.core.function.diff` which takes
a undefined function or an expression and differentiates it with respect to the second argument. This works irrespective of dimension, given that the corresponding arguments are correct.


.. jupyter-execute::

    f = sm.Function('f')
    f(t).diff(t)

.. jupyter-execute::

    sm.diff(f(x), x)

Let's say we have some complicated expression

.. jupyter-execute::

    expr4 = sm.Abs(x)*sm.sin(t)**2/x
    expr4

We can express the derivative of ``expr4`` with respect to :math:`x` and then :math:`t` by using ``Derivative()``

.. jupyter-execute::

    sm.Derivative(expr4, x, t)

We can compute the derivative with the method ``doit()``, which is the  as ``expr4.diff(args)``

.. jupyter-execute::

    sm.Derivative(expr4, x, t).doit()

.. jupyter-execute::

    expr4.diff(x, t)

Note that the derivative includes both real and imaginary components. This is intentional.

.. warning::

    SymPy assumes that all symbols are complex-valued unless it is given additional assumptions. We can attach assumptions
    to a symbol or function to specify if they are real, positive, negative etc.

    .. jupyter-execute::

        s = sm.symbols('s')
        H = sm.Function('H')
        sm.Abs(H(s)).diff(s)

    .. jupyter-execute::

        H = sm.Function('H', real=True)
        sm.Abs(H(s)).diff(s)

    .. jupyter-execute::

        H = sm.Function('H', real=True, positive=True)
        sm.Abs(H(s)).diff(s)

    In most cases, adding assumptions to variables isn't necessary, but it can be useful when you encounter unexpected components in your solutions.

.. admonition:: Exercise

    Demonstrate the chain rule by differentiating :math:`f(g(x))` with respect to :math:`x` using SymPy

.. dropdown:: Solution
    :color: success

    .. jupyter-execute::

        f(sm.Function('g')(x)).diff(x)


Substitution and Evaluation
----------------------------

SymPy has many methods for evaluating expressions numerically, and :external:py:meth:`~sympy.core.basic.Basic.replace` is often used.
In this course we prefer :external:py:meth:`~sympy.core.basic.Basic.xreplace` for its verbosity. We first create a dictionary to map
the symbols or expressions we want to substitute, and then pass it to ``xreplace()``

.. jupyter-execute::

    repl = {x: sm.sqrt(2), t: sm.pi/7}
    expr4.xreplace(repl)

SymPy doesn't evaluate the expression automatically after substituting. We can use the :external:py:meth:`~sympy.core.evalf.EvalfMixin.evalf` method to
evaluate the expression to a specified number of decimal points given a dictionary with substitutions.

.. jupyter-execute::

    expr4.evalf(n = 10, subs = repl)

We can do this because ``evalf()`` returns a special SymPy :external:py:class:`~sympy.core.numbers.Float` object which can have an arbitrary number of decimal places.
Here we evaluate pi at 1000 decimal places

.. jupyter-execute::

    pi_e3 =  sm.pi.evalf(n = 1000)
    pi_e3

If you want a regular machine precision floating point value you can easily convert a SymPy float to a Python float

.. jupyter-execute::

    type(float(pi_e3))

When we want to evaluate an expression with machine precision directly, we prefer to use :external:py:func:`~sympy.utilities.lambdify.lambdify` to
convert the expression into a Python function. We can convert an expression by providing the symbols that should be converted
into numbers as a tuple. We can then use ``help()`` to inspect our lambdified expression.

.. jupyter-execute::

    eval_expr4 = sm.lambdify((x, t), expr4)
    help(eval_expr4)

The lambdified function works as any other Python function. Note that it returns NumPy floats instead of Python floats.
These can be used with Python floats interchangeably, but neither should be mixed with SymPy floats. We prefer the much faster NumPy floats
since the arbitrary precision of a Python float isn't required. We will almost always want machine precision floats, so ``lambdify()`` is your friend.

.. jupyter-execute::

    type(eval_expr4(1,2))

If you want a quick plot without evaluating your expression, you can use ``plot()``

.. jupyter-execute::

    sm.plot(sm.sin(x)**2)


Matrices
---------

Matrices can be creating by passing a nested list to the ``Matrix()`` object

.. jupyter-execute::

    A = sm.Matrix([[0.2, - 1], [0, 0.9]])
    A

.. jupyter-execute::

    a, b, c, d = sm.symbols('a, b, c, d')
    B = sm.Matrix([[1/b, 1/b], [c/d, 1/a]])
    B

We can access individual elements of a matrix with square brackets

.. jupyter-execute::

    B[1,0]

We can also use slice notation to extract rows or columns

.. jupyter-execute::

    B[0:2, 1]

.. jupyter-execute::

    B[0, 0:2]

A list of elements is interpreted as a column vector

.. jupyter-execute::

    C = sm.Matrix([a, b])

We can get the shape of a matrix by using the ``shape()`` function or the ``shape`` attribute

.. jupyter-execute::

    print(sm.shape(C))
    print(C.shape)

There are many methods for creating common matrices

.. jupyter-execute::

    sm.eye(4,4)

.. jupyter-execute::

    sm.zeros(3,1)

.. jupyter-execute::

    sm.ones(6,4)

For creating matrices with elements or matrices on the diagonal we use ``diag()``

.. jupyter-execute::

    sm.diag(a, b, c, sm.ones(6,4))

To transpose a matrix we can use the attribute ``.T``

.. jupyter-execute::

    sm.diag(a, b, c, sm.ones(6,4)).T

We can easily perform matrix algebra

.. jupyter-execute::

    B + B

We can use both ``*`` and ``@`` to perform matrix multiplication. Since NumPy uses ``*`` for element-wise multiplication
and ``@`` for matrix multiplication, it's best to use ``@`` for SymPy matrix multiplication to avoid any confusion

.. jupyter-execute::

    B*C

.. jupyter-execute::

    B@C

For element-wise multiplication:

.. jupyter-execute::

    sm.hadamard_product(B,B)

Useful attributes, such as the determinant, eigenvalues, eigenvectors and singular values are implemented as matrix methods

.. jupyter-execute::

    r, theta = sm.symbols('r, theta', real=True)
    rot = sm.Matrix([[r*sm.cos(theta), -r * sm.sin(theta)],[r*sm.sin(theta), r*sm.cos(theta)]])
    rot

.. jupyter-execute::

    rot.det()

.. jupyter-execute::

    rot.singular_values()

.. jupyter-execute::

    D = sm.Matrix([[1, x], [y, 1]])
    D

.. jupyter-execute::

    D.eigenvals()

.. jupyter-execute::

    D.eigenvects()


Matrices are mutable, meaning that you can change them in place. This means they cannot be used inside other SymPy
expressions or as keys to dictionaries. If needed, there is an immutable version of a matrix in SymPy called ``ImmutableMatrix``

.. jupyter-execute::

    C *=2
    C += sm.Matrix([0, 1])
    C[0] = b
    C

We can differentiate a matrix by ``.diff()``

.. jupyter-execute::

    C.diff(b)

We can also calculate the `Jacobian <https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant>`_ of a vector with ``jacobian()``

.. jupyter-execute::

    C.jacobian([a, b])


.. admonition:: Exercise

    The nonlinear state space model for an inverted pendulum is given below. Use the ``jacobian()`` message to linearize
    the system around the equilibrium :math:`x_0 = \begin{bmatrix} 0 \\ 0 \end{bmatrix}`

    .. jupyter-execute::

        import sympy as sm

        x1, x2 = sm.symbols('x1 x2')
        u = sm.symbols('u')
        g, l, m = sm.symbols('g l m')

        x = sm.Matrix([x1, x2])

        f1 = x2
        f2 = -(g/l)*sm.sin(x1) + (1/(m*l**2))*u
        f = sm.Matrix([f1, f2])
        f

.. dropdown:: Solution
    :color: success

    .. jupyter-execute::

        A = f.jacobian(x)
        B = f.jacobian(sm.Matrix([u]))

        # Define the linearization point around equilibrium
        x_eq = sm.Matrix([0, 0])
        u_eq = 0

        subs = {x1: x_eq[0], x2: x_eq[1], u: u_eq}

        A_lin = A.xreplace(subs)
        B_lin = B.xreplace(subs)

        A_lin@x + B_lin*u

    Alternatively, the small-angle approximation will yield the same result.

Linear Systems
---------------

SymPy has `many ways <https://docs.sympy.org/latest/guides/solving/solve-matrix-equation.html#methods-for-solving-matrix-equations>`_ of solving Matrix equations on the form :math:`\bf{A}x = b`.
The best method depends on the nature of the matrix. By default, Gauss-Jordan elimination will be used, which can be quite inefficient for large matrices.
If you repeatedly need to solve matrix equations with the same matrix, it is usually faster to use LU decomposition via the ``LUsolve`` method

.. jupyter-execute::

    A = sm.Matrix([[c, d],[1, -a]])
    b = sm.Matrix([3, 0])
    solution = A.LUsolve(b)
    solution

We can verify the solution

.. jupyter-execute::

    sm.simplify(A@solution)

We could also find the inverse of the matrix :math:`A`, but this is usually significantly slower, especially with large matrices.

.. jupyter-execute::

    A_inv = A.inv()
    solution = A_inv@b
    solution

Equations with no solution will return an error

Simplification
---------------

When working with dynamical systems the computation of Jacobians and matrix inversion will inevitably lead to large and complicated expressions.
Luckily, SymPy has a function for automatically simplifying symbolic expressions, namely :external:py:func:`~sympy.simplify.simplify.simplify`.

.. jupyter-execute::

    a, t = sm.symbols('a t')
    expr6 = sm.Matrix([sm.cos(a)/t + t*sm.sin(t) + 100, sm.cos(a) + t*a])
    A = expr6.jacobian([a, t]).inv()
    sm.simplify(A)

Simplifying very large expressions usually won't give you a better result. Simplifying specific parts of your expressions can
sometimes yield better results. The ``trigsimp()`` function tries to find a simpler trigonometric expression

.. jupyter-execute::

    sm.trigsimp(sm.cos(t)**2 + sm.sin(t)**2)



--------------

More resources on SymPy
========================

It's highly recommended that you familiarize yourself with the SymPy documentation, available though `this link here <https://docs.sympy.org/latest/index.html>`_.
The documentation page on `common mistakes and "gochas" <https://docs.sympy.org/latest/tutorials/intro-tutorial/gotchas.html>`_ is particularty useful.
An older long-form version of this SymPy tutorial is available on YouTube.

.. raw:: html

    <center>
    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/AqnpuGbM6-Q?si=wjxy7BZ_0ZI9qVRm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </center>
