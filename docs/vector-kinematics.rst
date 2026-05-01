#########################
 Vector Kinematics (WIP)
#########################

Kinematics describes motion without considering the forces that cause it. In mechanics and robotics,
it provides the tools needed to describe position, velocity, and acceleration.

*****************
 Vector notation
*****************

A vector is a quantity with magnitude and direction. In three-dimensional space, a vector is
described by three components relative to a reference frame.

A vector expressed in terms of the unit vectors of frame :math:`i` may be written as

.. math::

    \vec{p} = a\,\vec{i}_i + b\,\vec{j}_i + c\,\vec{k}_i

Using coordinate notation, the same vector is written as

.. math::

    \mathbf{p}^i =
    \begin{pmatrix}
    a \\
    b \\
    c
    \end{pmatrix}

In these notes, the position of point :math:`B` relative to point :math:`A` is denoted
:math:`\mathbf{p}_{B/A}` or :math:`\vec{p}_{B/A}`.

*******************************
 Reference frames and position
*******************************

.. raw:: html
    :file: _includes/animation/threejs_ref_frame_and_position.html

Consider two reference frames:

- a fixed frame :math:`(x_0, y_0, z_0)`
- a moving frame :math:`(x_b, y_b, z_b)`

The moving frame is attached to a rigid body and may both translate and rotate relative to the fixed
frame.

A point :math:`P` is fixed in the moving frame, so its coordinates in :math:`(x_b, y_b, z_b)` are
constant. Even so, the point may still move relative to the fixed frame because the frame itself
moves.

The position of :math:`P` relative to the origin :math:`O` of the fixed frame is

.. math::

    \vec{r}_{P/O} = \vec{r}_{O_b/O} + \vec{r}_{P/O_b}

To evaluate this expression, all vectors must be expressed in the same reference frame.

**************************
 Rotation transformations
**************************

Rotation matrices are used to express vector coordinates in a different frame.

The three principal rotation matrices are

.. math::

    R_z(\psi) =
    \begin{pmatrix}
    \cos\psi & -\sin\psi & 0 \\
    \sin\psi & \cos\psi & 0 \\
    0 & 0 & 1
    \end{pmatrix}

.. math::

    R_y(\theta) =
    \begin{pmatrix}
    \cos\theta & 0 & \sin\theta \\
    0 & 1 & 0 \\
    -\sin\theta & 0 & \cos\theta
    \end{pmatrix}

.. math::

    R_x(\phi) =
    \begin{pmatrix}
    1 & 0 & 0 \\
    0 & \cos\phi & -\sin\phi \\
    0 & \sin\phi & \cos\phi
    \end{pmatrix}

If :math:`\mathbf{r}^b` is known in frame :math:`b`, then its coordinates in frame :math:`0` are
given by

.. math::

    \mathbf{r}^0 = R^0_b \mathbf{r}^b

An arbitrary orientation can be built by combining principal rotations. A common choice is

.. math::

    R^0_b = R_z(\psi)R_y(\theta)R_x(\phi)

****************************
 Velocity in a moving frame
****************************

If point :math:`P` is fixed in the moving frame, then its velocity relative to the fixed frame is

.. math::

    \vec{v}_{P/0} = \vec{v}_b + \vec{\omega} \times \vec{r}_{P/O_b}

where :math:`\vec{v}_b` is the velocity of the moving frame origin and :math:`\vec{\omega}` is the
angular velocity of the moving frame.

If :math:`P` also moves relative to the moving frame, then

.. math::

    \vec{v}_P = \vec{v}_b + (\vec{v}_P)_b + \vec{\omega} \times \vec{r}_{P/O_b}

where :math:`(\vec{v}_P)_b` is the velocity observed in the body-fixed frame.

********************************
 Acceleration in a moving frame
********************************

Differentiating the velocity expression gives

.. math::

    \vec{a}_P
    =
    \vec{a}_b
    + (\vec{a}_P)_b
    + \vec{\alpha} \times \vec{r}_{P/O_b}
    + \vec{\omega} \times (\vec{\omega} \times \vec{r}_{P/O_b})
    + 2\,\vec{\omega} \times (\vec{v}_P)_b

The terms have clear physical meaning:

- :math:`\vec{a}_b`: acceleration of the moving frame origin
- :math:`(\vec{a}_P)_b`: acceleration relative to the moving frame
- :math:`\vec{\alpha} \times \vec{r}_{P/O_b}`: tangential acceleration
- :math:`\vec{\omega} \times (\vec{\omega} \times \vec{r}_{P/O_b})`: centripetal acceleration
- :math:`2\,\vec{\omega} \times (\vec{v}_P)_b`: Coriolis acceleration

************************************
 Linear Velocities and Acceleration
************************************

Linear Velocity
===============

