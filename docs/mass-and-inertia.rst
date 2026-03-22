.. _mass-and-inertia:

======================
Mass and Inertia (WIP)
======================

Learning Objectives
===================

After reading this chapter the reader should know:

- What the inertia matrix is and how it is constructed from the mass distribution of a body.
- How the inertia matrix transforms when changing reference frames or reference points.
- What angular momentum is and how it relates to the inertia matrix and angular velocity.
- The Newton-Euler equations of motion for a rigid body, both about the center of mass and about an arbitrary point.
- How to apply the parallel axis theorem.


Introduction
============

Picture a figure skater doing a spin. As they pull their arms in close to their body, they spin noticeably faster.
Something about the *distribution of mass* is controlling how easy or hard it is to change the rotation.

That "something" is the **inertia matrix** (also called the **inertia tensor**). Just as mass is the scalar
quantity that resists changes to linear velocity (:math:`F = ma`), the inertia matrix is the 3×3 tensor
quantity that resists changes to angular velocity. When the skater pulls in their arms, the mass moves
closer to the axis of rotation and the effective inertia decreases, so the angular velocity must increase
to conserve angular momentum.

Given a rotating body, what inertia does it present to an applied torque? The answer to
this question is what drives the rotational equations of motion (Newton-Euler), which we also derive in
this chapter. By the end of the page you will be able to write down and compute the full equations of
motion for a rigid body in 3D.


A spinning top
--------------

Throughout this chapter we use a **spinning top** (often just referred to as "top"), 
a solid cone with a short cylindrical stem, as our running example, 
building up its inertia properties step by step.

.. Define top dimensions
.. jupyter-execute::

    import numpy as np

    # Cone (body)
    m_cone = 0.4    # kg
    R_cone = 0.04   # m
    H_cone = 0.06   # m

    # Stem (handle)
    m_stem = 0.1    # kg
    R_stem = 0.008  # m
    L_stem = 0.04   # m

    # Bolt (used in some examples to break symmetry)
    m_bolt  = 0.02                           # kg
    r_bolt  = np.array([R_cone, 0, H_cone])  # m
..

.. Top animation help functions
.. jupyter-execute::
    :hide-code:

    import pythreejs as pj
    import ipywidgets as widgets
    from scipy.spatial.transform import Rotation as _Rotation

    # Fixed rotation used to convert Z-up physics quaternions to Y-up Three.js quaternions.
    # A Z-up spin about +z becomes a Y-up spin about +y, matching the cone geometry axis.
    _R_zup_to_yup = _Rotation.from_euler('x', -90, degrees=True)

    def sol_to_yup_quats(sol):
        """Convert Z-up scipy integrator output to Y-up pythreejs [x,y,z,w] quaternions."""
        q = sol.y[:4].T                                    # (N,4) in [w,x,y,z]
        q /= np.linalg.norm(q, axis=1, keepdims=True)
        r_phys = _Rotation.from_quat(q[:, [1, 2, 3, 0]])  # scipy uses [x,y,z,w]
        r_yup  = _R_zup_to_yup * r_phys * _R_zup_to_yup.inv()
        return r_yup.as_quat()                             # [x,y,z,w] for pythreejs

    def make_top_animation(quats, times, width=600, height=400, show_bolt=False):
        s   = 10          # visual scale factor (metres → display units)
        R_v = R_cone * s
        H_v = H_cone * s
        r_v = R_stem * s
        L_v = L_stem * s

        # Two half-cones with different color
        cone_a = pj.Mesh(
            pj.CylinderGeometry(radiusTop=R_v, radiusBottom=0, height=H_v,
                                radialSegments=32,
                                thetaStart=0,      thetaLength=np.pi),
            pj.MeshLambertMaterial(color='royalblue', side='DoubleSide'),
        )
        cone_b = pj.Mesh(
            pj.CylinderGeometry(radiusTop=R_v, radiusBottom=0, height=H_v,
                                radialSegments=32,
                                thetaStart=np.pi,  thetaLength=np.pi),
            pj.MeshLambertMaterial(color='orange', side='DoubleSide'),
        )
        cone_a.position = cone_b.position = [0, H_v / 2, 0]

        # Stem on top of cone (handle)
        stem_mesh = pj.Mesh(
            pj.CylinderGeometry(radiusTop=r_v, radiusBottom=r_v, height=L_v,
                                radialSegments=16),
            pj.MeshLambertMaterial(color='#cccccc'),
        )
        stem_mesh.position = [0, H_v + L_v / 2, 0]

        top = pj.Group()
        top.add(cone_a)
        top.add(cone_b)
        top.add(stem_mesh)

        # Optionally added mass (bolt)
        if show_bolt:
            bolt_r = R_v * 0.15
            bolt_mesh = pj.Mesh(
                pj.SphereGeometry(radius=bolt_r, widthSegments=12, heightSegments=8),
                pj.MeshLambertMaterial(color='red'),
            )
            bolt_mesh.position = [R_v, H_v, 0]
            top.add(bolt_mesh)

        top.name = "top"

        cy = (H_v + L_v) / 2
        camera = pj.PerspectiveCamera(
            position=[0, cy + 3, 4], aspect=width / height)
        scene  = pj.Scene(
            background='#1a1a2e',
            children=[
                top, camera,
                pj.DirectionalLight(position=[5, 10, 5], intensity=0.8),
                pj.AmbientLight(intensity=0.4),
            ],
        )
        controls = pj.OrbitControls(controlling=camera, target=[0, cy, 0])
        camera.lookAt([0, cy, 0])
        renderer = pj.Renderer(
            scene=scene, camera=camera,
            controls=[controls],
            width=width, height=height,
        )
        renderer.layout = widgets.Layout(width="100%", height="auto")

        clip   = pj.AnimationClip(tracks=[
            pj.QuaternionKeyframeTrack(name="top.quaternion", times=times, values=quats),
        ], duration=float(times[-1]))
        action = pj.AnimationAction(pj.AnimationMixer(top), clip, top)

        return renderer, action
