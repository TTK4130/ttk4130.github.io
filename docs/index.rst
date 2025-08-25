============================================
Welcome to Modelling and Simulation!
============================================

.. figure:: _static/lorenz.png
  :align: center


.. toctree::
    :maxdepth: 1
    :caption: Contents:

    installation
    jupyter-notebook
    sympy-and-cas
    animation
    reference-frames
    vector-kinematics
    mass-and-inertia
    force-and-torque
    quaternions
    numerical-methods-for-odes
    whats-next
    project/index
    assignments/index
    lecture-notes/index
    sympy-live
    notation
    bibliography

About this website
===================

This website is an online resource for students taking the course `Modelling and Simulation TTK4130 <https://www.ntnu.edu/studies/courses/TTK4130#tab=omEmnet>`_ at
the Norwegian University of Science and Technology. Although it's a supplement to the course curriculum,
it's also written as to be available to anyone eager to learn about the topics taught in this course. The goal
of this website is to take a more hands-on approach to modelling and simulation of dynamical systems. All
code is written in Python using a mix of openly available tools and libraries. You are highly encouraged
to code along when possible and play around with the provided code. Any issues or questions regarding
this website are directed to the `Github repository <https://github.com/ttk4130/ttk4130.github.io>`_ where the code is hosted.

What Will You Learn?
====================

By the end of this course, you'll have a solid foundation in using Python and SymPy to solve systems of equations, both algebraically and numerically.
You'll gain hands-on experience in implementing fundamental numerical methods, along with an understanding of their limitations.
Furthermore, you'll be equipped to describe complex mechanical systems and formulate equations of motion, translating your theoretical knowledge into practical models.

This course serves as a stepping stone toward applying these skills in real-world engineering scenarios, where you can take your understanding of dynamics and simulation into areas like robotics, autonomous systems, and more.

Prerequisites
===============
- Basic programming knowledge
- Familiarity with Python
- Basic Linear Algebra
- Familiarity with Control Systems

Why Python?
==================

It's no secret that Matlab has been dominating in academia for some years, so why teach how to use Python?
The first obvious answer is price. Matlab is a commercial product not available to everyone, including companies.
The second answer is availability. Python is one of the most popular programming languages in the world. This is no
accident. Due to a vibrant community of open-source projects and contributors Python continues to flourish. An example of this
is Sphinx, which this website is built with. Another reason is one of pedagogy. Matlab often does more than you ask it to.
By doing all the "dirty work" in Python we get a much better understanding of how these tools work and their limitations.
In the end it all comes down to preference. We like Python, and we hope you'll like it too!

.. jupyter-execute::

    print("Hello world!")

Did you know Python can do symbolic math?

.. jupyter-execute::

   import sympy as sm
   sm.init_printing(use_latex='mathjax')
   
   b, t, phi = sm.symbols('b, t, phi')
   b, t, phi

Learning Through Struggle: Why Shortcuts Don't Work
====================================================

As our tools become more advanced, it's tempting to let them do all the heavy lifting. You might wonder: "Why not just modify existing code examples or ask ChatGPT when I'm stuck?"
The answer is straightforward: there are no shortcuts to genuine learning. The struggle itself is essential to developing your understanding and skills. This is something successful students recognize early.
The tools you're learning in this course are the foundation for subsequent advanced subjects. Many students later identify this course as one of the most important fundamentals to master in becoming a successful engineer.
We don't encourage hacking together assignments or relying on AI because those approaches bypass the valuable learning process. Yes, learning can be difficult, frustrating, and sometimes painful - but that's precisely how you develop true competence.
We provide solution references not to tempt you, but to close the learning loop. Many students submit work and move on without reviewing the recommended approach. By comparing your work to the solutions, you deepen your understanding and identify gaps in your knowledge.
Some might be tempted to simply copy solutions. Be warned: this strategy will come back to bite you. The understanding you've avoided building will be required on the final exam and in your future work.
We believe in your ability to learn through honest effort. Embrace the challenge, trust the process, and your skills will grow accordingly.

Good luck!