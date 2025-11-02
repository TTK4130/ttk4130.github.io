=================
Quaternions
=================

.. note::

    In the following section we will use the Hamiltonian quaternion convention presented in :cite:t:`sola2017`


As you might recall, with XYZ Euler angles, rotations are applied sequentially:

.. math::

   R_{XYZ}(\phi, \theta, \psi) = R_z(\psi) R_y(\theta) R_x(\phi)

where :math:`\phi` = roll, :math:`\theta` = pitch, :math:`\psi` = yaw.

The combined rotation matrix is:

.. math::

   R_{XYZ} = \begin{bmatrix}
   c_\theta c_\psi & -c_\theta s_\psi & s_\theta \\
   c_\phi s_\psi + s_\phi s_\theta c_\psi & c_\phi c_\psi - s_\phi s_\theta s_\psi & -s_\phi c_\theta \\
   s_\phi s_\psi - c_\phi s_\theta c_\psi & s_\phi c_\psi + c_\phi s_\theta s_\psi & c_\phi c_\theta
   \end{bmatrix}

where :math:`c_\alpha = \cos\alpha` and :math:`s_\alpha = \sin\alpha`.

Gimbal lock occurs when :math:`\theta = +90°` (pitch = 90°):

.. math::

   \cos\theta = 0, \quad \sin\theta = 1

The matrix becomes:

.. math::

   R_{XYZ} = \begin{bmatrix}
   0 & 0 & 1 \\
   \cos(\phi + \psi) & -\sin(\phi + \psi) & 0 \\
   \sin(\phi + \psi) & \cos(\phi + \psi) & 0
   \end{bmatrix}

The matrix now depends only on :math:`(\phi + \psi)`, not on
:math:`\phi` and :math:`\psi` individually.

As a consequence, the two rotations :math:`(\phi, \psi) \mapsto (\phi + \delta, \psi - \delta)` produce identical rotations.
The 3D parameter space :math:`(\phi, \theta, \psi)` collapses to 2D at :math:`\theta = \pm 90°`. Infinitely many Euler angle combinations represent the same physical rotation and one degree of rotational freedom is mathematically lost

This degeneracy makes smooth interpolation impossible and causes the characteristic
"flipping" behavior near gimbal lock orientations. **This is why quaternions are preferred
for 3D rotations** - they never
suffer from singularities, providing smooth interpolation for all possible orientations.
On this page we'll explore exactly what quaternions are and why they have this useful property.

