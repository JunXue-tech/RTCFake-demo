# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'offline-online-dataset'
copyright = '2025, none'
author = 'none'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_theme = 'basic'

html_theme_options = {
    'nosidebar': True,  
    'body_max_width': '1400px',  
    'body_min_width': '100%',  
    'stickysidebar': False,  
}

html_sidebars = {}

html_use_opensearch = False

html_search_options = {'enabled': False}

html_css_files = ['css/custom.css']

html_static_path = ['_static']

html_copy_source = True

html_extra_path = ['CNAME']

def setup(app):
    app.add_css_file('css/custom.css')