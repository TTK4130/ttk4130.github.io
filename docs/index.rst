============================================
Welcome to Modelling and Simulation TTK4130!
============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction
   assignment

Introduction
==================
This site will introduce you to tools for simulation in Python etc....

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
