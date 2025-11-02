=============
Installation
=============

.. note::

    This guide is under active maintenance. Changes to both dependencies and installation steps may occur.

This installation guide assumes you are using VSCode as your IDE. Some of you may encounter issues. Please
consult the all-knowing web or your preferred ChatGPT-like AI before reaching out about your issue. Errors or bugs
with the provided steps below are directed to `Github <https://github.com/orgs/TTK4130/discussions/2>`_.

Alternative 1: Miniconda
====================================

.. tab-set::

        .. tab-item:: Windows
            :sync: windows

            1. Install Python using Miniconda via `this download page <https://docs.anaconda.com/miniconda/install/#quick-command-line-install>`_
            2. Run the following three commands in a terminal or Anaconda prompt to update conda and create a conda environment

            .. code::

                conda init
                conda update -y conda
                conda create -y --name ttk4130 python=3.11 sympy numpy scipy matplotlib ipython jupyter pythreejs -c conda-forge

            3. Install Visual Studio Code (VSCode) via `the download page <https://code.visualstudio.com/download>`_
            4. Start VSCode and activate your newly created Python environment, ``ttk4130`` (See `this guide on python environments <https://code.visualstudio.com/docs/python/environments>`_)
            5. Install the following list of VSCode extensions (See `this guide on managing VSCode extensions <https://code.visualstudio.com/docs/editor/extension-marketplace>`_): `Jupyter Extension <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>`_, `Python Extension <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_
            6. Open or create a notebook file by opening the Command Palette (Ctrl+Shift+P) and select Jupyter: Create New Jupyter Notebook.

        .. tab-item:: Mac OSX
            :sync: osx

            1. Install Python using Miniconda via `this download page <https://docs.anaconda.com/miniconda/install/#quick-command-line-install>`_
            2. Run the following three commands in a terminal or Anaconda prompt to update conda and create a conda environment

            .. code::

                conda init
                conda update -y conda
                conda create -y --name ttk4130 python=3.11 sympy numpy scipy matplotlib ipython jupyter pythreejs -c conda-forge

            3. Install Visual Studio Code (VSCode) via `the download page <https://code.visualstudio.com/download>`_
            4. Start VSCode and activate your newly created Python environment, ``ttk4130`` (See `this guide on python environments <https://code.visualstudio.com/docs/python/environments>`_)
            5. Install the following list of VSCode extensions (See `this guide on managing VSCode extensions <https://code.visualstudio.com/docs/editor/extension-marketplace>`_): `Jupyter Extension <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>`_, `Python Extension <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_
            6. Open or create a notebook file by opening the Command Palette (Command+Shift+P) and select Jupyter: Create New Jupyter Notebook.

        .. tab-item:: GNU/Linux
            :sync: linux

            1. Install Python using Miniconda via `this download page <https://docs.anaconda.com/miniconda/install/#quick-command-line-install>`_
            2. Run the following three commands in a terminal or Anaconda prompt to update conda and create a conda environment

            .. code::

                conda init
                conda update -y conda
                conda create -y --name ttk4130 python=3.11 sympy numpy scipy matplotlib ipython jupyter pythreejs -c conda-forge

            3. Install Visual Studio Code (VSCode) via `the download page <https://code.visualstudio.com/download>`_
            4. Start VSCode and activate your newly created Python environment, ``ttk4130`` (See `this guide on python environments <https://code.visualstudio.com/docs/python/environments>`_)
            5. Install the following list of VSCode extensions (See `this guide on managing VSCode extensions <https://code.visualstudio.com/docs/editor/extension-marketplace>`_): `Jupyter Extension <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>`_, `Python Extension <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_
            6. Open or create a notebook file by opening the Command Palette (Ctrl+Shift+P) and select Jupyter: Create New Jupyter Notebook.

Troubleshooting
----------------

General tips:

- Make sure you're using the correct installer for your system architecture
- Run the Miniconda installer with admin/sudo privileges if needed
- Manually activate the coda environment in VSCode if it's not detected
- Restart your terminal or VSCode after installation to make sure the changes take effect

Common issues with ``conda`` are documented on the `official Anaconda troubleshooting page <https://docs.anaconda.com/reference/troubleshooting/#conda-command-not-found-on-macos-linux>`_.


Alternative 2: Manual Python Installation
=========================================

The steps for manual installation can vary a lot, hence I will only provide some hints that might help you.

.. tab-set::

        .. tab-item:: Windows
            :sync: windows

            (Being updated)

        .. tab-item:: Mac OSX
            :sync: osx

            Step 1. Install Homebrew Follow the guide on the Homebrew website via this link here(https://brew.sh/).

            Step 2. Install Python and PIP. The current supported Python version is Python 3.11.*.

            :code:`brew install python@3.11`

            Check the install location with

            :code:`brew info python@3.11`

            Which should print out ``/opt/homebrew/bin/python3.11``. We do not need this python version as the default python version on your path, but we just need to know the install location.

            Step 3. Create and activate a virtual environment in a directory (folder) of your choice

            :code:`/opt/homebrew/bin/python3.11 -m venv ./ttk4130_env`

            This will activate the environment

            :code:`source ttk4130_env/bin/activate`

            To exit the virtual environment press ``Ctrl + d``

            Step 4. Install requirements. Make sure you are at the root of this repository and you have activated the virtual environment. Run the following to install the requrirements

            :code:`pip install sympy numpy scipy matplotlib ipython jupyter pythreejs`

            You can now activate your new Python environment in VSCode


        .. tab-item:: GNU/Linux
            :sync: linux

            (Being updated)


Software Versions
=================

This website was built with the following software versions. If you are encountering compatability, issues this
list can be used as a reference:

.. jupyter-execute::

   import platform
   platform.python_version()
   
.. jupyter-execute::

   import IPython
   IPython.__version__

.. jupyter-execute::

   import jupyter_sphinx
   jupyter_sphinx.__version__

.. jupyter-execute::

   import matplotlib
   matplotlib.__version__

.. jupyter-execute::

   import notebook
   notebook.__version__

.. jupyter-execute::

   import numpy
   numpy.__version__

.. jupyter-execute::

   import plotly
   plotly.__version__

.. jupyter-execute::

    import pandas
    pandas.__version__

.. jupyter-execute::

   import pythreejs._version
   pythreejs._version.__version__

.. jupyter-execute::

   import sphinx_book_theme
   sphinx_book_theme.__version__

.. jupyter-execute::

   import scipy
   scipy.__version__

.. jupyter-execute::

   import sphinx
   sphinx.__version__

.. jupyter-execute::

   import sphinx_material
   sphinx_material.__version__

.. jupyter-execute::

   import sphinx_togglebutton
   sphinx_togglebutton.__version__

.. jupyter-execute::

   import sphinx_design
   sphinx_design.__version__

.. jupyter-execute::

   import sympy
   sympy.__version__

.. jupyter-execute::

   import jupyterlite_sphinx
   jupyterlite_sphinx.__version__

.. jupyter-execute::

   import jupyterlite_pyodide_kernel
   jupyterlite_pyodide_kernel.__version__
