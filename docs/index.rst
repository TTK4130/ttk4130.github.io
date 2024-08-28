============================================
Welcome to Modelling and Simulation TTK4130!
============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction
   installation
   jupyter-notebooks
   sympy-and-cas
   explicit-euler
   implicit-euler
   runge-kutta-methods
   simulation
   reference-frames
   assignment-1
   quaternions
   notation
   references

Learning outcome
==================
This site will introduce you to tools for simulation in Python etc....


Prerequisites
===============
- Basic programming knowledge
- Familiarity with Python (from TDT4110 Information Technology, Introduction or similar)
- Basic Linear Algebra

Why Python?
==================
Open source, widely supported

.. jupyter-execute::

    print("Hello world!")

And it supports useful tools...

.. jupyter-execute::

   import sympy as sm
   sm.init_printing(use_latex='mathjax')
   
   b, t, phi = sm.symbols('b, t, phi')
   b, t, phi

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
