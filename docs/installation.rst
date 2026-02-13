=============
Installation
=============

.. note::

    This guide is under active maintenance. Changes to both dependencies and installation steps may occur.

This installation guide assumes you are using VSCode as your IDE. Some of you may encounter issues. Please
consult the all-knowing web or your preferred ChatGPT-like AI before reaching out about your issue. Errors or bugs
with the provided steps below are directed to `Github <https://github.com/orgs/TTK4130/discussions/2>`_.

Alternative 1 (best): Pixi
====================================

.. tab-set::

        .. tab-item:: Windows
            :sync: windows

            1. Install Pixi via `this link here <https://pixi.prefix.dev/latest/installation/>`_ (https://pixi.prefix.dev/latest/installation/)
            2. Set up the course environment
            
               * Download the `code handouts <https://github.com/TTK4130/code-handouts/>`_ (https://github.com/TTK4130/code-handouts/) repository to get the dependencies, or just download the dependency file `here <https://github.com/TTK4130/code-handouts/blob/main/pixi.toml>`_.
               * Navigate to the directory (folder) that contains the :code:`pixi.toml` file, e.g. :code:`path/to/code-handouts/`
               * Run :code:`pixi install` to install all the dependencies in one command
            
            3. Install Visual Studio Code (VSCode) via `the download page <https://code.visualstudio.com/download>`_ (https://code.visualstudio.com/download)
            4. Use Jupyter notebooks

               **Option A**: Command Line (easiest)

               * Run :code:`pixi run jupyter` from the terminal (must be same folder as :code:`pixi.toml`) to launch Jupyter notebook
            
               **Option B**: VSCode integration
               
               * In VSCode, open the Command Palette (Ctrl + Shift + P)
               * Choose "Python: Select Interpreter"
               * Choose the interpreter at :code:`Scripts\python.exe`
               * Install the following list of VSCode extensions (See `this guide on managing VSCode extensions <https://code.visualstudio.com/docs/editor/extension-marketplace>`_): `Jupyter Extension <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>`_, `Python Extension <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_

        .. tab-item:: Mac OSX
            :sync: osx

            1. Install Pixi via `this link here <https://pixi.prefix.dev/latest/installation/>`_ (https://pixi.prefix.dev/latest/installation/)
            2. Set up the course environment
            
               * Download the `code handouts <https://github.com/TTK4130/code-handouts/>`_ (https://github.com/TTK4130/code-handouts/) repository to get the dependencies, or just download the dependency file `here <https://github.com/TTK4130/code-handouts/blob/main/pixi.toml>`_.
               * Navigate to the directory (folder) that contains the :code:`pixi.toml` file, e.g. :code:`path/to/code-handouts/`
               * Run :code:`pixi install` to install all the dependencies in one command
            
            3. Install Visual Studio Code (VSCode) via `the download page <https://code.visualstudio.com/download>`_ (https://code.visualstudio.com/download)
            4. Use Jupyter notebooks

               **Option A**: Command Line (easiest)

               * Run :code:`pixi run jupyter` from the terminal (must be same folder as :code:`pixi.toml`) to launch Jupyter notebook
            
               **Option B**: VSCode integration
               
               * In VSCode, open the Command Palette (Ctrl + Shift + P)
               * Choose "Python: Select Interpreter"
               * Choose the interpreter at :code:`.pixi/envs/default/bin/python`
               * Install the following list of VSCode extensions (See `this guide on managing VSCode extensions <https://code.visualstudio.com/docs/editor/extension-marketplace>`_): `Jupyter Extension <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>`_, `Python Extension <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_

        .. tab-item:: GNU/Linux
            :sync: linux

            1. Install Pixi via `this link here <https://pixi.prefix.dev/latest/installation/>`_ (https://pixi.prefix.dev/latest/installation/)
            2. Set up the course environment
            
               * Download the `code handouts <https://github.com/TTK4130/code-handouts/>`_ (https://github.com/TTK4130/code-handouts/) repository to get the dependencies, or just download the dependency file `here <https://github.com/TTK4130/code-handouts/blob/main/pixi.toml>`_.
               * Navigate to the directory (folder) that contains the :code:`pixi.toml` file, e.g. :code:`path/to/code-handouts/`
               * Run :code:`pixi install` to install all the dependencies in one command
            
            3. Install Visual Studio Code (VSCode) via `the download page <https://code.visualstudio.com/download>`_ (https://code.visualstudio.com/download)
            4. Use Jupyter notebooks

               **Option A**: Command Line (easiest)

               * Run :code:`pixi run jupyter` from the terminal (must be same folder as :code:`pixi.toml`) to launch Jupyter notebook
            
               **Option B**: VSCode integration
               
               * In VSCode, open the Command Palette (Ctrl + Shift + P)
               * Choose "Python: Select Interpreter"
               * Choose the interpreter at :code:`.pixi/envs/default/bin/python`
               * Install the following list of VSCode extensions (See `this guide on managing VSCode extensions <https://code.visualstudio.com/docs/editor/extension-marketplace>`_): `Jupyter Extension <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>`_, `Python Extension <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_




Troubleshooting
----------------

General tips:

- Make sure you're using the correct installer for your system architecture
- Restart your terminal or VSCode after installation to make sure the changes take effect

Alternative 2 (old): Miniconda 
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
