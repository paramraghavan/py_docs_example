import os
import sys
# Add the path to your module so Sphinx can find it to generate documentation:
sys.path.insert(0, os.path.abspath('../py_docs_example'))

# -- Project information -----------------------------------------------------

project = 'Py Docs Example'
author = 'Param Raghavan'

# The full version, including alpha/beta/rc tags
release = '0.1'


"""
Enable any Sphinx extensions you need. At the very least, you'll likely want to include:
- 'sphinx.ext.autodoc' for automatic documentation from docstrings, 
- 'sphinx.ext.viewcode' to include links to source code

"""
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon'
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The master toctree document.
# Set the source file encoding and the master document (which is typically index.rst):
master_doc = 'index'

# The encoding of source files.
source_encoding = 'utf-8-sig'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'alabaster'
