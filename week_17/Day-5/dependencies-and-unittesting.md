<style>
    .present {
        text-align: left;
    }
    img[alt=set_operations] {
        width: 60%;
        
    }
</style>

---

###### tags: `Week 17` `W17D5`

---

# Dependency Management & Unittesting
## Week 17 Day 5

---

## Dependency Management with Virtual Environments

---

### What is a virtual environment?

A virtual environment is a self-contained directory tree that contains a Python installation for a particular version of Python plus a number of additional dependencies necessary for a project.

---

### `pipenv`

`pipenv` is a tool that creates and manages virtual environments.

To create a virtual environment, simply run

```bash
pipenv install
````

If there is a Pipfile present, this will install the dependencies in the Pipfile, otherwise it will create a new Pipfile along with a virtual environment.

You can specify a particular version of Python to install in your virtual environment with the `--python` flag followed by the Python version number.

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

### Using the virtual environment

Activate and enter the virtual environment shell:
```bash
pipenv shell
```

Run a command without entering the virtual environment:
```bash
pipenv run command
```

Remove the virtual environment folder:
```bash
pipenv --rm
```

---

## Unittest & Pytest

---

`unittest` is the built-in unittesting framework in Python.

Most Python developers choose to use the external `pytest` package because it is cleaner and more readable.

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

Install `pytest` in a virtual environment.

```bash
pipenv install pytest
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

---

## Practices for Today...

### Python Environment (30 min)
pip, virtualenv, And pipenv - 12 min
Exercise: Pipenv Setup - 15 min


### Unit Testing (2 hrs 40 min)
Writing Unit Tests With unittest - 10 min
Writing Unit Tests With Pytest - 10 min
Exercise: Writing tests with pytest - 15 min
Bonus: TDD With unittest And pytest - 2 hrs


### Week 17 Practice Assessment! (1 hr 30 min)
Python Basics - Part I - 30 min
Python Basics - Part II - 1 hr