..

.. Spinning top demonstration
.. jupyter-execute::
    :hide-code:

    # Demo trajectory: 6 rad/s spin about z (Z-up), converted to Y-up for display
    t_demo     = np.linspace(0, 4, 240)
    r_demo     = _Rotation.from_euler('z', 6.0 * t_demo)

    _R_zup_to_yup = _Rotation.from_euler('x', -90, degrees=True)
    quats_demo = (_R_zup_to_yup * r_demo * _R_zup_to_yup.inv()).as_quat()

    renderer_demo, action_demo = make_top_animation(quats_demo, t_demo)
    renderer_demo

.. jupyter-execute::
    :hide-code:

    action_demo
..


Mass and Center of Mass
=======================

Before tackling the full inertia matrix, let us recall the simpler scalar quantities.
The total mass of a body is obtained by integrating the mass density over the body's volume:

.. Define mass
.. math::

    m = \int dm
..

The **center of mass** is the mass-weighted average position:

.. Define center of mass
.. math::

    \mathbf{r}_c = \frac{1}{m} \int \mathbf{r} \, dm
..

For a system of :math:`N` discrete point masses :math:`m_k` at positions :math:`\mathbf{r}_k`, these
integrals become sums:

.. Discrete mass and center of mass
.. math::

    m = \sum_{k=1}^{N} m_k, \qquad
    \mathbf{r}_c = \frac{1}{m} \sum_{k=1}^{N} m_k \mathbf{r}_k
..

The center of mass is special: the Newton-Euler equations take their simplest form when we measure
rotation relative to this point.

Our spinning top is a solid cone (the body) with a short cylindrical stem (the handle).
The cone's tip rests on the surface at the origin, and the spin axis points along :math:`z`.
Both components are axisymmetric, so their centers of mass lie on the :math:`z`-axis.
We can therefore find the combined center of mass by treating each component as a point
mass located at its own center of mass.

.. EXAMPLE: Center of mass
.. jupyter-execute::

    # Centers of mass of each component
    z_cm_cone = 3 * H_cone / 4
    r_cm_cone = np.array([0, 0, z_cm_cone])
    z_cm_stem = H_cone + L_stem / 2
    r_cm_stem = np.array([0, 0, z_cm_stem])

    masses    = np.array([m_cone, m_stem])
    positions = np.array([r_cm_cone, r_cm_stem])

    m_total = np.sum(masses)
    r_cm_top    = np.average(positions, axis=0, weights=masses)
    z_cm_top    = r_cm_top[2]

    print(f"Total mass:                {m_total:.2f} kg")
    print(f"Cone CoM (above tip):      z = {z_cm_cone:.4f} m")
    print(f"Stem CoM (above tip):      z = {z_cm_stem:.4f} m")
    print(f"Combined CoM (above tip):  z = {z_cm_top:.4f} m")
