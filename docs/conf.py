# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TTK4130'
author = 'Tord Natlandsmyr & Børge Rokseth'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_togglebutton',
    'sphinx.ext.githubpages',
    'sphinx_design',
    'jupyter_sphinx',
    'jupyterlite_sphinx',
    'sphinxcontrib.bibtex',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.graphviz',
    'sphinx.ext.imgconverter',
    'sphinx.ext.todo'
]

master_doc = 'index'
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
bibtex_bibfiles = ['refs.bib']

graphviz_output_format = 'svg'
math_number_all = True

intersphinx_mapping = {
    'sympy': ('https://docs.sympy.org/latest/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'py3js': ('https://pythreejs.readthedocs.io/en/stable', None)
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_title = 'Modelling and Simulation TTK4130'
html_static_path = ['_static']
html_js_files = ['lorenz.js']
html_favicon = "_static/lorenz.png"
html_theme_options = {
    "repository_url": "https://github.com/TTK4130/ttk4130.github.io",
    "repository_branch": "main",
}

# The URL which points to the root of the HTML documentation.
# It is used to indicate the location of document like canonical_url
html_baseurl = 'https://ttk4130.github.io'
