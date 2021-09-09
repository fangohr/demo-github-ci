demo-github-ci
==============

|minimal-status-badge| |python-app-status-badge|


Tiny project to demo use of github workflows:

We have one source file `example.py <example.py>`__ which contains one (undocument) function and one test.

A `minimal <.github/workflows/minimal.yml>`__ workflow example shows how the test can be executed 
(via `py.test`) automatically using Github workflows.

A less minimal `Python Application <.github/workflows/python-app.yml>`__ workflow example attempts to 

- install our Python project and 
- install its dependencies (both not required for this example), 
- runs some Python style analyis (using `flake8`) before calling `py.test`. 
This is nearly what Github suggested as the default template for testing a Python project.


.. |minimal-status-badge| image:: https://github.com/fangohr/demo-github-ci/actions/workflows/minimal.yml/badge.svg
   :target: https://github.com/fangohr/demo-github-ci/actions/workflows/minimal.yml

.. |python-app-status-badge| image:: https://github.com/fangohr/demo-github-ci/actions/workflows/python-app.yml/badge.svg
   :target: https://github.com/fangohr/demo-github-ci/actions/workflows/python-app.yml