This section introduces discusess linear velocity. Lets first discuss velocity before introducing
the equations. The two frames, intertial and moving(body) frame are defined. Our moving frame, in
some cases a boat, a drone or a plane is moving with translational velocity. We want to find an
analyze the kinematics of a point on these, say a moving person, a static sensor or heli platform.

.. math::

    \vec{v}_{P/i}^i
    =
    \vec{v}_{b/i}^i
    +
    \frac{d^b}{dt}\vec{r}_{P/b}
    +
    \vec{\omega}_{b/i}^i \times \vec{r}_{P/b}

This equation decomposes the motion of :math:`P` into contributions associated with the motion of
the reference frame :math:`b` and the motion relative to that frame.

The first term, :math:`\vec{v}_{b/i}^i`, represents the translational velocity of the origin of the
moving frame. It captures how the entire body moves through space.

The second term, :math:`\frac{d^b}{dt}\mathbf{r}_{P/b}`, represents the velocity of the point
relative to the moving frame. This term is nonzero only if the point moves within the body, for
example a person walking on a deck.

The third term, :math:`\boldsymbol{\omega}_{b/i}^i \times \mathbf{r}_{P/b}`, accounts for the
rotation of the moving frame. Even if the point is fixed in the body, rotation induces a velocity
relative to the inertial frame.

Together, these terms provide a complete description of the velocity of a point attached to or
moving within a rigid body. In many practical cases, one or more of the terms may vanish, which
simplifies the expression.

A note on the derivative
========================

The term :math:`\frac{d^b}{dt}\mathbf{r}_{P/b}` requires some care. The vector
:math:`\mathbf{r}_{P/b}` is expressed in the moving frame :math:`b`, whose basis vectors are
themselves rotating in time. As a result, the time derivative of a vector depends on which frame the
derivative is taken in.

The notation :math:`\frac{d^b}{dt}` means that the derivative is taken while observing the vector
from frame :math:`b`, where the basis vectors are fixed. In this frame, only changes in the
coordinates of the vector contribute to the derivative.

If the point :math:`P` is fixed in the moving frame, then its coordinates in :math:`b` are constant,
and therefore

.. math::

    \frac{d^b}{dt}\mathbf{r}_{P/b} = \mathbf{0}

However, when viewed from the inertial frame :math:`i`, the same vector may still change due to the
rotation of the frame. This effect is captured by the additional term

.. math::

    \boldsymbol{\omega}_{b/i}^i \times \mathbf{r}_{P/b}

This separation allows us to distinguish between motion relative to the body and motion caused
purely by the rotation of the reference frame.

A Visual Interpretation of the Linear Velocity Equation
=======================================================

.. raw:: html
    :file: _includes/animation/threejs_viz_lin_vel.html

A Visual Interpretation of the Linear Velocity Equation (boat)
==============================================================

.. raw:: html
    :file: _includes/animation/threejs_viz_lin_vel_boat.html

*********
 Summary
*********

The key ideas of vector kinematics are:

- vectors are described relative to reference frames
- vectors must be expressed in a common frame before they can be added
- rotation matrices transform coordinates between frames
- moving and rotating frames introduce extra velocity and acceleration terms

These ideas are fundamental in rigid-body mechanics, robotics, and vehicle dynamics.

.. admonition:: A modern cautionary tale

    In 2026, a French sailor reportedly revealed the position of the aircraft carrier
    :math:`\textit{Charles de Gaulle}` by uploading a public Strava run recorded on the deck.

.. figure:: figures/strava.jpg
    :width: 70%
    :align: center

    A recorded trajectory can reveal the motion of the entire reference frame.


Exercise 1: Velocity of a Point on a Rotating Vessel
=====================================================

A ship (body frame :math:`b`) moves through calm water with a constant translational
velocity :math:`\vec{v}_{b/i}^i = (3, 1, 0)^\top` m/s expressed in the inertial frame.
The ship rotates at a constant yaw rate :math:`\dot\psi = 0.2` rad/s about the vertical axis,
so the angular velocity is :math:`\vec{\omega}_{b/i}^i = (0, 0, 0.2)^\top` rad/s.

A sensor is mounted on the bow, fixed to the ship at position
:math:`\vec{r}_{P/b}^b = (5, 0, 0)^\top` m (5 m ahead of the ship's origin along the body
x-axis).

At the instant of interest the body frame coincides with the inertial frame
(:math:`R^0_b = I`), so :math:`\vec{r}_{P/b}^i = (5, 0, 0)^\top` m.

**Find** the velocity of the sensor relative to the inertial frame at this instant.