.. raw:: html

    <div id="gimbal-container" style="position: relative; width: 100%; height: 60vh; min-height: 500px; border: 1px solid #555; border-radius: 10px; overflow: hidden; background: radial-gradient(circle at center, #1a1a2e 0%, #0f0f23 100%);"></div>
    <script type="importmap">
    {
     "imports": {
       "three": "https://cdn.jsdelivr.net/npm/three@0.150.1/build/three.module.js"
     }
    }
    </script>
    <script type="module">
    import * as THREE from 'three';

    const container = document.getElementById('gimbal-container');
    const containerWidth = container.clientWidth;
    const containerHeight = container.clientHeight;

    // Create overlay
    const overlay = document.createElement('div');
    overlay.style.cssText = `
        position: absolute; bottom: 20px; right: 20px; background: rgba(0,0,0,0.85);
        backdrop-filter: blur(15px); border-radius: 15px; padding: 15px; max-width: 260px;
        border: 1px solid rgba(255,255,255,0.1); color: white; font-family: 'Segoe UI', sans-serif;
        z-index: 10;
    `;
    overlay.innerHTML = `
        <div id="status" style="text-align: center; font-size: 0.9em; font-weight: 700; padding: 8px; border-radius: 8px; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.5px; background: linear-gradient(135deg, #27ae60, #2ecc71); color: white;">✓ INDEPENDENT</div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 12px;">
            <div style="background: rgba(255,107,107,0.1); padding: 8px; border-radius: 6px; text-align: center; border-left: 3px solid #ff6b6b;">
                <div style="font-size: 0.7em; font-weight: 600; margin-bottom: 2px; color: #ff6b6b;">X AXIS</div>
                <div id="x-val" style="font-family: monospace; font-size: 1.1em; font-weight: 700; color: #ff6b6b;">0°</div>
            </div>
            <div style="background: rgba(78,205,196,0.1); padding: 8px; border-radius: 6px; text-align: center; border-left: 3px solid #4ecdc4;">
                <div style="font-size: 0.7em; font-weight: 600; margin-bottom: 2px; color: #4ecdc4;">Y AXIS</div>
                <div id="y-val" style="font-family: monospace; font-size: 1.1em; font-weight: 700; color: #4ecdc4;">0°</div>
            </div>
            <div style="background: rgba(254,202,87,0.1); padding: 8px; border-radius: 6px; text-align: center; border-left: 3px solid #feca57; grid-column: span 2;">
                <div style="font-size: 0.7em; font-weight: 600; margin-bottom: 2px; color: #feca57;">Z AXIS</div>
                <div id="z-val" style="font-family: monospace; font-size: 1.1em; font-weight: 700; color: #feca57;">0°</div>
            </div>
        </div>
        <div id="desc" style="font-size: 0.75em; line-height: 1.3; opacity: 0.9; background: rgba(255,255,255,0.05); padding: 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.1);">XYZ Euler angles: When Y ≈ ±90°, the first (X) and third (Z) rotation axes align, causing gimbal lock.</div>
    `;
    container.appendChild(overlay);

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x050510);

    const camera = new THREE.PerspectiveCamera(75, containerWidth/containerHeight, 0.1, 1000);
    camera.position.set(9, 7, 11);
    camera.lookAt(0, 0, 0);

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(containerWidth, containerHeight);
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    container.appendChild(renderer.domElement);

    // Lighting
    const ambientLight = new THREE.AmbientLight(0x404040, 0.4);
    scene.add(ambientLight);
    const mainLight = new THREE.DirectionalLight(0xffffff, 1.2);
    mainLight.position.set(10, 10, 5);
    mainLight.castShadow = true;
    scene.add(mainLight);
    const accentLight1 = new THREE.PointLight(0xff6b6b, 0.6);
    accentLight1.position.set(5, 5, 5);
    scene.add(accentLight1);
    const accentLight2 = new THREE.PointLight(0x4ecdc4, 0.6);
    accentLight2.position.set(-5, 5, -5);
    scene.add(accentLight2);

    // Create cube
    const cubeGeometry = new THREE.BoxGeometry(2, 2, 2);
    const cubeMaterials = [
        new THREE.MeshPhongMaterial({ color: 0xff4757, shininess: 100 }),
        new THREE.MeshPhongMaterial({ color: 0x2ed573, shininess: 100 }),
        new THREE.MeshPhongMaterial({ color: 0x3742fa, shininess: 100 }),
        new THREE.MeshPhongMaterial({ color: 0xffa502, shininess: 100 }),
        new THREE.MeshPhongMaterial({ color: 0xff6b6b, shininess: 100 }),
        new THREE.MeshPhongMaterial({ color: 0x57606f, shininess: 100 })
    ];
    const cube = new THREE.Mesh(cubeGeometry, cubeMaterials);
    cube.castShadow = true;
    scene.add(cube);

    // Create gimbal rings
    const ringRadius = 4;
    const ringTube = 0.15;

    // X gimbal (red)
    const xGimbal = new THREE.Mesh(
        new THREE.TorusGeometry(ringRadius, ringTube, 12, 48),
        new THREE.MeshPhongMaterial({ color: 0xff6b6b, transparent: true, opacity: 0.8, shininess: 100 })
    );
    xGimbal.rotation.y = Math.PI / 2;
    xGimbal.castShadow = true;
    scene.add(xGimbal);

    // Y gimbal (cyan)
    const yGimbal = new THREE.Mesh(
        new THREE.TorusGeometry(ringRadius * 0.8, ringTube, 12, 48),
        new THREE.MeshPhongMaterial({ color: 0x4ecdc4, transparent: true, opacity: 0.8, shininess: 100 })
    );
    yGimbal.castShadow = true;
    scene.add(yGimbal);

    // Z gimbal (yellow)
    const zGimbal = new THREE.Mesh(
        new THREE.TorusGeometry(ringRadius * 0.6, ringTube, 12, 48),
        new THREE.MeshPhongMaterial({ color: 0xfeca57, transparent: true, opacity: 0.8, shininess: 100 })
    );
    zGimbal.rotation.x = Math.PI / 2;
    zGimbal.castShadow = true;
    scene.add(zGimbal);

    // Ground plane
    const plane = new THREE.Mesh(
        new THREE.PlaneGeometry(25, 25),
        new THREE.MeshLambertMaterial({ color: 0x1a1a2e, transparent: true, opacity: 0.2 })
    );
    plane.rotation.x = -Math.PI / 2;
    plane.position.y = -6;
    plane.receiveShadow = true;
    scene.add(plane);

    // Animation variables
    let time = 0;
    const rotationSpeed = 0.6;

    // DOM elements
    const statusEl = document.getElementById('status');
    const xVal = document.getElementById('x-val');
    const yVal = document.getElementById('y-val');
    const zVal = document.getElementById('z-val');
    const desc = document.getElementById('desc');

    function updateDisplay(x, y, z) {
        const xDeg = ((x * 180 / Math.PI) % 360 + 360) % 360;
        const yDeg = ((y * 180 / Math.PI) % 360 + 360) % 360;
        const zDeg = ((z * 180 / Math.PI) % 360 + 360) % 360;

        xVal.textContent = Math.round(xDeg) + '°';
        yVal.textContent = Math.round(yDeg) + '°';
        zVal.textContent = Math.round(zDeg) + '°';

        const yNormalized = yDeg % 360;
        const nearPos90 = Math.abs(yNormalized - 90) < 20;
        const nearNeg90 = Math.abs(yNormalized - 270) < 20;
        const veryNearPos90 = Math.abs(yNormalized - 90) < 8;
        const veryNearNeg90 = Math.abs(yNormalized - 270) < 8;

        const isNear = nearPos90 || nearNeg90;
        const isLock = veryNearPos90 || veryNearNeg90;

        if (isLock) {
            statusEl.style.background = 'linear-gradient(135deg, #e74c3c, #c0392b)';
            statusEl.style.animation = 'pulse 1.5s infinite';
            statusEl.innerHTML = '🚨 GIMBAL LOCK';
            desc.textContent = 'CRITICAL: X and Z axes are parallel! First and third rotations now do the same thing.';
            xGimbal.material.opacity = 1.0;
            zGimbal.material.opacity = 1.0;
            yGimbal.material.opacity = 0.4;
        } else if (isNear) {
            statusEl.style.background = 'linear-gradient(135deg, #f39c12, #e67e22)';
            statusEl.style.animation = 'none';
            statusEl.innerHTML = '⚠️ APPROACHING';
            desc.textContent = 'WARNING: Y rotation nearing ±90°. X and Z axes becoming parallel.';
            xGimbal.material.opacity = 0.9;
            zGimbal.material.opacity = 0.9;
            yGimbal.material.opacity = 0.7;
        } else {
            statusEl.style.background = 'linear-gradient(135deg, #27ae60, #2ecc71)';
            statusEl.style.animation = 'none';
            statusEl.innerHTML = '✓ INDEPENDENT';
            desc.textContent = 'All rotation axes independent. Full 3D rotational freedom available.';
            xGimbal.material.opacity = 0.8;
            yGimbal.material.opacity = 0.8;
            zGimbal.material.opacity = 0.8;
        }
    }

    // Add CSS animation
    const style = document.createElement('style');
    style.textContent = '@keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }';
    document.head.appendChild(style);

    function animate() {
        requestAnimationFrame(animate);

        time += 0.012 * rotationSpeed;

        const xRotation = Math.sin(time * 0.8) * 0.7;
        const yRotation = Math.sin(time * 0.35) * Math.PI * 0.48;
        const zRotation = Math.sin(time * 0.6) * 0.9;

        cube.rotation.set(xRotation, yRotation, zRotation);

        xGimbal.rotation.set(0, Math.PI / 2, 0);
        yGimbal.rotation.set(xRotation, 0, 0);
        const zGimbalRotation = new THREE.Euler(xRotation, yRotation, Math.PI / 2, 'XYZ');
        zGimbal.rotation.copy(zGimbalRotation);

        updateDisplay(xRotation, yRotation, zRotation);

        const radius = 12;
        camera.position.x = Math.cos(time * 0.08) * radius;
        camera.position.z = Math.sin(time * 0.08) * radius;
        camera.position.y = 7;
        camera.lookAt(0, 0, 0);

        renderer.render(scene, camera);
    }

    animate();
    </script>


