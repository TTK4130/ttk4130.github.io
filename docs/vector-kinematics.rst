###################
 Vector Kinematics
###################

Kinematics describes motion without considering the forces that cause it. In mechanics and robotics,
it provides the tools needed to describe position, velocity, and acceleration of points in moving
reference frames.

.. note::

    This page assumes familiarity with reference frames and rotation matrices. See
    :doc:`reference-frames` for a full introduction including unit vectors, rotation matrix
    derivations, and Euler angle conventions.

*******************************
 Reference frames and position
*******************************

.. raw:: html
    :file: _includes/animation/threejs_ref_frame_and_position.html

Consider a fixed inertial frame :math:`i` and a moving body frame :math:`b` that may translate and
rotate relative to :math:`i`. A point :math:`P` fixed in :math:`b` may still move relative to
:math:`i` because the frame itself moves.

The position of :math:`P` relative to the origin :math:`O` of the fixed frame decomposes as

.. math::

    \vec{r}_{P/O} = \vec{r}_{O_b/O} + \vec{r}_{P/b}

All vectors in this sum must be expressed in the same frame before they can be added numerically.

**************************
 Rotation transformations
**************************

If :math:`\mathbf{r}^b` is a vector expressed in frame :math:`b`, its coordinates in frame :math:`0`
are obtained by

.. math::

    \mathbf{r}^0 = R^0_b \, \mathbf{r}^b

The three principal rotation matrices are

.. math::

    R_z(\psi) =
    \begin{pmatrix}
    \cos\psi & -\sin\psi & 0 \\
    \sin\psi & \cos\psi & 0 \\
    0 & 0 & 1
    \end{pmatrix}
    \qquad
    R_y(\theta) =
    \begin{pmatrix}
    \cos\theta & 0 & \sin\theta \\
    0 & 1 & 0 \\
    -\sin\theta & 0 & \cos\theta
    \end{pmatrix}
    \qquad
    R_x(\phi) =
    \begin{pmatrix}
    1 & 0 & 0 \\
    0 & \cos\phi & -\sin\phi \\
    0 & \sin\phi & \cos\phi
    \end{pmatrix}

An arbitrary orientation can be built by composing these. A common choice for ships, aircraft, and
drones is the ZYX (yaw, pitch, roll) sequence

.. math::

    R^0_b = R_z(\psi)\,R_y(\theta)\,R_x(\phi)

See :doc:`reference-frames` for the derivation of these matrices and a discussion of intrinsic
versus extrinsic rotation conventions.

.. dropdown:: Exercise: Coordinate transformation using a rotation matrix

    A drone's body frame :math:`b` is obtained from the inertial frame by a pure yaw rotation of
    :math:`\psi = 90°` followed by a pure pitch rotation of :math:`\theta = 30°`. The combined
    rotation matrix is

    .. math::

        R^0_b = R_z(90°)\,R_y(30°)

    A velocity vector is measured by an onboard sensor and expressed in the body frame as

    .. math::

        \mathbf{v}^b =
        \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix}
        \text{ m/s}

    **Find** the same velocity expressed in the inertial frame :math:`\mathbf{v}^0`.

.. dropdown:: Solution
    :color: success

    First, evaluate the two principal rotation matrices.

    **Yaw** (:math:`\psi = 90°`, so :math:`\cos 90° = 0`, :math:`\sin 90° = 1`):

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

    The rotation changes the direction of the velocity vector but not its magnitude.
    In both frames :math:`\lVert\mathbf{v}\rVert = \sqrt{5}` m/s.

****************************
 Velocity in a moving frame
****************************

The velocity of point :math:`P` relative to the inertial frame :math:`i`, expressed in :math:`i`, is

.. math::

    \vec{v}_{P/i}^i
    =
    \vec{v}_{b/i}^i
    +
    \frac{d^b}{dt}\vec{r}_{P/b}
    +
    \vec{\omega}_{b/i}^i \times \vec{r}_{P/b}

The three terms each capture a distinct contribution to the motion of :math:`P`:

- :math:`\vec{v}_{b/i}^i` is the translational velocity of the moving frame origin.
- :math:`\frac{d^b}{dt}\vec{r}_{P/b}` is the velocity of :math:`P` relative to the moving frame. It
  is zero when :math:`P` is fixed in the body, for example a static sensor.
