=======================
Vector Kinematics (WIP)
=======================

Kinematics describes motion without considering the forces that cause it.
In mechanics and robotics, it provides the tools needed to describe position,
velocity, and acceleration.

Vector notation
---------------
A vector is a quantity with magnitude and direction. In three-dimensional space,
a vector is described by three components relative to a reference frame.

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

In these notes, the position of point :math:`B` relative to point :math:`A`
is denoted :math:`\mathbf{p}_{B/A}` or :math:`\vec{p}_{B/A}`.

Reference frames and position
-----------------------------

.. raw:: html

   <div id="frame-container" style="width: 100%; height: 60vh; min-height: 420px; border: 1px solid #555;"></div>

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

   const container = document.getElementById('frame-container');

   const scene = new THREE.Scene();
   scene.background = new THREE.Color(0x1e1e1e);

   const width = container.clientWidth;
   const height = container.clientHeight;

   const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
   camera.position.set(6, 4, 8);

   const renderer = new THREE.WebGLRenderer({ antialias: true });
   renderer.setSize(width, height);
   renderer.setPixelRatio(window.devicePixelRatio);
   container.appendChild(renderer.domElement);

   const controls = new OrbitControls(camera, renderer.domElement);
   controls.enableDamping = true;
   controls.dampingFactor = 0.05;
   controls.target.set(1.5, 1.0, 0);

   function onWindowResize() {
   const w = container.clientWidth;
   const h = container.clientHeight;
   camera.aspect = w / h;
   camera.updateProjectionMatrix();
   renderer.setSize(w, h);
   renderer.setPixelRatio(window.devicePixelRatio);
   }
   window.addEventListener('resize', onWindowResize);

   if (window.ResizeObserver) {
   const ro = new ResizeObserver(() => onWindowResize());
   ro.observe(container);
   }

   scene.add(new THREE.AmbientLight(0xffffff, 0.65));

   const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
   dirLight.position.set(5, 8, 6);
   scene.add(dirLight);

   function makeAxis(origin, dir, color, length = 1.5) {
   const arrow = new THREE.ArrowHelper(
      dir.clone().normalize(),
      origin,
      length,
      color,
      0.18,
      0.1
   );
   scene.add(arrow);
   return arrow;
   }

   function makeSphere(radius, color) {
   const geo = new THREE.SphereGeometry(radius, 24, 24);
   const mat = new THREE.MeshPhongMaterial({ color, shininess: 80 });
   return new THREE.Mesh(geo, mat);
   }

   function makeLine(color) {
   const geometry = new THREE.BufferGeometry();
   const material = new THREE.LineDashedMaterial({
      color,
      dashSize: 0.18,
      gapSize: 0.08
   });
   const line = new THREE.Line(geometry, material);
   scene.add(line);
   return line;
   }

   function updateLine(line, start, end) {
   line.geometry.setFromPoints([start, end]);
   line.computeLineDistances();
   }

   function createTextSprite(text) {
   const canvas = document.createElement('canvas');
   canvas.width = 256;
   canvas.height = 128;
   const ctx = canvas.getContext('2d');

   ctx.fillStyle = 'rgba(0,0,0,0)';
   ctx.fillRect(0, 0, canvas.width, canvas.height);

   ctx.font = '28px Arial';
   ctx.fillStyle = 'white';
   ctx.textAlign = 'center';
   ctx.textBaseline = 'middle';
   ctx.fillText(text, canvas.width / 2, canvas.height / 2);

   const texture = new THREE.CanvasTexture(canvas);
   const material = new THREE.SpriteMaterial({ map: texture, transparent: true });
   const sprite = new THREE.Sprite(material);
   sprite.scale.set(1.4, 0.7, 1);
   scene.add(sprite);
   return sprite;
   }

   const O = new THREE.Vector3(0, 0, 0);
   const fixedFrameLength = 2.2;

   makeAxis(O, new THREE.Vector3(1, 0, 0), 0xff5555, fixedFrameLength);
   makeAxis(O, new THREE.Vector3(0, 1, 0), 0x55ff55, fixedFrameLength);
   makeAxis(O, new THREE.Vector3(0, 0, 1), 0x5599ff, fixedFrameLength);

   const Opoint = makeSphere(0.06, 0xffffff);
   Opoint.position.copy(O);
   scene.add(Opoint);

   const labelO = createTextSprite('O');
   labelO.position.set(-0.15, -0.15, 0);

   const labelX0 = createTextSprite('x₀');
   labelX0.position.set(fixedFrameLength + 0.25, 0, 0);

   const labelY0 = createTextSprite('y₀');
   labelY0.position.set(0, fixedFrameLength + 0.25, 0);

   const labelZ0 = createTextSprite('z₀');
   labelZ0.position.set(0, 0, fixedFrameLength + 0.25);

   const movingOriginPoint = makeSphere(0.07, 0xffcc66);
   scene.add(movingOriginPoint);

   const movingX = makeAxis(new THREE.Vector3(), new THREE.Vector3(1, 0, 0), 0xff8888, 1.5);
   const movingY = makeAxis(new THREE.Vector3(), new THREE.Vector3(0, 1, 0), 0x88ff88, 1.5);
   const movingZ = makeAxis(new THREE.Vector3(), new THREE.Vector3(0, 0, 1), 0x88bbff, 1.5);

   const labelOb = createTextSprite('O_b');
   const labelXb = createTextSprite('x_b');
   const labelYb = createTextSprite('y_b');
   const labelZb = createTextSprite('z_b');

   const Ppoint = makeSphere(0.08, 0xffd700);
   scene.add(Ppoint);
   const labelP = createTextSprite('P');

   const pLocal = new THREE.Vector3(1.1, 0.7, 0.4);

   const rObO = makeLine(0x00ffff);
   const rPOb = makeLine(0xff00ff);
   const rPO = makeLine(0xffff00);

   const labelr1 = createTextSprite('r_{O_b/O}');
   const labelr2 = createTextSprite('r_{P/O_b}');
   const labelr3 = createTextSprite('r_{P/O}');

   const grid = new THREE.GridHelper(10, 10, 0x444444, 0x333333);
   scene.add(grid);

   const clock = new THREE.Clock();

   function setArrow(arrow, origin, dir, length) {
   arrow.position.copy(origin);
   arrow.setDirection(dir.clone().normalize());
   arrow.setLength(length, 0.18, 0.1);
   }

   function animate() {
   requestAnimationFrame(animate);

   const t = clock.getElapsedTime();

   const Ob = new THREE.Vector3(
      1.8 + 1.2 * Math.cos(0.6 * t),
      1.0 + 0.5 * Math.sin(1.0 * t),
      1.0 + 0.8 * Math.sin(0.7 * t)
   );

   const euler = new THREE.Euler(
      0.45 * Math.sin(0.8 * t),
      0.7 * t,
      0.25 * Math.cos(0.9 * t)
   );
   const R = new THREE.Matrix4().makeRotationFromEuler(euler);

   const ex = new THREE.Vector3(1, 0, 0).applyMatrix4(R).normalize();
   const ey = new THREE.Vector3(0, 1, 0).applyMatrix4(R).normalize();
   const ez = new THREE.Vector3(0, 0, 1).applyMatrix4(R).normalize();

   const pWorld = pLocal.clone().applyMatrix4(R).add(Ob);

   movingOriginPoint.position.copy(Ob);
   Ppoint.position.copy(pWorld);

   setArrow(movingX, Ob, ex, 1.5);
   setArrow(movingY, Ob, ey, 1.5);
   setArrow(movingZ, Ob, ez, 1.5);

   labelOb.position.copy(Ob).add(new THREE.Vector3(-0.2, -0.2, 0));
   labelXb.position.copy(Ob.clone().add(ex.clone().multiplyScalar(1.8)));
   labelYb.position.copy(Ob.clone().add(ey.clone().multiplyScalar(1.8)));
   labelZb.position.copy(Ob.clone().add(ez.clone().multiplyScalar(1.8)));

   labelP.position.copy(pWorld).add(new THREE.Vector3(0.2, 0.2, 0.1));

   updateLine(rObO, O, Ob);
   updateLine(rPOb, Ob, pWorld);
   updateLine(rPO, O, pWorld);

   labelr1.position.copy(O.clone().lerp(Ob, 0.5)).add(new THREE.Vector3(0, 0.2, 0));
   labelr2.position.copy(Ob.clone().lerp(pWorld, 0.5)).add(new THREE.Vector3(0.2, 0.2, 0));
   labelr3.position.copy(O.clone().lerp(pWorld, 0.5)).add(new THREE.Vector3(-0.2, 0.25, 0));

   controls.update();
   renderer.render(scene, camera);
   }

   animate();
   </script>

