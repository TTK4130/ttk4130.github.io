==============================
3D Visualization and Animation
==============================

Visualization is a crucial part of evaluating any attempt of modelling a system. When dealing with a system with more than a couple of parameters, plots become
difficult to interpret. By visualizing our system in 3D we can leverage our spatial and physics intuition of the world. This is the same intuition
which tells us that when we throw a ball, its trajectory should be parabolic, or the intuition that it takes less effort stop a bike than a car. When it comes to mechanical systems,
when something doesn't look right, it's indicative of a model built on fundamentally flawed assumptions. Visualizing your system through animation
will help you weed out unintended behaviour from your model and will ultimately deepen your understanding of your model.
This page will go into the basic principles of animating a system in 3D, as well as some common frameworks for visualization an animation.


Principles of Animation
===========================

.. raw:: HTML

    <p><a href="https://commons.wikimedia.org/wiki/File:Animhorse.gif#/media/File:Animhorse.gif"><img src="https://upload.wikimedia.org/wikipedia/commons/e/e3/Animhorse.gif" alt="Animhorse.gif" height="230" width="307"></a><br>By <a href="//commons.wikimedia.org/wiki/User:Janke" title="User:Janke">Janke</a> - <span class="int-own-work" lang="en">Own work</span>, <a href="https://creativecommons.org/licenses/by-sa/2.5" title="Creative Commons Attribution-Share Alike 2.5">CC BY-SA 2.5</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=433430">Link</a></p>

We distinguish between two approaches to animation: **real-time animation** and **precomputed animation**.

**Real-time animation** means that we simulate the system's state in the same loop (as in programming) as the animation progress. For each new
animation frame we integrate our system from the last frame to the current frame. This allows for interactive and responsive animations,
but can be computationally demanding for complex systems or stiff systems that demand fine time resolutions.

**Precomputed animation** uses pre-generated trajectories (state over time). We compute the system's trajectory
*before* animating, and play back the trajectory upon animation. This approach is often more practical and efficient,
as it allows us to decouple simulation from rendering. This allows us to reuse our simulation data, and is generally
more stable for visualization purposes.

In both cases, we need a time series of the **trajectory** of our system. This trajectory could include positions, orientations
and other relevant quantities and measures. Additionally, we need to specify the time step or **frame duration** between each state,
as this determines how long each animation frame should last, consequently determining our frame rate (frames/second). Matching the
animation frame rate with the simulation time step produces a reproduction of the system's motion. However, in some cases
adjusting the playback speed (faster or slower) can be both practically useful (i.e. a very slow or fast system).

A trajectory alone is not very useful to animate without a corresponding 3D (or 2D) model of the system.
This model doesn't need to be photorealistic nor physically accurate. It just needs to capture the
essential geometry and behaviour of our system. For example, the details on the bike seat are of little interest when analysing the motion of a bike.
Most animation libraries include primitive geometric shapes like cubes, spheres and cylinders, which
are usually sufficient to represent the key components of a system. You'd be surprised how basic a model can be, as our
brains are excellent at filling in the blanks when the **motion** is convincing. A simple rectangle moving like a boat
can evoke the image of a vessel at sea given that the motion behaves as expected.

Our advice: **start simple**. Focus on correct motion first, as you undoubtedly will make some
interesting mistakes with reference frames and defining coordinate systems. You can always improve the visual flair and fidelity later.
The goal is by no means to produce a Pixar-quality animation, but rather to understand and effectively communicate how your system behaves.

In the following sections, we'll present four animation tools of increasing complexity, from
lightweight plotting using Matplotlib to state-of-the-art 3D engines using Blender.


Matplotlib.animation
=====================

.. note::

    Matplotlib is quite old and rigorous for simple data visualization. If you want to plot simple 2D data, we recommend checking out `Plotly <https://plotly.com/python/>`_ for
    a more modern plotting library. However, Plotly it is not designed for 3D animation.

Many of you are already familiar with the Matplotlib library. Inspired by Matlab's plotting library, Matplotlib offers many useful easy-to-use functions for plotting
and visualizing data. While library was made with data visualization in mind, it also supports a rudamentary framework for plotting and animating in 3D.
In this section we'll go through a basic example of a 3D pendulum with damping. For a more comprehensice introduction to Matplotlib.animation, take a look at
the `official documentation <https://matplotlib.org/stable/users/explain/animations/animations.html#animations-using-matplotlib>`_.

Example: Pendulum
--------------------

