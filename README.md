## packme

[![Python package](https://github.com/tomszink/packme/actions/workflows/main.yml/badge.svg)](https://github.com/tomszink/packme/actions/workflows/main.yml)

I created this little repo to try out and show how a typical Python
project setup could look.

Below are some general explanations about the setup and some background
information.

Design goals:

- using a canonical directory structure
- packaging using setup.py
- testing using pytest
- linting using flake8
- test execution via tox in virtual environments
- providing a development environment


#### Directory structure

The source goes into a `src` directory.

  ```
  ├── setup.py
  ├── src
  │   ├── __init__.py
  │   ├── packme
  │   └── ...
  ├── requirements-test.txt
  ├── tests
  │   └── test_packme.py
  └── tox.ini
  ```

- Why a `src` dir?

  The main reason is: this ensures the tests are always
  executed against an installed package. This can be either done via
  using `tox` since it installs first the package into the virtual einvronment.
  The other option is to install the package locally with `pip --e .`,
  which installs the package from sources and editable locally.

- The alternative would be to have a folder with the package name instead
  of src directly in the project's root directory.
  For simple projects it is also possible to package a single python file
  in the root directory without a package directory.
  But to have a more canonical setup, the solution with `src` is preferred.

#### setup.py

- Should normally not include pinned version. This is to avoid
  unnecessary version conflicts for users of the package.
  Exceptions are: if the are hard constraints or if the deployment
  shall be independent of other packages and it is more important to have
  a controlled deployment (e.g. for "application like" packages).
- If however the package is an application, version pinning might be
  preferred to control the deployment.

#### tox and virtual envs

- Tox installs the package created via the `setup.py` into each virtual
  environment unless specified otherwise in the tox.ini.
  
#### requirements.txt

- Captures 3rd party dependencies -- if any (here we don't have them yet,
  so the file is not there).
- Normally "pins" the versions for reproducability, e.g.
  `requrest=2.15.0`
- A snapshot of the dependencies can be stored via `pip freeze`.
  Such dependencies can be installed via pip with
  `pip install -r requirements.txt`.

#### requirements-test.txt

- Could be specified also in the `tox.ini`, but this way it is more
  explicit and can be used without tox also.
  The requirements-test.txt can include the normal rquirements.txt
  as base by adding a line: `-r requirements.txt`.

#### devenv (Development environment)

- Why a `devenv`? The devenv is a virtual environement created via `tox`.
  Thus it is easily reproducible for everyone to create such a development
  environment via `tox -e devenv` and use it via `source devenv/bin/activate.
- An alternative would be to use a requirements(-devenv).txt file with pip and
  a "manually" created venv, but this is a bit less standardized then and less
  convenient as a user.
- Reference: https://tox.readthedocs.io/en/latest/example/devenv.html#development-environment


#### ToDos

- Code coverage
- Black
- Doc / Sphinx
- Include a 3rd party dependency (to use a requirements.txt or pipenv)
- Describe typical workflow
