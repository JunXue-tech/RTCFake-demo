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

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
html_theme_options = {
    'show_powered_by': False,
    'show_related': False,
    'sidebar_width': '300px',
    'page_width': '1200px',
    'fixed_sidebar': False,
    'gray_1': '#fff',
    'gray_2': '#fff',
    'gray_3': '#f8f8f8',
    'text': '#000000',
    'link': '#000000',
    'link_hover': '#333333',
    'sidebar_link': '#000000',
    'sidebar_link_underscore': '#666666',
    'sidebar_list': '#000000',
    'note_bg': '#f5f5f5',
    'note_border': '#e0e0e0',
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/custom.css']
html_copy_source = True
html_static_path = ['_static']
html_extra_path = []
def setup(app):
    app.add_css_file('css/custom.css')
html_use_opensearch = True
