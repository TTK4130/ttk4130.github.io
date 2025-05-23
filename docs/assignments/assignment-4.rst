=============================
Assignment 4 - Newton-Euler
=============================

.. note::

    Submit your assignment as a single PDF, including plots and source code (if any).
    We expect academic honesty. Collaboration is encouraged, but must be declared. Any use of AI must be declared along with any other sources used.
    This is not an exam. Do your best and show that you put in effort and the assignment will be approved.

This assignment is about the Newton-Euler method for developing a dynamic model of a mechanical system. This topic is treated in :cite:t:`Egeland2002` from chapter 6.13 to 7.3.

Problem 1 - Satellite
===========================

.. note::

    This problem contains a programming exercise.
    Template code is available as a Jupyter notebook at `<https://github.com/TTK4130/code-handouts>`_.
    The relevant notebook is `assignment-4-satellite.ipynb`.

.. admonition:: Animation code
    :class: dropdown

    .. jupyter-execute::

        import pythreejs as pj
        import numpy as np
        import requests
        import base64

        def load_image_from_url(url):
            response = requests.get(url)
            if response.status_code == 200:
                return f"data:image/png;base64,{base64.b64encode(response.content).decode('utf-8')}"
            else:
                raise Exception(f"Failed to load image from {url}")

        # Cubemap texture URLs, because I'm lazy
        texture_urls = [
            "https://raw.githubusercontent.com/TTK4130/ttk4130.github.io/refs/heads/main/docs/_static/space_cubemap/px.png",  # Positive X
            "https://raw.githubusercontent.com/TTK4130/ttk4130.github.io/refs/heads/main/docs/_static/space_cubemap/nx.png",  # Negative X
            "https://raw.githubusercontent.com/TTK4130/ttk4130.github.io/refs/heads/main/docs/_static/space_cubemap/py.png",  # Positive Y
            "https://raw.githubusercontent.com/TTK4130/ttk4130.github.io/refs/heads/main/docs/_static/space_cubemap/ny.png",  # Negative Y
            "https://raw.githubusercontent.com/TTK4130/ttk4130.github.io/refs/heads/main/docs/_static/space_cubemap/pz.png",  # Positive Z
            "https://raw.githubusercontent.com/TTK4130/ttk4130.github.io/refs/heads/main/docs/_static/space_cubemap/nz.png"   # Negative Z
        ]

        scene = pj.Scene()
        camera = pj.PerspectiveCamera(position=[10, 6, 10], aspect=800/600)

        skybox_geometry = pj.BoxGeometry(width=500, height=500, depth=500)
        materials = [
            pj.MeshBasicMaterial(
                map=pj.ImageTexture(imageUri=load_image_from_url(url)),
                side='BackSide'
            ) for url in texture_urls
        ]
        skybox = pj.Mesh(skybox_geometry, materials)
        scene.add(skybox)

        cubesat = pj.Mesh(
            pj.BoxGeometry(1, 1, 1),
            pj.MeshStandardMaterial(color='red')
        )
        scene.add(cubesat)

        axis_helper = pj.AxesHelper(size=5)
        axis_helper.position = cubesat.position
        axis_helper.quaternion = cubesat.quaternion

        scene.add(axis_helper)

        scene.add(pj.AmbientLight(color='#ffffff', intensity=1.0))
        scene.add(pj.DirectionalLight(position=[0, 10, 0]))

        controls = pj.OrbitControls(controlling=camera)
        renderer = pj.Renderer(camera=camera, scene=scene, width=800, height=600, controls=[controls])


.. jupyter-execute::

     renderer


In this task, we will consider a satellite orbiting Earth. We define an inertial reference frame with its origin at Earth's center and with an arbitrary and fixed orientation.

We will consider two cases:

1. The satellite is a cube of uniform, unitary density, having an edge of :math:`50\ cm`.
2. The satellite is the cube mentioned above, with the addition of a punctual mass of :math:`m_o = 0.1\ kg` placed at one of the cube's corners.

