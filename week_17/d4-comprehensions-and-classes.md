# More Built-ins, Comprehensions, and Classes
## Week 17 Day 4

---

## Part 1: More Built-ins

---

### Lecture Videos (22 minutes)
Watch:
- Built-Ins: All And Any (8:00)
- Built-Ins: Filter and Map (10:32)

---

### Built-in functions: `all()`
`all()` returns `True` if *all* items in a collection are truthy or if the iterable is empty.

It returns `False` if there is at least one falsey item.

```python=
test1 = {"item", "truthy", ""}
test2 = []
test3 = [[]]
print(all(test1))
print(all(test2))
print(all(test3))
```

---

### Built-in functions: `any()`
`any()` returns `True` if there are *any* truthy items in the provided collection.

It returns `False` if there are no truthy items or if the iterable is empty.

```python=
test1 = ["item", [], []]
test2 = []
test3 = [[]]
print(any(test1))
print(any(test2))
print(any(test3))
```

---

### Built-in functions: `filter()`
`filter()` takes in a function and an iterable as arguments and returns a *filter object*.

The returned collection includes only the items which, when the function parameter was applied to them, returned a truthy value.

`filter()` does not filter in place. It returns an entirely new object.

```python=
def is_a(num):
    if num >= 90:
        return True
    else:
        return False


scores = [90, 86, 75, 91, 62, 99, 88, 90]
only_as = filter(is_a, scores)  # does not mutate original
print(only_as)                  # <filter object at 0x10546ad30>
print(list(only_as))            # [90, 91, 99, 90]
```


---

### Built-in functions: `filter()`
`filter`'s function parameter can also be defined in line as a `lambda` function.
```python=
scores = [90, 86, 75, 91, 62, 99, 88, 90]
only_as = filter(lambda num: num >= 90, scores)
print(only_as)        # <filter object at 0x10546ad30>
print(list(only_as))  # [90, 91, 99, 90]
```

---

### Built-in functions: `map()`
`map()` takes in a function and an iterable as arguments and returns a *map object*.

`map()` transforms each value from the original iterable according to the provided function and returns them in a new object.

```python=
def get_grade(num):
    if (num >= 90):
        return "A"
    elif (num <90 and num >= 80):
        return "B"
    elif (num < 80 and num >= 70):
        return "C"
    elif (num < 70 and num >= 60):
        return "D"
    else:
        return "F"
scores = [90, 86, 75, 91, 62, 99, 88, 90]
print(map(get_grade, scores))  # <map object at 0x106faffa0>
grades = list(map(get_grade, scores))
print(grades)                  # ['A', 'B', 'C', 'A', 'D', 'A', 'B', 'A']

```

---

### Built-in functions: `zip()`
`zip()` takes two iterables as arguments and returns a *zip object* that pairs values at corresponding indices.

You can typecast the *zip object* as a sequence of tuples or as a dictionary.

```python=
scores = [90, 86, 75, 91, 62, 99, 88, 90]
grades = ["A", "B", "C", "A", "D", "A", "B", "A"]
combined = zip(scores, grades)
combined_list = list(combined)
combined_dict = dict(combined_list)
print(combined)       # <zip object at 0x1023a9600>
print(combined_list)  # [(90, 'A'), (86, 'B'), (75, 'C'), (91, 'A'), (62, 'D'), (99, 'A'), (88, 'B'), (90, 'A')]
print(combined_dict)  # {90: 'A', 86: 'B', 75: 'C', 91: 'A', 62: 'D', 99: 'A', 88: 'B'}
```

---

## Part 2: Comprehensions

---

### Lecture videos (22 minutes)
Watch:
- List Comprehensions Demo (18:50)

---

### Comprehensions

Comprehensions are composed of an expression followed by a `for...in` statement, followed by an optional `if` clause. They can be used to create new lists (or other mutable sequence types).


```python=
my_list = [expression for member in iterable]
# with optional if statement
my_list = [expression for member in iterable if condition]
```

---

### Copying a list
With a `for` loop:
```python=
my_list = [1, "2", "three", True, None]
my_list_copy = []
#     for loop
#    ----------
# /               \
for item in my_list:
    my_list_copy.append(item)
#                        |
#                       var
print(my_list_copy)  # [1, '2', 'three', True, None]
```

---

### Copying a list

With a list comprehension:
```python=
my_list = [1, "2", "three", True, None]
#              var         for loop
#               |        -------------
#               |      /              \
my_list_copy = [item for item in my_list]

print(my_list_copy)  # [1, '2', 'three', True, None]
```

---

### Mapping over a list with comprehensions
Include the desired expression before the `for` statement

```python=
my_list = ["jerry", "MARY", "carrie", "larry"]
#          expression            for loop
#               |               -------------
#               |             /              \
mapped_list = [item.lower() for item in my_list]

print(mapped_list)  # ['jerry', 'mary', 'carrie', 'larry']
```

---

### Convert `map()` to list comprehension

```python=
nums = [-5, 11, 10, 14]
mapped_nums = map(lambda num: num * 2 + 1, nums)

print(list(mapped_nums))  # [-9, 23, 21, 29]
```

---

### Convert `map()` to list comprehension
Answer:
```python=
nums = [-5, 11, 10, 14]
# mapped_nums = map(lambda num: num * 2 +1, nums)
mapped_nums = [num * 2 + 1 for num in nums]

print(mapped_nums)  # [-9, 23, 21, 29]
```

---

### Filtering a list with comprehensions
```python=
nums = [-5, 11, 10, 14]

filtered_nums = filter(lambda num: num > 0, nums)

print(list(filtered_nums))  # [11, 10, 14]
```

---


### Filtering a list with comprehensions
Answer:
```python=
nums = [-5, 11, 10, 14]

# filtered_nums = filter(lambda num: num > 0, nums)
filtered_nums = [num for num in nums if num > 0]

print(filtered_nums)  # [11, 10, 14]
```

---

### Nested loops

Nested for loop:
```python=
letters = ["a", "b", "c"]
nums = [1, 2]

new_list = []

#  outer loop
#  ----------
# /          \
for l in letters:
    for n in nums:  # <- inner loop
        new_list.append((l, n))
#                        \   /
#                         ---
#                      expression

print(new_list)  # [('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)]
```


---

### Nested loops (list comprehension)

With list comprehension—note that the outer loop is first:
```python=
letters = ["a", "b", "c"]
nums = [1, 2]
#       expression    outer loop     inner loop
#            ---    --------------   -----------
#           /   \  /              \ /           \
new_list = [(l, n) for l in letters for n in nums]

print(new_list)  # [('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)]
```

---

### Dictionary comprehensions

Use a colon in the expression to separate the key and value.

```python=
# a dictionary that maps numbers to the square of the number
number_dict = {num: num**2 for num in range(5)}
print(number_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## Part 3: Classes

---

## Lecture videos (23 minutes)
Watch:
- Classes in Python Demo (19:18)

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