..

.. EXERCISE: Center of mass
.. admonition:: Exercise
    :class: dropdown

    A small mounting bolt of mass is attached at the rim of the cone at its top.

    .. jupyter-execute::

        print(f"Bolt mass (kg):          {m_bolt}")
        print(f"Bolt position (m):       {r_bolt}")

    Find the center of mass of the combined system (cone + stem + bolt).
    By how many millimetres does the bolt shift the CoM in the :math:`x`-direction?

.. dropdown:: Solution
    :color: success

    .. jupyter-execute::

        masses    = np.array([m_cone, m_stem, m_bolt])
        positions = np.array([r_cm_cone, r_cm_stem, r_bolt])

        r_cm_top = np.average(positions, axis=0, weights=masses)
        print(f"Center of mass: {r_cm_top}")
        print(f"x-shift due to bolt: {r_cm_top[0]*1000:.3f} mm")
..


The Inertia Matrix
==================

Definition via Integral
-----------------------

For rotation, the role of scalar mass is played by the **inertia matrix** :math:`\mathbf{M}_{b/c}`,
which encodes how the mass of body :math:`b` is distributed around its center of mass :math:`c`.

.. Define inertia matrix
.. admonition:: Inertia Matrix

    The inertia matrix of body :math:`b` about center of mass :math:`c`, expressed in frame :math:`i`, is

    .. math::
        :label: inertia-def

        \mathbf{M}^i_{b/c}
        = -\int_b [\mathbf{r}^i]^\times [\mathbf{r}^i]^\times \, dm
        = \int_b \left[ (\mathbf{r}^i)^\top \mathbf{r}^i \, \mathbf{I}
          - \mathbf{r}^i (\mathbf{r}^i)^\top \right] dm

    where :math:`\mathbf{r}^i` is the position of the mass element relative to :math:`c` expressed in
    frame :math:`i`, and :math:`[\mathbf{r}]^\times` is the skew-symmetric cross-product matrix such
    that :math:`[\mathbf{r}]^\times \mathbf{v} = \mathbf{r} \times \mathbf{v}` for any vector
    :math:`\mathbf{v}`.
..

The skew-symmetric matrix of a vector :math:`\mathbf{r} = [x, y, z]^\top` is:

.. Define skew symmetric matrix
.. math::

    [\mathbf{r}]^\times =
    \begin{bmatrix}
         0 & -z &  y \\
         z &  0 & -x \\
        -y &  x &  0
    \end{bmatrix}
..

Let us build this in SymPy and compute the inertia contribution of a single point mass at a
general position :math:`(x, y, z)`:

.. Degine single-point inertia contribution
.. math::

    m \left[ (\mathbf{r})^\top \mathbf{r} \, \mathbf{I} - 
    \mathbf{r} (\mathbf{r})^\top \right]
..

.. Single-point inertia contribution
.. jupyter-execute::

    import sympy as sm
    sm.init_printing(use_latex='mathjax')

    x, y, z, m = sm.symbols('x y z m', real=True)
    r = sm.Matrix([x, y, z])

    M_point = m * (r.dot(r) * sm.eye(3) - r * r.T)
    M_point
..

We can verify this equals the skew-matrix formula:

.. Degine single-point inertia contribution
.. math::

    -m [\mathbf{r}]^\times [\mathbf{r}]^\times
..

.. Alternative single-point inertia contribution
.. jupyter-execute::

    def skew_sm(v):
        return sm.Matrix([
            [    0, -v[2],  v[1]],
            [ v[2],     0, -v[0]],
            [-v[1],  v[0],     0],
        ])
    

    def skew_np(v):
        return np.array([[    0, -v[2],  v[1]],
                         [ v[2],     0, -v[0]],
                         [-v[1],  v[0],     0]])
    

    r_cross     = skew_sm(r)
    M_from_skew = -m * r_cross * r_cross
    sm.simplify(M_from_skew)
..


Symmetry and Positive Definiteness
------------------------------------

The inertia matrix is always **symmetric** (follows directly from the definition) and
**positive definite**, meaning the rotational kinetic energy is always strictly positive:

