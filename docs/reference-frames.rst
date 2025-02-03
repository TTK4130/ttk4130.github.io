============================
Reference frames (WIP)
============================


.. note::

    This page is based on the `SymPy mechanics module documentation <https://docs.sympy.org/latest/modules/physics/mechanics/index.html>`_.


Reference frames are useful when examining the relationships between bodies in multibody systems. It also serves a useful purpose in physics when working with inertial frames, where Newton's laws of physics apply, and non-inertial reference frames.
We can loosely define a reference frames as the `Euclidean space <https://en.wikipedia.org/wiki/Euclidean_space>`_ spanned by orthogonal unit vectors oriented following the `right-hand rule <https://en.wikipedia.org/wiki/Right-hand_rule>`_. This may be a two dimensional space spanned by two unit orthogonal unit vectors or a three dimensional space spanned by three orthogonal unit vectors.
In this course reference frames don't have a position in space, but are defined by orientation alone. We often define reference frames relative to some "base frame" that we consider fixed in space. This may be the center of mass on a drone or the center of the earth in a navigation system. We can think of reference frames intuitively as perspectives. The characters on this page change relative to me as I change my perspective (or reference frame) in 3D space. If I rotate my phone while taking a picture, the world rotates relative to the reference frame of the camera.

Unit Vectors
=============

Vectors have both a magnitude and a direction. Unit vectors are vectors with a magnitude of *one* oriented parallel to a direction (or dimension) in the reference frame they span.
We can think of a reference frame as a box in 3D. A unit vector points along the side of the box. For convenience, we often like to imagine the unit vectors being aligned in a corner of a "box" pointing along the edges of the box.
A unit vector follows the right-hand rule. This means that a reference system :math:`A` defined by the orthogonal unit vectors :math:`\hat{a}_x`, :math:`\hat{a}_y`, :math:`\hat{a}_z`, the following cross-products hold

.. math::

    \hat{a}_x \times \hat{a}_y = \hat{a}_z

    \hat{a}_z \times \hat{a}_x = \hat{a}_y

    \hat{a}_y \times \hat{a}_z = \hat{a}_x


Note that the unit vectors :math:`\hat{a}_x`, :math:`\hat{a}_y`, :math:`\hat{a}_z` are by definition fixed in reference frame :math:`A`. If we want to define a new reference frame :math:`B` relative to frame :math:`A` we can express their relative orientation with the relationship between their respective unit vectors.
We'll examine this in the next section.

.. note::

    **Basis vectors** are vectors that define a reference frame, but they are not necessarily of unit length. When the basis vectors are normalized to have a magnitude of one, they become unit vectors. In an orthonormal reference frame, the basis vectors are both unit vectors and mutually perpendicular.

Simple Rotation Example
=======================

.. _fig:box:

.. figure:: figures/box_w_lid.svg
    :width: 50%
    :align: center

    Box with sides :math:`d` with rotating lid

The figure :numref:`fig:box` depics a box with sides :math:`d` and a rotating square lid with sides :math:`d`. The lid is rotated
by an angle :math:`\theta` relative to the box. If we want to find some vector :math:`\vec{p}` represented in terms of reference frame :math:`A`, we simply find and substitute its elements in frame :math:`B`.

.. _fig:box_w_vector:

.. figure:: figures/box_w_lid_vector.svg
    :width: 50%
    :align: center

    Box with sides :math:`d` with rotating lid and vector :math:`\vec{p}`


Using the unit vectors we see that :math:`\vec{p} = d \hat{a}_y + d \hat{a}_z + d \hat{b}_x + d \hat{b}_z`. By looking at the hinge we can find the relationship between the unit vectors frame :math:`A` and frame :math:`B`.

.. _fig:box2d:

.. figure:: figures/box_lid_rotationtransform.svg
    :width: 35%
    :align: center

    2D representation of :numref:`fig:box` rotating lid

Looking at the hinge in :numref:`fig:box2d` we use trigonometry to find

.. math::
    :label: x-rotation-example

    \hat{b}_x = \hat{a}_x

    \hat{b}_y = cos(\theta) \hat{a}_y + sin(\theta) \hat{a}_z

    \hat{b}_z = -sin(\theta) \hat{a}_y + cos(\theta) \hat{a}_z

We can then substitute the unit vectors in frame :math:`B`

