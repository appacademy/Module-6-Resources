# Python dependency management & unit-testing

---

## Part 1: Dependency Management with Virtual Environments

---

### Pip, Virtualenv, and Pipenv

- **pyenv**: version manager for Python
- **pip**: package manager for Python (but only works for globally installing packages)
- **virtualenv**: the environment containing a specified python version and a collection of installed packages(in a `.venv` folder)
- **pipenv**: dependency manager for individual projects


---


### Pip, Virtualenv, and Pipenv

| Python tool   | Node.js equivalent      |
|:------------- |:----------------------- |
| pyenv	        | nvm                     |
| pip           | npm --global            |
| virtualenv    | nvm + node_modules      |
| pipenv        | npm + nvm               |
| Pipfile       | package.json            |
| Pipfile.lock  | package-lock.json       |


---

### Using `pipenv`


Create a virtual environment by running `pipenv install`. If there is a Pipfile present, this will install the dependencies in the Pipfile, otherwise it will create a new Pipfile along with a virtual environment.

You can specify a particular version of Python to use in your virtual environment with `--python` flag.
```bash
pipenv install --python 3.9.4
```
You can also pass in a path instead of a number .
```bash
pipenv install --python "/Users/username/.pyenv/versions/3.9.4/bin/python"
```

---

### Specifying a Python version (note for projects this week)

Many of the projects this week will specify a version of Python to use. If you try to use a version that you don't have installed, it will not work. Also, these projects expect you to be specifying the path instead of just a number.

If you see something like this
```bash
pipenv install --python "$PYENV_ROOT/versions/3.8.3/bin/python"
```
Run this instead:

```bash
pipenv install --python 3.9.4 # or whatever version you do have installed
```

If you aren't sure, you can check to see which version you have available with the command `pyenv versions`.

---

### Installing packages with `pipenv`
Install a dependency:
```bash
pipenv install package-name
```
Install a development-only dependency:
```bash
pipenv install --dev package-name
```
Uninstall a dependency:
```bash
pipenv uninstall package-name
```

---

### More `pipenv` commands
Activate your virtual environment shell:
```bash
pipenv shell
```
Remove a virtual environment:
```bash
pipenv --rm
```

---

## Part 2: Unittest & Pytest

---

### The `unittest` package

To run tests with unittest:
```bash
python -m unittest
```

All tests must be in a folder called `test` at the top level of the project. The `test` folder must contain a `__init__.py`

---

### Writing `unittest` tests
Inside a test file:
- import `unittest`.
- import the code that we are testing.
- create a class that inherits from `unittest.TestCase`. 

```python=
import unittest
from widget import Widget

class TestWidget(unittest.TestCase):
    pass
```

---

### Writing `unittest` tests

Tests are written as methods on the class.
- names begin with `test_`
- use methods from the `unittest.TestCase` class to make assertions
    - see assert methods [documentation](https://docs.python.org/3/library/unittest.html#test-cases)

```python=
import unittest
from widget import Widget


class TestWidgetInitialize(unittest.TestCase):
    def test_initialize_widget_with_color(self):
        # arrange
        color = "blue"
        test_widget = Widget(color)
        # act
        result = test_widget.color
        # assert
        self.assertEqual(result, color)
```

---

### The `pytest` package

Create a virtual environment if you haven't yet, and install pytest.

```bash
pipenv install pytest --python 3.9.4
```

Run tests at the command line by running
```bash
pytest
```

Make a directory called `test` at the top level of your project (be sure it contains a `__init__.py`).

Test files must be in `test` directory, and filenames must begin or end with `test`.


---

### Writing `pytest` tests


Define test functions directly—no need for classes. Function names must begin with `test` to be treated as a unit test.

Use `assert` keyword, followed by the conditional you are trying to test.

You can run `unittest` tests with `pytest`, but not vice versa.

```python=
from widget import Widget


def test_initialize_widget_with_color():
    # arrange
    color = "blue"
    test_widget = Widget(color)
    # act
    result = test_widget.color
    # assert
    assert result == color
```
