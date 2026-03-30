# TTK4130 Course Book

To read the course content and installation guide go to [the deployment of this website](https://ttk4130.github.io). This README relates to developing and building the page.

# Website How-to's
## Installing and setting up the environment

### macOS

**Step 1 — Install Homebrew**

Follow the guide on the Homebrew website via [this link](https://brew.sh/).

**Step 2 — Install uv**

[uv](https://docs.astral.sh/uv/) is the package manager used for this project.
Install it with Homebrew:
```bash
brew install uv
```

**Step 3 — Install system dependencies**

Install Graphviz and Pandoc, which are required during the documentation build:
```bash
brew install graphviz pandoc
```

**Step 4 — Clone the repository**
```bash
git clone git@github.com:TTK4130/ttk4130.github.io.git
```

If git is not installed run `brew install git`. If you have not set up SSH keys
with GitHub, follow [this guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

**Step 5 — Install dependencies**

Navigate to the root of the cloned repository and run:
```bash
uv sync
```

This creates a virtual environment and installs all required packages
automatically. You do not need to create or activate a virtual environment
manually — uv manages this for you.

**Step 6 — Build the website**

From the root of the repository run:
```bash
uv run make -C docs html
```

Which should produce output similar to:
```
Running Sphinx v8.1.3
loading translations [en]... done
building [html]: targets for 0 source files that are out of date
updating environment: 0 added, 0 changed, 0 removed
no targets are out of date.
build succeeded.

The HTML pages are in _build/html.
```

To view the built website locally run:
```bash
open docs/_build/html/index.html
```

**Step 7 — Install pre-commit hooks**

This project uses pre-commit hooks to automatically format and lint `.rst`
files before each commit. Install them with:
```bash
uv run pre-commit install
```

You only need to do this once. After this, formatting and linting run
automatically every time you run `git commit`.
To view the built website, first launch a local http server with python at port 8000 in the docs directory
```
python -m http.server 8000
```
Then access the webserver at [http://0.0.0.0:8000/_build/html/](http://0.0.0.0:8000/_build/html/) to view the website.
 
### Windows
To install Python follow [this guide](https://learn.microsoft.com/en-us/windows/python/beginners) (all steps may not be necessary) and follow the steps above for MacOS. Some syntax may vary. 

## How to edit

The site is written in RetructuredText.

### Tabs and grouped tabs

Tabs can easily be created by:

```
.. tab-set::

      .. tab-item:: Windows
      
         Something is here 

      .. tab-item:: Mac OSX
    
         Something is here 

      .. tab-item:: GNU/Linux
         
         Something is here 

```

## Documentation tooling

The website uses three tools to keep the `.rst` source files consistent and correct. 

### `docstrfmt` formatter

[`docstrfmt`](https://github.com/LilSpazJoekp/docstrfmt?tab=readme-ov-file) is a tool for automatically formatting Sphinx flavored reStructuredText in files and Python docstrings. This makes it easier to collaborate, as each file is enforced to follow the same formatting, thereby reducing the cognitive load of editing. It fixes indentations, line lengths and spacing around directives and so on. It runs automatically on every `git commit` via pre-commit, so formatting differences never make it into version control.

### `rstcheck` syntax linter

[`rstcheck`](https://rstcheck.readthedocs.io/en/latest/) checks the `.rst` files and checks that the reStructuredText syntax is valid. This is to make sure we do not push something that would not build and deploy correctly. It reports problems such as malformed directives, broken code blocks or markup that Sphinx would fail to build. Like dosctrfmt, it runs on every commit. This is to filter unnecessary commits with "fix broken build" that litter the history.

### (Optional) lextudio reStructuredText (VSCodeExtension)

The [reStructuredText extension](https://docs.lextudio.com/restructuredtext/) is an optional extension you can use to improve the editing experience in VSCode. It supports syntax highlighting and reports linting errors from rstcheck and much more. It does not change your files, but reports any issues before you reach the commit stage. 

## How to build the site

## Acknowledgements

This site is heavily inspired by the Jason K. Moore's book and course "Learn Multibody Dynamics" taught at TU Delft.

## References

Moore, J. K., “Learn Multibody Dynamics”, 2022, https://moorepants.github.io/learn-multibody-dynamics/
