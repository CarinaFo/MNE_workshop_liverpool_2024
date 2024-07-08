# EEG Analysis with MNE Python @ University of Liverpool

This is the repository for a 2-day workshop on EEG analysis using [MNE-Python](https://github.com/mne-tools/mne-python).
The workshop is taking place July 11th-12th, 2024 in [Liverpool].


## Materials

Authors of the material:

- Carina Forster, Max Planck Institute for Human Cognitive and Brain Sciences, Leipzig
- Alexandre Gramfort, Intro to Python scripts
- [Britta Westner](https://britta-wstnr.github.io/posts/about/), Radboud University, Donders Institute, Nijmegen, source localization scripts

Huge credits to the authors of this amazing online book [Neural Data Science in Python](https://neuraldatascience.io/intro.html)

## Before you arrive

Please make sure you do the following steps before the first hands-on session:

1. You will need to download this directory of scripts.
2. You can download [this example data](https://drive.google.com/file/d/1etefiAIRG6CMBeU91Fu2CTqM5KT9Ng_Z/view?usp=sharing) to play around with MNE-Python.
3. You must download the following data for time-frequency analysis and this data for group analysis.
4. You must have an up-to-date version of MNE-Python installed on your machine (you need a *full install* with all dependencies, **not** "MNE-Python with core functionalities only"). See instructions at: https://mne.tools/stable/install/index.html
5. To check your installation, please look at the (very short!) notebook [Check your installation](Installation_check.ipynb). See below if you need a reminder on how to start it.
6. If you are not familiar with Python, we invite you to take the time to work on these tutorials:
[Intro to Python](intro_to_python/0a-Intro_Python.ipynb), [Intro to Numpy](intro_to_python/0b-Intro_Numpy.ipynb).

## Highly recommended: Git as a tool for Version Control
### An online course by Lennart Wittkuhn on Version Control using Git
We won't have time to cover version control and git in great detail but I recommend checking out this [great resource](https://lennartwittkuhn.com/version-control-course-mpib-2024/)


### Start a Jupyter notebook

To start a Jupyter notebook, open your terminal and navigate to the directory where you saved this directory of scripts.
Then type the command `jupyter notebook` and Jupyter should open in your internet browser.
Click on the notebook you want to run!

You can of course use Jupyter Notebooks in your preferred IDE (Integrated Developer Environment), e.g.
[VSCode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

## Program

Intro to [EEG](https://docs.google.com/presentation/d/1rzpTC_sevdU2HvpLugRJqtd6uTertPP9ILGmGP8DCr8/edit?usp=sharing)

## References and credit

The code from this tutorial is heavily inspired from this article:

	Mainak Jas, Eric Larson, Denis Engemann, Jaakko Leppakangas, Samu Taulu, Matti Hamalainen,
	and Alexandre Gramfort. 2018. A Reproducible MEG/EEG Group Study With the MNE Software:
	Recommendations, Quality Assessments, and Good Practices.
	Frontiers in Neuroscience. 12, doi: 10.3389/fnins.2018.00530

The MNE software when used in publications should be acknowledged using citations.

To cite MNE-C or the inverse imaging implementations provided by the MNE software, please use:

	A. Gramfort, M. Luessi, E. Larson, D. Engemann, D. Strohmeier, C. Brodbeck, L. Parkkonen,
	M. Hämäläinen, MNE software for processing MEG and EEG data, NeuroImage, Volume 86,
	1 February 2014, Pages 446-460, ISSN 1053-8119.

To cite the MNE-Python package, please use:

	A. Gramfort, M. Luessi, E. Larson, D. Engemann, D. Strohmeier, C. Brodbeck, R. Goj, M. Jas,
	T. Brooks, L. Parkkonen, M. Hämäläinen, MEG and EEG data analysis with MNE-Python,
	Frontiers in Neuroscience, Volume 7, 2013, ISSN 1662-453X.