Intuition: Discovering the Quaternion
=====================================

The goal of this section is to build an intuition for how quaternions were discovered and how they relate to rotations and vectors.
Many textbooks just give you definitions and conversions to work with. This can be quite unsatisfying for the curious minded among you.
If you just care about how to use quaternions you can skip the following subsection.


Quaternions were discovered by Sir William Rowan Hamilton, a brilliant irish mathematician and physicist who lived in the 1800s.
Briefly explained, he wanted to find a general way to multiply what he called "couplets", but what we today recognise as four dimensional vectors.
Let's follow in his footsteps and see what we can discover

Creating an n-dimensional vector is quite simple for us. We can simply use the following notation

.. math::

    Q = \begin{pmatrix} 1 & 2 & 3 & 4\end{pmatrix}, Q \in \mathbb{R}^4

But remember, this was before vector calculus, so how would we represent a higher dimensional number?
Similar to what we do when we work with reference frames, we can explicitly define the basis vectors of each dimension.
To avoid using the modern vector algebra, let's consider number lines. We know we have real numbers (1, 2, 3, etc.) along the
real number line. If we wanted another one we can define a new axis :math:`i` (1i, 2i, 3i, etc.). If we want a number in four dimensions
we can make the axes explicit by writing

.. math::

    Q = 1 + 2i + 3j + 4k

