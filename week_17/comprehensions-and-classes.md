# More Built-ins, Comprehensions, and Classes

---

## Part 1: Python Imports

---

### Basic imports in Python

Python import syntax is backwards from import syntax in JavaScript. 
```python=
# from module_name import variable_name
from random import randint

print(randint(0, 10))
```

You can also import an entire module, and then access all the values from it using dot notation.
```python=
import random

print(random.randint(0, 10))
```

---

### ~~Exports in Python~~

Unlike JavaScript, Python does not require exports. All of the objects, classes, functions, etc. that are defined in a module are automatically available to import.

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

## Part 2: Decorators

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

## Part 3: Classes

---

### Classes

To create a class we use the `class` keyword, and by convention, we capitalize the names of classes. 

```python=
# python example
class Icon:
    # more code to come
```

Looks a lot like JavaScript
```javascript=
// javascript comparison
class Icon {
    // more code to come
}
```

---

### Initializing classes
Generally speaking:
- Python's `__init__()` is like JavaScript's `constructor()`
- Python's `self` is like JavaScript's `this`

```python=
# python example
class Icon:
    def __init__(self):
        # more code to follow
```

```javascript=
// javascript comparison
class Icon {
    constructor() {
        // more code to follow
    }
}
```

---

### the `__init__()` method

Python's constructor method is called `__init__()`. 
```python=
# python example
class Icon:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
```

```javascript=
// javascript comparison
class Icon {
    constructor(color, shape) {
        this.color = color;
        this.shape = shape;
    }
}
```


---

### Instance variables and methods

You can set attributes on the instance with dot notation (`self.some_attribute = value`).

You can add methods to the class by defining functions and passing in `self`.

```python=
class Icon:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

    def my_method(self, word):
        print(f"hello {word}")
        return
```

---

### Wait, what _is_ `self`?

`self` refers to the instance that a method was called on.

Whenever you invoke a method on an instance of a class, it is as though you are invoking the class's own method, and passing in the instance as an argument.


```python=
some_icon = Icon("blue", "square")
# both below do the same thing
some_icon.my_method("other argument")
Icon.my_method(some_icon, "other argument")
```

---

### Wait, what _is_ `self`?

Calling the first parameter `self` is a convention.


This is technically valid Python, and it would do the same thing as calling it `self`. But no one would write it this way.
```python=
class Icon:
    def __init__(banana, color, shape):
        banana.color = color
        banana.shape = shape
```

---

### Instances of classes

