pybear-dask
===========

|Tests|
|Coverage|
|Test Status 314|
|Test Status 313|
|Test Status 312|
|Test Status 311|
|Test Status 310|

.. |Tests| image:: https://raw.githubusercontent.com/PylarBear/pybear-dask/main/.github/badges/tests-badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions

.. |Coverage| image:: https://raw.githubusercontent.com/PylarBear/pybear-dask/main/.github/badges/coverage-badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions

.. |Test Status 314| image:: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py314.yml/badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py314.yml

.. |Test Status 313| image:: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py313.yml/badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py313.yml

.. |Test Status 312| image:: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py312.yml/badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py312.yml

.. |Test Status 311| image:: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py311.yml/badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py311.yml

.. |Test Status 310| image:: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py310.yml/badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py310.yml

|TestPyPI Build Status|

.. |TestPyPI Build Status| image:: https://github.com/PylarBear/pybear-dask/actions/workflows/testpypi-publish.yml/badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions/workflows/testpypi-publish.yml

|PyPI Build Status|
|Version|
|PyPI Downloads|

.. |PyPI Build Status| image:: https://github.com/PylarBear/pybear-dask/actions/workflows/pypi-publish.yml/badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions/workflows/pypi-publish.yml

.. |Version| image:: https://img.shields.io/pypi/v/pybear-dask?style=flat&color=blue
   :target: https://pypi.org/project/pybear-dask
   :alt: PyPI Version

.. |PyPI Downloads| image:: https://static.pepy.tech/badge/pybear-dask
   :target: https://pepy.tech/project/pybear-dask/
   :alt: PyPI Downloads

|DOI|

.. |DOI| image:: https://zenodo.org/badge/1009051313.svg
   :target: https://doi.org/10.5281/zenodo.16548280
   :alt: DOI

|BMC|

.. |BMC| image:: https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png
   :target: https://www.buymeacoffee.com/pybear
   :alt: Buy Me A Coffee


.. |PythonVersion314| replace:: ==3.14
.. |DaskVersion314| replace:: >=2025.1.0
.. |DaskMLVersion314| replace:: >=2025.1.0
.. |DistributedVersion314| replace:: >=2025.1.0
.. |PybearVersion314| replace:: >=0.2.4
.. |PytestVersion314| replace:: >=8.0.0
.. |ScikitVersion314| replace:: >=1.7.2

.. |PythonVersion313| replace:: ==3.13
.. |DaskVersion313| replace:: >=2025.1.0
.. |DaskMLVersion313| replace:: >=2025.1.0
.. |DistributedVersion313| replace:: >=2025.1.0
.. |PybearVersion313| replace:: >=0.2.0
.. |PytestVersion313| replace:: >=7.0.0
.. |ScikitVersion313| replace:: >=1.6.1

.. |PythonVersion312| replace:: ==3.12
.. |DaskVersion312| replace:: >=2024.4.1
.. |DaskMLVersion312| replace:: >=2024.3.20
.. |DistributedVersion312| replace:: >=2024.4.1
.. |PybearVersion312| replace:: >=0.2.0
.. |PytestVersion312| replace:: >=7.0.0
.. |ScikitVersion312| replace:: >=1.4.2

.. |PythonVersion311| replace:: ==3.11
.. |DaskVersion311| replace:: >=2024.4.1
.. |DaskMLVersion311| replace:: >=2024.3.20
.. |DistributedVersion311| replace:: >=2024.4.1
.. |PybearVersion311| replace:: >=0.2.0
.. |PytestVersion311| replace:: >=7.0.0
.. |ScikitVersion311| replace:: >=1.4.2

.. |PythonVersion310| replace:: ==3.10
.. |DaskVersion310| replace:: >=2024.3.0
.. |DaskExprVersion310| replace:: >=1.0,<2.0.0
.. |DaskMLVersion310| replace:: >=2024.3.20
.. |DistributedVersion310| replace:: >=2024.3.0
.. |PybearVersion310| replace:: >=0.2.0
.. |PytestVersion310| replace:: >=7.0.0
.. |ScikitVersion310| replace:: >=1.3.0,<1.8


Python packages that augment your data analytics experience.

pybear-dask is a scikit-style Python computing library that supplements the
pybear library with analogous modules that have dask capability.

Python versions 3.10, 3.11, 3.12, 3.13, and 3.14 are supported.

Website: https://github.com/PylarBear/pybear-dask

License
-------

BSD 3-Clause License. See `License File <https://github.com/PylarBear/pybear-dask/blob/main/LICENSE>`__.

=======

Installation
------------

Dependencies
~~~~~~~~~~~~

pybear-dask operating on Python 3.14 requires:

- Python (|PythonVersion314|)
- dask (|DaskVersion314|)
- dask-ml (|DaskMLVersion314|)
- distributed (|DistributedVersion314|)
- pybear (|PybearVersion314|)
- scikit-learn (|ScikitVersion314|)

pybear-dask operating on Python 3.13 requires:

- Python (|PythonVersion313|)
- dask (|DaskVersion313|)
- dask-ml (|DaskMLVersion313|)
- distributed (|DistributedVersion313|)
- pybear (|PybearVersion313|)
- scikit-learn (|ScikitVersion313|)

pybear-dask operating on Python 3.12 requires:

