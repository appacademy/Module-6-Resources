# Python decorators, dependency management, & unit-testing
## Week 18 Day 1


---

## Part 1: Decorators

---

### What's a decorator?

A decorator is syntactic sugar for a function that decorates another.

A decorator function takes in another function as a callback and returns a modified version of the callback function.

We can use decorators to add to or modify the behavior of regular functions.

---

### Decorators
Let's create a decorator that could be used for timing function calls.
```python=
from datetime import datetime

# our decorator, which takes in a callback function
def timer(func):
    
    # define the wrapper function that we're going to return
    def wrapper():
        # get current time before function call
        before_time = datetime.now()
        
        # invoke the callback
        val = func()
        # log the return value of the function
        print(val)
        
        # get current time after function call
        after_time = datetime.now()
        
        # calculate total time
        total = after_time - before_time
        
        # return the total time
        return total
    
    # decorator returns the wrapper function object
    return wrapper
```

---

### Decorators

Without the decorator syntax, we would have to define our function, then reassign our function to the return value from invoking the decorator function on our old function.

```python=
# decorator function
from datetime import datetime

def timer(func):
    def wrapper():
        before_time = datetime.now()
        val = func()
        print(val)
        after_time = datetime.now()
        total = after_time - before_time
        return total
    
    return wrapper


# function to decorate
def my_function():
    return "hello"


# before decorating
print(my_function())  # returns "hello"

# decorated function
my_function = timer(my_function)

# after decorating
print(my_function())
```


---

### Decorators

Using the `@decorator_name` syntax, we can shorten this:
```python=
def my_function():
    return "hello"

my_function = timer(my_function)
```
To this:
```python=
@timer
def my_function():
    return "hello"
```

Decorating a function definition (with the `@decorator` syntax) does the same thing as reassigning the function name to the return value of the decorator.


---

### Passing arguments through a decorator

What if I want to wrap functions that take arguments?
```python=
from datetime import datetime

def timer(func):
    def wrapper(name):
        before_time = datetime.now()
        val = func(name)
        print(val)
        after_time = datetime.now()
        total = after_time - before_time
        return total
    
    return wrapper


@timer
def my_function_args(name):
    return f"hello {name}"
```


---

### Passing arguments through a decorator

What if I want to wrap functions that take arguments... but I want to be flexible about what kind of arguments the function takes?


```python=
from datetime import datetime

def timer(func):
    def wrapper(*args, **kwargs):
        before_time = datetime.now()
        val = func(*args, **kwargs)
        print(val)
        after_time = datetime.now()
        total = after_time - before_time
        return total
    
    return wrapper


@timer
def my_function_args(name):
    return f"hello {name}"

@timer
def my_sum(sum1, sum2):
    return sum1 + sum2
```

---

## Part 2: The Import System

---

### Python Modules
A module is code that is imported from a file or directory. A package is a collection of modules. A module/package can be:
1. Built-in: already in Python's standard module library 
2. Third-party: downloaded via command line 
3. Custom: your own code

To import code from a module, we use the `import` keyword. The import keyword will locate and initialize a module, and give you access to the specific names you have imported in the file.


---

### The `import` keyword
The Python standard library has a number of packages you can import without having to install them—they are included when you install Python ([documentation](https://docs.python.org/3/tutorial/stdlib.html)). 


Let's use the random package as an example (this would work the same with any package).

```python=
import random  # import everything from random
print(random.randint(0, 10))
```
With aliasing
```python=
import random as rand  # import everything, alias random as rand
print(rand.randint(0, 10))
```

---

### The `import` keyword

You can also import just specific functions from a package using the `from` keyword.

```python=
from random import randint  # import just the randint function
print(randint(0, 10))
```
```python=
from random import randint, shuffle  # import multiple functions at the same time
print(randint(0, 10))
```

```python=
from random import randint as r_i, shuffle
print(r_i(0, 10))
```

---


### Import Python code from a file
If I have two files at the same level, I can import one file using the filename (minus the `.py`).
```
project_folder
|  my_code.py
|  other_code.py
```

```python=
# inside my_code.py
import other_code
# import just a specific item
from other_code import my_function
```

When I import the `other_code.py` file, all of the code in that file will run, even if I'm just importing one function.

---


### Import Python code from a subdirectory

```
project_folder
|  my_code.py
|  other_code.py
|  subfolder
   |  __init__.py
   |  file_one.py
```


To import code from inside a subfolder, use `import folder_name.file_name`.

```python=
# inside my_code.py
import subfolder.file_one
# or
from subfolder import file_one
# or
from subfolder.file_one import my_function
```

---

### Quick note about `__init__.py`

This file should go in any directory being imported. It will transform a plain old directory into a Python module/package.

Upon import from a module/package,  its`__init__.py` file is implicitly executed, and all objects it defines are bound to the module's namespace ([documentation](https://docs.python.org/3/reference/import.html#regular-packages)).

---

### Why do we need `__init__.py` if we can import without it?

Python 3.3+ creates an *implicit namespace package* if no `__init__.py` file exists for a directory. We want to avoid this most of the time!

We need a `__init__.py` if we want to run the directory as a module, if we want to run `pytest` on it, etc. 

This file can be completely empty (and often will be). It can also be the place where we initialize our applications!

---

### JavaScript imports

Reminder: In Javascript, when we imported from other files, we used relative import statements.
```
project_folder
|  top_level_file.js
└──subfolder
   |  file_one.js
   |  file_two.js 
```

The import path changes depending on what file we are in.
```javascript=
// inside top_level_file.js
import { someObject } from "./subfolder/file_two"
```

```javascript=
// inside file_one.js
import { someObject } from "./file_two"
```


---

### Python imports

```
project_folder
|  top_level_file.py
└──subfolder
   |  __init__.py
   |  file_one.py
   |  file_two.py 
```

In Python, absolute import statements are preferred when we are importing code from other files.

"Absolute" means that all imports are relative only to one location - the top-level file being executed.

Absolute imports are preferred because they are more explicit and straightforward.


```python=
# inside top_level_file.py
import subfolder.file_two
```

```python=
# inside file_one.py
import subfolder.file_two
```

However...


---

### Python Imports

...that means that if I try to run a file directly, instead of from the intended entrypoint of my application, the file won't work correctly.
```python=
# inside top_level_file.py
import subfolder.file_one
print("Hello from top_level_file.py")
```


```python=
# inside file_one.py
import subfolder.file_two
print("Hello from file_one.py")
```

```python=
# inside file_two.py
print("Hello from file_two.py")
```

---

### Python Imports

If you run the `top_level_file.py` file at the command line, you will get the following output:
```
Hello from file_two.py
Hello from file_one.py
Hello from top_level_file.py
```

If you run the `file_one.py` file at the command line, you will get the following output:
```
ModuleNotFoundError: No module named 'subfolder'
```

If I rewrote `file_one.py` so that its import statement worked when it runs in isolation (`import file_two`), then it wouldn't work in the context of the application. 

---

### Python imports (takeaways)

1. All import statements should usually be "absolute" - meaning relative to the top level of your project.
2. Include a `__init__.py` file in any folder that has python code if you are going to be importing from that folder. The `__init__.py` file can be completely empty (and often will be).


---

## Part 3: Dependency Management with Virtual Environments

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

## Part 4: Unittest & Pytest

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

---

## Today's project
### Test Driven Development (TDD) with Python

- Roman numeral -> Hindu-Arabic numeral translator and unittests along with it
- Use what we learned about dependency management & unittesting