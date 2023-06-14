<style>
    .present {
        text-align: left;
    }
    img[alt=set_operations] {
        width: 60%;
        
    }
</style>

---

###### tags: `Week 17` `W17D3`

---

# Structured Data
## Week 17 Day 3


---

## Today's Topics:
Tuples
Ranges
Dictionaries
Sets
Built in Functions
List Comprehensions


---

### Structured Data Quizzes (10 min)

Define Structured Term Data - 5 min
Structured Data Quiz - 5 min


---

### Tuples

Docs link:
https://docs.python.org/3.9/library/stdtypes.html?highlight=tuple#tuple


---

Tuples are an ordered, immutable collection type. 

They are defined using parentheses `()`, with values separated by a comma.



```python=
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = ('a', 'b', 'c', 'd', 'e')
c = 10, 20, 30

print(a)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(b)  # ('a', 'b', 'c', 'd', 'e')
print(c)  # (10, 20, 30)
```

---

### Tuples are immutable

- You cannot append, remove, or sort the tuple in place. 
- We can concatenate tuples together, but the result will be an entirely new tuple

```python=
tup = ("red", "blue")
tup = ("yellow", "green")  # no error, this works
print(tup)                 # ("yellow", "green")
tup += ("red", "blue")    # no error, this works
print(tup)                 # ("yellow", "green", "red", "blue")
```

---

### Empty or "Singleton" Tuples
- An empty tuple must be defined using parentheses ()
```python=
empty = ()
```
- A tuple with a single value must have a trailing comma
```python=
single = (1,) 
single = 1,
```


---

### Sorting

The `sorted()` function works on tuples, just like lists. This will return a list by default.

```python=
fruits = ("banana", "apple", "kiwi")
print(sorted(fruits))  # ['apple', 'banana', 'kiwi']
sorted_fruits = tuple(sorted(fruits))
print(sorted_fruits)
print(fruits)
```

---

### Tuple Practices (35 min)
Explore the Tuple - 5 min
Sort Tuple - 3 min
Add Value - 3 min
Concat Tuple - 3 min
Big Words - 3 min
Recursive Add - 5 min
Index Sort - 5 min
Fill Tuple - 5 min
Bubble Sum - Challenge - 20 min
Tuple With Same Product - Challenge - 20 min


---

## Ranges

Docs link:
https://docs.python.org/3.9/library/stdtypes.html?highlight=range#range

---

### The `range` object

- An immutable sequence of numbers in order
- Arguments:
  - start (default 0)
  - stop (required)
  - step (default 1)
- Can go in forward or reverse order
- Range is exclusive(the stop argument is not included in the returned list)

---

### Declaring Basic Ranges

```python=
numbers_range = range(10)
print(list(numbers_range))

reversed = range(51, 5, -1) 
print(list(reversed))
```

---

### For loops and the `range` object

`range` gives us access to both the current element and its index in the list

```python=
items = [1, 2, 3]

for i in range(len(items)):
    print(i, items[i])

for i in range(1, 10, 2):
    print(i)
```

---

### Iterating over Collections with `enumerate()`

The built-in function `enumerate()` gives us both an item and its index in a sequence/iterator.

`enumerate()` takes in a sequence and returns an enumerate object. 

This object can be typecast as a sequence of tuples, where each tuple contains both an element and its index in a sequence/iterator.

```python=
items = ['a', 'b', 'c']

enumerated_items = enumerate(items)
print(enumerated_items)

enumerated_list = list(enumerated_items)
print(enumerated_list)

for i, element in enumerated_list:
    print(i, element)
```

---

### Range Practices (35 min)
Explore the Range - 5 min
Range Loops - 2 min
Factorial - 5 min
Check Nested Arrays - 10 min
Maximum Difference - 5 min
Find The Smallest Number In A List - 5 min
Range List - Challenge - 5 min
Range Sum of BST - Challenge - 10 min


---

## Dictionaries

Docs link:
https://docs.python.org/3.9/library/stdtypes.html?highlight=tuple#dict

---

- Dictionaries are ordered and mutable. 
- They consist of pairs of keys and values. 
    - The keys must be "hashable" (immutable) values
    - e.g. keys can be strings, numbers, tuples, booleans, but not lists or dictionaries
- Dictionaries use curly braces, similar to JavaScript objects, although keys do not have to be strings.
    - but if the keys _are_ strings, they must use quotes, unlike JS

---

### What's Hashable?

An object is hashable if it has a hash value that does not change during its lifetime.

In Python, all immutable objects are hashable. We know that accessing that object by its hash value will always give us the same object with the same value.

While dictionaries *themselves* and each *value* within them are mutable, the *keys* must be hashable. This is because Python internally accesses a dictionary element via the hash value of the key.

While we cannot index into a dictionary, hashable keys allow for the same O(1) lookup time.

---

### Declaring Dictionaries
```python=
a = {'one':1, 'two':2, 'three':3}
```

---

### Dictionary lookup

Unlike JS, in Python we do not use dot notation to get values from a dictionary, we need to use bracket notation!

```python=
my_dict = {'one':1, 'two':2, 'three':3}
print(my_dict.one) #AttributeError: 'dict' object has no attribute 'one'
print(my_dict['one']) #1
print(my_dict['new']) # KeyError: 'new'

print(my_dict.get('one', None))
print(my_dict.get('banana', "Nope!"))
```