In this example we'll simulate a 3D pendulum with damping terms.

.. dropdown:: Derivation

    We consider a point mass :math:`m` suspended by a rigid rod of length :math:`L` from a fixed pivot. Using spherical coordinates, the generalized coordinates are

    .. math::
       q = \begin{bmatrix} \theta \\ \phi \end{bmatrix},

    where :math:`\theta` is the polar angle from the vertical and :math:`\phi` is the azimuthal angle around the vertical axis.

    The position of the mass is :math:`\mathbf{r} = L(\sin\theta\cos\phi, \sin\theta\sin\phi, -\cos\theta)`. Computing the kinetic energy :math:`T = \tfrac{1}{2}m|\dot{\mathbf{r}}|^2` gives us

    .. math::
       T = \tfrac{1}{2}mL^2\left[\dot{\theta}^2 + \sin^2\theta \, \dot{\phi}^2\right]

    The potential energy, with reference at the pivot at the origin, is

    .. math::
       V = -mgL\cos\theta.

    Thus, the Lagrangian can be expressed as

    .. math::
       \mathcal{L} = T - V.

    The kinetic energy can be written in quadratic form

    .. math::
       T = \tfrac{1}{2} \dot{q}^\mathsf{T} W(q)\, \dot{q},

    with inertia matrix

    .. math::
       W(q) = mL^2
       \begin{bmatrix}
         1 & 0 \\
         0 & \sin^2\theta
       \end{bmatrix}

    The Euler-Lagrange equations yield

    .. math::
       W(q) \, \ddot{q} + c(q, \dot{q}) + g(q) = 0,

    where

    .. math::
       c(q, \dot{q}) = mL^2
       \begin{bmatrix}
          -\sin\theta\cos\theta \, \dot{\phi}^2 \\
          -2\cos\theta \, \dot{\theta}\dot{\phi}
       \end{bmatrix},
       \qquad
       g(q) =
       \begin{bmatrix}
          mgL\sin\theta \\
          0
       \end{bmatrix}.

    The final equations of motion are

    .. math::
       \begin{bmatrix}
       mL^2 & 0 \\
       0 & mL^2\sin^2\theta
       \end{bmatrix}
       \begin{bmatrix}
       \ddot{\theta} \\ \ddot{\phi}
       \end{bmatrix}
       +
       \begin{bmatrix}
       -mL^2\sin\theta\cos\theta \, \dot{\phi}^2 + mgL\sin\theta \\
       -2mL^2\cos\theta \, \dot{\theta}\dot{\phi}
       \end{bmatrix}
       = 0.

    This compact form can be inverted to solve for :math:`\ddot{\theta}` and :math:`\ddot{\phi}` explicitly:

    .. math::
       \ddot{\theta} &= \sin\theta\cos\theta \, \dot{\phi}^2 - \frac{g}{L}\sin\theta \\
       \ddot{\phi} &= -\frac{2\cos\theta}{\sin\theta} \dot{\theta}\dot{\phi}

    Adding damping terms :math:`-c\dot{\theta}` and :math:`-c\dot{\phi}`, we finally have:

    .. math::
       \ddot{\theta} &= \sin\theta\cos\theta \, \dot{\phi}^2 - \frac{g}{L}\sin\theta - c\dot{\theta} \\
       \ddot{\phi} &= -\frac{2\cos\theta}{\sin\theta} \dot{\theta}\dot{\phi} - c\dot{\phi}

From Euler-Lagrange using vertical angle :math:`\theta` and azimuth :math:`\phi` as generalized coordinates we get the following EoM:

.. note::
    This simplified damping model works for demonstration but isn't fully realistic

.. math::
   \ddot{\theta} &= \sin\theta\cos\theta \, \dot{\phi}^2 - \frac{g}{L}\sin\theta - c\dot{\theta} \\
   \ddot{\phi} &= -\frac{2\cos\theta}{\sin\theta} \dot{\theta}\dot{\phi} - c\dot{\phi}

We separate the second order ODE into four first order ODEs on the standard SciPy format. We also define our parameters.

.. jupyter-execute::

    import numpy as np

    g, L = 9.81, 2.0
    c = 0.5  # damping coeff

    def spherical_pendulum_damped(t, y):
        theta, theta_dot, phi, phi_dot = y
        theta_ddot = (np.sin(theta)*np.cos(theta)*phi_dot**2
                      - (g/L)*np.sin(theta)
                      - c*theta_dot)
        phi_ddot = (-2*np.cos(theta)/max(np.sin(theta), 1e-6))*theta_dot*phi_dot - c*phi_dot # Numerical stability
        return [theta_dot, theta_ddot, phi_dot, phi_ddot]


