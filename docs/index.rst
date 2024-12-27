============================================
Welcome to Modelling and Simulation TTK4130!
============================================

.. figure:: _static/lorenz.png
  :align: center


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   installation
   jupyter-notebooks
   sympy-and-cas
   numerical-methods-for-odes
   numerical-instability
   simulation
   rotations
   reference-frames
   assignment-1
   quaternions
   sympy-live
   notation
   bibliography

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