Where each of the letters :math:`i, j, k` represent a new dimension or "number line". Just like Hamilton, we quickly discover that
adding such numbers is simple

.. math::

    A = 1 + 2i + 3j + 4k \\
    B = 0 + 2i - 1j + 0k \\
    A + B = 1 + 4i + 2j + 4k

and more generally

.. math::

    Q_1 = a + bi + cj + dk \\
    Q_2 = e + fi + gj + hk \\
    Q_1 + Q_2 = Q_2 + Q_2 = (a + e) + (b + f)i + (c + g)j + (d +h)k

Hamilton then asked himself: How do I multiply two of these numbers in a way that results in the same type of number?

.. math::

    Q_1 Q_2 = ae + afi + agi + ahk \\
    bei + bfi^2 + bgij + bhik \\
    cej + cfji + cgj^2 + chjk \\
    dek + dfki + dgkj + dhk^2

Hamilton's issue was what to do with the products of the letters :math:`i, j, k` representing each dimension. There must
be a way to make sure that the product becomes a new number of the same kind. Since :math:`i, j, k` are special symbols, we cannot
assume that they are commutable, meaning that :math:`ij ≠ ji`. After struggling for a while, Hamilton famously had a eureka moment
by the Broom Bridge in Dublin. Having no paper with him, he inscribed the fundamental rules for quaternion multiplication on the bridge

.. math::

    i^2 = j^2 = k^2 = ijk = -1

.. raw:: html

    <p style="text-align:center;">
      <a href="https://commons.wikimedia.org/wiki/File:Inscription_on_Broom_Bridge_(Dublin)_regarding_the_discovery_of_Quaternions_multiplication_by_Sir_William_Rowan_Hamilton.jpg#/media/File:Inscription_on_Broom_Bridge_(Dublin)_regarding_the_discovery_of_Quaternions_multiplication_by_Sir_William_Rowan_Hamilton.jpg">
        <img
          src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Inscription_on_Broom_Bridge_%28Dublin%29_regarding_the_discovery_of_Quaternions_multiplication_by_Sir_William_Rowan_Hamilton.jpg"
          alt="Inscription on Broom Bridge (Dublin) regarding the discovery of Quaternions multiplication by Sir William Rowan Hamilton"
          style="width:60%; height:auto; display:block; margin:0 auto;"
        >
      </a>
      <br>
      By <a href="//commons.wikimedia.org/w/index.php?title=User:Cone83&amp;action=edit&amp;redlink=1" class="new" title="User:Cone83 (page does not exist)">Cone83</a> -
      <span class="int-own-work" lang="en">Own work</span>,
      <a href="https://creativecommons.org/licenses/by-sa/4.0" title="Creative Commons Attribution-Share Alike 4.0">CC BY-SA 4.0</a>,
      <a href="https://commons.wikimedia.org/w/index.php?curid=64867702">Link</a>
    </p>


