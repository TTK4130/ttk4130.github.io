# TTK4130 Course Book

To read the course content and installation guide go to [the deployment of this website](https://ttk4130.github.io). This documentation relates to editing the webpage and not the course work.

# Website How-to's

## Installing and setting up the environment 

### MacOS

Step 1. Install Homebrew
Follow the guide on the hombrew website via [this link here](https://brew.sh/)(https://brew.sh/).

Step 2. Install Python and PIP
The current supported Python version is Python 3.11.*. 
```
brew install python@3.11
```
Check the install location with 
```
brew info python@3.11
```
Which should print out `/opt/homebrew/bin/python3.11`. We do not need this python version as the default pythn version on your path, but we just need to know the install location.

Step 3. Create and activate a virtual environment
Open the terminal and clone this repo with
```
git clone git@github.com:TTK4130/ttk4130.github.io.git
```
If git is not installed run `brew install git`. If you don't have set up any SSH-keys with github, follow [this guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh). Navigate to the cloned git repository and create a new environment with (adjust according to your python install location)
```
/opt/homebrew/bin/python3.11 -m venv ./env
```
This wil create the virtual environment we will use when building this site. To activate it run
```
source env/bin/activate
```
To exit the virtual environment press `Ctrl + d`

Step 4. Install requirements
Make sure you are at the root of this repository and you have activated the virtual environment. Run the following to install the requrirements
```
pip install -r docs/requirements.txt
```
Step 4. Build the website
To build the website go to the `docs` subfolder with `cd docs`. Then run
```
make
```
Which should generate an output similar to this
```
Running Sphinx v8.0.2
loading translations [en]... done
loading pickled environment... done
building [mo]: targets for 0 po files that are out of date
writing output... 
building [html]: targets for 0 source files that are out of date
updating environment: 0 added, 0 changed, 0 removed
reading sources... 
looking for now-outdated files... none found
no targets are out of date.
build succeeded.

The HTML pages are in _build/html.
```
To view the built website locally this from the docs direcotry
```
open _build/html/index.html 
```
 
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



## How to build the site

## Acknowledgements

This site is heavily inspired by the Jason K. Moore's book and course "Learn Multibody Dynamics" taught at TU Delft.

## References

Moore, J. K., “Learn Multibody Dynamics”, 2022, https://moorepants.github.io/learn-multibody-dynamics/