.. Rotational kinetic energy is always strictly positive
.. math::

    T_\text{rot} = \frac{1}{2} \boldsymbol{\omega}^\top \mathbf{M}_{b/c} \, \boldsymbol{\omega} > 0
    \qquad \forall \, \boldsymbol{\omega} \neq \mathbf{0}
..

Positive definiteness guarantees all eigenvalues of :math:`\mathbf{M}` are strictly positive.
Let's ensure that this is the case for our spinning top:

.. EXAMPLE: Spinning top inertia matrix
.. jupyter-execute::

    # Cone and stem inertia formulas
    Izz_cone = 3 * m_cone * R_cone**2 / 10
    Ixx_cone = Iyy_cone = 3 * m_cone * (4*R_cone**2 + H_cone**2) / 80
    Izz_stem = m_stem * R_stem**2 / 2
    Ixx_stem = Iyy_stem = m_stem * (3*R_stem**2 + L_stem**2) / 12

    # Define the body-frame inertia for the cone and stem, respectively
    # Axisymmetric cone and stem -> All off-diagonal elements are zero
    M_cone = np.diag([Ixx_cone, Iyy_cone, Izz_cone])
    M_stem = np.diag([Ixx_stem, Iyy_stem, Izz_stem])

    # Vectors from the top's cm to each component's cm
    r_top_to_cone = r_cm_cone - r_cm_top
    r_top_to_stem = r_cm_stem - r_cm_top

    # Use the parallel axis theorem calculate the total top inertia matrix
    # The theorem will be discussed in greater detail later
    M_top = (
        M_cone + m_cone * skew_np(r_top_to_cone) @ skew_np(r_top_to_cone) +
        M_stem + m_stem * skew_np(r_top_to_stem) @ skew_np(r_top_to_stem)
    )

    print("Top inertia in the body frame (kg·m²):")
    print(np.round(M_top * 1e6, 2), "  (×10⁻⁶)")
..


Frame Transformations
=====================

The inertia matrix depends on which frame the position vectors :math:`\mathbf{r}^i` are expressed in.
The body frame :math:`b` is usually the most convenient for computation (the geometry is fixed), but the
Newton-Euler equations are defined in the inertial frame :math:`i`. The transformation between the two is:

.. Inertia fram transform
.. math::
    :label: inertia-frame-transform

    \mathbf{M}^i_{b/c} = \mathbf{R}^b_i \, \mathbf{M}^b_{b/c} \, \mathbf{R}^i_b
..

where :math:`\mathbf{R}^b_i` is the rotation matrix from frame :math:`i` to frame :math:`b`, and
:math:`\mathbf{R}^i_b = (\mathbf{R}^b_i)^\top`.

A rotation never changes the physical mass distribution, so the eigenvalues of the
inertia matrix are frame-independent. Let us verify this by comparing the inertia of the 
spinning top's body in the body frame with its inertia in the inertial frame after being
tilted 30° about the y-axis:

.. EXAMPLE: Spinning top rotated inertia matrix
.. jupyter-execute::

    # Tilt the top 30° about the y-axis
    theta = np.radians(30)
    Ry = np.array([
        [ np.cos(theta), 0.0, np.sin(theta)],
        [           0.0, 1.0,           0.0],
        [-np.sin(theta), 0.0, np.cos(theta)],
    ])

    M_top_inertial = Ry.T @ M_top @ Ry
    print("\nInertia in inertial frame after 30° tilt (kg·m²):")
    print(np.round(M_top_inertial * 1e6, 2), "  (×10⁻⁶)")

    eigs_body     = np.sort(np.linalg.eigvalsh(M_top))
    eigs_inertial = np.sort(np.linalg.eigvalsh(M_top_inertial))
    print(f"\nEigenvalues body frame:     {np.round(eigs_body*1e6, 4)} (×10⁻⁶)")
    print(f"Eigenvalues inertial frame: {np.round(eigs_inertial*1e6, 4)} (×10⁻⁶)")
..


Angular Momentum
================

About the Center of Mass
-------------------------

Angular momentum is the rotational analogue of linear momentum :math:`\mathbf{p} = m\mathbf{v}`.
The angular momentum of body :math:`b` about its center of mass :math:`c` is:

.. Define angular momentum about the CM
.. math::
    :label: angular-momentum-cm

    \mathbf{h}_{b/c} = \mathbf{M}_{b/c} \, \boldsymbol{\omega}_{b/i}
..