Using this rule we can find every product between each basis :math:`i, j, k`

.. math::

    iijk = -i \\
    i^2 jk = -i \\
    -jk = -i

By applying a similar method we can build a multiplication table

.. math::

    &\begin{array}{c|c|c|c}
        <x, y> & i & j & k \\
        \hline
        i & -1 &  k & -j  \\
        j & -k & -1 &  i  \\
        k &  j & -i & -1  \\
    \end{array}


(Forshadowing: Notice the symmetry?)

Applying these rules to our unfinished product

.. math::

    Q_1 Q_2 = ae + afi + agj + ahk \\
    bei - bf + bgk - bhj \\
    cej - cfk - cg + chi \\
    dek + dfj - dgi - dh \\
    = (ae - bf - cg - dh) \\
    + (af + be + ch - dg)i \\
    + (ag - bh + ce + df)j \\
    + (ah + bg - cf + de)k  \\
    = Q_3

Voila! We now have a new quaternion :math:`Q_3`! Notice that the product isn't commutative, meaning :math:`Q_1 Q_2 ≠ Q_2 Q_1`.
From the shape of the equations above, you might be tempted to represent the product as a matrix vector product. In fact,
the rules for quaternions are respected in the matrix form of their multiplications as well. Try it yourself! We won't do that here, but this is
a very telling hint if you know the history of vectors. We'll dive deeper into this connection in the next section.

Cross and Dot products: Discovering the vector
-----------------------------------------------

Contrary to what one might think, quaternions were actually discovered before vector algebra and calculus. In fact,
vectors are a direct result from the theory of quaternions. We'll represent each "direction" in our quaternion multiplication by a row
we can try to find some familiar patterns.


.. math::

    Q_1 Q_2 = \\
    (a, b, c, d) (e, f, g, h) = \\
    (ae - bf - cg - dh, \\
    af + be + ch - dg, \\
    ag - bh + ce + df, \\
    ah + bg - cf + de)  \\

See anything familiar? Maybe not. Let's try to separate the quaternion product in similar parts.
The top row is involves all the terms in both quaternions, while the bottom three rows share a similar structure.
Looking at the three bottom rows we see that we can separate them into linear terms and cross terms.
Separating the quaternions into scalar and vector parts we can see the pattern more clearly.

.. math::

    \vec{v_1} = (b, c, d) \\
    \vec{v_2} = (f, g, h) \\

Then our quaternion product becomes

.. math::
    Q_1 Q_2 = \\
    (a, \vec{v_1}) (e, \vec{v_2}) = \\
    (ae - bf - cg - dh, \rightarrow ae - \vec{v_1} \cdot \vec{v_2}\\
    af + be + ch - dg, \rightarrow a \vec{v_2}[1] + e \vec{v_1}[1] + rest\\
    ag - bh + ce + df, \rightarrow a \vec{v_2}[2] + e \vec{v_1}[2] + rest\\
    ah + bg - cf + de) \rightarrow a \vec{v_2}[3] + e \vec{v_1}[3] + rest \\

By isolating the vector parts in the quaternion product we recognise the definition of the dot product in the first row!
We also recognise some linear terms, but what about the rest?
If we just focus on the bottom three rows and what remains after subtracting :math:`e \vec{v_1}` :math:`a \vec{v_2}` we get

.. math::

    ch - dy \\
    df - bh \\
    bg - cf \\