---

### Adding, Updating, Deleting Data in Dictionaries

- `del` keyword to delete a key/value pair
- `[]` to add or update a key/value pair
```python=
my_dict = {
    "word": "cooool",
    1: "one",
    False: 42,
    ("tuple", "keys"): ["lists", "can", "be", "values", "not", "keys"],
    None: {"key": "value"}
}

my_dict[1] = "two" # Updates value
print(my_dict[1]) # "two"
my_dict["new_key"] = "new_value" #Adds key/value
del my_dict["word"] # Deletes key/value
print(my_dict) # I promise, all the changes are there!
```

---

### Dictionary Practices (30 min)
Explore The Dictionary - 5 min
Does The Dictionary Have A Key? - 2 min
Is The Dictionary Empty? - 1 min
Dictionaries vs Objects - 3 min
Create Name Tag - 5 min
Concatenate Dictionaries - 5 min
Merge Two Lists - 5 min
Majority Character - Challenge - 5 Min
Jewels and Stones - Challenge - 10 min
Two Sum Revisited - Challenge - 10 min


---

## Sets

Docs link:
https://docs.python.org/3.9/library/stdtypes.html?highlight=set#set

---

Sets are mutable, unordered collections where all elements are unique. 

Sets use curly braces, like a dictionary. You can create an empty set with `set()`.

While sets can be mutated, the individual elements must be immutable types.

```python=
not_an_empty_set = {}
print(type(not_an_empty_set))

empty_set = set()
print(type(empty_set))

set_with_elements = {1, "hello", None}
print(set_with_elements)

ones = {1, 1, 1}
print(ones)
```

---

### Creating sets from other iterables

You can use the `set()` function to create new sets from other iterable types.

```python=
my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))    # {1, 2, 3, 4, 5}
my_string = "hello"
print(set(my_string))  # {'l', 'h', 'o', 'e'}
my_tuple = (1, 1, 1)
print(set(my_tuple))   # {1}
my_dict = {"hello": "value", "goodbye": "value"}
print(set(my_dict))    # {'goodbye', 'hello'}
```

---

### Set operations

The `set` data type allows for many operations, including union (`|`), intersection (`&`), difference (`-`), and symmetric difference (`^`).

```python=
# union of two sets
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)       # {1, 2, 3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
```

---

### Set Practices (18 min)
Create Set from List - 3 min
Add to Set from List - 3 min
Left Difference - 3 min
Remove Repeats - 3 min
Check Binary - 3 min
Find the Town Judge - Challenge - 10 min


---

## Built-in functions

Docs link:
https://docs.python.org/3.9/library/functions.html?highlight=any#any


---

### `sorted()`

`sorted()` sorts any iterable data type. It returns a list of every element in the iterable in sorted order (using [Timsort](https://en.wikipedia.org/wiki/Timsort)).

`sorted()` takes two optional keyword arguments:
- `key`: a function that takes a single argument and returns a key to use for sorting
- `reverse`: a boolean value, if `True` the iterable will be sorted in reverse order

```python=
names = ["JAMES", "julie", "Ana", "Ria"]
sorted_names = sorted(names)
print(sorted_names)

# ensure a case-insensitive sort with the `.lower` string method 
# and sort in reverse order
sorted_names = sorted(names, key=str.lower(), reverse=True)
print(sorted_names)
```

---

### `all()` and `any()`
`all()` returns `True` if *all* items in a collection are truthy or if the iterable is empty. It returns `False` if there is at least one falsey item.

`any()` returns `True` if there are *any* truthy items in the provided collection. It returns `False` if there are no truthy items or if the iterable is empty.

```python=
test = ["item", [], []]
print(any(test)) # True
print(all(test)) # False
```

all is "happy" if nothing inside is falsy, 
any is "happy" if at least one thing is truthy


---

### Built-in functions: `filter()`
`filter()` takes in a function and an iterable as arguments and returns a *filter object*.

The returned collection includes only the items which, when the function parameter was applied to them, returned a truthy value.

`filter()` does not filter in place. It returns an entirely new object.

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

### Built-in Function Practices (25 min)
Built-In Functions Quiz - 3 min
Adopted Cats - 5 min
Most Used Card - 5 min
Nested Sort - 5 min
Remove Duplicates - 5 min


---

## Comprehensions

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

### Convert `map()` to list comprehension

```python=
nums = [-5, 11, 10, 14]
mapped_nums = map(lambda num: num * 2 + 1, nums)

print(list(mapped_nums))  # [-9, 23, 21, 29]
```

---

### Convert `filter()` to list comprehension
```python=
nums = [-5, 11, 10, 14]

filtered_nums = filter(lambda num: num > 0, nums)

print(list(filtered_nums))  # [11, 10, 14]
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

### List Comprehensions and Advanced Lists (30 min)
Vowels - 3 min
Third Power - 3 min
Gas Prices - 3 min
Fizz Buzz - 3 min
Multiply List - 5 min
Dictionary Pairs - 5 min
Transpose Matrix - 5 min
Merge Two Sorted Lists - Challenge - 10 min


---

### Long Projects
Bonus: Track The Robot
Bonus: Averages
