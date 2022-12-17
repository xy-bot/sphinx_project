# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'test'
copyright = '2022, test'
author = 'test'
release = '0.1'

version = "0.1"
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_multiversion"]

templates_path = ['_templates']
exclude_patterns = ["sphinx-multiversion.md"]

language = 'zh'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

html_sidebars = {
    '**': [
        'versions.html',
    ],
}

smv_tag_whitelist = r'1.4'

# # Whitelist pattern for branches (set to None to ignore all branches)
# smv_branch_whitelist = r"develop"

# # Whitelist pattern for remotes (set to None to use local branches only)
# smv_remote_whitelist = None

# # Pattern for released versions
# smv_released_pattern = r'refs/tags/1.4'  

smv_latest_version = '1.4'

smv_metadata = {
  "1.4": {
    "name": "1.4",
    "version": "",
    "release": "0.1",
    "is_released": True,
    "source": "tags",
    "creatordate": "2022-12-16 20:46:00 +0800",
    "basedir": "C:\\Users\\32621\\AppData\\Local\\Temp\\tmp4_sc3ptu\\0e76ed34331768575e65ce69260bdc0db845aefc",
    "sourcedir": "C:\\Users\\32621\\AppData\\Local\\Temp\\tmp4_sc3ptu\\0e76ed34331768575e65ce69260bdc0db845aefc\\source",
    "outputdir": "D:\\workspace\\sphinx_project\\build\\html\\1.4",
    "confdir": "C:\\Users\\32621\\AppData\\Local\\Temp\\tmp4_sc3ptu\\0e76ed34331768575e65ce69260bdc0db845aefc\\source",
    "docnames": [
      "index",
      "resources/\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5",
      "resources/\u8fed\u4ee3\u5668",
      "resources/index"
    ]
  },
  "develop": {
    "name": "develop",
    "version": "",
    "release": "0.1",
    "is_released": False,
    "source": "heads",
    "creatordate": "2022-12-16 20:46:00 +0800",
    "basedir": "C:\\Users\\32621\\AppData\\Local\\Temp\\tmp4_sc3ptu\\0e76ed34331768575e65ce69260bdc0db845aefc",
    "sourcedir": "C:\\Users\\32621\\AppData\\Local\\Temp\\tmp4_sc3ptu\\0e76ed34331768575e65ce69260bdc0db845aefc\\source",
    "outputdir": "D:\\workspace\\sphinx_project\\build\\html\\develop",
    "confdir": "C:\\Users\\32621\\AppData\\Local\\Temp\\tmp4_sc3ptu\\0e76ed34331768575e65ce69260bdc0db845aefc\\source",
    "docnames": [
      "index",
      "resources/\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5",
      "resources/\u8fed\u4ee3\u5668",
      "resources/index"
    ]
  }
}
