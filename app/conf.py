# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'goit_hw'  # Назва вашого проекту
copyright = '2023, Your Name'  # Авторські права
author = 'Videograph'  # Автор проекту

# The full version, including alpha/beta/rc tags
release = '1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',  # Генерація автоматичної документації з docstrings
    'sphinx.ext.napoleon',  # Підтримка NumPy/Google стилю docstrings
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'  # Тема документації

# Theme options are theme-specific and customize the look and feel of a theme
html_theme_options = {
    'logo': 'logo.png',  # Шлях до лого
    'github_user': 'NickStS',
    'github_repo': 'hw-14-python-web',
    'github_banner': True,
    'github_type': 'star',
    'description': 'Домашнє завдання GoIT WEB',
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/logo.png'  # Лого, яке відображатиметься в боковому меню

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'MyDocumentation'

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': '',
}

# -- Options for manual page output ------------------------------------------

master_doc = 'app'

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'mydocumentation', 'My Documentation', [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'MyDocumentation', 'My Documentation', author, 'MyDocumentation',
     'One line description of project.', 'Miscellaneous'),
]

# -- Extension configuration -------------------------------------------------

# Auto-generate section labels.
autosectionlabel_prefix_document = True