.. figure:: figures/Satellite.svg
   :width: 50%
   :align: center
   :alt: Schematic of the satellite

   Schematic of the satellite.

We will assume that the force of gravity is given by Newton's law of universal gravitation:

.. math::
    :label: newton

    \vec{F} = - \frac{G\,m_\mathrm{T}\,m}{\|\vec r_\mathrm{c}\|^2} \cdot \frac{\vec r_\mathrm{c}}{\|\vec r_\mathrm{c}\|}

The inertia matrix in the reference frame attached to the cube with its origin at the cube's center of mass and with the axes going through the center of the cube's faces is given by

.. math::
    :label: inertia-matrix

    \frac{1}{6}ml^2 I

where `m` is the mass, `l` is the length of the sides, and `I` is the 3-by-3 identity matrix.

This exercise is about dynamics, but we still have to parameterize the kinematics of the satellite.

We will describe the satellite's position by a vector from the world center to the satellite's center of mass given in the inertia frame :math:`\mathbf{r}_c^i`, and the orientation by the unit quaternion :math:`\mathbf{q}` corresponding to the rotation between the inertial and body frame, :math:`\mathbf{R}_b^i`.

.. math::

    \mathbf{q} \triangleq \left[ \begin{array}{l}
    q_w \\
    \mathbf{q}_v
    \end{array} \right] = \left[ \begin{array}{l}
    q_w \\
    q_x \\
    q_y \\
    q_z
    \end{array} \right]

The kinematics are given by:

.. math::

    \dot{\mathbf{r}}_c^i = \mathbf{v}_c^i

.. math::

    \dot{\mathbf{q}} = \frac{1}{2} \mathbf{q} \otimes \boldsymbol{\omega}_{b/i}^b = \frac{1}{2} \boldsymbol{\Omega}(\boldsymbol{\omega}_{b/i}^b) \mathbf{q}

Where :math:`\mathbf{v}_c^i` is the velocity of the center of mass given in the inertial frame, :math:`\boldsymbol{\omega}_{b/i}^b` is the angular velocity of the satellite given in the body frame, and :math:`\boldsymbol{\Omega}(\boldsymbol{\omega})` is defined as:

.. math::

    \boldsymbol{\Omega}(\boldsymbol{\omega}) \triangleq [\boldsymbol{\omega}]_R = \left[ \begin{array}{cc}
    0 & -\boldsymbol{\omega}^{\top} \\
    \boldsymbol{\omega} & -[\boldsymbol{\omega}]_{\times}
    \end{array} \right] = \left[ \begin{array}{cccc}
    0 & -\omega_x & -\omega_y & -\omega_z \\
    \omega_x & 0 & \omega_z & -\omega_y \\
    \omega_y & -\omega_z & 0 & \omega_x \\
    \omega_z & \omega_y & -\omega_x & 0
    \end{array} \right]

.. hint::
    :class: dropdown

    You will find the Python code template in the `code handout repository <https://github.com/TTK4130/code-handouts>`_ or on Blackboard.

.. admonition:: Tasks

    a) Consider the satellite without the added mass. Use the Newton-Euler equations to derive the dynamics of the satellite, i.e., find expressions for :math:`\dot{\mathbf{v}}_c^i` and :math:`\dot{\boldsymbol{\omega}}_b^i`.

    b) Now consider the added mass (case 2 above). The added mass will shift the center of mass of the system. Calculate the inertia matrix around this new center of mass and find the updated expressions for :math:`\dot{\mathbf{v}}_c^i` and :math:`\dot{\boldsymbol{\omega}}_b^i`.

    .. hint::

        Use the parallel axis theorem to find the new inertia matrix.

    c) Simulate the two cases in parts 1 and 2. What differences do you observe?

Problem 2 - Pendulum on an oscillator
==========================================

.. figure:: figures/pendulum_osc.svg
    :width: 30%
    :name: pendulum

    Pendulum on a vertical oscillator