Note that :math:`\mathbf{h}_{b/c}` is generally **not parallel** to
:math:`\boldsymbol{\omega}_{b/i}` unless the rotation happens to be about a principal axis.

For our axisymmetric spinning top (no bolt), the inertia matrix in the body frame is diagonal.
Spinning along the :math:`z`-axis therefore gives angular momentum exactly parallel to
:math:`\boldsymbol{\omega}`:

.. jupyter-execute::

    omega = np.array([0.0, 0.0, 100.0])
    h     = M_cone @ omega

    cos_angle = np.dot(h, omega) / (np.linalg.norm(h) * np.linalg.norm(omega))
    angle_deg = np.degrees(np.arccos(np.clip(cos_angle, -1.0, 1.0)))

    print("--- Balanced cone (no bolt) ---")
    print(f"omega: {omega} rad/s")
    print(f"h:     {np.round(h, 6)} kg·m²/s")
    print(f"Angle between h and omega: {angle_deg:.4f}°  (parallel: no wobble)")

Now attach the bolt at the rim. The bolt's inertia contribution has off-diagonal terms because
its position :math:`[R\_cone, 0, H\_cone]` is not on the spin axis:

.. jupyter-execute::

    r_rel = r_bolt - r_cm_cone

    M_bolt = -m_bolt * skew_np(r_rel) @ skew_np(r_rel)
    M_unbalanced = M_cone + M_bolt

    h_unbal   = M_unbalanced @ omega
    cos_angle = np.dot(h_unbal, omega) / (np.linalg.norm(h_unbal) * np.linalg.norm(omega))
    angle_deg = np.degrees(np.arccos(np.clip(cos_angle, -1.0, 1.0)))

    print("--- Unbalanced cone (with bolt) ---")
    print(f"omega: {omega} rad/s")
    print(f"h:     {np.round(h_unbal, 6)} kg·m²/s")
    print(f"Angle between h and omega: {angle_deg:.4f}°  ← bolt causes wobble!")

The bolt shifts the angular momentum away from the spin axis. This is why even a small
imbalance in a rapidly spinning rotor causes vibration.


About a Different Point
-----------------------

When computing angular momentum about a point :math:`o` that is *not* the center of mass, an extra
term appears due to the translational motion of the center of mass:

.. math::
    :label: angular-momentum-o

    \mathbf{h}_{b/o} = \mathbf{M}_{b/o} \, \boldsymbol{\omega}_{b/i}
    + \mathbf{r}_{c/o} \times m \mathbf{v}_{c/i}

where :math:`\mathbf{r}_{c/o}` is the position of :math:`c` relative to :math:`o`, and
:math:`\mathbf{v}_{c/i}` is the velocity of the center of mass in the inertial frame.


Newton-Euler Equations of Motion
=================================

We now have all the ingredients to write down the full equations of motion for a rigid body.
There are two vector equations: one for translation and one for rotation.

About the Center of Mass
-------------------------

.. admonition:: Newton-Euler Equations (About Center of Mass)

    .. math::
        :label: newton-euler-cm

        \sum \mathbf{F} &= m \, \mathbf{a}^i_{c/i} \\[4pt]
        \sum \boldsymbol{\tau} &= \mathbf{M}^i_{b/c} \, \boldsymbol{\alpha}^i_{b/i}
        + \boldsymbol{\omega}^i_{b/i} \times \left(\mathbf{M}^i_{b/c} \, \boldsymbol{\omega}^i_{b/i}\right)

The translational equation is simply :math:`F = ma` applied to the center of mass :math:`c`.
In block matrix form both equations read:

.. math::

    \begin{bmatrix} m\mathbf{I} & \mathbf{0} \\ \mathbf{0} & \mathbf{M}_{b/c} \end{bmatrix}
    \begin{bmatrix} \mathbf{a}_{c/i} \\ \boldsymbol{\alpha}_{b/i} \end{bmatrix}
    +
    \begin{bmatrix} \mathbf{0} \\ \boldsymbol{\omega}_{b/i} \times (\mathbf{M}_{b/c}
    \boldsymbol{\omega}_{b/i}) \end{bmatrix}
    =
    \begin{bmatrix} \mathbf{F}_{b} \\ \boldsymbol{\tau}_{b} \end{bmatrix}


About a Different Point *o*
----------------------------

