## System Imports
import os
import sys


## Application Imports


## Library Imports
import sphinx_rtd_theme


# Extra paths
sys.path.insert(0, os.path.abspath('_ext'))


# -- Project information -----------------------------------------------------

project = 'CodeShaper'
copyright = '2022, CodeShaper'
author = 'CodeShaper'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'myst_parser',
	'page_read_time'
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

html_logo = "_static/img/logos/codeshaper/logo-only.png"
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_context = {
  'display_github': True,
  'github_user': 'OriDevTeam',
  'github_repo': 'CodeShaperDocs',
  'github_version': 'master/docs/',
}

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'collapse_navigation': False
}

# CSS Files
html_css_files = [
	'css/custom.css',
	'css/algolia.css',
	'https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.css',
	'css/rtd_dark.css',
]

# Javascript files
html_js_files = [
    'js/external-hyperlinks.js'
]

# reST Options
rst_prolog = """
.. include:: <s5defs.txt>

"""


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# Pygments configuration
pygments_style = "vs"

# Page Read Time configuration
page_read_time = True