Integrating with SciPy

.. jupyter-execute::

    from scipy.integrate import solve_ivp
    # Initial conditions
    theta0, theta_dot0 = 0.8, 0.0
    phi0, phi_dot0 = 0.8, 2.0

    # Integrate
    t_span = (0, 10) # 10 seconds
    t_eval = np.linspace(*t_span, 600) # Resolution
    y0 = [theta0, theta_dot0, phi0, phi_dot0]
    sol = solve_ivp(spherical_pendulum_damped, t_span, y0, t_eval=t_eval)

    theta, phi = sol.y[0], sol.y[2] # Extract trajectory polar coordinates


Polar coordinates can be tricky to work with, so to make animation simpler we convert to cartesian

.. jupyter-execute::

    x = L * np.sin(theta) * np.cos(phi)
    y = L * np.sin(theta) * np.sin(phi)
    z = -L * np.cos(theta)


Similar to an ordinary plot, we create a figure with :code:`plt.fig()` and add a 3D subplot. We can also set the bounds
of our plot explicitly by :code:`set_lim()` for all axes.

.. jupyter-execute::

    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xlim(-L, L)
    ax.set_ylim(-L, L)
    ax.set_zlim(-L, 0.5*L)
    ax.set_box_aspect([1, 1, 0.6]) # Not strictly necessary, but nice for web view

We've now created out plot. Now for the animation. The simplest way to animate using Matplotlib is to define
a trajectory for every object in your system. We create one for the line (rod) and one for the bob (mass attached to rod).
Like any other plot we can pick the formatting for each of the trajectories.

.. jupyter-execute::

    line, = ax.plot([], [], [], lw=2, c="black") # The comma "," unpacks the one-element list returned by ax.plot()
    bob, = ax.plot([], [], [], "o", c="red", markersize=8)


We'll now define the functions we need to animate the trajectory using :code:`FuncAnimation`. Apart from our figure and data,
the animation function needs an initialization function and an update function to animate our trajectory. The initialization
function sets up all the properties we need for the trajectories we animate, and gets called whenever we reset or restart our animation.
The update function takes in which time step we are on, and returns the updated trajectory of the objects we animate.

That's it!

.. jupyter-execute::

    def init():
        line.set_data([], [])
        line.set_3d_properties([])
        bob.set_data([], [])
        bob.set_3d_properties([])
        return line, bob

    def update(i):
        line.set_data([0, x[i]], [0, y[i]])
        line.set_3d_properties([0, z[i]])
        bob.set_data([x[i]], [y[i]])
        bob.set_3d_properties([z[i]])
        return line, bob

Then we just have to pass our figure, functions and remaining parameters.
The frame argument is the number of steps we integrated is self explanatory. The interval parameter controls milliseconds between frames, use 50-100ms for smooth playback.
Additionally, you can use :code:`blit=True` to make the animation more efficient, as it makes sure only
updated pixels are drawn for every frame. If the animation doesn't appear when testing locally, try removing `blit=True` or use `plt.show()` instead of HTML display.

.. jupyter-execute::

    from matplotlib.animation import FuncAnimation
    from IPython.display import HTML # HTML needed to display on webpage

    ani = FuncAnimation(fig, update, frames=len(t_eval), init_func=init,
                        blit=True, interval=10)

    plt.close(fig)  # suppress static plot, animate using HTML instead
    HTML(ani.to_jshtml()) # Display inline

Alternative display methods include `plt.show()` for interactive viewing or `ani.save('pendulum.mp4')` to save as video.
Matplotlib animations may behave differently depending on your backend. If the animation doesn't display properly, try switching backends before importing pyplot:

.. code-block:: python3

    import matplotlib
    matplotlib.use('TkAgg')  # or 'Qt5Agg', 'notebook' for Jupyter
    import matplotlib.pyplot as plt

Common backends include TkAgg for desktop applications, Qt5Agg for interactive plots and 'notebook' for Jupyter environments, such as Jupyter notebooks.

Pythreejs
======================

.. warning::

    This is a sparsely maintained Python package. It's simple to use, but since compatability is not guaranteed, use it at your own risk.


Example: Pendulum-cart
-------------------------