- Python (|PythonVersion312|)
- dask (|DaskVersion312|)
- dask-ml (|DaskMLVersion312|)
- distributed (|DistributedVersion312|)
- pybear (|PybearVersion312|)
- scikit-learn (|ScikitVersion312|)

pybear-dask operating on Python 3.11 requires:

- Python (|PythonVersion311|)
- dask (|DaskVersion311|)
- dask-ml (|DaskMLVersion311|)
- distributed (|DistributedVersion311|)
- pybear (|PybearVersion311|)
- scikit-learn (|ScikitVersion311|)

pybear-dask operating on Python 3.10 requires:

- Python (|PythonVersion310|)
- dask (|DaskVersion310|)
- dask-expr (|DaskExprVersion310|)
- dask-ml (|DaskMLVersion310|)
- distributed (|DistributedVersion310|)
- pybear (|PybearVersion310|)
- scikit-learn (|ScikitVersion310|)

User installation
~~~~~~~~~~~~~~~~~

Install pybear-dask from the online PyPI package repository using ``pip``::

   (your-env) $ pip install pybear-dask

A Conda distribution is not expected to be made available anytime soon.

=======

Usage
-----
The folder structure of pybear-dask is nearly identical to scikit-learn. This
is so those that are familiar with the scikit layout and have experience with
writing the associated import statements have an easy transition to pybear-dask.
The pybear-dask subfolders are *base* and *model_selection*.

You can import pybear-dask's packages in the same way you would with scikit.
Here are a few examples of how you could import and use pybear-dask modules:

.. code-block:: console

    from pybear-dask.model_selection import GSTCVDask

    search = GSTCVDask()
    search.fit(X, y)

    from pybear-dask import model_selection as ms

    search = ms.AutoGridSearchCVDask()
    search.fit(X, y)


=======

Major Modules
-------------

AutoGridSearchCVDask
~~~~~~~~~~~~~~~~~~~~
Perform multiple uninterrupted passes of grid search with dask_ml GridSearchCV 
and dask objects utilizing progressively narrower search grids.

- Access via pybear-dask.model_selection.AutoGridSearchCVDask.

GSTCVDask (GridSearchThresholdCV for Dask)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Perform conventional grid search on a classifier with concurrent threshold 
search using dask objects in parallel and distributed environments. Finds the 
global optima for the passed parameters and thresholds. Fully compliant with 
the dask_ml/scikit-learn GridSearchCV API.

- Access via pybear-dask.model_selection.GSTCVDask.

AutoGSTCVDask (AutoGridSearchThresholdCV for Dask)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Perform multiple uninterrupted passes of grid search with pybear-dask GSTCVDask
utilizing progressively narrower search grids.

- Access via pybear-dask.model_selection.AutoGSTCVDask.

=======

Changelog
---------

See the `changelog <https://github.com/PylarBear/pybear-dask/blob/main/CHANGELOG.md>`__
for a history of notable changes to pybear-dask.

=======

Development
-----------

Important links
~~~~~~~~~~~~~~~

- Official source code repo: https://github.com/PylarBear/pybear-dask
- Download releases: https://pypi.org/project/pybear-dask/
- Issue tracker: https://github.com/PylarBear/pybear-dask/issues

Source code
~~~~~~~~~~~

You can clone the latest source code with the command::

    git clone https://github.com/PylarBear/pybear-dask.git

Contributing
~~~~~~~~~~~~

pybear-dask is not ready for contributions at this time!
If you have a good idea that uses dask, it may be better to try to contribute
directly to
`dask <https://image.dask.org/en/latest/contributing.html>`__ or
`dask-ml <https://ml.dask.org/contributing.html>`__.

Testing
~~~~~~~

pybear-dask 0.2 is tested via GitHub Actions to run on Linux, Windows, and MacOS,
with Python versions 3.10, 3.11, 3.12, 3.13, and 3.14. pybear-dask is not supported
nor tested on earlier versions.

If you want to test pybear-dask yourself, you will need:

- pytest (|PytestVersion314|) for Python version 3.14
- pytest (|PytestVersion313|) for Python versions 3.13, 3.12, 3.11, and 3.10

The tests are not available in the PyPI pip installation. You can get
the tests by downloading the tarball from the pybear-dask project page on
`pypi.org <https://pypi.org/project/pybear-dask/>`_ or cloning the pybear-dask
repo from `GitHub <https://github.com/PylarBear/pybear-dask>`_. Once you have
the source files in a local project folder, create a poetry environment for the
project and install the test dependencies. After installation, open the poetry
environment shell and you can launch the test suite from the root of your
pybear-dask project folder with::

    (your-pybear-dask-env) you@your_computer:/path/to/pybear-dask/project$ pytest tests/

Project History
---------------

This project was spun off the main pybear project just prior to the first
public release of both. pybear-dask was spun off to ensure maximum stability
for the main pybear project, while keeping these modules available.

Help and Support
----------------

Documentation
~~~~~~~~~~~~~

Documentation is not expected to be made available via a website for this
package. Use the documentation for similar packages in the main pybear package.
See the repo for pybear: https://github.com/PylarBear/pybear/
See the online docs for pybear: https://pybear.readthedocs.io/en/stable/index.html

Communication
~~~~~~~~~~~~~

- GitHub Discussions: https://github.com/PylarBear/pybear-dask/discussions
- Website: https://github.com/PylarBear/pybear-dask





