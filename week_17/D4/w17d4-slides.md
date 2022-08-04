<style>
    .present {
        text-align: left;
    }
    img[alt=set_operations] {
        width: 60%;
        
    }
</style>

---

###### tags: `Week 17` `W17D4`

---

# Python Imports, Decorators, and Classes
## Week 17 Day 4

---

## Today's Topics
- Importing
- Decorators
- Classes
   - Basic Class Syntax
   - Inheritance
   - Polymorphism

---

## The Python Import System

---

To import code from a module, we use the `import` keyword. The import keyword will locate and initialize a module, and give you access to the specific names you have imported in the file.

There are no exports in Python! Anything we define in a module/file is automatically available for import.

---

### The `import` keyword
The Python standard library has a number of packages you can import without having to install them. Let's use the `random` package as an example (this would work the same with any package).

```python=
import random  # import everything from random
print(random.randint(0, 10))
```
Use the `as` keyword to alias package/object names.
```python=
import random as rand  # import everything, alias random as rand
print(rand.randint(0, 10))
```
You can also import specific objects from a package using the `from` keyword.

```python=
from random import randint, shuffle  # import multiple functions at the same time
print(randint(0, 10))
```

---


### Import Python code from another file
If two files are at the same level, import using the filename (without the `.py` extension).
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

If we need to specify a path to a file, we use dot notation:

```python=
# inside my_code.py
from folder.subfolder.filename import something
```

---

###  `__init__.py`

This file should go in any directory being imported. It will transform a plain old directory into a Python module/package. It can be completely empty, and often will be!

Upon import from a module/package,  its`__init__.py` file is implicitly executed, and all objects it defines are bound to the module's namespace ([documentation](https://docs.python.org/3/reference/import.html#regular-packages)).

---

### Import Practices (25 min)
Import Quiz - 3 min
Python Import Short Practice - 15 min


---

## Decorators

---

### What's a decorator?

A decorator is a function that takes in another function as a callback and modifies or extends the behavior of the callback function.

---

### Decorator Reading & Video (25 min)
Decorators - 10 min
Decorators Demo - 11 min


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

### Decorator Practices (35 min)
Decorators Quiz - 5 min
Hello World Decorator - 3 min
Order Decorator - 3 min
Timer Decorator - 10 min
Chain Decorator - 10 min
 

---

### Classes

---

To create a class we use the `class` keyword, and by convention, we capitalize the names of classes. 

```python=
# python example
class Icon:
    # more code to come
```

Python's constructor method is called `__init__()`.
```python=
# python example
class Icon:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
```

---

### Instances of classes

We create instances of a class by invoking the class as though it is a function (this invokes the class's `__init__()` method).
```python=
# in python
my_new_icon = Icon("blue", "circle")
```

---

### Wait, what _is_ `self`?

`self` refers to the instance that a method was called on.

Whenever you invoke an instance method on a class instance, it is as though you are invoking the class's own method, and passing in the instance as an argument.

```python=
some_icon = Icon("blue", "square")
# both below do the same thing
some_icon.my_method("other argument")
Icon.my_method(some_icon, "other argument")
```

---

### Instance variables and methods

You can set attributes on the instance with dot notation (`self.some_attribute = value`).

You can add instance methods to the class by defining functions and passing in `self`.

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

### Class variables

Class variables are not attached to `self`. They are available for access on the class itself and across instances.

If we update a class variable on an instance, a shadow instance variable is created that hides the class variable of the same name.

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

### Getters and setters
Getters & setters allow us to have methods that behave like properties.

They provide a convenient interface for implementing more complicated logic necessary for getting/setting a class property.

They can also be useful for protecting "private" values on your class.

---

### Getters

A getter allows you to define a method that behaves like a readable property. The `@property` decorator over a method creates a getter.

While the getter is a function, it is invoked as if it were a property.

```python=
class Icon():
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
    
    # getter for ~secret~ password
    @property
    def my_password(self):
        return "somebody's secret password"
    
my_icon = Icon("blue", "square")
print(my_icon.color)

# call the getter method as if we were just
# reading a property
print(my_icon.my_password)
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

### Basic Class Syntax Practice (35 min)
Bad Calculator - 10 min
Getters and Setters - 10 min
Regular Polygon - 15 min
Tree Traversal - Challenge - 15 min


---

### Inheritance

---

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

### Class Inheritance Practice (30 min)
Quadrilateral with Inheritance - 10 min
Triangle with Inheritance - 10 min


---

### Polymorphism

---

In OOP, polymorphism allows us to have methods/attributes that behave differently for different classes.

Polymorphism is tied to inheritance. When a child class inherits from a parent class, that child class can override methods from the parent class.

---

With polymorphism, we can have our `Gadget` class redefine a method from our parent `Icon` class:

```python=
class Icon:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
        
    def info(self):
        return f"Icon that is a {self.color} {self.shape}"


class Gadget(Icon):
    def __init__(self, color, shape, noise):
        super().__init__(color, shape)
        self.noise = noise
    
    def info(self):
        return f"Gadget that is a {self.color} {self.shape} and makes a {self.noise} noise"

icon = Icon("blue", "square")
print(icon.info())

thingie = Gadget("purple", "spiral", "whrrrrrr")
print(thingie.info())
```

---

### Duck-Typing

"If it looks like a duck, and quacks like a duck, it must be a duck"

We can implement polymorphism with duck typing. All classes in Python automatically inherit from the `object` parent class, which defines certain magic methods.

We can redefine these magic methods on classes we implement!

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

### Polymorphism Practices (40 min)
Book Polymorphism - 10 min
Magic Methods - 10 min
Linked List Iterator - 20 min

### Long Practice (2 hrs)
Linked List Project - 2 hrs

---
