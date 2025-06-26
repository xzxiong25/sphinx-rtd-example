
# Sphinx configuration file

import os
import sys
from datetime import datetime

# Add project directory to system path
sys.path.insert(0, os.path.abspath('../../../sphinx-rtd-example'))

# Project information
project = 'Calculator API Documentation'
copyright = f'{datetime.now().year}, Example Company'
author = 'AI Developer'
version = '1.0'
release = '1.0.0'

# Extensions
extensions = [
    'sphinx.ext.autodoc',    # Automatically generate docs from docstrings
    'sphinx.ext.napoleon',   # Support for Google-style docstrings
    'sphinx.ext.viewcode',   # Add links to source code
    'sphinx.ext.todo',       # Support TODO items
    'sphinx.ext.coverage',   # Documentation coverage
    'sphinx.ext.githubpages' # Create .nojekyll for GitHub Pages
]

# AutoDoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'show-inheritance': True,
}

# Theme settings
html_theme = 'sphinx_rtd_theme'

# Output options
exclude_patterns = []
templates_path = ['_templates']
html_static_path = ['_static']

# Enable TODO extension
todo_include_todos = True

# Napoleon settings (for Google-style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
