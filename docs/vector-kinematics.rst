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

    <div id="frame-velocity-demo" style="width:100%; margin:1.5rem 0;">
      <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:16px;">
        <div style="background:#1e1e1e; border:1px solid #555; padding:10px;">
          <div style="color:white; font-weight:600; margin-bottom:8px;">1. Frame translation</div>
          <canvas id="frame-panel-1" style="width:100%; height:220px; display:block;"></canvas>
          <div style="color:#d0d0d0; font-size:0.95rem; margin-top:8px;">
            Only the translation of frame b relative to frame i is shown.
          </div>
        </div>
        <div style="background:#1e1e1e; border:1px solid #555; padding:10px;">
          <div style="color:white; font-weight:600; margin-bottom:8px;">2. Relative motion in frame b</div>
          <canvas id="frame-panel-2" style="width:100%; height:220px; display:block;"></canvas>
          <div style="color:#d0d0d0; font-size:0.95rem; margin-top:8px;">
            The point moves relative to frame b.
          </div>
        </div>
        <div style="background:#1e1e1e; border:1px solid #555; padding:10px;">
          <div style="color:white; font-weight:600; margin-bottom:8px;">3. Frame rotation</div>
          <canvas id="frame-panel-3" style="width:100%; height:220px; display:block;"></canvas>
          <div style="color:#d0d0d0; font-size:0.95rem; margin-top:8px;">
            The point is fixed in frame b, but frame b rotates.
          </div>
        </div>
        <div style="background:#1e1e1e; border:1px solid #555; padding:10px;">
          <div style="color:white; font-weight:600; margin-bottom:8px;">4. Combined motion</div>
          <canvas id="frame-panel-4" style="width:100%; height:220px; display:block;"></canvas>
          <div style="color:#d0d0d0; font-size:0.95rem; margin-top:8px;">
            Only the total velocity of P in the inertial frame is shown.
          </div>
        </div>
      </div>
    </div>

    <script>
    (function () {
      const ids = ["frame-panel-1", "frame-panel-2", "frame-panel-3", "frame-panel-4"];
      const canvases = ids.map(id => document.getElementById(id));
      const ctxs = canvases.map(c => c.getContext("2d"));

      function resize() {
        canvases.forEach(c => {
          const dpr = window.devicePixelRatio || 1;
          const rect = c.getBoundingClientRect();
          c.width = rect.width * dpr;
          c.height = rect.height * dpr;
          c.getContext("2d").setTransform(dpr, 0, 0, dpr, 0, 0);
        });
      }

      resize();
      window.addEventListener("resize", resize);

      function rot(x, y, a) {
        return {
          x: x * Math.cos(a) - y * Math.sin(a),
          y: x * Math.sin(a) + y * Math.cos(a)
        };
      }

      function add(a, b) {
        return { x: a.x + b.x, y: a.y + b.y };
      }

      function mul(a, s) {
        return { x: a.x * s, y: a.y * s };
      }

      function perp(a) {
        return { x: -a.y, y: a.x };
      }

      function drawArrow(ctx, x1, y1, x2, y2, color, width = 2) {
        const dx = x2 - x1;
        const dy = y2 - y1;
        const L = Math.hypot(dx, dy);
        if (L < 1e-6) return;
        const ux = dx / L;
        const uy = dy / L;
        const h = 9;
        ctx.strokeStyle = color;
        ctx.fillStyle = color;
        ctx.lineWidth = width;
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(x2, y2);
        ctx.lineTo(x2 - h * ux - 0.5 * h * uy, y2 - h * uy + 0.5 * h * ux);
        ctx.lineTo(x2 - h * ux + 0.5 * h * uy, y2 - h * uy - 0.5 * h * ux);
        ctx.closePath();
        ctx.fill();
      }

      function drawDot(ctx, x, y, r, color) {
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.arc(x, y, r, 0, 2 * Math.PI);
        ctx.fill();
      }

      function drawBackground(ctx, w, h) {
        ctx.fillStyle = "#202830";
        ctx.fillRect(0, 0, w, h);
        ctx.strokeStyle = "#314050";
        ctx.lineWidth = 1;
        for (let x = 24; x < w; x += 32) {
          ctx.beginPath();
          ctx.moveTo(x, 0);
          ctx.lineTo(x, h);
          ctx.stroke();
        }
        for (let y = 24; y < h; y += 32) {
          ctx.beginPath();
          ctx.moveTo(0, y);
          ctx.lineTo(w, y);
          ctx.stroke();
        }
      }

      function drawFrameI(ctx, w, h) {
        const o = { x: 28, y: h - 26 };
        drawArrow(ctx, o.x, o.y, o.x + 34, o.y, "#ff6b6b", 1.6);
        drawArrow(ctx, o.x, o.y, o.x, o.y - 34, "#6bb7ff", 1.6);
        ctx.fillStyle = "white";
        ctx.font = "12px Arial";
        ctx.fillText("i", o.x - 8, o.y + 14);
      }

      function drawFrameB(ctx, origin, angle) {
        const ex = rot(34, 0, angle);
        const ey = rot(0, -28, angle);
        drawDot(ctx, origin.x, origin.y, 4, "#ffd54f");
        drawArrow(ctx, origin.x, origin.y, origin.x + ex.x, origin.y + ex.y, "#ff8a80", 1.6);
        drawArrow(ctx, origin.x, origin.y, origin.x + ey.x, origin.y + ey.y, "#80e27e", 1.6);
        ctx.fillStyle = "#ffd54f";
        ctx.font = "12px Arial";
        ctx.fillText("b", origin.x - 7, origin.y - 8);
      }

      function drawPointP(ctx, p) {
        drawDot(ctx, p.x, p.y, 5, "#ffffff");
        ctx.fillStyle = "#ffd54f";
        ctx.font = "12px Arial";
        ctx.fillText("P", p.x + 7, p.y - 8);
      }

      function drawMathLabel(ctx, x, y, color, spec) {
        let cursor = x;
        ctx.fillStyle = color;
        for (const part of spec) {
          if (part.type === "normal") {
            ctx.font = "12px Arial";
            ctx.fillText(part.text, cursor, y);
            cursor += ctx.measureText(part.text).width;
          } else if (part.type === "sub") {
            ctx.font = "9px Arial";
            ctx.fillText(part.text, cursor, y + 4);
            cursor += ctx.measureText(part.text).width;
          } else if (part.type === "sup") {
            ctx.font = "9px Arial";
            ctx.fillText(part.text, cursor, y - 5);
            cursor += ctx.measureText(part.text).width;
          }
        }
      }

      function phase(t, T) {
        return (t % T) / T;
      }

      function state(t, mode) {
        const Ttrans = 5.0;
        const Trel = 3.6;
        const Trot = 4.4;

        const omegaRot = 0.75 * (2 * Math.PI / Trot) * Math.cos(2 * Math.PI * phase(t, Trot));
        const angle = 0.75 * Math.sin(2 * Math.PI * phase(t, Trot));

        const bMove = { x: 70 + 145 * phase(t, Ttrans), y: 115 };
        const bFixed = { x: 145, y: 115 };
        const vTrans = { x: 145 / Ttrans, y: 0 };

        const xRel = 26 * Math.sin(2 * Math.PI * phase(t, Trel));
        const xRelDot = 26 * (2 * Math.PI / Trel) * Math.cos(2 * Math.PI * phase(t, Trel));

        if (mode === 1) {
          const b = bMove;
          const rLocal = { x: 32, y: -16 };
          const p = add(b, rLocal);
          return {
            b, p, angle: 0, vArrow: vTrans, color: "#4dd0e1",
            label: [{type:"normal",text:"v"},{type:"sub",text:"b/i"},{type:"sup",text:"i"}]
          };
        }

        if (mode === 2) {
          const b = bFixed;
          const rLocal = { x: xRel, y: -16 };
          const p = add(b, rLocal);
          const vRel = { x: xRelDot, y: 0 };
          return {
            b, p, angle: 0, vArrow: vRel, color: "#ffb74d",
            label: [
              {type:"normal",text:"d"},
              {type:"sup",text:"b"},
              {type:"normal",text:"r"},
              {type:"sub",text:"P/b"},
              {type:"normal",text:"/dt"}
            ]
          };
        }

        if (mode === 3) {
          const b = bFixed;
          const rLocal = { x: 36, y: -16 };
          const rWorld = rot(rLocal.x, rLocal.y, angle);
          const p = add(b, rWorld);
          const vRot = mul(perp(rWorld), omegaRot);
          return {
            b, p, angle, vArrow: vRot, color: "#81c784", showR: true,
            label: [
              {type:"normal",text:"ω × r"},
              {type:"sub",text:"P/b"}
            ]
          };
        }

        const b = bMove;
        const rLocal = { x: 12 + xRel, y: -16 };
        const rWorld = rot(rLocal.x, rLocal.y, angle);
        const p = add(b, rWorld);
        const vRel = rot(xRelDot, 0, angle);
        const vRot = mul(perp(rWorld), omegaRot);
        const vTot = add(add(vTrans, vRel), vRot);
        return {
          b, p, angle, vArrow: vTot, color: "#ef5350",
          label: [{type:"normal",text:"v"},{type:"sub",text:"P/i"},{type:"sup",text:"i"}]
        };
      }

      function renderPanel(ctx, canvas, t, mode) {
        const w = canvas.getBoundingClientRect().width;
        const h = canvas.getBoundingClientRect().height;

        ctx.clearRect(0, 0, w, h);
        drawBackground(ctx, w, h);
        drawFrameI(ctx, w, h);

        const s = state(t, mode);
        drawFrameB(ctx, s.b, s.angle);
        drawPointP(ctx, s.p);

        if (s.showR) {
          drawArrow(ctx, s.b.x, s.b.y, s.p.x, s.p.y, "#8a8a8a", 1.2);
        }

        const scale = 0.85;
        const arrowEnd = add(s.p, mul(s.vArrow, scale));
        drawArrow(ctx, s.p.x, s.p.y, arrowEnd.x, arrowEnd.y, s.color, 2.6);
        drawMathLabel(ctx, arrowEnd.x + 6, arrowEnd.y - 6, s.color, s.label);
      }

      let start = null;

      function animate(ts) {
        if (!start) start = ts;
        const t = (ts - start) / 1000;
        renderPanel(ctxs[0], canvases[0], t, 1);
        renderPanel(ctxs[1], canvases[1], t, 2);
        renderPanel(ctxs[2], canvases[2], t, 3);
        renderPanel(ctxs[3], canvases[3], t, 4);
        requestAnimationFrame(animate);
      }

      requestAnimationFrame(animate);
    })();
    </script>