The example system we'll be animating is a pendulum with a mass attached at the end. We'll ignore collision and friction forces for now.

.. figure:: figures/pendulum_w_cart.png
   :scale: 60%
   :align: center

.. dropdown:: Derivation

    We consider a cart of mass :math:`M` moving horizontally, with a pendulum
    of mass :math:`m` and length :math:`L` attached at its pivot.

    Using Euler-Lagrange, the generalized coordinates are chosen as

    .. math::

       q = \begin{bmatrix} x \\ \theta \end{bmatrix},

    where :math:`x` is the horizontal displacement of the cart and
    :math:`\theta` is the pendulum angle from the y-axis.

    The standard formulation for kinetic energy gives us

    .. math::

       T = \tfrac{1}{2}(M+m)\dot{x}^2
           + mL\cos\theta \,\dot{x}\dot{\theta}
           + \tfrac{1}{2} m L^2 \dot{\theta}^2

    Using the same principle, we have potential energy

    .. math::

       V = m g L \cos\theta.

    Thus, the Lagrangian is

    .. math::

       \mathcal{L} = T - V.

    The kinetic energy can be written in quadratic form

    .. math::

       T = \tfrac{1}{2} \dot{q}^\mathsf{T} W(q)\, \dot{q},

    with inertia matrix

    .. math::

       W(q) =
       \begin{bmatrix}
         M + m & m L \cos\theta \\
         m L \cos\theta & m L^2
       \end{bmatrix}


    The Euler-Lagrange equations yield

    .. math::

       W(q) \, \ddot{q} + c(q, \dot{q}) + g(q) = 0,

    where

    .. math::

       c(q, \dot{q}) =
       \begin{bmatrix}
          -m L \sin\theta \, \dot{\theta}^2 \\
          0
       \end{bmatrix},
       \qquad
       g(q) =
       \begin{bmatrix}
          0 \\
          m g \sin\theta
       \end{bmatrix}.

    Thus, the final equations of motion are

    .. math::

       \begin{bmatrix}
       M+m & mL\cos\theta \\
       mL\cos\theta & mL^2
       \end{bmatrix}
       \begin{bmatrix}
       \ddot{x} \\ \ddot{\theta}
       \end{bmatrix}
       +
       \begin{bmatrix}
       -mL\sin\theta \, \dot{\theta}^2 \\
       m g \sin\theta
       \end{bmatrix}
       = 0.

    This compact form can be inverted to solve for :math:`\ddot{x}` and
    :math:`\ddot{\theta}` explicitly:

    .. math::

       \ddot{q} = - W(q)^{-1} \left[ c(q,\dot{q}) + g(q) \right].

From the derivation above we have the EoM

.. math::

    \ddot{q} = - W(q)^{-1} \left[ c(q,\dot{q}) + g(q) \right],
    \qquad q := \begin{bmatrix} x \\ \theta \end{bmatrix}

where

.. math::

    c(q, \dot{q}) =
    \begin{bmatrix}
      -m L \sin\theta \, \dot{\theta}^2 \\
      0
    \end{bmatrix},
    \qquad
    g(q) =
    \begin{bmatrix}
      0 \\
      m g \sin\theta
    \end{bmatrix},
    \qquad
    W(q) = \begin{bmatrix}
    M+m & mL\cos\theta \\
    mL\cos\theta & mL^2
    \end{bmatrix}



