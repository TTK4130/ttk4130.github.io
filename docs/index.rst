.. ttk4130 documentation master file, created by
   sphinx-quickstart on Sun Jul 28 17:35:19 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Modelling and Simulation TTK4130!
============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

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
