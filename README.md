# Table of Contents extension for Jupyter

Generates floating table of contents inside your notebook from the heading cells.
Adds a button to the toolbar to toggle the floating table of contents.

You can install this extension as Python Packages. The details are shown in [Distributing Jupyter Extensions as Python Packages](https://jupyter-notebook.readthedocs.org/en/stable/examples/Notebook/rstversions/Distributing%20Jupyter%20Extensions%20as%20Python%20Packages.html).

# How to install

## Install the python package

The package have not been uploaded to PyPI yet, so you should clone this repository and install it using setuptools

```
$ git clone https://github.com/yacchin1205/ipython_extensions.git
$ cd ipython_extensions
$ python3 setup.py sdist
$ pip3 install dist/nbextension_toc-0.1.tar.gz
```

## Install and Enable the extension in the package

You can install and enable the extension using `jupyter nbextension` command.

```
$ jupyter nbextension install --py nbextension_toc
$ jupyter nbextension enable --py nbextension_toc
```

After these commands, run `jupyter notebook` command. Then the *Table of Contents* button is shown in tool bar.
