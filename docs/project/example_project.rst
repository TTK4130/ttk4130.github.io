Example Project: Bicycle
========================

For the example project I chose to model and examine a bicycle. I chose
this because most of us have an intuition of how bicycles should work
and move, yet few of us actually understand the underlying dynamics. I
therefore set the goal of examining different ways of modelling a
bicycle, how different parameters affect the behaviour of the bicycle
and lastly what makes a bicycle stable.

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

.. jupyter-execute::

    import pythreejs as pj
    import sympy as sm

    from IPython.display import  display
    box = pj.BoxGeometry(width=4, height=4, depth=4)
    box



Testing different bicycle parameters
------------------------------------

.. image:: https://imgs.xkcd.com/comics/timeline_of_bicycle_design.png

A good place to start to look for parameters is looking for similar
components’ specifications online through different stores or vendors.

Looking at bike wheels etc
https://www.sykkelkomponenter.no/sykkeldeler/el-sykkel-deler/hjul/bakhjul-for-skivebrems/m-wave-4-30-e-mtb-12-x-148mm-boost-29-bakhjul

The anatomy of a bicycle
------------------------

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

Animation
---------

.. note::

    Please look at the animation page :ref:`3D Visualization and Animation` for an
    introduction to how you make animations in Python.

