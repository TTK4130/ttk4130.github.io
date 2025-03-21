=================
Quaternions
=================

.. note:: Quaternion convention

    In the following section we will use the Hamiltonian quaternion convention presented in :cite:t:`sola2017`

The problem with Euler angles
=============================

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
        < > & i & j & k
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
    + (ah + bg - cf + de)k = Q_3

Voila! We now have a new quaternion :math:`Q_3`! Notice that the product isn't commutative, meaning :math:`Q_1 Q_2 ≠ Q_2 Q_1`.

Cross and Dot products: Discovering the vector
-----------------------------------------------

The Quaternion Exponential: Quaternions with a twist!
-----------------------------------------------------


Visualizing the Quaternion Rotations
=====================================

- IMplementere i Python og ha sånne sliders i pywidgets for å justere på hver av de fierr komponentene til et kvaternion

Unit Quaternions and Rotations (WIP)
=====================================




Driver å skisserer siden for kvaternioner. Hva tenker du om denne strukturen:

The problem with euler angles -> Forklare singularitet
Intuition: Discovering the Quaternion -> utlede kvaternioner
Dot and cross products: Hvordan vektorer ble oppfunnet fra kvaternioner
The Quaternion Exponential: Quaternions with a twist! -> Forklare hvordan en akserotasjon er relatert til eksponentet av en kvaternion
3D rotations and quaternions -> Sette alt sammen og se hvordan man ender opp med en rotasjon som et kvaternionprodukt & rodrigues formel
Quaternion Properties - > div egenskaper til kvaternioner
Visualizing Quaternions: Implementere kvaternioner i Python og visualisere m pythreejs + vise hvordan man bruker de i SymPy
Further reading: Linke til 3blue1brown og andre nyttige kilder


Further reading
================

I can really recommend watching the 3blue1brown video. The paper written by Sola is very good, but goes far beyond the scope of this subject.



For more information of the life I recommend reading this post `<https://kathylovesphysics.com/quaternions-are-amazing-and-so-was-william-rowan-hamilton-their-creator/>`_.


.. raw:: html

   <p>YouTube player test</p>

   <center>
    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/zjMuIxRvygQ?si=0l1dZbLth3qO2HHt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
   </center>

To play around with this demo, go to `this site <https://eater.net/quaternions>`_ made by Ben Eater.
