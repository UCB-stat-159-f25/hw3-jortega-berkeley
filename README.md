STAT 159 HW3

What’s included:

Notebook: LOSC_Event_tutorial.ipynb

Package: ligotools/ (utils.py, readligo.py)

Tests: ligotools/tests/ (test_utils.py, test_readligo.py)

Website: built with MyST, auto-deployed via GitHub Pages

Repo layout:

data/        # input data (.hdf5, .json) + final CSV
figures/     # generated plots (ignored by git)
audio/       # generated wav files (ignored by git)
ligotools/   # package code + tests
.github/workflows/pages.yml  # Pages deploy workflow
myst.yml     # MyST site config
index.md     # site landing page (Binder link)

Quick start:

# (optional) conda env from environment.yml
conda env create -f environment.yml && conda activate stat159

# editable install
python -m pip install -e .

# run tests
python -m pytest ligotools -q

Reproducible outputs:

Build the site locally:

myst build --html
# open _build/html/index.html

Live site:

https://ucb-stat-159-f25.github.io/hw3-jortega-berkeley/

Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](
https://mybinder.org/v2/gh/UCB-stat-159-f25/hw3-jortega-berkeley/HEAD?labpath=LOSC_Event_tutorial.ipynb)

Credits:

LIGO tutorial adapted from LOSC materials.  
Authors: LIGO Scientific Collaboration (LSC) and Joseph Ortega.

AI Documentation:

See "ai_documentation.txt" for use of ai on this assignment.