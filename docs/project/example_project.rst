.. _example_project:

Example Project: Bicycle (WIP)
===============================

For the example project I chose to model and examine a bicycle. I chose
this because most of us have an intuition of how bicycles should work
and move, yet few of us actually understand the underlying dynamics. I
therefore set the goal of examining different ways of modelling a
bicycle, how different parameters affect the behaviour of the bicycle
and lastly simulating the self-correcting behaviour of a bicycle in simulation.

Early stage investigation
-------------------------

The start of any project involves investigating existing literature on
your chosen topic. I usually start by looking for relevant Wikipedia
pages to find relevant source material. A quick search yielded a
comprehensive Wikipedia page for `Bicycle and motorcycle
dynamics <https://en.wikipedia.org/wiki/Bicycle_and_motorcycle_dynamics%3E>`__.
We’ll note that down, and look in its references. We’ll look for
anything that looks relevant to our project. Then we’ll try to look for
more colloquial articles which may help us dive gently into the topic.
Some quick Google searches later, and we have the following list of
potential sources:

-  (Wikipedia) `Bicycle and motorcycle
   dynamics <https://en.wikipedia.org/wiki/Bicycle_and_motorcycle_dynamics%3E>`__
   - A good starting point for understanding common bicycle models
-  (Article) `A bicycle can be self-stable without gyroscopic or caster
   effects <http://bicycle.tudelft.nl/stablebicycle/StableBicyclev34Revised.pdf>`__
   - This may be relevant for our stability analysis
-  (Interactive Blog) `Bicycle -
   Chiechanowski <https://ciechanow.ski/bicycle/>`__ - May help us get a
   surface-level understanding of bicycle physics
-  (Book) `Bicycling
   Science <https://mitpress.mit.edu/9780262538404/bicycling-science/>`__
   - May serve as a rigerous point of comparison for our model
-  (PhD Dissertation) `Human Control of a
   Bicycle <https://moorepants.github.io/dissertation/index.html>`__ -
   Advanced point of comparison, if human control is to be considered

These are just some types of sources one might encounter during a
literature search. Even though we won’t use them right away, it’s always
a good idea to familiarize yourself with literature on your chosen
topic. This will give you a good indication of how well researched your
system is, and will make it easier to know where to look once you’ve
moved passed the initial stage of modelling your system. Luckily for us,
bicycles are a well studied topic, so we’ll have no issues comparing our
work against others or check that we are on the right track when
modelling our system. One important aspect to keep in mind is the even
though there exists a lot of different approaches to this topic, we
still have to explore them on our own. We can cite sources, compare our
work, but it’s not acceptable to copy someone else’s work and then add
minor modifications. Keeping this in mind, we’ll move on and take a
closer look at the basic elements that make up a bicycle.

The Anatomy of a Bicycle: Understanding our system
----------------------------------------------------

The first step of modelling any system is to break it down into its most
essential components. A bicycle has four basic components:

1. Bicycle frame: Distributes the loads to all the attached components
2. Back wheel: Drives the bicycle through a torque from the chain and
   pedals
3. Front wheel: Leads the bicycle trajectory
4. Bicycle fork: Steers the front wheel through a rotating axle

Putting our modelling and simulation glasses on we can now break down
each one of these components into different states and parameters. All
of these components have mass and inertia, and seen from the perspective
of the bicycle frame, the only moving component is the bicycle fork
which moves the front wheel. All other components either stay still or
rotate in place relative to the bike frame. Before we begin, we’ll have
to declare our initial assumptions. It’s crucial that we keep track of
assumptions throughout the entire modelling and simulation process. I
usually prefer to keep them in a list which we’ll update for every new
assumption we make.

.. admonition:: Assumptions

    1. All components are rigid bodies: By assuming this we disregard any bending/torsion/elasticity in our components. Effects like vibrations disappear from our model


Starting from this assumption, let’s examine the most essential feature
of a bicycle, namely its wheels.

The bike wheel
---------------

Looking at the bike wheel, the most obvious and simplest way of
modelling it is as a simple flywheel. This adds a new term to our list
of assumptions.

.. admonition:: Assumptions

    1. All components are rigid bodies: By assuming this we disregard any bending/torsion/elasticity in our components. Effects like vibrations disappear from our model
    2. The mass of our wheels is evenly distributed: This is not usually the case, as the spokes of a bike wheel have less mass than the main wheel.



The Simplest Bike
------------------

- Bike with fixed fork
- Simulate
- Why does it not self stabilize?

Conclude that we need a more complicated model

.. note::

    Please look at the animation page :ref:`3D Visualization and Animation` for an
    introduction to how you make animations in Python.

A Not So Simple Bike
---------------------

- Model with fork
- Visualize