.. math::

    \vec{p} = d \hat{a}_y + d \hat{a}_z + d \hat{b}_x + d \hat{b}_z

    \vec{p} = d \hat{a}_y + d \hat{a}_z + d \hat{a}_x + d(-sin(\theta) \hat{a}_y + cos(\theta) \hat{a}_z)

    p^A =
    \begin{bmatrix}
    d \\
    d - d sin(\theta) \\
    d + d cos(\theta)
    \end{bmatrix}

We can generalize this  by a matrix product in :eq:`x-rotation-example`

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
    =
    {\bf R}_A^B(\theta)
    \begin{bmatrix}
    \hat{a}_x \\
    \hat{a}_y \\
    \hat{a}_z
    \end{bmatrix}

This matrix is the transformation matrix **from** :math:`A` **to** :math:`B`, :math:`{\bf R}_A^B(\theta)`, which means we can transform any vector in frame :math:`A` to its representation in frame :math:`B` by means of matrix multiplication.
This kind of transformation matrix is belongs to a group we call rotation matrices. More specifically, it belongs to the `special orthogonal group 3 (SO(3)) <https://en.wikipedia.org/wiki/3D_rotation_group>`_. This means that
it has useful properties such that its inverse is equal to its transpose, meaning :math:`{{\bf R}_A^B}^T(\theta) = {{\bf R}_A^B}^{-1}(\theta) = {\bf R}_B^A(\theta)`, thus

.. math::

    {\bf v}^B = {\bf R}_A^B(\theta) {\bf v}^A

    {\bf v}^A = {{\bf R}_B^A}^T(\theta) {\bf v}^B = {{\bf R}_B^A} (\theta){\bf v}^B

Instead of looking at unit vectors to find :math:`p^A`, we can simply transform the components of :math:`\vec{p}` in the :math:`B`-frame **from** :math:`B` **to** :math:`A`

.. note::

    We use the following convention for transformation matrices :math:`{\bf R}_{from}^{to}`

.. math::

    p^A
    =
    \begin{bmatrix}
    0 \\
    d  \\
    d
    \end{bmatrix}
    +
    {\bf R}_B^A
        \begin{bmatrix}
    d \\
    0  \\
    d
    \end{bmatrix}

calculating that

.. math::

    {\bf R}_B^A
    =
    {{\bf R}_A^B}^T
    =
    {
    \begin{bmatrix}
    1 & 0 & 0 \\
    0 & \cos(\theta) & \sin(\theta) \\
    0 & -\sin(\theta) & \cos(\theta)
    \end{bmatrix}
    }^T
    =
    \begin{bmatrix}
    1 & 0 & 0 \\
    0 & \cos(\theta) & -\sin(\theta) \\
    0 & \sin(\theta) & \cos(\theta)
    \end{bmatrix}

We insert and get

.. math::

    p^A
    =
    \begin{bmatrix}
    0 \\
    d  \\
    d
    \end{bmatrix}
    +
    \begin{bmatrix}
    1 & 0 & 0 \\
    0 & \cos(\theta) & -\sin(\theta) \\
    0 & \sin(\theta) & \cos(\theta)
    \end{bmatrix}
    \begin{bmatrix}
    d \\
    0\\
    d
    \end{bmatrix}
    =
    \begin{bmatrix}
    d \\
    d - d sin(\theta) \\
    d + d cos(\theta)
    \end{bmatrix} \  \ \blacksquare.


We can easily implement this in SymPy


.. jupyter-execute::

    import sympy as sm
    sm.init_printing(use_latex='mathjax')
    from sympy import sin, cos

    theta, d = sm.symbols('theta d')
    R_b_to_a = sm.Matrix([  [1, 0, 0],
                            [0, cos(theta), -sin(theta)],
                            [0, sin(theta), cos(theta)]])
    R_b_to_a

.. jupyter-execute::

    v_A = sm.Matrix([0, d, d]) + R_b_to_a @ sm.Matrix([d, 0, d])
    v_A

SymPy Reference Frames
======================

As you can see from section :ref:`Simple Rotation Example`, even simple examples can get quite tedious when working with reference frames. Luckily, the SymPy module :external:py:obj:`~sympy.physics.vector` implements reference frames with the :external:py:class:`~sympy.physics.vector.frame.ReferenceFrame` class.

.. jupyter-execute::

    from sympy.physics.vector import ReferenceFrame

    A = ReferenceFrame('A')

Each reference frame has three associated basis vectors that define the frame

