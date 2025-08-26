============================================
Welcome to Modelling and Simulation!
============================================

.. raw:: html

   <div id="lorenz-container" style="width: 100%; height: 60vh; min-height: 400px; border: 1px solid #555;"></div>

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

   const container = document.getElementById('lorenz-container');
   const scene = new THREE.Scene();
   scene.background = new THREE.Color(0x1e1e1e); // Dark modern gray

   // Get initial container dimensions
   const containerWidth = container.clientWidth;
   const containerHeight = container.clientHeight;

   const camera = new THREE.PerspectiveCamera(75, containerWidth / containerHeight, 0.1, 1000);
   const renderer = new THREE.WebGLRenderer({ antialias: true });
   renderer.setSize(containerWidth, containerHeight);
   renderer.setPixelRatio(window.devicePixelRatio); // For high DPI displays
   container.appendChild(renderer.domElement);

   // Add controls
   const controls = new OrbitControls(camera, renderer.domElement);
   controls.enableDamping = true;
   controls.dampingFactor = 0.05;
   controls.enableZoom = false;
   controls.enablePan = false;
   controls.enableRotate = false;
   controls.autoRotate = true;

   // Handle window resize
   function onWindowResize() {
       const width = container.clientWidth;
       const height = container.clientHeight;

       camera.aspect = width / height;
       camera.updateProjectionMatrix();

       renderer.setSize(width, height);
       renderer.setPixelRatio(window.devicePixelRatio);
   }

   // Add resize listener
   window.addEventListener('resize', onWindowResize, false);

   // Also listen for container size changes (for responsive layouts)
   if (window.ResizeObserver) {
       const resizeObserver = new ResizeObserver(entries => {
           for (let entry of entries) {
               if (entry.target === container) {
                   onWindowResize();
               }
           }
       });
       resizeObserver.observe(container);
   }

   // Lighting
   const ambientLight = new THREE.AmbientLight(0x404040, 0.6);
   scene.add(ambientLight);

   const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
   directionalLight.position.set(10, 10, 10);
   scene.add(directionalLight);

   // Camera rotation parameters - focus on the crossing/transition region
   let cameraAngle = 0;
   const cameraRadius = 5; // Closer to see crossing detail
   const cameraHeight = 1.2; // Positioned to see the transition region
   const rotationSpeed = 0.0005; // Slow rotation speed
   
   // Crossing point where trajectory switches between lobes (approximate center of transition)
   const crossingPoint = new THREE.Vector3(0, 0, 1.4); // Elevated to capture transition region

   // Lorenz attractor parameters
   const sigma = 10;
   const rho = 28;
   const beta = 8/3;
   const dt = 0.01;

   // Generate Lorenz attractor trajectory
   function generateLorenzTrajectory(steps = 100000) {
       const points = [];
       let x = 1, y = 1, z = 1; // Initial conditions

       for (let i = 0; i < steps; i++) {
           // Lorenz equations
           const dx = sigma * (y - x);
           const dy = x * (rho - z) - y;
           const dz = x * y - beta * z;

           // Euler integration
           x += dx * dt;
           y += dy * dt;
           z += dz * dt;

           // Scale for better visualization
           points.push(new THREE.Vector3(x * 0.1, y * 0.1, z * 0.1));
       }

       return points;
   }

   const lorenzPoints = generateLorenzTrajectory();
   const trajectoryGeometry = new THREE.BufferGeometry();
   const trajectoryMaterial = new THREE.LineBasicMaterial({
       color: 0xffd700,
       transparent: true,
       opacity: 0.8,
       linewidth: 2
   });
   const trajectoryLine = new THREE.Line(trajectoryGeometry, trajectoryMaterial);
   scene.add(trajectoryLine);

   // Create a glowing sphere to show current position
   const sphereGeometry = new THREE.SphereGeometry(0.05);
   const sphereMaterial = new THREE.MeshPhongMaterial({
       color: 0xffd700, // Match trajectory color
       emissive: 0x664400,
       shininess: 100
   });
   const currentPoint = new THREE.Mesh(sphereGeometry, sphereMaterial);
   scene.add(currentPoint);

   // Animation variables
   let currentFrame = 0;
   let animatedPoints = [];
   const animationSpeed = 3; // Points per frame

   // Set initial camera position and target to the crossing point
   controls.target.copy(crossingPoint);
   controls.update();

   function updateCameraPosition() {
       // Update camera angle
       cameraAngle += rotationSpeed;

       // Calculate new camera position in a circle around the crossing point
       const x = crossingPoint.x + Math.cos(cameraAngle) * cameraRadius;
       const z = crossingPoint.z + Math.sin(cameraAngle) * cameraRadius;
       const y = crossingPoint.y + cameraHeight;

       camera.position.set(x, y, z);
       camera.lookAt(crossingPoint); // Look at the crossing/transition region

       // Update controls target to maintain focus on crossing point
       controls.target.copy(crossingPoint);
   }

   function updateAnimation() {
       // Add new points to the animated trajectory
       for (let i = 0; i < animationSpeed && currentFrame < lorenzPoints.length; i++) {
           animatedPoints.push(lorenzPoints[currentFrame]);
           currentFrame++;
       }

       // Update the trajectory line
       if (animatedPoints.length > 0) {
           trajectoryGeometry.setFromPoints(animatedPoints);

           // Update current position sphere
           const lastPoint = animatedPoints[animatedPoints.length - 1];
           currentPoint.position.copy(lastPoint);
       }

       // Reset when complete and start over
       if (currentFrame >= lorenzPoints.length) {
           currentFrame = 0;
           animatedPoints = [];
       }
   }

   // Animation loop
   function animate() {
       requestAnimationFrame(animate);

       updateCameraPosition(); // Update camera rotation around crossing point
       controls.update();
       updateAnimation();

       // Add some rotation for visual interest on the current point
       if (animatedPoints.length > 0) {
           currentPoint.rotation.x += 0.01;
           currentPoint.rotation.y += 0.01;
       }

       renderer.render(scene, camera);
   }

   animate();
   </script>


.. toctree::
    :maxdepth: 1
    :caption: Contents:

    installation
    jupyter-notebook
    sympy-and-cas
    reference-frames
    vector-kinematics
    mass-and-inertia
    force-and-torque
    quaternions
    numerical-methods-for-odes
    whats-next
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