.. admonition:: Solution
   :class: dropdown

   Because the sensor is fixed in the body frame, the relative velocity term vanishes:

   .. math::

       \frac{d^b}{dt}\vec{r}_{P/b} = \mathbf{0}

   The velocity equation therefore reduces to

   .. math::

       \vec{v}_{P/i}^i
       = \vec{v}_{b/i}^i + \vec{\omega}_{b/i}^i \times \vec{r}_{P/b}^i

   Compute the cross product:

   .. math::

       \vec{\omega} \times \vec{r}_{P/b}
       =
       \begin{pmatrix} 0 \\ 0 \\ 0.2 \end{pmatrix}
       \times
       \begin{pmatrix} 5 \\ 0 \\ 0 \end{pmatrix}
       =
       \begin{pmatrix}
         0 \cdot 0 - 0.2 \cdot 0 \\
         0.2 \cdot 5 - 0 \cdot 0 \\
         0 \cdot 0 - 0 \cdot 5
       \end{pmatrix}
       =
       \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
       \text{ m/s}

   Adding the translational velocity:

   .. math::

       \vec{v}_{P/i}^i
       =
       \begin{pmatrix} 3 \\ 1 \\ 0 \end{pmatrix}
       +
       \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
       =
       \begin{pmatrix} 3 \\ 2 \\ 0 \end{pmatrix}
       \text{ m/s}

   The rotation adds 1 m/s in the :math:`y`-direction because the bow sweeps sideways
   as the ship yaws.

   Exercise 2: Coordinate Transformation Using a Rotation Matrix
=============================================================

A drone's body frame :math:`b` is obtained from the inertial frame by a pure yaw rotation
of :math:`\psi = 90°` followed by a pure pitch rotation of :math:`\theta = 30°`.
The combined rotation matrix is

.. math::

    R^0_b = R_z(90°)\,R_y(30°)

A velocity vector is measured by an onboard sensor and expressed in the body frame as

.. math::

    \mathbf{v}^b =
    \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix}
    \text{ m/s}

**Find** the same velocity expressed in the inertial frame :math:`\mathbf{v}^0`.

.. admonition:: Solution
   :class: dropdown

   First, evaluate the two principal rotation matrices.

   **Yaw** (:math:`\psi = 90°`, so :math:`\cos 90° = 0`,  :math:`\sin 90° = 1`):

   .. math::

       R_z(90°) =
       \begin{pmatrix}
         0 & -1 & 0 \\
         1 &  0 & 0 \\
         0 &  0 & 1
       \end{pmatrix}

   **Pitch** (:math:`\theta = 30°`, so :math:`\cos 30° = \tfrac{\sqrt{3}}{2}`,
   :math:`\sin 30° = \tfrac{1}{2}`):

   .. math::

       R_y(30°) =
       \begin{pmatrix}
         \tfrac{\sqrt{3}}{2} & 0 & \tfrac{1}{2} \\
         0                   & 1 & 0            \\
        -\tfrac{1}{2}        & 0 & \tfrac{\sqrt{3}}{2}
       \end{pmatrix}

   **Combined rotation:**

   .. math::

       R^0_b
       = R_z(90°)\,R_y(30°)
       =
       \begin{pmatrix}
         0 & -1 & 0 \\
         1 &  0 & 0 \\
         0 &  0 & 1
       \end{pmatrix}
       \begin{pmatrix}
         \tfrac{\sqrt{3}}{2} & 0 & \tfrac{1}{2} \\
         0                   & 1 & 0            \\
        -\tfrac{1}{2}        & 0 & \tfrac{\sqrt{3}}{2}
       \end{pmatrix}
       =
       \begin{pmatrix}
         0                   & -1 & 0            \\
         \tfrac{\sqrt{3}}{2} &  0 & \tfrac{1}{2} \\
        -\tfrac{1}{2}        &  0 & \tfrac{\sqrt{3}}{2}
       \end{pmatrix}

   **Transform the vector:**

   .. math::

       \mathbf{v}^0
       = R^0_b\,\mathbf{v}^b
       =
       \begin{pmatrix}
         0                   & -1 & 0            \\
         \tfrac{\sqrt{3}}{2} &  0 & \tfrac{1}{2} \\
        -\tfrac{1}{2}        &  0 & \tfrac{\sqrt{3}}{2}
       \end{pmatrix}
       \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix}
       =
       \begin{pmatrix}
         0\cdot2 + (-1)\cdot0 + 0\cdot(-1) \\
         \tfrac{\sqrt{3}}{2}\cdot2 + 0 + \tfrac{1}{2}\cdot(-1) \\
         -\tfrac{1}{2}\cdot2 + 0 + \tfrac{\sqrt{3}}{2}\cdot(-1)
       \end{pmatrix}
       =
       \begin{pmatrix}
         0 \\
         \sqrt{3} - \tfrac{1}{2} \\
         -1 - \tfrac{\sqrt{3}}{2}
       \end{pmatrix}
       \approx
       \begin{pmatrix}
         0 \\
         1.23 \\
        -1.87
       \end{pmatrix}
       \text{ m/s}

   Note that the rotation changes the direction of the velocity vector but not its
   magnitude — :math:`\lVert\mathbf{v}\rVert = \sqrt{5}` m/s in both frames.