- :math:`\vec{\omega}_{b/i}^i \times \vec{r}_{P/b}` is the velocity caused by the rotation of the
  frame. It is nonzero even when :math:`P` is fixed in the body.

A note on the frame-dependent derivative
========================================

The notation :math:`\frac{d^b}{dt}` means the derivative is taken while observing the vector from
frame :math:`b`, where the basis vectors are fixed. Only changes in the coordinates of the vector
contribute.

If :math:`P` is fixed in the body frame, its coordinates in :math:`b` are constant, so

.. math::

    \frac{d^b}{dt}\vec{r}_{P/b} = \mathbf{0}

When the same vector is viewed from the inertial frame, it still appears to change because the frame
rotates. That effect is captured separately by the third term :math:`\vec{\omega}_{b/i}^i \times
\vec{r}_{P/b}`.

The animations below illustrate the three terms acting simultaneously, first for a generic rigid
body and then for a ship.

.. raw:: html
    :file: _includes/animation/threejs_viz_lin_vel.html

.. raw:: html
    :file: _includes/animation/threejs_viz_lin_vel_boat.html

.. dropdown:: Exercise: Velocity of a point on a rotating vessel

    A ship (body frame :math:`b`) moves through calm water with a constant translational velocity
    :math:`\vec{v}_{b/i}^i = (3, 1, 0)^\top` m/s expressed in the inertial frame. The ship rotates
    at a constant yaw rate :math:`\dot\psi = 0.2` rad/s about the vertical axis, so the angular
    velocity is :math:`\vec{\omega}_{b/i}^i = (0, 0, 0.2)^\top` rad/s.

    A sensor is mounted on the bow, fixed to the ship at position
    :math:`\vec{r}_{P/b}^b = (5, 0, 0)^\top` m (5 m ahead of the ship origin along the body
    x-axis).

    At the instant of interest the body frame coincides with the inertial frame
    (:math:`R^0_b = I`), so :math:`\vec{r}_{P/b}^i = (5, 0, 0)^\top` m.

    **Find** the velocity of the sensor relative to the inertial frame at this instant.

.. dropdown:: Solution
    :color: success

    Because the sensor is fixed in the body frame, the relative velocity term vanishes:

    .. math::

        \frac{d^b}{dt}\vec{r}_{P/b} = \mathbf{0}

    The velocity equation reduces to

    .. math::

        \vec{v}_{P/i}^i
        = \vec{v}_{b/i}^i + \vec{\omega}_{b/i}^i \times \vec{r}_{P/b}^i

    Compute the cross product:

    .. math::

        \vec{\omega}_{b/i}^i \times \vec{r}_{P/b}^i
        =
        \begin{pmatrix} 0 \\ 0 \\ 0.2 \end{pmatrix}
        \times
        \begin{pmatrix} 5 \\ 0 \\ 0 \end{pmatrix}
        =
        \begin{pmatrix}
          0 \cdot 0   - 0.2 \cdot 0 \\
          0.2 \cdot 5 - 0 \cdot 0   \\
          0 \cdot 0   - 0 \cdot 5
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

    The rotation adds 1 m/s in the :math:`y`-direction because the bow sweeps sideways as the
    ship yaws.

********************************
 Acceleration in a moving frame
********************************

To find the acceleration, differentiate the velocity equation with respect to time in the inertial
frame. The key tool is the **transport theorem**: for any vector :math:`\vec{u}`,

.. math::

    \frac{d^i}{dt}\vec{u} = \frac{d^b}{dt}\vec{u} + \vec{\omega}_{b/i} \times \vec{u}

Applying this to each term in the velocity equation and collecting gives

.. math::

    \vec{a}_{P/i}^i
    =
    \vec{a}_{b/i}^i
    + \left(\vec{a}_P\right)_b
    + \vec{\alpha}_{b/i}^i \times \vec{r}_{P/b}
    + \vec{\omega}_{b/i}^i \times \left(\vec{\omega}_{b/i}^i \times \vec{r}_{P/b}\right)
    + 2\,\vec{\omega}_{b/i}^i \times \frac{d^b}{dt}\vec{r}_{P/b}

Each term has a clear physical meaning:

