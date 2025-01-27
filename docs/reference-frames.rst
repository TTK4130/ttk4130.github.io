============================
Reference frames (WIP)
============================


.. note::

    This page is based on the `SymPy mechanics module documentation <https://docs.sympy.org/latest/modules/physics/mechanics/index.html>`_.


Reference frames are useful when examining the relationships between bodies in multibody systems. It also serves a useful purpose in physics when working with inertial frames, where Newton's laws of physics apply, and non-inertial reference frames.
We can loosely define a reference frames as the `Euclidian space <https://en.wikipedia.org/wiki/Euclidean_space>`_ spanned by orthogonal unit vectors oriented following the `right-hand rule <https://en.wikipedia.org/wiki/Right-hand_rule>`_. This may be a two dimensional space spanned by two unit orthogonal unit vectors or a three dimensional space spanned by three orthogonal unit vectors.
In this course reference frames don't have a position in space, but are defined by orientation alone. We often define reference frames relative to some "base frame" that we consider fixed in space. This may be the center of mass on a drone or the center of the earth in a navigation system. We can think of reference frames intuitively as perspectives. The characters on this page change relative to me as I change my perspective (or reference frame) in 3D space. If I rotate my phone while taking a picture, the world rotates relative to the reference frame of the camera.

Unit Vectors
=============

Vectors have both a magnitude and a direction. Unit vectors are vectors with a magnitude of *one* oriented parallel to a direction (or dimension) in the reference frame they span.
We can think of a reference frame as a box in 3D. A unit vector points along the side of the box. For convenience, we often like to imagine the unit vectors being aligned in a corner of a "box" pointing along the edges of the box.
A unit vector follows the right-hand rule. In a reference system :math:`A` defined by the orthogonal unit vectors :math:`\hat{a}_x`, :math:`\hat{a}_y`, :math:`\hat{a}_z`, the following cross-products hold

.. math::

    \hat{a}_x \times \hat{a}_y = \hat{a}_z

    \hat{a}_z \times \hat{a}_x = \hat{a}_y

    \hat{a}_y \times \hat{a}_z = \hat{a}_x


Note that the unit vectors :math:`\hat{a}_x`, :math:`\hat{a}_y`, :math:`\hat{a}_z` are by definition fixed in reference frame :math:`A`. If we want to define a new reference frame :math:`B` relative to frame :math:`A` we can express their relative orientation with the relationship between their respective unit vectors.
We'll examine this in the next section.

Simple Rotation Example
=======================

.. _fig:box:

.. figure:: figures/box_w_lid.svg
    :width: 50%
    :align: center

    Box with sides :math:`d` with rotating lid

The figure :numref:`fig:box` depics a box with sides :math:`d` and a rotating square lid with sides :math:`d`. The lid is rotated
by an angle :math:`\theta` relative to the box. By looking at the hinge we can find the relationship between frame :math:`A` and reference frame :math:`B` attached to the rotating lid.


.. _fig:box2d:

.. figure:: figures/box_lid_rotationtransform.svg
    :width: 35%
    :align: center

    2D representation of :numref:`fig:box` rotating lid

Looking at the hinge in :numref:`fig:box2d` we use trigonometry to find

.. math::

    \hat{b}_x = \hat{a}_x

    \hat{b}_y = cos(\theta) \hat{a}_y + sin(\theta) \hat{a}_z

    \hat{b}_z = -sin(\theta) \hat{a}_y + sin(\theta) \hat{a}_z


We can rewrite this as a matrix product

.. math::

    \begin{bmatrix}
    \hat{b}_x \\
    \hat{b}_y \\
    \hat{b}_z
    \end{bmatrix}
    =
    \begin{bmatrix}
    1 & 0 & 0 \\
    0 & \cos(\theta) & \sin(\theta) \\
    0 & -\sin(\theta) & \cos(\theta)
    \end{bmatrix}
    \begin{bmatrix}
    \hat{a}_x \\
    \hat{a}_y \\
    \hat{a}_z
    \end{bmatrix}

This matrix is the transformation matrix **from** :math:`A` **to** :math:`B`, :math:`R_A^B(\theta)` which means we can transform any vector in frame :math:`A` to its representation in frame :math:`B` by means of matrix multiplication

.. math::

    v_B = R_A^B(\theta)v_A

.. note::

    We use the following convention for tranformation matrices :math:`R_{from}^{to}`

We can easily implement this in SymPy


.. jupyter-execute::

    import sympy as sm
    from sympy import sin, cos

    theta = sm.symbols('theta')
    R_a_to_b = sm.Matrix([  [0, 0, 1],
                            [cos(theta), sin(theta), 0],
                            [-sin(theta), cos(theta), 0]])
    R_a_to_b

This transformation matrix is belongs to a group of matrices we call rotation matrices. More specifically, it belongs to the special orthogonal group 3 (SO(3)). This means that
it has useful properties such that its inverse is equal to its transpose.



.. _fig:box_w_vector:

.. figure:: figures/box_w_lid_vector.svg
    :width: 50%
    :align: center

    Box with sides :math:`d` with rotating lid and vector :math:`\vec{p}`


Euler angles
=============

.. figure:: https://upload.wikimedia.org/wikipedia/commons/8/85/Euler2a.gif
    :align: center

    Euler2.gif by Juansempere. Derivative work: Xavax - Euler2.gif:, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=24338647


Further reading
===============

There are many different ways of representing rotations. We'll take a closer look at the most robust way in the section :ref:`Quaternions (WIP)`.
