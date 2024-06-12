# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

sys.path.insert(0, os.path.abspath('../'))

github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'
def setup(app):
    app.add_config_value('recommonmark_config',{
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)

project = 'PItBE'
copyright = '2024, Reo BABA'
author = 'Reo BABA'

version = '1.0.2'
release = '1.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx',
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = [
    '_build', 'Thumbs.db', 
    '.DS_Store', '.ipynb_checkpoints'
    ]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

source_parser = {
    '.md': CommonMarkParser
}

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# HTML出力用の設定
#html_theme_options = {
#    'style_external_links': True,
#    'style_nav_header_background': '#2980B9',
#    'style_text': '#2C3E50',
#    'style_text_selection': '#E74C3C',
#    'style_bg': '#ECF0F1',
#    'style_bg_selection': '#BDC3C7',
#    'style_link': '#3498DB',
#    'style_link_hover': '#2980B9',
#    'style_code': '#3498DB',
#    'style_code_font_size': '0.85em',
#    'style_pre': '#1ABC9C',
#    'style_pre_font_size': '0.85em',
#    'style_border': '#BDC3C7',
#    'style_outlink': '#1ABC9C',
#}
# スクロールバーのスタイルを設定
html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']
#html_css_files = [
#    'custom.css',
#]

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True