- :math:`\vec{a}_{b/i}^i` is the acceleration of the moving frame origin.
- :math:`\left(\vec{a}_P\right)_b` is the acceleration of :math:`P` relative to the moving frame.
- :math:`\vec{\alpha}_{b/i}^i \times \vec{r}_{P/b}` is the tangential acceleration caused by angular
  acceleration of the frame.
- :math:`\vec{\omega}_{b/i}^i \times \left(\vec{\omega}_{b/i}^i \times \vec{r}_{P/b}\right)` is the
  centripetal acceleration, always directed toward the rotation axis.
- :math:`2\,\vec{\omega}_{b/i}^i \times \frac{d^b}{dt}\vec{r}_{P/b}` is the Coriolis acceleration,
  which arises when :math:`P` moves within a rotating frame.

The animation below shows the two most commonly encountered terms: centripetal (panel 1) and
Coriolis (panel 2).

.. raw:: html
    :file: _includes/animation/threejs_accel_moving_frame.html

*********
 Summary
*********

The key ideas of vector kinematics are:

- Vectors must be expressed in a common frame before they can be added.
- Rotation matrices transform coordinates between frames. See :doc:`reference-frames` for
  derivations and Euler angle conventions.
- A rotating frame induces an extra velocity term :math:`\vec{\omega} \times \vec{r}` even for
  points fixed in the body.
- Differentiating the velocity equation via the transport theorem yields five acceleration terms,
  including centripetal and Coriolis contributions.

These ideas are fundamental in rigid-body mechanics, robotics, and vehicle dynamics.

.. admonition:: A modern cautionary tale

    In 2026, a French sailor reportedly revealed the position of the aircraft carrier
    :math:`\textit{Charles de Gaulle}` by uploading a public Strava run recorded on the deck.

.. figure:: figures/strava.jpg
    :width: 70%
    :align: center

    A recorded trajectory can reveal the motion of the entire reference frame.

********************************************
 Vector kinematics with SymPy ``mechanics``
********************************************

``sympy.physics.mechanics`` lets you work with symbolic reference frames, points, and vectors.
Orientations between frames are declared once; SymPy then differentiates vectors in the correct
frame when you ask for velocities and accelerations.

Setting up frames and orientation
=================================

.. jupyter-execute::

    import sympy as sm
    from sympy.physics.mechanics import ReferenceFrame, Point, dynamicsymbols
    sm.init_printing(use_latex='mathjax')

    psi, v_x, v_y = dynamicsymbols("psi v_x v_y")

    N = ReferenceFrame("N")  # inertial frame
    B = N.orientnew("B", "Axis", [psi, N.z])  # body frame: yaw by psi about N.z

    B.ang_vel_in(N)

The prime denotes :math:`d/dt`, so the result is :math:`\vec\omega_{B/N} = \dot\psi\,\hat{N}_z`.

Velocity via the two-point theorem
==================================

``v2pt_theory(Q, N, B)`` sets the velocity of a point using the transport theorem, given the
velocity of a reference point ``Q`` and assuming both points are fixed in frame ``B``:

.. jupyter-execute::

    O = Point("O")  # inertial origin (fixed)
    O_b = Point("O_b")  # ship origin

    O.set_vel(N, 0)
    O_b.set_vel(N, v_x * N.x + v_y * N.y)

    P = O_b.locatenew("P", 5 * B.x)  # bow sensor, 5 m along body x-axis
    P.v2pt_theory(O_b, N, B)

    P.vel(N)

Substituting :math:`\psi = 0`, :math:`\dot\psi = 0.2` rad/s, :math:`v_x = 3` m/s, :math:`v_y = 1`
m/s recovers the result from the exercise above:

.. jupyter-execute::

    P.vel(N).subs({psi: 0, psi.diff(): 0.2, v_x: 3, v_y: 1}).to_matrix(N)

Acceleration
============

``acc()`` differentiates the stored velocity, applying the transport theorem again to produce all
five terms from the acceleration formula, including centripetal and Coriolis:

.. jupyter-execute::

    P.acc(N).express(N).simplify()

Vectors can be expressed in any frame with ``.express()`` and converted to a column matrix with
``.to_matrix()``.

.. note::

    For more examples of rolling discs, pendulums, multi-body systems, and full equations of motion
    via Kane's and Lagrange's methods, see the `SymPy mechanics documentation
    <https://docs.sympy.org/latest/modules/physics/mechanics/>`_.