Consider two reference frames:

* a fixed frame :math:`(x_0, y_0, z_0)`
* a moving frame :math:`(x_b, y_b, z_b)`

The moving frame is attached to a rigid body and may both translate and rotate
relative to the fixed frame.

A point :math:`P` is fixed in the moving frame, so its coordinates in
:math:`(x_b, y_b, z_b)` are constant. Even so, the point may still move relative
to the fixed frame because the frame itself moves.

The position of :math:`P` relative to the origin :math:`O` of the fixed frame is

.. math::

   \vec{r}_{P/O} = \vec{r}_{O_b/O} + \vec{r}_{P/O_b}

To evaluate this expression, all vectors must be expressed in the same
reference frame.

Rotation transformations
------------------------
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

If :math:`\mathbf{r}^b` is known in frame :math:`b`, then its coordinates in
frame :math:`0` are given by

.. math::

   \mathbf{r}^0 = R^0_b \mathbf{r}^b

An arbitrary orientation can be built by combining principal rotations. A common
choice is

.. math::

   R^0_b = R_z(\psi)R_y(\theta)R_x(\phi)

Velocity in a moving frame
--------------------------
If point :math:`P` is fixed in the moving frame, then its velocity relative to
the fixed frame is

.. math::

   \vec{v}_{P/0} = \vec{v}_b + \vec{\omega} \times \vec{r}_{P/O_b}

where :math:`\vec{v}_b` is the velocity of the moving frame origin and
:math:`\vec{\omega}` is the angular velocity of the moving frame.

If :math:`P` also moves relative to the moving frame, then

.. math::

   \vec{v}_P = \vec{v}_b + (\vec{v}_P)_b + \vec{\omega} \times \vec{r}_{P/O_b}

where :math:`(\vec{v}_P)_b` is the velocity observed in the body-fixed frame.

Acceleration in a moving frame
------------------------------
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

* :math:`\vec{a}_b`: acceleration of the moving frame origin
* :math:`(\vec{a}_P)_b`: acceleration relative to the moving frame
* :math:`\vec{\alpha} \times \vec{r}_{P/O_b}`: tangential acceleration
* :math:`\vec{\omega} \times (\vec{\omega} \times \vec{r}_{P/O_b})`: centripetal acceleration
* :math:`2\,\vec{\omega} \times (\vec{v}_P)_b`: Coriolis acceleration

Summary
-------
The key ideas of vector kinematics are:

* vectors are described relative to reference frames
* vectors must be expressed in a common frame before they can be added
* rotation matrices transform coordinates between frames
* moving and rotating frames introduce extra velocity and acceleration terms

These ideas are fundamental in rigid-body mechanics, robotics, and vehicle
dynamics.