.. jupyter-execute::

    import pythreejs as pj
    import ipywidgets as widgets
    import numpy as np
    from IPython.display import display
    from scipy.integrate import odeint

    def cart_pendulum_ode(state, t, L, m, M):
        theta, theta_dot, x, x_dot = state
        g = 9.81
        S, C = np.sin(theta), np.cos(theta)

        W = np.array([
            [M + m,      m*L*C],
            [m*L*C,      m*L**2]
        ])

        f = np.array([
            -m*L*S*theta_dot**2,
            m*g*S
        ])

        q_ddot = np.linalg.solve(W, -f) # Solve to get rhs
        x_ddot, theta_ddot = q_ddot[0], q_ddot[1]
        return [theta_dot, theta_ddot, x_dot, x_ddot] # Same shape as input


    time = np.arange(0, 30, 0.1)
    L = 3
    m = 1
    M = 3
    initial_state = [0.7, 0, 0, 0]
    solution = odeint(cart_pendulum_ode, initial_state, time, args=(L, m, M))

    cart_y = 0.5

    x_pos = solution[:, 2]
    x_vals = [[x, cart_y, 0] for x in x_pos]

    pendulum_vals = [
        [x + L*np.sin(theta), cart_y - L*np.cos(theta), 0]
        for theta, x in zip(solution[:,0], x_pos)
    ]

    cart_values = np.asarray(x_vals).ravel()
    pend_values = np.asarray(pendulum_vals).ravel()




    # Animation

    camera = pj.PerspectiveCamera(position=[0, 0, 7], aspect=6/4)
    scene = pj.Scene(children=[camera, pj.DirectionalLight(position=[0, 3, 7], intensity=0.6),])
    renderer = pj.Renderer(scene=scene, camera=camera, controls=[pj.OrbitControls(controlling=camera)], width=600, height=400)



    cart = pj.BoxGeometry(1, 1, 1)
    cart_mesh = pj.Mesh(cart, material=pj.MeshLambertMaterial(color='red', side='FrontSide'))

    pivot = pj.Group(position=[0, 0, 0])
    cart_mesh.add(pivot)
    scene.add(cart_mesh)

    rod = pj.CylinderGeometry(radiusTop=0.05, radiusBottom=0.05, height=L)
    rod_mesh = pj.Mesh(rod, material=pj.MeshLambertMaterial(color='black'))
    rod_mesh.position = [0, -L/2, 0] # top at pivot
    pivot.add(rod_mesh)

    bob = pj.SphereGeometry(radius=0.2)
    bob_mesh = pj.Mesh(bob, pj.MeshLambertMaterial(color='blue'))
    bob_mesh.position = [0, -L, 0] # at end of rod
    pivot.add(bob_mesh)

    angles = solution[:, 0]
    pend_values = np.array([[0 , 0, np.sin(a/2), np.cos(a/2)] for a in angles])
    cart_mesh.name = "cart_mesh"
    pivot.name = "pivot"

    cart_values = cart_values.astype(np.float32)
    pend_values = pend_values.astype(np.float32)

    cart_position_track = pj.VectorKeyframeTrack(name="cart_mesh.position", times=time, values=cart_values)
    rotation_track = pj.QuaternionKeyframeTrack("pivot.quaternion", times=time, values=pend_values)
    clip = pj.AnimationClip(tracks=[cart_position_track, rotation_track], duration=time[-1])
    mixer = pj.AnimationMixer(cart_mesh)
    action = pj.AnimationAction(mixer, clip, cart_mesh)
    renderer.layout = widgets.Layout(width="100%", height="auto")

    renderer

.. jupyter-execute::

    action


Threejs
======================


Example: Sphere in bowl
------------------------


.. code:: javascript

    var a = 2

.. dropdown:: Derivation