.. jupyter-execute::

    A.x, A.y, A.z

We can create new vectors by using the basis vectors

.. jupyter-execute::

    a = d*A.y + d*A.z
    a

We can orient a new reference :math:`B` relative to our frame :math:`A` with an axis rotation around :math:`\hat{a}_x`

.. jupyter-execute::

    B = A.orientnew('B', 'Axis', [theta, A.x]) # x-axis rotation from box example

If we want the rotation matrix between two frames, we can call the *direct cosine matrix* or `dcm` method

.. jupyter-execute::

    B_to_A = B.dcm(A)
    B_to_A

SymPy makes it trivial to solve the simple example in :numref:`fig:box_w_vector`

.. jupyter-execute::

    b = d*B.x + d*B.z
    p = a + b
    p

Using the `express` method we can find the vector :math:`v^A`. As long as there is a relationship between the reference frames
in a vector, SymPy will be able to automatically calculate the vector relative to any frame.

.. jupyter-execute::

    p.express(A)


Implementation Details
-------------------------------

The `ReferenceFrame` class stores the name given upon creation as a string and its orientation as a direction cosine matrix (dcm) with type `sympy.Matrix`. Crucially, it also stores the relationships between other reference frames in a private dictionary, `_Frame__frame_dict`.
The dictionary uses `ReferenceFrames` as keys and direction cosine matrices with type `sympy.Matrix` as values. These are set bi-directionally, which means that if we orient reference frame :math:`A` to :math:`B` we set the key :math:`B` and `Matrix` for frame :math:`A`'s dictionary,
and the key :math:`A` and the transposed `Matrix` for frame :math:`B`'s dictionary.


.. admonition:: Exercise

    Use SymPy ReferenceFrames to find an expression of the position relative to origin (base of the robot) of the end effector on the SCARA robot depicted below. Use
    :math:`\theta` to denote the joint angles, :math:`d` to denote link length and :math:`J3` to denote the z-displacement.

    .. figure:: https://upload.wikimedia.org/wikipedia/commons/0/09/SCARA_robot_2R.png
        :width: 50%

        Mitsubishi Electric Automation, Inc. 500 Corporate Woods Pkwy - Vernon Hills, IL - 60061 - US, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons

.. dropdown:: Solution
    :color: success

    .. jupyter-execute::

        from sympy import symbols
        from sympy.physics.vector import ReferenceFrame

        theta1, theta2, theta3 = symbols('theta1:4') # Angles
        J3, d1, d2 = symbols('J3 d_1 d_2') # Distances (z-displacement is defined by actuator height)

        origin = ReferenceFrame('O')
        J1 = origin.orientnew('J1', 'Axis', [theta1, origin.z])
        J2 = J1.orientnew('J2', 'Axis', [theta2, J1.z])
        J4 = J2.orientnew('J4', 'Axis', [theta3, J2.z])

        p = d1 * J1.x + d2 * J2.x + J3 * J4.z
        p.to_matrix(origin) # Print matrix form relative to origin


Euler angles
==================

.. warning::

    Rotations in 3D space can often be confusing. This confusion arises from all the different convention used, or rather the lack thereof. Students
    are often told to "think opposite" or just simply memorize one convention of rotation. **There is logic to this madness**, so just hold on tight and
    pay attention to the following subsections.

In three dimensional space we can transform to any orientation we wish by applying three separate rotations. The most intuitive way to visualize such a sequence of rotation
is first rotating your reference frame :math:`A` about the :math:`\hat{a}_z`-axis, rotating the newly rotated reference frame :math:`A'` about :math:`\hat{a'}_y`-axis and finally
rotating the new coordinate system :math:`A''` about :math:`\hat{a''}_x`.

.. figure:: https://upload.wikimedia.org/wikipedia/commons/8/85/Euler2a.gif
    :align: center

    Euler2.gif by Juansempere. Derivative work: Xavax - Euler2.gif:, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=24338647

This type of rotation with mobile axes is called an *intrinsic* sequence of rotation. During each rotation the axes are also rotated.

Proper Euler Angles vs Tait-Bryan
---------------------------------

Intrinsic and Extrinsic Rotations
---------------------------------


ZYX Euler Angles
----------------------------

SymPy Example: Drone with Gimbal
---------------------------------


Further reading
===============

There are many different ways of representing rotations. We'll take a closer look at the most commonly used way of representing orientation in the section :ref:`Quaternions (WIP)`.
