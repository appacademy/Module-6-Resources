<style>
    .present {
        text-align: left;
    }
</style>

---

###### tags: `Week 17` `W17D2` `W17D1`

---

# Python Data Types & Basic Control Flow
## Week 17 Day 2

---

## Boolean Logic

---

In Python, the Boolean values `True` and `False` are represented in title case.

Equality comparison operators (`==`, `!=`, `<`, `>`, `^`, etc.) return Boolean values.

---

### Truthiness & Falsiness

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

We can group conditions with parentheses.

Python will short-circuit on a logical statement if it can already determine the outcome:

```python=
False and print("not printed")  # does not print
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

### Boolean Practices (15 min)
Using Not Or - 2 min
Length of List - 2 min
Has Remainder - 2 min
Xor - 2 min
DeMorgan's Law - Challenge - 10 min


---


## Strings

---

Just like JavaScript, strings in Python are immutable collections of characters.

- In Python, single quotes (`'`) and double quotes (`"`) are interchangeable
- Using three quotes in a row (either `"""` or `'''`) will open a multiline string
```python=
my_long_string = '''
you can make
longer strings over multiple lines
individual quote characters ' " won't end the string
'''
```

---

### String Interpolation

In Python version 3.6, `f` strings were introduced as the preferred method of string interpolation.

String formatting with `f` strings:
```python=
word = "hi"
num = 6
print(f"{word} and {num}")
```

Similar to interpolated strings in JavaScript:
```javascript=
let word = "hi"
let num = 6
console.log(`${word} and ${num}`)
```

You can read about more [traditional methods of string interpolation in the PEP 498 documentation](https://peps.python.org/pep-0498/)!

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

- Can index a range with ``[start:stop]``. The `stop` value is excluded from the resulting range!
```python=
# indexing with ranges
print("Spaghetti"[1:4])   # pag
print("Spaghetti"[4:-1])  # hett
```

---

### Built-in string methods

There are many built-in methods on the string data type in Python:
- `.index()`: returns the first index where a substring is found
- `.count()`: returns the number of times a substring is found
- `.split()`: returns a list of substrings, split on a character or substring
- `.join()`: use a given string to join all the substrings from a list
- `.upper()`, `.lower()`, and `.title()`: transform a string to the specified case

And many more!

---

### String Practices (35 min)
Indexing Strings - 2 min
String Immutability - 2 min
Index Of - 2 min
Is The Last Character N? - 3 min
Burrrrrp - 5 min
Last Three - 5 min
Is Palindrome - 5 min
Recursive String - 5 min


---

## Numbers

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

### Number Practices (35 min)
Integer Division - 2 min
Total Digits - 5 min
Perfect Square - 2 min
Recursive Fibonacci - 10 min
Recursive Countdown - 10 min
Recursive Is Prime - Challenge - 10 min


---

## Operators

---

### Identity vs. Equality

In Python, we have `is` to compare identity and `==` to compare equality. 

Both are useful, just for different purposes.

---

### Equality Comparison

- In JavaScript, `===` is preferred because it does strict equality comparison (value and type)
- In Python, equality is not about typechecking, it's just about whether the values are the same
```python=
my_int = 4
my_float = 4.0

# check if the values are the same
print(my_int == my_float)  # True

# check if the values are the same and check type
print(my_int == my_float and isinstance(my_int, float))  # False
```

---

### Equality Comparison

#### When to use `==` (equality):
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

### Equality Comparison

Equality comparison operators (`==`, `!=`, `<`, `>`, `^`, etc.) return Boolean values.

---

### Identity Comparison

The `is` operator in Python compares identity. 

The identity of an object is an integer guaranteed to be unique and constant for an object during its lifetime (i.e. while the program is running). It is the object's memory address!

We can use the built-in `id()` function to get the identity of an object.

```python=
a = None
print(id(a))
```

---

#### The `is` operator

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

### Operators Practices (18 min)
First Before Second - 10 min
Equality in Python - 2 min
Comparison in Python - 2 min
Largest Perimeter Triangle - Challenge - 15 min


---

## Statements

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

### For loops

- `for` keyword to start the loop
- `in` iterates over each element in the sequence
- We do not need to define an iterator variable!

```python=
items = ['a', 'b', 'c']

for item in items:
    print(item)
```

---

### The `in` keyword

The `in` keyword can be used on its own to lookup a value in a collection:

```python=
my_nums = [1, 2, 3]

print(4 in my_nums) # False
```

---

### Try/Except statements

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

### Statements Practices(60 min)
Try/Except - 2 min
Print List - 2 min
Check Membership - 2 min
Double That Penny - 5 min
Valid Hex Code - 10 min
Sequence of Numbers - 30 min  (save this one for last)
Split On Capitals - 10 min
Count Characters In String - 5 min
Vowel Count - 2 min
Add Upper - 2 min
Regex - Challenge - 10 min



---

## Functions

---

### Python Functions
- We use the `def` keyword to define a function followed by:
    - The name of the function
    - The parameters that it accepts
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
    -  Parameters on left side of `:`
    -  Returns the value resulting from the right side of the `:`
-  They return automatically and cannot contain an explicit `return` keyword
-  Lambda functions are meant to be anonymous, one-liner functions


```python=
is_even = lambda num: num % 2 == 0

print(is_even(8)) # True
```

---

### Python Scoping

- Scoping is done at the function (and class) level
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

### Function Practices (18 min)
Fun With Functions - 5 min
Function Arguments - 2 min
Using Lambdas - 2 min
Add Binary Leet Code Challenge - 5 min
Merge Helper - Challenge - 20 min


---

## Lists

---


Lists are mutable, ordered collections (like arrays in JavaScript). Use square brackets to make lists.

```python=
empty = []
print(empty)   # []
```

Values are separated by commas.
```python=
fruits = ["banana", "apple", "kiwi"]
print(fruits)  # ["banana", "apple", "kiwi"]
```


---

### Indexing with lists

Indexing with lists uses the same syntax as indexing with strings:

- Single index: `list_name[single_index]`
- Index range: `list_name[start:stop:step]`

---

### Built-ins functions & methods

- `len()`: function that gets the length of an iterable
- `.append()`: append one element to the end of a list
- `.extend()`: add all individual elements of an iterable to the end of a list
- `.remove()`: remove the first instance of a given value from a list
- `.sort()`: sort a list in place (with Timsort)
- `sum()`, `min()`, `max()`: get the sum, minimum value, or maximum value of a list of numerics

---

### List Practices (45 min)
Explore The List - 5 min
Return First Element Of A List - 2 min
Sum The Elements Of A List - 5 min
First And Last Entries - 1 min
First Last List - 5 min
Insertion Sort - 20 min
All Occurrences Of A Value In A List - 5 min
Find Target Indices Leet Code - 10 min
Matrix Diagonal Sum - Leet Code Challenge - 10 min


---
