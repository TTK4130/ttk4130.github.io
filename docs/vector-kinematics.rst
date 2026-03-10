===========================
Vector Kinematics (WIP)
===========================

Kinematics describes how objects move in space without considering the forces that cause the motion. 
It provides the mathematical tools needed to describe position, velocity, and acceleration, which are 
fundamental for analyzing and controlling mechanical and robotic systems.

Vector notation
---------------
A vector is defined as a directional entity with magnitude without a specific starting point.
In a three dimentional space a vector needs three components which corresponds to the three axis that define the space. 
For example a vector with components *a*, *b*, *c* in a space definded by the *xyz*-frame have a length *a* along the *x*-axis, *b* along the *y*-axis and *c* along the *z*-axis.

A vector expressed in terms of the component directions of the reference frame :math:`i`
is given as

.. math::

   \vec{p} = a\,\vec{i}_i + b\,\vec{j}_i + c\,\vec{k}_i

using the unit vector notation, where :math:`\vec{i}_i`, :math:`\vec{j}_i`, and
:math:`\vec{k}_i` are the unit vectors of the reference frame :math:`i`.

Using coordinate notation, we may write the same vector as

.. math::

   \mathbf{p}^i =
   \begin{pmatrix}
   a \\
   b \\
   c
   \end{pmatrix}

Vectors, reference frames and rotation transformations
-------------------------------------------------------

Velocities and accelerations
-----------------------------