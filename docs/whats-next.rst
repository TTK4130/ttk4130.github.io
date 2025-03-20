What's Next?
============

In this course, we’ve shown you how to use Python and SymPy to describe and simulate dynamic systems. Now that you’ve learned the basics, you might be wondering: **How do I take these models and apply them in the real world?** This is a big step beyond what we’ve covered here, but we can guide you in the right direction.

From Equations to Execution
===========================

When it comes to deploying models in real-world applications, compiled languages (like C++) are often preferred. Why? Because they’re much faster and better suited for real-time or safety-critical systems. For example, C++ is widely used in robotics, aerospace, and the automotive industry because of its speed and versatility.

Here are some important C++ libraries used in these fields:

- **ROS (Robot Operating System)**: A set of tools and libraries that help build robotic applications. ROS is popular in both research and industry, and C++ is often used to handle the core functions. `<https://www.ros.org/>`_
- **Eigen**: A library for performing linear algebra operations, which is essential for robotics and computer vision, like manipulating matrices and solving systems of equations. `<https://eigen.tuxfamily.org/>`_
- **OpenCV**: A library for computer vision, enabling tasks like image processing and visual data analysis. `<https://opencv.org/>`_
- **OMPL (Open Motion Planning Library)**: A library that provides motion planning algorithms, used in robotics to help robots figure out how to move efficiently and safely. `<https://ompl.kavrakilab.org/>`_
- **Ceres Solver**: A powerful tool for optimization problems, such as improving the accuracy of camera calibration or other complex computations. `<http://ceres-solver.org/>`_

These tools allow you to take models you’ve created and apply them in real-time systems, from robots moving in dynamic environments to autonomous vehicles navigating safely.

Where Your Models Go
======================

Taking equations of motion and applying them to real-world systems often involves complex processes like state estimation and control. These are critical for several industries, including:

- **Robotics**: Robots need to plan their movements and adjust in real-time as they interact with their environment. Libraries like **Eigen**, **OMPL**, and **pybullet** help with this.
- **Autonomous Vehicles**: Self-driving cars rely on precise state estimation to navigate safely. Libraries like **Ceres Solver** and **ROS** help make real-time decisions based on sensor data.
- **Aerospace**: For flight control systems, **GNAT** and **Apex Ada** (Ada) are commonly used to ensure safety and reliability in real-time applications.
- **Manufacturing**: In factories, robots and automated systems need to perform precise tasks. Tools like **ROS**, **Eigen**, and **OMPL** are used to optimize movement and decision-making.

These tools enable the transition from theoretical models to real-world applications.

Code Generation: Simplifying the Transition
============================================

A more modern approach to deploying models is code generation, where symbolic mathematical models are automatically converted into optimized, deployable code. A great example of this is **SymForce** `<https://symforce.org/>`_:

    "SymForce is a fast symbolic computation and code generation library for robotics applications like computer vision, state estimation, motion planning, and controls. It combines the flexibility of symbolic math with the speed of highly optimized code in C++ or other target languages."


Using tools like SymForce, you can easily turn complex mathematical models into efficient code that’s ready for real-world systems, without manually coding every detail.

Conclusion: Your Next Steps
===========================

This course has given you the foundational tools to model and simulate dynamic systems. But remember, this is just the beginning. As you continue your learning, you’ll find ways to apply what you’ve learned to real-world systems.
The journey from simulation to real-world application is not just about understanding theory, but also about mastering the tools and languages that are used in industry. We hope this course has served as a solid foundation for your development as a skilled engineer.

Good luck!