We create instances of a class by invoking the class as though it is a function (this invokes the class's `__init__()` method)
```python=
# in python
my_new_icon = Icon("blue", "circle")
```


```javascript=
// javascript comparison
const myNewIcon = new Icon("blue", "circle");
```


---

### Inheritance

To inherit from another class, we pass a reference to that class as an argument in the class definition.


We can use the `super()` function to get a reference to the parent class, then invoke the desired function.
```python=
class Icon:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape


class Gadget(Icon):
    def __init__(self, color, shape, noise):
        super().__init__(color, shape)
        self.noise = noise


thingie = Icon("purple", "spiral", "whrrrrrr")
print(thingie)  # <__main__.Gadget object at 0x105103d60>
print(thingie.color, thingie.shape, thingie.noise)  # purple spiral whrrrrrr
```

---

### Getters and setters
Getters & setters allow us to have methods that behave like properties.

They provide a convenient interface for implementing more complicated logic necessary for setting a class property.

They can also be useful for protecting "private" values on your class.

---

### Getters

A getter allows you to define a method that behaves like a property. The `@property` decorator over a method creates a getter.

While the getter is a function, it is invoked as if it were a property.

```python=
class Icon():
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
    
    @property
    def info(self):
        print("in the getter!")
        return f"{self.color} {self.shape}"
    
my_icon = Icon("blue", "square")
print(my_icon.color)

# call the getter method as if we were just
# accessing a property
print(my_icon.info)
```

---

### Setters

A setter allows you to define a method that updates the getter "property". The decorator used to create a setter is `@<getter_method_name>.setter`.

You can have a standalone getter, but you must have a getter in order to have a setter. The setter method runs when you change the getter "property."

```python=
class Icon():
    def __init__(self, color, shape, pswd):
        self.color = color
        self.shape = shape
        
        # set initial ~secret~ password
        # this calls the setter method!
        self.my_password = pswd
    
    @property
    def info(self):
        print("in the getter")
        return f"{self.color} {self.shape}"
    
    # getter for ~secret~ password
    @property
    def my_password(self):
        return self._password

    # setter for ~secret~ password
    @my_password.setter
    def my_password(self, new_val):
        print("hashing password....")
        self._password =  str(new_val) + "12345" * 3
        
my_icon = Icon("blue", "square", "beepboop")
print(my_icon.my_password)

# call the setter method as if we were
# setting my_password as a regular property
my_icon.my_password = "new thing"
print(my_icon.my_password)
```

---

### "Private" properties
Python does not really have private attributes. All properties on a class can be accessed from outside the class/instance.

Getters and setters just help us indicate that certain properties should not be directly accessed in this way.

Conventionally, private properties are indicated with a single underscore followed by the property name:

`self._password`

---

### Duck-Typing

"If it looks like a duck, and quacks like a duck, it must be a duck"
- What does it mean for an object to "look/quack like a duck"?
    - it has the relevent "magic method" that python uses to implement a given built-in function (like `len()` or `print()`)
- What does it mean to "be a duck"?
    - that means built-in functions will be able to work on classes that you create
- Why is this good?
    - duck-typing means that classes that you define can work as though they are already part of python!

---

### Duck-typing
Using duck-typing you can:
- have your class work with the addition operator (`+`)
- define what equality operator (`==`) means for your class
- loop over an instance of your class with `for ... in`
- and much more!
- duck-typing is powerful!

---

### Duck-typing

The default value when you print a user-defined class instance is not typically very helpful...
```python=
class Icon:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

my_new_icon = Icon("blue", "circle")
print(my_new_icon)  # <__main__.Icon object at 0x1071cebb0>
```


---

### Duck-typing
You can use the `__repr__` method that will let you control what gets printed for your class.

```python=
class Icon:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape


    def __repr__(self):
        return f"Icon({self.color}, {self.shape})"

my_new_icon = Icon("blue", "circle")
print(my_new_icon)  # Icon(blue, circle)
```

---

## More About Classes

---

### Instance variables
- Specific to each instance of the class—changing on one instance won't affect another
- Defined in the constructor and attached to `self`
- You can access on an instance, but not on the class as a whole


```python=
class Widget:
    # constructor
    def __init__(self, color):
        # instance variables
        self.color = color


my_widget = Widget("blue")
print(my_widget.color)  # "blue"
print(Widget.color)     # error 
```

---

### Class variables
- Shared across instances and on the class itself
- Each instance points to the same class variables, so updating the value on the class will change for all instances (unless their value was already changed)
- Updating on one instance will not change other instances


```python=
class Widget:
    price = "$5"
    def __init__(self, color):
        # instance variables
        self.color = color


my_widget = Widget("blue")
second_widget = Widget("chartreuse")
print(my_widget.price)  # "$5"
print(Widget.price)     # "$5"
my_widget.price = "$100"
print(second_widget.price) # "$5"
print(Widget.price)        # "$5"
Widget.price = "$50"
print(second_widget.price) # "$50"
print(my_widget.price)     # "$100"
```



---


### Instance methods
So far, we've written instance methods on classes—that is the default type of method on a class.
- `self` is passed in implicitly as the first parameter—this refers to the instance the method was invoked on

```python=
# inside class
def greet_widget(self):
    return f"hello, {self.color} widget"

my_widget = Widget("blue")
print(my_widget.greet_widget())  # "hello blue widget"
```

---

### Class methods
We can use the `@classmethod` decorator to write class methods. 

The first argument will refer to the class itself (conventionally called `cls`), rather than an individual instance.

```python
# inside class
@classmethod
def widget_factory(cls, colors):
    widgets = [cls(color) for color in colors]
    print([widget.greet_widget() for widget in widgets])
    return widgets


print(Widget.widget_factory(["red", 
"yellow", "beige"]))
```

---

### Static methods
Static methods don't take implicit arguments—they can't access the class or any instance of it.
```python=
@staticmethod
def something_about_widgets():
    return "widgets are neat"
```

---

## Today's projects

We have 2 projects today:
1. Refactor Manager and Employee Salaries
    - This is a project you've already done in JS - now translate it to Python!
2. Linked List
    - Use what you've learned about classes to implement a singly linked list

---

## Using Classes to Implement a Node

We can use what we learned about classes to represent a node in a linked list. In a singly linked list, each node will have a value and a reference to the next node in the list.

```python=
class Node:
  def __init__(self, value):
    self._value = value
    self._next = None
```

---


## Using Classes to Implement a Linked List

We can also represent an entire linked list as a class. The linked list class will need a reference to the head and tail nodes as well as the length of the list:

```python=
class LinkedList:
  def __init__(self):
    self._head = None
    self._tail = None
    self._length = 0
```

You will also need to add a suite of methods to the linked list class to implement operations to the list, e.g., adding nodes, removing nodes, etc.
