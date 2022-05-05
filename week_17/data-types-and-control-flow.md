# Python Data Types & Basic Control Flow

---

## Part 1: Python Basics

---

### `print()`

We can use `print` to write messages to the console terminal
```python=
print("Hello world")
```

Equivalent to `console.log` in JavaScript
```javascript=
console.log("Hello world")
```


---

### Commenting code

In Python, comments start with `#`
```python=
# this is a comment
print("Hello")  # can also start in line 
```

Just like the `//` in JavaScript
```javascript=
// this is a comment
console.log("Hello world") // can also start in line 
```

---

### Commenting code

Longer comment blocks can use the `"""` syntax
```python=
"""
You can use three quotes in a row
for multiline comments
"""
```


Like in JavaScript, where `/* ... */` creates multiline comments
```javascript=
/* 
longer comment
more commenting here
*/
```

---

### Docstrings

A docstring is a string literal that is used to document a function, class, or module.

```python=
def my_function():
    """
    This is my function. It doesn't do
    anything special. It's just a
    function.
    """
    return 1
```

We can access docstrings in two ways:
```python=
help(my_function)
print(my_function.__doc__)
```

---

### Number Data Types
We'll mostly interact with `int` and `float` types
- `int` (integers): counting numbers with no decimal points
- `float` (floating point numbers): numbers with decimal places.
    - They may occasionally have rounding errors, just like JavaScript
    - see [documentation on floating point arithmetic](https://docs.python.org/3/tutorial/floatingpoint.html)
- `complex`: complex numbers 

---

| Operator | Meaning          | Example                |
| :------: | :--------------- | :--------------------- |
|   `+`    | addition         | `print(10+4)  # 14`    |
|   `-`    | subtraction      | `print(10-4)  # 6`     |
|   `*`    | multiplication   | `print(10*4)  # 40`    |
|   `/`    | division         | `print(10/4)  # 2.25`  |
|   `%`    | modulo           | `print(10%4)  # 2`     |
|   `**`   | exponent         | `print(10**4) # 10000` |
|   `//`   | integer division | `print(10//4) # 2`     |

---

### Number Operations
- Plus operator (`+`) can be used for both numeric addition and string concatenation
- But type conversion between strings and numbers won't happen automatically (unlike JavaScript)
```python=
print("hello " + "world")  # "hello world"
print("hello " + 7)        # TypeError
# explicitly convert types
print("hello" + str(7))    # "hello7"
```

---

### Assignment operators
We can use assignment operators (like in JavaScript) to concisely update values
```python=
a = 2
a += 3 
print(a)  # 5
a *= 2
print(a)  # 10
```
But no more `++` or `--`
```python=
a++       # SyntaxError: invalid syntax
```

---

## Part 2: Strings

---

### String Data Type

- Strings use single quotes (`'`) or double quotes (`"`)
- Using three quotes in a row (either `"""` or `'''`) will open a multiline string
```python=
my_long_string = '''
you can make
longer strings over multiple lines
individual quote characters ' " won't end the string
'''
```

---

### String Interpolation (Good)

String formatting with `%` operator
```python=
word = "hi"
num = 6
print("%s is a word. %i is an integer" % (word, num))
# prints "hi is a word. 6 is an integer"
```

---

### String Interpolation (Better)

String formatting with `.format()` method
```python=
word = "hi"
num = 6
print("{stuff} and {number}".format(stuff=word, number=num))
# prints "hi and 6"

# positional
print("{1} is a value, so is {0}".format(word, num))
```

---

### String Interpolation (Best)

String formatting with `f` strings
```python=
word = "hi"
num = 6
print(f"{word} and {num}")
```

Most similar to interpolated strings in JavaScript:
```javascript=
let word = "hi"
let num = 6
console.log(`${word} and ${num}`)
```

---

### String Arithmetic

```python=
a = "a"
b = "b"
an = "an"

print(b + an)
print(b + a*7)
print(b + an*2 + a)

print("$1" + ",000"*3)
```


---

### String indexing

- Use square brackets (`[]`)
- Index starts at 0 (like in JavaScript)
```python=
print("Spaghetti"[0])  # S
print("Spaghetti"[4])  # h
```

- Can use a negative index
```python=
print("Spaghetti"[-1])
print("Spaghetti"[-4])
```

---

### String indexing

Indexing with ranges: the start value is inclusive, the end value is skipped
```python=
# indexing with ranges
print("Spaghetti"[1:4])   # pag
print("Spaghetti"[4:-1])  # hett
print("Spaghetti"[4:4])   # (empty string)
print("Spaghetti"[:4])    # Spag
print("Spaghetti"[:-1])
print("Spaghetti"[1:])
print("Spaghetti"[-4:])
```

---

### String indexing

Out of range values will through errors if you try to access the single value, but they are valid as part of a range.
```python=
print("Spaghetti"[15])     # IndexError: string index out of range
print("Spaghetti"[-15])    # IndexError: string index out of range
print("Spaghetti"[:15])    # Spaghetti
print("Spaghetti"[15:])    # (empty string)
print("Spaghetti"[-15:])   # Spaghetti
print("Spaghetti"[:-15])
print("Spaghetti"[15:20])
```

---

### String methods: `.index()`
Returns the first index where the substring is found
```python=
print("kiwi".index("k"))  # 0
print("kiwi".index("m"))  # ValueError: substring not found
```

---

### String methods: `.count()`
Returns the number of times the substring is found
```python=
print("kiwi".count("k"))  # 1
print("kiwi".count("i"))  # 2
print("kiwi".count("m"))  # 0
```

---

### String methods: `.split()`

Returns a list (array) of substrings, split on the character (or substring) passed
- If no character is passed, a space is used to split

```python=
print("Hello World".split())     # ["Hello", "World"]
print("Hello World".split(" "))  # ["Hello", "World"]
print("i-am-a-dog".split("-"))   # ["i", "am", "a", "dog"]
```

---

### String methods: `.join()`

Use a given string to join all the substrings from the list argument
- Works in reverse from what you may be used to with JavaScript

```python=

print(" ".join(["Hello", "World"]))       # "Hello World"
# ["Hello", "World"].join(" ") JavaScript
print("-".join(["i", "am", "a", "dog"]))  # "i-am-a-dog"
```


---

### String methods: `.upper()` & `.lower()`
Transform a string to the specified case
- these methods return an entirely new string - they do not mutate the original string
```python=
a = 'Hello'
print(a)          # 'Hello'
print(a.upper())  # 'HELLO'
print(a)          # 'Hello'
```

---

## Part 3: Try/Except Statements

---

#### Better to ask forgiveness than permission

A pythonic principle & fundamental part of Python control flow

---

### Control flow with `try/except` blocks

Keywords:
- `try`: run this code until an exception occurs
- `except`: run this code when an exception occurs
- `else`: run this code only if no exception occurs
- `finally`: run this code no matter what


---

### Control flow with `try/except` blocks

```python=
num = 0
try:
    print("Trying now...")
    print(4/num)
except ZeroDivisionError:
    print("oops i tried to divide by zero!")
finally:
    print("this happens no matter what")
```


---

### Control flow with `try/except` blocks

Avoid using a bare `except`— you should specify the type of error in almost every case.

Different exceptions should be handled differently because they indicate different types of issues.

A bare `except` can even prevent a user from exiting a program:
```python=
while True:
    try:
        num = int(input("say a number "))
        print(num)
        break
    except:
        print("try again")
```

---

## Part 4: Identity & Equality

---

### Truthiness vs. `True`

The concept of "truthiness" refers to values that *evaluate* to `True` when typecast as a Boolean.

"Truthy" values however are not necessarily *equal* to `True`.

---

### Falsiness

Falsey values in Python are:
- 0 (for any number type)
    - `0`, `0.0`, `0j`
- any empty collection
    - `""`, `[]`, `set()`, `{}`, `range(0)`
- `False`
- `None`

All other values are truthy!

---

### Logic Operators
We use the keywords `and`, `or`, and `not` in Python instead of `&&`, `||`, and `!`
```python=
print(True and False)      # False
print(True or False)       # True
print(True and not False)  # True
```

---

### Logical operators
Parentheses can group our conditions, just like JavaScript
```python=
print(False and (True or True))  # False
print((False and True) or True)  # True
```

---

### Short circuiting
If we can already determine the overall outcome of a conditional, Python won't bother evaluating the rest of the statement.

(JavaScript also has short-circuiting)

```python=
False and print("not printed")  # does not print
False or print("printed #1")    # prints "printed #1"
True and print("printed #2")    # prints "printed #2"
True or print("not printed")    # does not print
```

---

### If statements

If statement structure resembles Javascript. 

In Python, the if statement keywords are:
- `if`
- `elif`
- `else`

```python=
if i < 4:
    print("i is less than 4")
elif i == 4:
    print("i is equal to 4")
else:
    print("i is neither less than nor equal to 4")
```

---

### While loops

While loops also follow a very similar structure to JavaScript.

```python=
i = 0
while i < 5:
    print(f"{i}. Hello, world.")
    i += 1

print("You've printed 5 times. Goodbye.")
```

---

### Loop keywords: `continue` and `break`

- `continue`: goes to the next iteration of the loop
- `break`: exits out of the loop completely
```python=
i = 0
while True:
    print(f"{i}. Hello, world.")
    if i < 4:
        i += 1
        continue
    print("You've printed 5 times. Goodbye.")
    break
```

---

### Identity vs. Equality
- in JavaScript, `==` is bad, `===` is good
- in Python, `is` and `==` are both useful, just for different things
- Equality is not about typechecking, it's just about whether the values are the same
```python=
my_int = 4
my_float = 4.0

# check if the values are the same
print(my_int == my_float)  # True

# check if the values are the same and check type
print(my_int == my_float and isinstance(my_int, float))  # False
```

---

### When to use `==` (equality):
- Most of the time!
- Whenever you are comparing two values to see if they are the same
    - strings, numbers, lists, dictionaries, etc
```javascript=
// javascript version
console.log([1, 2, 3] === [1, 2, 3]) 
// false
```
```python=
# python version
print([1, 2, 3] == [1, 2, 3]) 
# True
```

---

### The `is` operator

What if we compared two lists of the same value with `is`?
```python=
print([1, 2, 3] is [1, 2, 3]) 
# False
```

While these lists have the same *value*, they are two distinct objects in memory with different identities.

---

### When to use `is` (identity) [1/3]:
1. For checking if a value is not `None`
```python=
a = []

if a is not None:
    print("a is not None")  # prints "a is not None"
else:
    print("a is None")

```

---

### When to use `is` (identity) [2/3]:

2. For checking is `True` / `False`
```python=
a = 1
print(a == True)  # don't do this, in Python 1 is equal in value to True
print(a is True)
```

---

### When to use `is` (identity) [3/3]:
3. For checking whether variables reference the same object in memory
```python=
print([] == [])  # True
print([] is [])  # False
a = []
b = a
print(a is b)    # True
b.append(5)
print(a)         # [5]
```

---

### Interned memory
For many small, immutable (unchangeable) data types, Python stores only one distinct copy in memory. 

This is a space optimization mechanism called *interning*.

```python=
# python version
a = 5
b = 5
print(a is b) # True

c = "hey"
d = "hey"
print(c is d) # True
```

Due to interning, these variables can share the same identity if they have equal value.

---

### What is the "identity"

`id()` returns the “identity” of an object. 
- Integer which is guaranteed to be unique and constant for this object during its lifetime (i.e. while the program is running)

```python=
print(id(None))
print(id(None))
a = None
print(id(a))
```

---

## Part 5: Functions

---

### Python Functions
- We use the `def` keyword to define a function followed by:
    - The name of the function
    - The arguments that it accepts
    - A new block identified as `:` and indent the next line
```python=
def is_even(num):
    return num % 2 == 0

print(is_even(5)) # False
print(is_even(2)) # True
```

---

### Lambda Functions

- For simple one-line functions, we can also use a lambda, which takes in:
    -  Arguments on left side of `:`
    -  Returns the value resulting from the right side of the `:`
-  They return automatically and cannot contain an explicit `return` keyword
```python=
is_even = lambda num: num % 2 == 0

print(is_even(8)) # True
```


---

### PEP-8 Style Guidlines

- The use case of lambdas is when you are going to use a function once without assigning it
- Assigning a lambda to a variable essentially duplicates the purpose of the def keyword, hence it is not pythonic


---

### Functions Returning Functions

```python=
def order_pizza(pizza_type):
    order = f"I would like a {pizza_type} pizza"
    print(pizza_type)
    return lambda topping_type: order + f" with {topping_type}."

sausage_pizza = order_pizza("sausage") 
# prints from line 3: "sausage" 

print(sausage_pizza)
# prints lambda function object

print(sausage_pizza("bell pepper")) 
# "I would like a sausage pizza with bell pepper."
```

---

### Python Scoping

- Scoping is done at the function level
    - In JS, we had block scopes
    - In PY, our `if` statements do not create new scopes

```python=
def make_a_five():
    y = 5
    return y

if True:
    x = 10


print(x) #10
# `x` was created in the global scope

print(y) # NameError: name 'y' is not defined
# `y` was created in the scope of the make_a_five function
```
