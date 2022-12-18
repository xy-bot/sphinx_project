# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = "wwww"
copyright = "2022, wwww"
author = "www"
extensions = ["myst_parser", "sphinx_multiversion"]
html_theme = "sphinx_rtd_theme"
language = "zh"


# release = "0.2"
# version = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration




# exclude_patterns = ["sphinx-multiversion.md"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


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

templates_path = ["_templates"]

smv_tag_whitelist = r"1.4"

# Whitelist pattern for branches (set to None to ignore all branches)
smv_branch_whitelist = r"develop"

# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = None

smv_testing_whitelist = r"refs/tags/1.4"

# Pattern for released versions
smv_released_pattern = r"refs/tags/1.4"

smv_latest_version = "1.4"

# smv_metadata = {
#     "develop": {
#         "name": "develop",
#         "version": "",
#         "release": "0.1",
#         "is_released": False,
#         "source": "heads",
#         "creatordate": "2022-12-16 20:46:00 +0800",
#         "basedir": "D:\\workspace\\sphinx_project",
#         "sourcedir": "D:\\workspace\\sphinx_project\\source",
#         "outputdir": "D:\\workspace\\sphinx_project\\build\\html\\develop",
#         "confdir": "D:\\workspace\\sphinx_project\\source",
#         "docnames": [
#             "index",
#             "resources/\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5",
#             "resources/\u8fed\u4ee3\u5668",
#             "resources/index",
#         ],
#     }
# }
