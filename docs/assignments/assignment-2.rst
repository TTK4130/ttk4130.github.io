========================================
Assignment 2 - 2D Kinetics
========================================

.. note::

    Submit your assignment as a single PDF.
    We expect academic honesty. Collaboration is encouraged, but must be declared. Any use of AI must be declared along with any other sources used.
    This is not an exam. Do your best and show that you put in effort and the assignment will be approved.


Problem 1 - Rotation transformations in 2D
==========================================

In this problem, we will study coordinate transformation in the two reference frames shown (in terms of their unit vectors) in the figure below.

.. figure:: figures/ned_and_ship_frames.svg
   :scale: 60%
   :align: center

   The orientation of the unit vectors of the NED-frame and the :math:`s`-frame.

.. admonition:: Tasks

    a) Express the unit vectors :math:`\mathbf{i_s}` and :math:`\mathbf{j_s}` of the :math:`s`-frame in terms of the unit vectors :math:`\mathbf{i_N}` and :math:`\mathbf{j_N}` of the NED-frame. Refer to the figure above for support.

    b) Consider a vector

       .. math::

          \mathbf{v} = \xi_1 \mathbf{i_s} + \xi_2 \mathbf{j_s}

       This vector can also be expressed through the unit vectors of the NED-frame as :math:`\mathbf{v} = \chi_1 \mathbf{i_N} + \chi_2 \mathbf{j_N}`. Your task is to express :math:`\chi_1` and :math:`\chi_2` as functions of :math:`\xi_1`, :math:`\xi_2`, and :math:`\psi`.

    c) A more compact and practical way of transforming the coordinates of vectors between the component directions of the two reference frames (NED-frame and :math:`s`-frame) is to use coordinate vector notation and rotation matrices. Based on the results from the previous task, find the 2×2 matrix :math:`\mathbf{R}^N_s(\psi)` that is defined such that

       .. math::

          \mathbf{v}^N =
          \begin{bmatrix} \chi_1 \\ \chi_2 \end{bmatrix}
          = \mathbf{R}^N_s(\psi)
          \begin{bmatrix} \xi_1 \\ \xi_2 \end{bmatrix}
          = \mathbf{R}^N_s(\psi) \mathbf{v}^s

Problem 2 - Barge with crane
=============================

:numref:`fig:lekter` shows a barge located some distance from a stationary platform. The stationary platform has a fixed reference frame attached to it, referred to as the NED-frame (for North, East, Down), whose axes are pointing northwards, eastwards, and downwards toward the center of the Earth.

.. _fig:lekter:

.. figure:: figures/lekter.pdf
   :width: 50%
   :align: center

   A barge with a crane.

We also attach a reference system :math:`x_s, y_s, z_s` (i.e., the :math:`s`-frame) to the barge, as shown in the figure. The z-axis is pointing downwards in accordance with the right-hand rule. The location of the origin of the :math:`s`-frame relative to the origin of the NED-frame is given as:

.. math::

    \mathbf{r}_{s/n} = n \mathbf{i}_{n} + e \mathbf{j}_{n} + d \mathbf{k}_{n}

The position of the crane on the barge is given as:

.. math::

    \mathbf{r}_{c/s} = a \mathbf{i}_{s} + b \mathbf{j}_{s} + c \mathbf{k}_{s}

The angle between the :math:`x_s`-axis and the :math:`x_c`-axis is :math:`\alpha`.

Finally, the distance from the origin of the crane-fixed reference frame to the tip of the crane is :math:`l`.

.. note::

   When we ask for a vector in this problem, your answer should be in the form:

   .. math::

      \mathbf{r} = g \mathbf{i}_{k} + h \mathbf{j}_{k}

   or:

   .. math::

      \mathbf{r}^k =  \begin{bmatrix} g \\ h \end{bmatrix}

   where we need expressions for :math:`g` and :math:`h`.

   **The expressions should be formulated in terms of the parameters** :math:`(a, b, c, l)` **, the variables** :math:`(\psi, \alpha, n, e, d)` **and their time derivatives** :math:`(\dot{\psi}, \dot{\alpha}, \dot{n}, \dot{e}, \dot{d})`.


.. admonition:: Tasks

    a) Find an expression for the position of the origin of the barge-fixed reference frame relative to the origin of the NED-frame expressed in terms of the barge-fixed reference frame.

    b) Find an expression for the position of the tip of the crane relative to the origin of the :math:`s`-frame as a function of :math:`\alpha`. Express the vector in terms of the :math:`s`-frame.

    c) Find an expression for the position of the tip of the crane relative to the origin of the NED-frame. Express the vector in terms of the NED-frame.

    d) What is the angular velocity of the crane when the barge has a turn rate of :math:`\dot{\psi}` and the crane base is rotating at the rate :math:`\dot{\alpha}`?

    e) The vessel has a forward velocity :math:`u` and a sideways velocity of :math:`v` relative to the inertial reference frame (the NED-frame). Find expressions for :math:`\dot{n}` and :math:`\dot{e}` (i.e., the time derivatives of the components in the equation above).

    f) What is the linear velocity of the crane tip? The vessel still moves with a forward velocity component :math:`u` and a sideways velocity component :math:`v`, and in addition, it has an angular speed of magnitude :math:`\dot{\psi}`. The crane has an angular speed with magnitude :math:`\dot{\alpha}`. You can express the answer in terms of the NED-frame.
