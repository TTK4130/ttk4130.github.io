=================
Quaternions (WIP)
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
    :file: _includes/animation/threejs_gimbal_lock.html


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


To play around with quaterions, go to `this site <https://eater.net/quaternions>`_ made by Ben Eater.
