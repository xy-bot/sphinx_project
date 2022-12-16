# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "test"
copyright = "2022, test"
author = "test"
release = "0.1"

# version = ""

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_multiversion"]

templates_path = ["_templates"]
exclude_patterns = []

language = "zh"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# custom theme
import sys
import os
sys.path.insert(0, os.path.abspath('./_themes'))

import myTheme

html_theme = "myTheme"

html_theme_path = myTheme.get_html_theme_path()

# html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

html_sidebars = {
    "**": [
        "versions.html",
    ],
}

html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
    "logo_only": True,
    "logo_url": "www.baidu.com",
}

# Whitelist pattern for tags (set to None to ignore all tags)
# smv_tag_whitelist = r'^.*$'

# Whitelist pattern for branches (set to None to ignore all branches)
smv_branch_whitelist = r'^(develop|main)$'

# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = r'^(develop|main)$'

# Pattern for released versions
smv_released_pattern = r'^(heads|remotes/[^/]+)/(?!:master).*$'

# 指定哪个分支为 lastest 版本
smv_latest_version = "develop"

html_show_sourcelink = False

master_doc = "index"

html_logo = "logo.png"

# logo_url = "www.baidu.com"