A Visual Interpretation of the Linear Velocity Equation (boat)
==============================================================

.. raw:: html

    <div id="boat-velocity-demo" style="width:100%; margin:1.5rem 0;">
      <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:16px;">
        <div style="background:#1e1e1e; border:1px solid #555; padding:10px;">
          <div style="color:white; font-weight:600; margin-bottom:8px;">1. Boat translation</div>
          <canvas id="boat-panel-1" style="width:100%; height:220px; display:block;"></canvas>
          <div style="color:#d0d0d0; font-size:0.95rem; margin-top:8px;">
            Only the translation of the boat relative to the inertial frame is shown.
          </div>
        </div>
        <div style="background:#1e1e1e; border:1px solid #555; padding:10px;">
          <div style="color:white; font-weight:600; margin-bottom:8px;">2. Relative motion on deck</div>
          <canvas id="boat-panel-2" style="width:100%; height:220px; display:block;"></canvas>
          <div style="color:#d0d0d0; font-size:0.95rem; margin-top:8px;">
            The person moves relative to the boat.
          </div>
        </div>
        <div style="background:#1e1e1e; border:1px solid #555; padding:10px;">
          <div style="color:white; font-weight:600; margin-bottom:8px;">3. Boat rotation</div>
          <canvas id="boat-panel-3" style="width:100%; height:220px; display:block;"></canvas>
          <div style="color:#d0d0d0; font-size:0.95rem; margin-top:8px;">
            The person is fixed on deck, but the boat rotates.
          </div>
        </div>
        <div style="background:#1e1e1e; border:1px solid #555; padding:10px;">
          <div style="color:white; font-weight:600; margin-bottom:8px;">4. Combined motion</div>
          <canvas id="boat-panel-4" style="width:100%; height:220px; display:block;"></canvas>
          <div style="color:#d0d0d0; font-size:0.95rem; margin-top:8px;">
            Only the total velocity of P in the inertial frame is shown.
          </div>
        </div>
      </div>
    </div>

    <script>
    (function () {
      const ids = ["boat-panel-1", "boat-panel-2", "boat-panel-3", "boat-panel-4"];
      const canvases = ids.map(id => document.getElementById(id));
      const ctxs = canvases.map(c => c.getContext("2d"));

      function resize() {
        canvases.forEach(c => {
          const dpr = window.devicePixelRatio || 1;
          const rect = c.getBoundingClientRect();
          c.width = rect.width * dpr;
          c.height = rect.height * dpr;
          c.getContext("2d").setTransform(dpr, 0, 0, dpr, 0, 0);
        });
      }

      resize();
      window.addEventListener("resize", resize);

      function rot(x, y, a) {
        return {
          x: x * Math.cos(a) - y * Math.sin(a),
          y: x * Math.sin(a) + y * Math.cos(a)
        };
      }

      function add(a, b) {
        return { x: a.x + b.x, y: a.y + b.y };
      }

      function mul(a, s) {
        return { x: a.x * s, y: a.y * s };
      }

      function perp(a) {
        return { x: -a.y, y: a.x };
      }

      function drawArrow(ctx, x1, y1, x2, y2, color, width = 2) {
        const dx = x2 - x1;
        const dy = y2 - y1;
        const L = Math.hypot(dx, dy);
        if (L < 1e-6) return;
        const ux = dx / L;
        const uy = dy / L;
        const h = 9;
        ctx.strokeStyle = color;
        ctx.fillStyle = color;
        ctx.lineWidth = width;
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(x2, y2);
        ctx.lineTo(x2 - h * ux - 0.5 * h * uy, y2 - h * uy + 0.5 * h * ux);
        ctx.lineTo(x2 - h * ux + 0.5 * h * uy, y2 - h * uy - 0.5 * h * ux);
        ctx.closePath();
        ctx.fill();
      }

      function drawDot(ctx, x, y, r, color) {
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.arc(x, y, r, 0, 2 * Math.PI);
        ctx.fill();
      }

      function drawSea(ctx, w, h) {
        ctx.fillStyle = "#202830";
        ctx.fillRect(0, 0, w, h);
        ctx.strokeStyle = "#314050";
        ctx.lineWidth = 1;
        for (let y = 18; y < h; y += 24) {
          ctx.beginPath();
          for (let x = 0; x <= w; x += 14) {
            const yy = y + 2.2 * Math.sin(0.05 * x + 0.08 * y);
            if (x === 0) ctx.moveTo(x, yy);
            else ctx.lineTo(x, yy);
          }
          ctx.stroke();
        }
      }

      function drawFrameI(ctx, w, h) {
        const o = { x: 28, y: h - 26 };
        drawArrow(ctx, o.x, o.y, o.x + 34, o.y, "#ff6b6b", 1.6);
        drawArrow(ctx, o.x, o.y, o.x, o.y - 34, "#6bb7ff", 1.6);
        ctx.fillStyle = "white";
        ctx.font = "12px Arial";
        ctx.fillText("i", o.x - 8, o.y + 14);
      }

      function drawBoat(ctx, cx, cy, angle) {
        const pts = [
          {x:-50,y:-16},
          {x:30,y:-16},
          {x:50,y:0},
          {x:30,y:16},
          {x:-50,y:16}
        ].map(p => rot(p.x, p.y, angle));

        ctx.fillStyle = "#7b4f2a";
        ctx.strokeStyle = "#d8b48a";
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(cx + pts[0].x, cy + pts[0].y);
        for (let i = 1; i < pts.length; i++) {
          ctx.lineTo(cx + pts[i].x, cy + pts[i].y);
        }
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        const ex = rot(32, 0, angle);
        const ey = rot(0, -26, angle);
        drawDot(ctx, cx, cy, 4, "#ffd54f");
        drawArrow(ctx, cx, cy, cx + ex.x, cy + ex.y, "#ff8a80", 1.5);
        drawArrow(ctx, cx, cy, cx + ey.x, cy + ey.y, "#80e27e", 1.5);

        ctx.fillStyle = "#ffd54f";
        ctx.font = "12px Arial";
        ctx.fillText("b", cx - 7, cy - 8);
      }

      function drawPerson(ctx, x, y) {
        ctx.strokeStyle = "#f5f5f5";
        ctx.fillStyle = "#f5d08a";
        ctx.lineWidth = 1.8;

        ctx.beginPath();
        ctx.arc(x, y - 9, 4.5, 0, 2 * Math.PI);
        ctx.fill();

        ctx.beginPath();
        ctx.moveTo(x, y - 4);
        ctx.lineTo(x, y + 8);
        ctx.moveTo(x, y);
        ctx.lineTo(x - 6, y + 4);
        ctx.moveTo(x, y);
        ctx.lineTo(x + 6, y + 4);
        ctx.moveTo(x, y + 8);
        ctx.lineTo(x - 5, y + 17);
        ctx.moveTo(x, y + 8);
        ctx.lineTo(x + 5, y + 17);
        ctx.stroke();

        ctx.fillStyle = "#ffd54f";
        ctx.font = "12px Arial";
        ctx.fillText("P", x + 7, y - 8);
      }

      function drawMathLabel(ctx, x, y, color, spec) {
        let cursor = x;
        ctx.fillStyle = color;
        for (const part of spec) {
          if (part.type === "normal") {
            ctx.font = "12px Arial";
            ctx.fillText(part.text, cursor, y);
            cursor += ctx.measureText(part.text).width;
          } else if (part.type === "sub") {
            ctx.font = "9px Arial";
            ctx.fillText(part.text, cursor, y + 4);
            cursor += ctx.measureText(part.text).width;
          } else if (part.type === "sup") {
            ctx.font = "9px Arial";
            ctx.fillText(part.text, cursor, y - 5);
            cursor += ctx.measureText(part.text).width;
          }
        }
      }

      function phase(t, T) {
        return (t % T) / T;
      }

      function state(t, mode) {
        const Ttrans = 5.0;
        const Trel = 3.6;
        const Trot = 4.4;

        const omegaRot = 0.75 * (2 * Math.PI / Trot) * Math.cos(2 * Math.PI * phase(t, Trot));
        const angle = 0.75 * Math.sin(2 * Math.PI * phase(t, Trot));

        const bMove = { x: 70 + 145 * phase(t, Ttrans), y: 115 };
        const bFixed = { x: 145, y: 115 };
        const vTrans = { x: 145 / Ttrans, y: 0 };

        const xRel = 24 * Math.sin(2 * Math.PI * phase(t, Trel));
        const xRelDot = 24 * (2 * Math.PI / Trel) * Math.cos(2 * Math.PI * phase(t, Trel));

        if (mode === 1) {
          const b = bMove;
          const rLocal = { x: 18, y: -6 };
          const p = add(b, rLocal);
          return {
            b,
            p,
            angle: 0,
            vArrow: vTrans,
            color: "#4dd0e1",
            label: [
              { type: "normal", text: "v" },
              { type: "sub", text: "b/i" },
              { type: "sup", text: "i" }
            ]
          };
        }

        if (mode === 2) {
          const b = bFixed;
          const rLocal = { x: xRel, y: -6 };
          const p = add(b, rLocal);
          const vRel = { x: xRelDot, y: 0 };
          return {
            b,
            p,
            angle: 0,
            vArrow: vRel,
            color: "#ffb74d",
            label: [
              { type: "normal", text: "d" },
              { type: "sup", text: "b" },
              { type: "normal", text: "r" },
              { type: "sub", text: "P/b" },
              { type: "normal", text: "/dt" }
            ]
          };
        }

        if (mode === 3) {
          const b = bFixed;
          const rLocal = { x: 24, y: -6 };
          const rWorld = rot(rLocal.x, rLocal.y, angle);
          const p = add(b, rWorld);
          const vRot = mul(perp(rWorld), omegaRot);
          return {
            b,
            p,
            angle,
            vArrow: vRot,
            color: "#81c784",
            showR: true,
            label: [
              { type: "normal", text: "ω × r" },
              { type: "sub", text: "P/b" }
            ]
          };
        }

        const b = bMove;
        const rLocal = { x: 8 + xRel, y: -6 };
        const rWorld = rot(rLocal.x, rLocal.y, angle);
        const p = add(b, rWorld);
        const vRel = rot(xRelDot, 0, angle);
        const vRot = mul(perp(rWorld), omegaRot);
        const vTot = add(add(vTrans, vRel), vRot);

        return {
          b,
          p,
          angle,
          vArrow: vTot,
          color: "#ef5350",
          label: [
            { type: "normal", text: "v" },
            { type: "sub", text: "P/i" },
            { type: "sup", text: "i" }
          ]
        };
      }

      function renderPanel(ctx, canvas, t, mode) {
        const w = canvas.getBoundingClientRect().width;
        const h = canvas.getBoundingClientRect().height;

        ctx.clearRect(0, 0, w, h);
        drawSea(ctx, w, h);
        drawFrameI(ctx, w, h);

        const s = state(t, mode);
        drawBoat(ctx, s.b.x, s.b.y, s.angle);
        drawPerson(ctx, s.p.x, s.p.y);

        if (s.showR) {
          drawArrow(ctx, s.b.x, s.b.y, s.p.x, s.p.y, "#8a8a8a", 1.2);
        }

        const scale = 0.85;
        const arrowEnd = add(s.p, mul(s.vArrow, scale));
        drawArrow(ctx, s.p.x, s.p.y, arrowEnd.x, arrowEnd.y, s.color, 2.6);
        drawMathLabel(ctx, arrowEnd.x + 6, arrowEnd.y - 6, s.color, s.label);
      }

      let start = null;

      function animate(ts) {
        if (!start) start = ts;
        const t = (ts - start) / 1000;
        renderPanel(ctxs[0], canvases[0], t, 1);
        renderPanel(ctxs[1], canvases[1], t, 2);
        renderPanel(ctxs[2], canvases[2], t, 3);
        renderPanel(ctxs[3], canvases[3], t, 4);
        requestAnimationFrame(animate);
      }

      requestAnimationFrame(animate);
    })();
    </script>

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

.. figure:: images/strava_carrier_example.png
    :width: 70%
    :align: center

    A recorded trajectory can reveal the motion of the entire reference frame.