Presenting it in familiar terms

.. math::

    \begin{pmatrix} ch - dg \\ df - bh \\ bg - cf \end{pmatrix} = \begin{pmatrix} b \\ c  \\ d \end{pmatrix} \times \begin{pmatrix} f \\ g  \\ h \end{pmatrix} = \vec{v_1} \times \vec{v_2}

This is the formula of the cross product, and thus the rest is simply the cross product of the vector terms.
Using our newly discovered dot and cross product we can state our quaternion product in the following manner

.. math::

    (a, \vec{v_1}) (e, \vec{v_2}) = \begin{pmatrix} a e - \vec{v_1} \cdot \vec{v_2} \\ e \vec{v_1} + a \vec{v_2} + \vec{v_1} \times \vec{v_2} \end{pmatrix}

This isn't vectors as we know them, but let's see what happens when we make the scalar parts :math:`a` and :math:`e` zero.

.. math::

    V_1 V_2 = (0, \vec{v_1}) (0, \vec{v_2}) = \begin{pmatrix} -\vec{v_1} \cdot \vec{v_2} \\ \vec{v_1} \times \vec{v_2} \end{pmatrix}

By cheating a bit we can find the dot and cross product by means of quaternion multiplication.
We know that the cross product takes in two vectors and the resulting vector is orthogonal to both, following the right hand rule. Thus

.. math::

    V_2 V_2 = (0, \vec{v_2}) (0, \vec{v_1}) = \begin{pmatrix} -\vec{v_1} \cdot \vec{v_2} \\ - \vec{v_1} \times \vec{v_2} \end{pmatrix}

We can then isolate both the dot and cross product by addition and subtraction of the quaternion products :math:`V_1 V_2` and :math:`V_2 V_1`

.. math::

    V_1 V_2 + V_2 V_1 = (-2 \vec{v_1} \cdot \vec{v_1}, 0) = -2 \vec{v_1} \cdot \vec{v_1} \\
    Dot\ Product\ \Rightarrow \vec{v_1} \cdot \vec{v_1} := -\frac{1}{2} ( V_1 V_2 + V_2 V_1 )

.. math::

    V_1 V_2 - V_2 V_1 = (0, 2 \vec{v_1} \times \vec{v_2}) = 2 \vec{v_1} \times \vec{v_2} \\
    Cross\ Product\ \Rightarrow \vec{v_1} \times \vec{v_2} := \frac{1}{2} ( V_1 V_2 - V_2 V_1 )

Which is the formal definition of a dot and cross product by means of quaternion multiplication.
From this you can derive all the fundamental properties of dot and cross products.
This is not a proof, but we've now demonstrated how the dot and cross products emerge from quaternion multiplication.
Hamilton worked with this representation, but later mathematicians decided on the vector notation as less cumbersome
than the complicated quaternion form.

The Quaternion Exponential: Representing rotation
-----------------------------------------------------

Now the question remains: How can we connect quaternions and vector products to rotations?
We'll first have to take a look at the fundamental properties of rotations in 3D.
The difficulty with 3D rotations stem from the fact that there are infinitely many axes you can rotate around, as
opposed to 2D where there is only one.


**Involving Quaternions**



Properties of the Unit Quaternion
==================================

This section will repeat some of the properties we derived for the unit quaternion. We'll also briefly present how you can
use quaternions to represent rotations.



Visualizing the Quaternion Rotations
=====================================

- IMplementere i Python og ha sånne sliders i pywidgets for å justere på hver av de fierr komponentene til et kvaternion


Further reading
================

I can really recommend watching the 3blue1brown video below. This paper written by Sola :cite:t:`sola2017` is excellent, but goes far beyond the scope of this subject.
For more information of the life I recommend reading this post `<https://kathylovesphysics.com/quaternions-are-amazing-and-so-was-william-rowan-hamilton-their-creator/>`_.


.. raw:: html

   <p>YouTube player test</p>

   <center>
    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/zjMuIxRvygQ?si=0l1dZbLth3qO2HHt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
   </center>

To play around with this demo, go to `this site <https://eater.net/quaternions>`_ made by Ben Eater.