When the body is constrained to rotate about a fixed point :math:`o` that is not the center of mass
(a door hinge, a robot joint, a pendulum pivot), the equations change because the offset
:math:`\mathbf{r}^i_{c/o}` between the center of mass and the pivot couples translation and rotation:

.. math::
    :label: newton-euler-force-o

    \mathbf{F}_{b/o} = m \left(
        \mathbf{a}_c
        + \boldsymbol{\alpha}_{b/i} \times \mathbf{r}^i_{c/o}
        + \boldsymbol{\omega}_{b/i} \times \bigl(\boldsymbol{\omega}_{b/i} \times \mathbf{r}^i_{c/o}\bigr)
    \right)

.. math::
    :label: newton-euler-torque-o

    \boldsymbol{\tau}_{b/o} =
        \mathbf{r}^i_{c/o} \times m\mathbf{a}_c
        + \mathbf{M}_{b/o} \cdot \boldsymbol{\alpha}_{b/i}
        + \boldsymbol{\omega}_{b/i} \times \left(\mathbf{M}_{b/o} \cdot \boldsymbol{\omega}_{b/i}\right)

In block matrix form:

.. math::

    \begin{bmatrix}
        m\mathbf{I} & m(\mathbf{r}^i_{c/o})^{\times\top} \\
        m(\mathbf{r}^i_{c/o})^\times & \mathbf{M}_{b/o}
    \end{bmatrix}
    \begin{bmatrix} \mathbf{a}_o \\ \boldsymbol{\alpha}_{b/i} \end{bmatrix}
    +
    \begin{bmatrix}
        m(\boldsymbol{\omega}_{b/i})^\times (\boldsymbol{\omega}_{b/i})^\times \mathbf{r}^i_{c/o} \\
        \boldsymbol{\omega}_{b/i} \times (\mathbf{M}_{b/o} \boldsymbol{\omega}_{b/i})
    \end{bmatrix}
    =
    \begin{bmatrix} \mathbf{F}_{b/o} \\ \boldsymbol{\tau}_{b/o} \end{bmatrix}


The Parallel Axis Theorem
==========================

You computed the inertia matrix about the center of mass, but you need it about the wheel hub,
a joint, or the end of a rod. The **parallel axis theorem** lets you shift the reference point
without re-integrating.

.. admonition:: Parallel Axis Theorem (3D)

    Given the inertia matrix :math:`\mathbf{M}_{b/c}` about the center of mass :math:`c`, the inertia
    matrix about a new point :math:`o` is

    .. math::
        :label: parallel-axis-3d

        \mathbf{M}_{b/o} = \mathbf{M}_{b/c} - m [\mathbf{r}_{o/c}]^\times [\mathbf{r}_{o/c}]^\times

    where :math:`\mathbf{r}_{o/c}` is the vector from :math:`c` to :math:`o`.

In 2D, rotating about a fixed axis, the theorem reduces to the scalar form:

.. math::
    :label: parallel-axis-2d

    I_o = I_c + m d^2

where :math:`d` is the perpendicular distance between the original axis (through :math:`c`) and the
new axis (through :math:`o`). The inertia always *increases* when moving away from the center of mass, which means
the correction :math:`-m[\mathbf{r}]^\times[\mathbf{r}]^\times` is positive semi-definite.

The spinning top rests with its tip on a surface. Let us find the inertia matrix of the cone
about the tip :math:`o` by shifting from the cone's CoM :math:`c` (located at
:math:`z = \tfrac{3}{4}H_cone` above the tip) down to the tip at :math:`z = 0`:

.. jupyter-execute::

    import sympy as sm
    sm.init_printing(use_latex='mathjax')

    Ixx_c, Izz_c, m, H = sm.symbols('I_xx I_zz m H', positive=True)

    # Shift vector from CoM to tip: r_{o/c} = [0, 0, -3H/4]
    r_oc = sm.Matrix([0, 0, -sm.Rational(3, 4) * H])

    M_c = sm.diag(Ixx_c, Ixx_c, Izz_c)   # axisymmetric: Ixx = Iyy
    M_o = M_c - m * skew_sm(r_oc) * skew_sm(r_oc)
    M_o

:math:`I_{zz}` is unchanged because the shift is *along* the spin axis. The transverse moments
:math:`I_{xx}` and :math:`I_{yy}` each gain :math:`m\!\left(\tfrac{3H}{4}\right)^2`.
