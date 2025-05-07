# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CIPs'
copyright = '2025, Nanyang System Developers'
author = 'Nanyang System Developers'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",  # for markdown support
]

# Explicitly include .rst and .md files as source files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

include_patterns = [
    "index.*",
    "cip-????.md",
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Warn on missing references
nitpicky = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
