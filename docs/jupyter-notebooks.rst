=======================================
Quick intro to Jupyter Notebooks
=======================================

.. note::

    We highly recommend using Jupyter notebooks for your coding assignments. This will allow your so seamlessly integrate code, plots, text and LaTeX
    into a single document.

This is a quick intro(duction) to how to use Python in a Jupyter Notebook. Jupyter Notebook is an open source web application you can use to create documents that contain code, plots, LaTeX equations and text
in a single document. Jupyter notebooks support a many different scripts and programming languages, such as Python, JavaScript, HTML5, CSS, Julia and R. This makes it a powerful tool for creating interactive multi-media documents.
Different programming languages use different kernels. This course book will use a Python 3 kernel.

.. note::

     If you need a refresher on Python, we recommend reading the `tutorial section of the official Python documentation <https://docs.python.org/3/tutorial/>`_.

Starting Jupyter
-----------------

If you're using VSCode, the Jupyter extension will automatically detect any Jupyter notebook with the file extension ``.ipynb``.
If you prefer the browser application you can start the Jupyter notebook application by running the following command in your
terminal or command prompt:

.. code-block::

    jupyter notebook

This will open your browser where you can create a new notebook or open existing notebooks in your current directory (folder).
Jupyter notebooks are organized with cells of different flavours. You can write Python code in the ``code cell``, which is followed
by a result cell with the program output after the cell has been run. The ``text cell`` supports static content like text written in `Markdown <https://en.wikipedia.org/wiki/Markdown>`_.
Markdown supports different text formatting such as LaTeX notation, rendering :code:`$\frac{1}{a^2}$` into :math:`\frac{1}{a^2}`. You can change
the type of cell using the drop-down menu on the toolbar above your notebook.

Shortcuts
------------
Here's a short list of useful keyboard shortcuts in Jupyter notebooks

Command Mode (Blue border):

- A: Insert cell above
- B: Insert cell below
- X: Cut selected cell(s)
- D D: Delete selected cell(s)
- Y: Change cell to code
- M: Change cell to markdown
- Shift + Up/Down: Select multiple cells
- Shift + M: Merge selected cells

Edit Mode (Green border):

- Shift + Enter: Run cell and select below
- Ctrl + Enter: Run cell
- Ctrl + Shift + -: Split cell at cursor

Both Modes:

- Esc: Enter command mode
- Enter: Enter edit mode
- H: Show all shortcuts

Restarting your kernel
-----------------------
Sometimes your code might get stuck in an endless loop. You might also like to clear all your workspace variables.
We can solve this by clicking the ``Kernel`` menu item ``Interrupt`` and ``Restart``.

Magic Commands
---------------

There are special commands that only work in a Jupyter notebook environment. Magic commands are preceded by ``%`` or
``%%``. The magic command :code:`lsmagic` lists all available commands

.. jupyter-execute::

    %lsmagic

You can list a cheat sheet with :code`quickref`

.. jupyter-execute::

    %quickref

:code:`who` can list all the variables in your current notebook. :code:`whos` is more detailed.

.. jupyter-execute::

    name = "linus"

    %whos

We can also list the variables of a specific data type

.. jupyter-execute::

    %who str

Another useful command is :code:`timeit`, which can time the execution of a Python statement or expression

.. jupyter-execute::

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)

    %timeit fib(1000)

Details about any Python object can be found by adding ``?`` to the end of a function or an object

.. jupyter-execute::

    round?

Exporting a Jupyter Notebook
-----------------------------

Exporting a Jupyter notebook to other formats requires ``nbconvert`` to be installed. ``nbconvert`` can be installed via the `official nbconvert installation instructions <https://nbconvert.readthedocs.io/en/latest/install.html#installation>`_.
The simplest way to export your notebook is to save your notebook to a HTML file and print the webpage as a PDF. This often yields
suboptimal documents. We recommend that you download the notebook as a ``PDF via LaTeX`` via the graphical interface. Optionally,
you can convert the notebook to a PDF or a WebPDF using the following commands. If you're struggling to install a LaTeX compiler,
WebPDF is often the easiest and most reliable method.

Using LaTeX:

.. code-block::

    jupyter nbconvert your_notebook.ipynb --to pdf

Using WebPDF:

.. code-block::

    jupyter nbconvert your_notebook.ipynb --to webpdf

Learn more about Jupyter
-------------------------

There are many resources online for learning more about Jupyter. `This tutorial <https://realpython.com/jupyter-notebook-introduction/>`_ by RealPython is an example.
YouTube hosts a great number of videos on the topic as well. The one listed below is a good started to learn the basics.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/jZ952vChhuI?si=MV5zJZdcK4ghVhCw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>