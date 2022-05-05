# Welcome to Mod6!
## Learning a second (programming) language

---

## Module 6 Overview
- Week 17: Python language (inverted style)
- Week 18: Python web applications (lecture style)
- Week 19: Docker (lecture style)
- Week 20: Group projects


---

## This week
- Today: Python setup & basics
- Tuesday: Python data types & control flow
- Wednesday: Python collections
- Thursday: Python importing, decorators, and classes
- Friday: Python dependency management, unittesting, and study day

---

## JavaScript vs. Python

|                | JavaScript | Python |
| -------------- | ---------- | ------ |
| Strings        | ☑          | ☑      |
| Booleans       | ☑          | ☑      |
| Arrays (Lists) | ☑          | ☑      |
| Functions      | ☑          | ☑      |
| Classes        | ☑          | ☑      |
| Loops          | ☑          | ☑      |
| if-else        | ☑          | ☑      |



---

## So what _is_ the difference?

---

### JavaScript runs in the browser
- JavaScript is the language of the browser
- Python is not going to manipulate the DOM, or replace React.
- You can write your server in Python, but not the front-end code.

---

### Python is great multi-purpose tool

- Python does backend really well (we'll see this firsthand next week!)
- Python has diverse popular libraries that extend the functionality.
    - widely used by for applications in sciences, machine learning

---

### Syntax

We'll be using the same concepts we already know, just with a new look!
- whitespace aware vs. curly braces for code blocks
- no more semi-colons to end lines
- `True` and `False` instead of `true` and `false`
- and MUCH more


---


### Python style guide
- People may have opinions on how to format your JavaScript code...
- But Python (the language!) has opinions about how to format your Python code.
    - [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/)
- Python also defines guiding principles on designing "Pythonic" code
    - [The Zen of Python, by Tim Peters](https://www.python.org/dev/peps/pep-0020/)

---

## Today:
1. Python Install
    - Use the [python-setup.md](https://github.com/appacademy/unified-setup/blob/main/python-setup.md) in the repo linked in a/A Open
2. Explore the basics of Python syntax & data types

---

## Installation walkthrough
- Install Pyenv
- Configure shell environment for Pyenv by updating startup scripts
    - Windows users need to install some extra dependencies for Python
- Install Python (using Pyenv)
- Install Pipenv
    - Don't worry about this - we'll get to it next week!

---

## Verifying your Python install

1. The following commands should return the same Python 3.9.4+ version:
```
python --version
python3 --version
```
2. `which python` should return `~/.pyenv/shims/python`