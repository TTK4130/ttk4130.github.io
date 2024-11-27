-----------
SymPy Live
-----------

Here you can try SymPy in your browser. This feature is experimental and might not support every browser.

.. replite::
   :kernel: python
   :theme: JupyterLab Dark
   :width: 100%
   :height: 600px

   import sympy as sm
   from sympy import symbols, expand
   sm.init_printing(use_latex='mathjax')
   x, y = symbols('x y')
   expand((x + y)**3)

