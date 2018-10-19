## packme

I created this little repo to try out and show how a typical Python
project setup could look.

Below are some general explanations about the setup and some background
information.

My goal has been to include:

- defining a standard directory structure
- packaging using setup.py
- testing using pytest
- linting using flake8
- test execution via tox in virtual environments
- providing a development environment specified via tox


#### Directory structure

The source goes into a `src` directory.

  ```
  ├── setup.py
  ├── src
  │   ├── __init__.py
  │   ├── packme
  │   └── ...
  ├── test-requirements.txt
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


### tox and virtual envs

- Why a `devenv`? The devenv is a virtual environement created via `tox`.
  Thus it easily reproducible for everyone to create such a development
  environment via `tox -e devenv`.


### ToDos

- TravisCI or alike
- Code coverage
- Black
- Doc / Sphinx
- Include a 3rd party dependency (to use a requirements.txt or pipenv)