.. raw:: html

    <div id="bicycle-container" style="width: 100%; height: 60vh; min-height: 400px; border: 1px solid #555555ff;"></div>
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

    const container = document.getElementById('bicycle-container');
    const containerWidth = container.clientWidth;
    const containerHeight = container.clientHeight;

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xf0f0f0);

    const camera = new THREE.PerspectiveCamera(75, containerWidth/containerHeight, 0.1, 1000);
    camera.position.set(2.5, 1.5, 2.5);
    camera.lookAt(0, 0.4, 0);

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(containerWidth, containerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    container.appendChild(renderer.domElement);

    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.target.set(0, 0.4, 0);

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
    directionalLight.position.set(5, 10, 5);
    scene.add(directionalLight);

    // Configuration
    const config = {
      wheelRadius: 0.335,
      wheelWidth: 0.025,
      wheelSegments: 32,
      wheelbase: 0.99,
      bottomBracketHeight: 0.268,
      bottomBracketForward: 0.42,
      headTubeHeight: 0.58,
      headTubeSetback: 0.04,
      seatTubeHeight: 0.52,
      seatTubeSetback: 0.10,
      tubeRadius: 0.015,
      seatPostHeight: 0.20,
      seatSize: { width: 0.15, height: 0.03, depth: 0.25 },
      handlebarStemHeight: 0.10,
      handlebarWidth: 0.42,
      colors: {
        wheel: 0x333333,
        frame: 0xff6347,
        seat: 0x444444,
        grip: 0x666666
      }
    };

    const materials = {
      wheel: new THREE.MeshStandardMaterial({ color: config.colors.wheel }),
      frame: new THREE.MeshStandardMaterial({ color: config.colors.frame }),
      seat: new THREE.MeshStandardMaterial({ color: config.colors.seat }),
      grip: new THREE.MeshStandardMaterial({ color: config.colors.grip })
    };

    // Reference points
    const rearWheelPos = new THREE.Vector3(-config.wheelbase / 2, config.wheelRadius, 0);
    const frontWheelPos = new THREE.Vector3(config.wheelbase / 2, config.wheelRadius, 0);
    const bottomBracket = new THREE.Vector3(
      rearWheelPos.x + config.bottomBracketForward,
      config.wheelRadius + config.bottomBracketHeight,
      0
    );
    const headTubeTop = new THREE.Vector3(
      frontWheelPos.x - config.headTubeSetback,
      config.wheelRadius + config.headTubeHeight,
      0
    );
    const seatTubeTop = new THREE.Vector3(
      bottomBracket.x - config.seatTubeSetback,
      config.wheelRadius + config.seatTubeHeight,
      0
    );

    function createTubeBetweenPoints(start, end, radius, material = materials.frame) {
      const direction = new THREE.Vector3().subVectors(end, start);
      const length = direction.length();
      const midpoint = new THREE.Vector3().addVectors(start, end).multiplyScalar(0.5);

      const geometry = new THREE.CylinderGeometry(radius, radius, length, 8);
      const mesh = new THREE.Mesh(geometry, material);

      mesh.position.copy(midpoint);

      const axis = new THREE.Vector3(0, 1, 0);
      const quaternion = new THREE.Quaternion();
      quaternion.setFromUnitVectors(axis, direction.normalize());
      mesh.setRotationFromQuaternion(quaternion);

      return mesh;
    }

    // Main bicycle group
    const bicycle = new THREE.Group();
    bicycle.name = 'bicycle';

    const wheelGeometry = new THREE.TorusGeometry(config.wheelRadius, config.wheelWidth, 16, config.wheelSegments);

    const stripe1Geometry = new THREE.BoxGeometry(config.wheelRadius * 1.8, 0.008, config.wheelWidth * 0.5);
    const stripeMaterial = new THREE.MeshStandardMaterial({ color: 0xff6347 });

    // Rear wheel
    const rearWheelGroup = new THREE.Group();
    rearWheelGroup.name = 'rearWheel';
    rearWheelGroup.position.copy(rearWheelPos);

    const rearWheelMesh = new THREE.Mesh(wheelGeometry, materials.wheel);
    rearWheelMesh.rotation.z = Math.PI / 2;
    rearWheelGroup.add(rearWheelMesh);

    const stripe1 = new THREE.Mesh(stripe1Geometry, stripeMaterial);
    rearWheelGroup.add(stripe1);

    const stripe2 = new THREE.Mesh(stripe1Geometry, stripeMaterial);
    stripe2.rotation.z = Math.PI / 2;
    rearWheelGroup.add(stripe2);

    bicycle.add(rearWheelGroup);

    // Frame
    const frameGroup = new THREE.Group();
    frameGroup.name = 'frame';

    frameGroup.add(createTubeBetweenPoints(headTubeTop, bottomBracket, config.tubeRadius));
    frameGroup.add(createTubeBetweenPoints(headTubeTop, seatTubeTop, config.tubeRadius));
    frameGroup.add(createTubeBetweenPoints(bottomBracket, seatTubeTop, config.tubeRadius));
    frameGroup.add(createTubeBetweenPoints(bottomBracket, rearWheelPos, config.tubeRadius * 0.9));
    frameGroup.add(createTubeBetweenPoints(seatTubeTop, rearWheelPos, config.tubeRadius * 0.8));

    const seatPostTop = new THREE.Vector3(
      seatTubeTop.x,
      seatTubeTop.y + config.seatPostHeight,
      seatTubeTop.z
    );
    frameGroup.add(createTubeBetweenPoints(seatTubeTop, seatPostTop, config.tubeRadius * 0.8));

    const seatGeometry = new THREE.BoxGeometry(config.seatSize.width, 0.02, config.seatSize.depth);
    const seat = new THREE.Mesh(seatGeometry, materials.seat);
    seat.position.copy(seatPostTop);
    seat.position.y += 0.01;
    frameGroup.add(seat);

    bicycle.add(frameGroup);

    // Steering assembly
    const steeringGroup = new THREE.Group();
    steeringGroup.name = 'steering';
    steeringGroup.position.set(frontWheelPos.x, config.wheelRadius, 0);

    const frontWheelGroup = new THREE.Group();
    frontWheelGroup.name = 'frontWheel';
    const frontWheelMesh = new THREE.Mesh(wheelGeometry, materials.wheel);
    frontWheelMesh.rotation.z = Math.PI / 2;
    frontWheelGroup.add(frontWheelMesh);

    const frontStripe1 = new THREE.Mesh(stripe1Geometry, stripeMaterial);
    frontWheelGroup.add(frontStripe1);

    const frontStripe2 = new THREE.Mesh(stripe1Geometry, stripeMaterial);
    frontStripe2.rotation.z = Math.PI / 2;
    frontWheelGroup.add(frontStripe2);

    steeringGroup.add(frontWheelGroup);

    const forkStart = new THREE.Vector3(0, 0, 0);
    const forkEnd = new THREE.Vector3(
      headTubeTop.x - frontWheelPos.x,
      headTubeTop.y - config.wheelRadius,
      0
    );
    steeringGroup.add(createTubeBetweenPoints(forkStart, forkEnd, config.tubeRadius));

    const handlebarCenter = new THREE.Vector3(
      headTubeTop.x - frontWheelPos.x,
      headTubeTop.y - config.wheelRadius + config.handlebarStemHeight,
      0
    );

    steeringGroup.add(createTubeBetweenPoints(forkEnd, handlebarCenter, config.tubeRadius * 0.9));

    const handlebarGeometry = new THREE.CylinderGeometry(
      config.tubeRadius * 0.9,
      config.tubeRadius * 0.9,
      config.handlebarWidth,
      8
    );
    const handlebar = new THREE.Mesh(handlebarGeometry, materials.frame);
    handlebar.position.copy(handlebarCenter);
    handlebar.rotation.x = Math.PI / 2;
    steeringGroup.add(handlebar);

    const gripGeometry = new THREE.SphereGeometry(0.04, 8, 8);
    const leftGrip = new THREE.Mesh(gripGeometry, materials.grip);
    leftGrip.position.set(handlebarCenter.x, handlebarCenter.y, -config.handlebarWidth / 2);
    steeringGroup.add(leftGrip);

    const rightGrip = new THREE.Mesh(gripGeometry, materials.grip);
    rightGrip.position.set(handlebarCenter.x, handlebarCenter.y, config.handlebarWidth / 2);
    steeringGroup.add(rightGrip);

    bicycle.add(steeringGroup);
    scene.add(bicycle);

    // Ground
    const groundGeometry = new THREE.PlaneGeometry(20, 20);
    const groundMaterial = new THREE.MeshStandardMaterial({ color: 0xcccccc });
    const ground = new THREE.Mesh(groundGeometry, groundMaterial);
    ground.rotation.x = -Math.PI / 2;
    scene.add(ground);

    const gridHelper = new THREE.GridHelper(10, 10);
    scene.add(gridHelper);

    // Animation
    let wheelRotation = 0;
    let steerAngle = 0;
    let leanAngle = 0;
    const clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);

      const time = clock.getElapsedTime();

      wheelRotation += 0.02;
      frontWheelGroup.rotation.z = -wheelRotation;
      rearWheelGroup.rotation.z = -wheelRotation;

      steerAngle = Math.sin(time * 2) * 0.3;
      steeringGroup.rotation.y = steerAngle;

      leanAngle = Math.sin(time * 1.5) * 0.15;
      bicycle.rotation.x = leanAngle;

      controls.update();
      renderer.render(scene, camera);
    }

    animate();

    window.addEventListener('resize', () => {
      const width = container.clientWidth;
      const height = container.clientHeight;
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
      renderer.setSize(width, height);
    });
    </script>

Testing different bicycle parameters
------------------------------------


.. image:: https://imgs.xkcd.com/comics/timeline_of_bicycle_design.png

A good place to start to look for parameters is looking for similar
components’ specifications online through different stores or vendors.

- Three different parameters -> What can we learn from them
- What about inertia? Does this affect stability?

Conclusion
-----------

- What have we learned from simulating
- Different parameters and stability


Final Report
-------------------

- Simple two page report in Typst
