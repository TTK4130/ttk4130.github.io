=============================
Assignment 8 - Bond Graphs II
=============================

.. note::

    Submit your assignment as a single PDF, including plots and source code (if any).
    We expect academic honesty. Collaboration is encouraged, but must be declared. Any use of AI must be declared along with any other sources used.
    This is not an exam. Do your best and show that you put in effort and the assignment will be approved.

In this assignment we will develop bond graphs for three different systems. A mechanical system, an electrical system and a hydraulic system.

Problem 1 - Pendulum on an oscillator
-------------------------------------

.. figure:: ./figures/assignment_8/pendulum_osc.png
    :width: 100%
    :align: center
    :name: assignment_8_pendulum

    Pendulum on a vertical oscillator.

We will revisit the oscillating pendulum one last time. 
This time we will use bond graph to model the system.

Figure  :numref:`assignment_8_pendulum` shows a sktch of the system. 
A pendulum with a point mass :math:`m_2` is attached to a mass :math:`m_1` that can oscillate along a vertical axis. 
The pendulum rod has a length :math:`L` and the rod can be considered mass-less 
(i.e. the pendulum can be considered as a point mass at the end of a mass-less rod).

The oscillating mass is connected to a stationary construction through a spring with stiffness :math:`k`. 
The vertical position :math:`z` of the mass is defined such that :math:`z = 0` when the spring is in its neutral position.
The angular displacement of the pendulum rod is :math:`\theta`, as shown in the figure. 
For simplicity we also constrain body one to only move up or down, i.e no movement along the :math:`y_0` or :math:`z_0` axis.

.. admonition:: Tasks
    
    a. Draw a bond graph for the system, as described above. Include gravity force on the two masses.

    .. hint::
        :class: dropdown
        
        A good starting point is to place a 1-junction for each relevant velocity.
        In this case, you will need a velocity representing the vertical movement of the oscillating mass, and two 1-junctions representing the horizontal velocity and the vertical velocity of the pendulum mass.
        In addition, you will need a 1 junction for :math:`\dot{\theta}` because the vertical and horizontal velocity of the point mass on the pendulum is a function of :math:`\dot{\theta}`.
        You then need to establish a relationship between them using MTF-elements and 0-junctions.
    
    b. Now include linear friction on the motion of oscillating mass and the pendulum hinge.

    c. Assume now that the mass at the end of the pendulum is not a point mass but a sphere with mass :math:`m_2` and moment of inertia of :math:`J_2`. Update the bond graph to account for this.


Problem 2 - Electrical circuit with a battery
---------------------------------------------

.. figure:: ./figures/assignment_8/electrical.png
    :width: 100%
    :align: center
    :name: assignment_8_electrical

    Electrical circuit with a battery.

Figure  :numref:`assignment_8_electrical` show an electrical circuit powered by voltage source :math:`u(t)`. 
The task is to develop a bond graph for this system. 
The parameters for the two resistors, two capacitors and the inductance, are :math:`R_1` and :math:`R_2`, :math:`C_1` and :math:`C_2`, and :math:`L` respectively.


.. admonition:: Task
    
    Make a bond graph for the circuit.


Problem 3 - Single acting spring return hydraulic actuator
----------------------------------------------------------

.. figure:: ./figures/assignment_8/hydraulic.png
    :width: 100%
    :align: center
    :name: assignment_8_hydraulic

    A single acting spring return hydraulic actuator powered by a hydraulic pump.

Figure  :numref:`assignment_8_hydraulic` shows a hydraulic system were fluid can be pumped from a reservoir and into to single acting hydraulic actuator, or back to the reservoir via a controllable valve.
The opening area of the valve can be controlled though the signal :math:`u(t)` to return fluid to the reservoir and hence reduce the pressure on the hydraulic actuator.
When the pressure is low enough, the spring will return the hydraulic actuator piston back to the position :math:`x = 0`.

.. admonition:: Task
    
    Draw a bond graph for this system where :math:`P_a`  is the atmospheric pressure.