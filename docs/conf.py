# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'bracketology'
copyright = '2020, Kyle Stahl'
author = 'Kyle Stahl'

# The full version, including alpha/beta/rc tags
release = '0.0.9'
version = release

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary', 'numpydoc'] # Should convert numpy or google style docstrings
extensions = ['sphinx.ext.autodoc', 'sphinxcontrib.napoleon'] # Should convert numpy or google style docstrings

autodoc_default_options = {
    'member-order': 'bysource',
    'special-members': '__init__,score,sim',
    'undoc-members': False,
    'exclude-members': '__repr__,run_first_round,run_second_round,run_sweet_sixteen,run_elite_eight,run_final_four,run_championship'
}




# Point to the master.rst
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']