:numref:`pendulum` shows a pendulum with a point mass :math:`m_2` attached to a mass :math:`m_1` that can oscillate along a vertical axis. The pendulum rod has a length :math:`L` and the rod can be considered mass-less (i.e. the pendulum can be considered as a point mass at the end of a mass-less rod).

The oscillating mass is connected to a stationary construction through a spring with stiffness :math:`k`. The vertical position :math:`z` of the mass is defined such that :math:`z_0` when the spring is in its neutral position. The angular displacement of the pendulum rod is :math:`\theta`, as shown in the figure. For simplicity we also constrain body one to only move up or down, i.e no movement along the :math:`\text{y}_0` or :math:`\text{z}_0` axis.

.. admonition:: Tasks

    **a. Kinematics**

    We will start by expressing the kinematics of the system. Show that the acceleration of the COMs, :math:`\mathbf{\vec{a}}_1` and :math:`\mathbf{\vec{a}}_2` and the angular acceleration of body 2, :math:`\mathbf{\vec{\alpha}}`, is given by:

    .. math::

       \mathbf{a}_1 = \ddot{z} \mathbf{k}_0

    .. math::

       \mathbf{a}_2 = \left(L\ddot{\theta}\cos\theta - L\dot{\theta}^2\sin\theta\right) \mathbf{j}_0 + \left(\ddot{z} + L\dot{\theta}^2\cos\theta + L\ddot{\theta}\sin\theta\right)\mathbf{k}_0

    .. math::

       \mathbf{\alpha} = \ddot{\theta} \mathbf{i}_0

    **b. Newton Euler equations**

    Show that the Newton Euler equations for the two rigid bodies are given by:

    .. math::

       m_1 \mathbf{a}_1 = \mathbf{F}_{\text{spring}} + \mathbf{F}_{g1} + \mathbf{F}_{\text{joint}}

    .. math::

       m_2 \mathbf{a}_2 = \mathbf{F}_{g2} + \mathbf{F}_{\text{joint}}

    .. math::

       \mathbf{r}_{2/1} \times m_2 \mathbf{a}_2 = \boldsymbol{\tau}_{g2}

    Where :math:`\mathbf{F}_{\text{spring}}` is the force acting from the spring, :math:`\mathbf{F}_{g1}` and :math:`\mathbf{F}_{g2}` are the gravitational forces acting on mass 1 and 2, :math:`\boldsymbol{\tau}_{g2}` is the torque induced by :math:`\mathbf{F}_{g2}` acting around the origin of frame 1, and :math:`\mathbf{F}_{\text{joint}}` is the joint force keeping the two bodies together.

    **c. Equation of motion**


    Using the results from part a and b, show that the equation of motion can be expressed as:

    .. math::

       (m_1+m_2)\ddot{z} + m_2 L \dot{\theta}^2 \cos\theta + m_2 L \ddot{\theta} \sin\theta + (m_1+m_2)g + kz = 0

    .. math::

       L^2 m_2 \ddot{\theta} + L m_2 \ddot{z} \sin\theta + L m_2 g \sin\theta = 0

    .. hint::

        Since the oscillating mass is constrained to move along the :math:`\text{z}_0` axis, this makes some simplifications to equations :eq:`newton` and :eq:`inertia-matrix`.

    **d. Modeling with uniformly distributed mass**

    Assume now that we were to remove the point mass :math:`m_2`, and instead model the pendulum as a rod with uniformly distributed mass :math:`m_2` with center of gravity at the midpoint of the rod, such that the moment of inertia about the center point is :math:`I_{xx} = \frac{L^2 m_2}{12}`. What are the equations of motion now?

    **e. Parallel Axis Theorem**

    In some cases, when dealing with moment balances of rigid bodies that are rotating about some point that is not their center of gravity, we may modify the moment of inertia expression by employing the parallel axis theorem. This adjustment allows us to simplify the modeling of motion as a pure rotation.

    Why can we not simply use the parallel axis theorem in Task d) above, and model the pendulum as a pure rotation about the hinge point of the rod? What term would be missing in the model you derived in Task d)?