.. raw:: html

   <div id="threejs-container" style="width: 600px; height: 400px; border: 1px solid #ccc;"></div>
   <div id="controls" style="margin-top: 10px;">
       <button id="playPause">Play/Pause</button>
       <button id="reset">Reset</button>
       <span id="timeDisplay" style="margin-left: 20px;">Time: 0.00s</span>
       <span style="margin-left: 20px; font-size: 0.9em; color: #666;">
           Click and drag to pan
       </span>
   </div>

   <script type="importmap">
   {
     "imports": {
       "three": "https://cdn.jsdelivr.net/npm/three@0.150.1/build/three.module.js"
     }
   }
   </script>

   <script type="module">
   import * as THREE from 'three';
   import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.150.1/examples/jsm/controls/OrbitControls.js';

   const container = document.getElementById('threejs-container');
   const scene = new THREE.Scene();
   scene.background = new THREE.Color(0xf5f5f5);

   const camera = new THREE.PerspectiveCamera(75, 600/400, 0.1, 1000);
   const renderer = new THREE.WebGLRenderer({ antialias: true });
   renderer.setSize(600, 400);
   renderer.shadowMap.enabled = true;
   renderer.shadowMap.type = THREE.PCFSoftShadowMap;
   container.appendChild(renderer.domElement);

   // Add OrbitControls but disable rotation and zoom - only allow panning
   const controls = new OrbitControls(camera, renderer.domElement);
   controls.enableDamping = true;
   controls.dampingFactor = 0.05;
   controls.enableZoom = true;      // Disable zoom
   controls.enablePan = true;        // Enable panning
   controls.enableRotate = true;    // Disable rotation

   // Lighting setup
   const ambientLight = new THREE.AmbientLight(0x404040, 0.4);
   scene.add(ambientLight);

   const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
   directionalLight.position.set(5, 5, 5);
   directionalLight.castShadow = true;
   scene.add(directionalLight);

   // Coordinate axes for reference
   const axesHelper = new THREE.AxesHelper(1.5);
   scene.add(axesHelper);

   // Create pendulum components
   const pendulumGroup = new THREE.Group();
   scene.add(pendulumGroup);

   // Pivot point
   const pivotGeometry = new THREE.SphereGeometry(0.08);
   const pivotMaterial = new THREE.MeshPhongMaterial({color: 0x333333});
   const pivot = new THREE.Mesh(pivotGeometry, pivotMaterial);
   pivot.position.set(0, 0, 0);
   pendulumGroup.add(pivot);

   // Pendulum bob
   const bobGeometry = new THREE.SphereGeometry(0.12);
   const bobMaterial = new THREE.MeshPhongMaterial({color: 0xff4444});
   const bob = new THREE.Mesh(bobGeometry, bobMaterial);
   bob.castShadow = true;
   pendulumGroup.add(bob);

   // String
   const stringMaterial = new THREE.LineBasicMaterial({color: 0x333333, linewidth: 3});
   const stringGeometry = new THREE.BufferGeometry();
   const string = new THREE.Line(stringGeometry, stringMaterial);
   pendulumGroup.add(string);

   // Trajectory trail
   const trailMaterial = new THREE.LineBasicMaterial({
       color: 0x4444ff,
       transparent: true,
       opacity: 0.7
   });
   const trailGeometry = new THREE.BufferGeometry();
   const trail = new THREE.Line(trailGeometry, trailMaterial);
   scene.add(trail);

   // Set initial camera position
   camera.position.set(4, 3, 4);
   camera.lookAt(0, -1, 0);
   controls.target.set(0, -1, 0);
   controls.update();

   // Animation variables
   let trajectoryData = null;
   let currentFrame = 0;
   let isPlaying = false;
   let trailPoints = [];
   const maxTrailLength = 300;

   // Load trajectory data
   fetch('_static/pendulum_3d_trajectory.json')
       .then(response => response.json())
       .then(data => {
           trajectoryData = data;
           isPlaying = true;
           console.log(`Loaded 3D trajectory with ${data.time.length} points`);
       })
       .catch(error => {
           console.error('Error loading trajectory:', error);
           createFallbackAnimation();
       });

   function createFallbackAnimation() {
       trajectoryData = {
           position: { x: [], y: [], z: [] },
           time: []
       };
       for (let i = 0; i < 1000; i++) {
           const t = i * 0.02;
           const radius = 1.5;
           trajectoryData.position.x.push(radius * Math.sin(t) * Math.cos(t/3));
           trajectoryData.position.y.push(radius * Math.sin(t) * Math.sin(t/3));
           trajectoryData.position.z.push(-radius * Math.cos(t));
           trajectoryData.time.push(t);
       }
       isPlaying = true;
   }

   function updatePendulum() {
       if (!trajectoryData) return;

       const x = trajectoryData.position.x[currentFrame];
       const y = trajectoryData.position.y[currentFrame];
       const z = trajectoryData.position.z[currentFrame];

       bob.position.set(x, y, z);

       const points = [
           new THREE.Vector3(0, 0, 0),
           new THREE.Vector3(x, y, z)
       ];
       string.geometry.setFromPoints(points);

       trailPoints.push(new THREE.Vector3(x, y, z));
       if (trailPoints.length > maxTrailLength) {
           trailPoints.shift();
       }
       trail.geometry.setFromPoints(trailPoints);

       const currentTime = trajectoryData.time[currentFrame];
       document.getElementById('timeDisplay').textContent = `Time: ${currentTime.toFixed(2)}s`;
   }

   // Animation controls
   document.getElementById('playPause').addEventListener('click', () => {
       isPlaying = !isPlaying;
   });

   document.getElementById('reset').addEventListener('click', () => {
       currentFrame = 0;
       trailPoints = [];
       trail.geometry.setFromPoints([]);
   });

   // Main animation loop
   function animate() {
       requestAnimationFrame(animate);

       controls.update();

       if (isPlaying && trajectoryData) {
           updatePendulum();
           currentFrame = (currentFrame + 1) % trajectoryData.time.length;
       }

       renderer.render(scene, camera);
   }

   animate();
   </script>


Blender
==========


Example: Tennis racket theorem
----------------------------------


