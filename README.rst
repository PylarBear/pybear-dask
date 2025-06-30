pybear-dask
===========

|Tests|
|Coverage|
|Test Status 313|
|Test Status 312|
|Test Status 311|
|Test Status 310|
|Test Status 39|

.. |Tests| image:: https://raw.githubusercontent.com/PylarBear/pybear-dask/main/.github/badges/tests-badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions

.. |Coverage| image:: https://raw.githubusercontent.com/PylarBear/pybear-dask/main/.github/badges/coverage-badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions

.. |Test Status 313| image:: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py313.yml/badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py313.yml

.. |Test Status 312| image:: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py312.yml/badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py312.yml

.. |Test Status 311| image:: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py311.yml/badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py311.yml

.. |Test Status 310| image:: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py310.yml/badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py310.yml

.. |Test Status 39| image:: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py39.yml/badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions/workflows/matrix-tests-py39.yml

|PyPI Build Status|
|TestPyPI Build Status|

.. |PyPI Build Status| image:: https://github.com/PylarBear/pybear-dask/actions/workflows/pypi-publish.yml/badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions/workflows/pypi-publish.yml

.. |TestPyPI Build Status| image:: https://github.com/PylarBear/pybear-dask/actions/workflows/testpypi-publish.yml/badge.svg
   :target: https://github.com/PylarBear/pybear-dask/actions/workflows/testpypi-publish.yml

|PyPI Downloads|

.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/pybear-dask.svg?label=PyPI%20downloads
   :target: https://pypi.org/project/pybear-dask/

|Version Status|

.. |Version Status| image:: https://img.shields.io/pypi/v/pybear-dask.svg
   :target: https://pypi.python.org/pypi/pybear-dask/

|PyPi|

.. |PyPi| image:: https://img.shields.io/pypi/v/pybear-dask
   :target: https://pypi.org/project/pybear-dask



.. |PythonVersion| replace:: >=3.9, <3.14
.. |DaskVersion| replace:: >=X.X.X
.. |DaskMLVersion| replace:: >=X.X.X
.. |DistributedVersion| replace:: >=X.X.X
.. |PybearVersion| replace:: >=0.1.19



pybear-dask is a Python computing library that supplements the pybear
library with analogous modules that have dask capability.

Website: https://github.com/PylarBear/pybear-dask

License
-------

BSD 3-Clause License. See `License File <https://github.com/PylarBear/pybear-dask/blob/main/LICENSE>`__.

=======

Installation
------------

Dependencies
~~~~~~~~~~~~

pybear-dask requires:

- Python (|PythonVersion|)
- dask (|DaskVersion|)
- dask-ml (|DaskMLVersion|)
- distributed (|DistributedVersion|)
- pybear (|PybearVersion|)

pybear-dask 0.2 is tested via GitHub Actions to run on Linux, Windows, and MacOS,
with Python versions 3.9, 3.10, 3.11, and 3.12. pybear-dask is not tested on earlier
versions, but some features may work.

User installation
~~~~~~~~~~~~~~~~~

pybear-dask has not been released to PyPI yet. First publish to PyPI is
anticipated to be July 2025. If you really want to try it out, the only way to
install pybear-dask is from TestPyPI using ``pip``::

   pip install -i https://test.pypi.org/simple/ pybear-dask

In the future, pip install from PyPI using ``pip``::

   pip install pybear-dask

Conda distributions are expected to be made available sometime after release to
PyPI.

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
- Download releases: https://test.pypi.org/project/pybear-dask/ (pypi coming soon!)
- Issue tracker: https://github.com/PylarBear/pybear-dask/issues

Source code
~~~~~~~~~~~

You can clone the latest source code with the command::

    git clone https://github.com/PylarBear/pybear-dask.git

Contributing
~~~~~~~~~~~~

pybear-dask is not ready for contributions at this time!

Testing
~~~~~~~

After installation, you can launch the test suite from outside the pybear-dask
root directory (you will need to have pytest installed in your environment)::

    pytest pybear-dask

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

Communication
~~~~~~~~~~~~~

- GitHub Discussions: https://github.com/PylarBear/pybear-dask/discussions
- Website: https://github.com/PylarBear/pybear-dask





