# Python Collections and Built-ins

---

### Part 1: Lists

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

To get individual values:
- `list_name[single_index]`
```python=
fruits = ["banana", "apple", "kiwi", "mango", "tangerine"]

print(fruits[1])   # apple
print(fruits[-1])  # tangerine
```

---

### Indexing with lists (ranges)

To get a range of values:
```python=
fruits = ["banana", "apple", "kiwi", "mango", "tangerine"]

# list_name[inclusive_start:exclusive_end]
print(fruits[1:4])
print(fruits[-1:])

# list_name[inclusive_start:exclusive_end:step_size]
print(fruits[::-1])
print(fruits[3::-1])
```

---

### Built-in functions (`len()`)
We can use the `len()` function to get the length of lists.

```python=
fruits = ["banana", "apple", "kiwi", "mango", "tangerine"]

print(len(fruits))       # 5
print(len(fruits[1:4]))  # 3
```

---

## Part 2: Built-in List Methods

---


### List methods

Use `append` to add an item to the end of a list (like `push` in JavaScript). This mutates the list.

```python=
fruits = ["banana", "apple", "kiwi"]

fruits.append("apple")
print(fruits)  # ["banana", "apple", "kiwi", "apple"]
```

Use `extend` to add all items of an iterable to the end of a list.

```python=
fruits = ["banana", "apple", "kiwi"]

fruits.extend(["apple", "mango", "tangerine"])
print(fruits)  # ["banana", "apple", "kiwi", "apple", "mango, "tangerine"]
```


Use `remove` to delete the first instance of a given value. (Also mutates the list).
```python=
fruits.remove("apple")
print(fruits)  # ["banana", "kiwi", "apple"]

# Error if value is not present in list
fruits.remove("mango") # ValueError: list.remove(x): x not in list
```

(for more list methods, check out [the documentation here](https://docs.python.org/3/tutorial/datastructures.html).)

---

### Sorting lists

The `.sort()` method will sort a list, mutating the list

```python=
fruits = ["mango", "banana", "apple", "kiwi"]
fruits.sort()
print(fruits)  # ["apple", "banana", "kiwi", "mango"]
```

---

### Sorting lists (custom sort)

You can provide a key to change how the list is sorted
- The key is a function that takes a single argument and returns a key to use for sorting
- Rather than sort the list values directly, the sort will apply the key function to each value and sort based on the resulting value
- This will not mutate the original values in the list - just the order!

```python=
names = ["JAMES", "julie", "Ana", "Ria"]
names.sort()
print(names)  # ['Ana', 'JAMES', 'Ria', 'julie']

# ensure a case-insensitive sort with the `.lower` string method
names.sort(key=str.lower)
print(names)  # ['Ana', 'JAMES', 'julie', 'Ria']
```

---


### Sorting, continued

The `sorted()` function can be used to sort lists without mutating. It also works with other iterable types (e.g. tuples).

```python=
fruits = ["mango", "banana", "apple", "kiwi"]
sorted_fruits = sorted(fruits)
reversed_fruits = sorted(fruits, reverse=True)
print(sorted_fruits)   # ['apple', 'banana', 'kiwi', 'mango']
print(reversed_fruits) # ['mango', 'kiwi', 'banana', 'apple']
```

- note that the parameters `key` and `reverse` work with both `.sort()` and `sorted()`


---

### Sorting lists (fun fact)

Sorting in Python uses [Timsort](https://en.wikipedia.org/wiki/Timsort). (The inventor's name is Tim. Really.)

It is based on a combination of merge sort and insertion sort.

---

### More built-in functions
`sum()`, `min()`, `max()`, can be used to compute values over lists.

```python=
values = [49, 22, 13, 25]
print(values)       # [49, 22, 13, 25]

total_value = sum(values)
print(total_value)  # 109

top_value = max(values)
print(top_value)    # 49

min_value = min(values)
print(min_value)    # 13

avg_val = sum(values)/len(values)
print(avg_val)     # 27.25
```

---

### Part 3: Tuples

---

### Tuples

- Tuples are an ordered, immutable collection type. 
- They are defined using parentheses `()`, with values separated by a comma.

```python=
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = ('a', 'b', 'c', 'd', 'e')
c = 10, 20, 30

print(a)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(b)  # ('a', 'b', 'c', 'd', 'e')
print(c)  # (10, 20, 30)
```

---

### Tuples are immutable [1/2]

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

### Tuples are immutable [2/2]

Mutable items in a tuple can be mutated:

```python=
tup = ([1, 2, 3], "hello")
print(tup[0])  # [1, 2, 3]
tup[0].append(4)
print(tup[0])  # [1, 2, 3, 4]
print(tup)     # ([1, 2, 3, 4], "hello")
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

### Returning tuples

- Using a comma in your return statement will return a tuple
- You can store the tuple in one variable or destructure the tuples values into multiple variables.

```python=
def min_max(numbers):
    return min(numbers), max(numbers)

values = (14, 2, -2, 3.3, -8, -25, 9, 0)

low_and_high = min_max(values)
print(low_and_high)  # (-25, 14)

lowest, highest = min_max(values)
print(lowest)        # -25
print(highest)       # 14
```

---

### Singleton tuples

Since parentheses are also used for grouping, python won't interpret a single like you might expect.

```python=
hopefully_a_tuple = (5)
print(hopefully_a_tuple)  # 5
# whoops! not a tuple
```

You need to use a comma so that python can recognize that a tuple is present.

```python=
hopefully_a_tuple = (5,)
print(hopefully_a_tuple)  # (5,)
# nice, that is a tuple
also_a_tuple= 5,
print(also_a_tuple) # (5,)
# awesome, that is also a tuple
```

---

### Tuples vs. Lists: which is better?

As always, it depends!

Tuples are:
- Immutable
- Hashable
- More memory efficient than a list

Lists are:
- More familiar
- Mutable and dynamic

---

## Part 4: Ranges

---

### Ranges

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
print(numbers_range) # range(0, 10)
# How can we make this a list?

starting_at_one = range(1, 11)
```

---

### Reverse Ranges

```python=
reversed_maybe = range(51, 5)
print(list(reversed_maybe))

reversed = range(51, 5, -1) 
print(list(reversed))
```

---

### Iterating over Sequences with For Loops

- `for` keyword to start the loop
- `in` iterates over each element in the sequence
- We do not need to define an iterator variable!

```python=
items = ['a', 'b', 'c']

for item in items:
    print(item)

# range gives us access to both the 
# current element and its index in the list
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

## Part 5: Dictionaries

---

### Dictionaries

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
b = dict(one=1, two=2, three=3)
c = dict([('two', 2), ('one', 1), ('three', 3)])
print(a == b == c)   # True
```
If keys are the same, they are considered equivalent, doesn't matter how they were defined

---

### Using `[]` and `.get()` to index into a Dictionary
- Unlike javascript in Python you cannot index into a dictionary with dot notation
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

### Using `in`
- `in` also allows you to check if a value exists in a sequence
    - For dictionaries, it checks whether a value is a *key* in the dictionary
```python=
print(1 in {1: "one", 2: "two"})
print("1" in {1: "one", 2: "two"})
print(4 in {1: "one", 2: "two"})
print("one" in {1: "one", 2: "two"})
```

---

### .items()
 - `.items()` returns a list of tuples
     - Each tuple contains the key/value pair of the item in the dictionary
```python=
book = {
    'title': 'Goodnight Moon',
    'ratings': 7492,
    'stars': 4.8,
    'author': {'firstName': 'Margaret', 'lastName': 'Wise Brown'},
    'images': ['goodnight1.png', 'goodnight2.png'],
}
    
for key, value in book.items():
    print('key:', key, 'value:', value)

for key in book:
     print('key:', key, 'value:', book[key])

```

---

### `.keys()` and `.values()`
- `.keys()` returns a list of the keys in the dictionary
- `.values()` returns a list of the values in the dictionary
```python=
book = {
    'title': 'Goodnight Moon',
    'ratings': 7492,
    'stars': 4.8,
    'author': {'firstName': 'Margaret', 'lastName': 'Wise Brown'},
    'images': ['goodnight1.png', 'goodnight2.png'],
}

for value in book.values():
    print('value:', value)

for key in book.keys():
    print('key:', key)
```

---

## Part 5.5: *Args and **Kwargs

---

### Collecting Function Arguments

In JavaScript, we could use the spread/rest operator (`...`) to collect a variable number of function arguments into an array.

```javascript=
// javascript example
const myHobbies = (name, ...args) => {
    console.log("name (first positional arg):", name)
    console.log("collected arguments:", args)
    return `${name}'s favorite hobbies are ${args.join(', ')}`
}
console.log(myHobbies("Mitchell", "swimming", "cycling", "making pizza", "BBQ"))
```

In Python, we can use the "splat" operator (`*`) and the "double-splat" operator (`**`) to do something similar.

---

### Positional arguments

In Python, if we want to collect some variable number of anonymous positional arguments, we use the splat operator after all of the named positional arguments.

Note that the `args` will be collected into a tuple, not a list.


```python=
def my_hobbies(name, *args):
    print("name (first positional arg):", name)
    print("collected positional args:", args)
    return f"{name}'s favorite hobbies are {', '.join(args)}"


print(my_hobbies("Mitchell", "swimming", "cycling", "making pizza", "BBQ"))
# name (first positional arg): Mitchell
# collected positional args: ('swimming', 'cycling', 'making pizza', 'BBQ')
# Mitchell's favorite hobbies are swimming, cycling, making pizza, BBQ
```

---

### Keyword Arguments

In addition to positional arguments (`args`), Python also has keyword arguments (`kwargs`). Anonymous keyword arguments can be collected using the `**` operator.

Keyword arguments must follow all positional arguments, so the input order is always:
- `named_arguments, *args, named_keyword_args=value, **kwargs`

The `**` operator collects keyword arguments into a dictionary.
```python=
def my_hobbies(name, *args, age=10, **kwargs):
    print("age (collected args):", age)
    print("collected kwargs:", kwargs)
    info_dict = {
        "hobbies": f"{name} favorite hobbies are {', '.join(args)}",
        "stats": {**kwargs, "age": age}
    }
    return info_dict


print(my_hobbies("Mitchell", "swimming", "cycling",
      "making pizza", "BBQ", age=30, height=60, glasses=False))
```

---

## Part 6: Sets

---

### Sets

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

---

#### Union `(a | b)`
All elements in a and b (or in both)

![set_operations](https://i.imgur.com/5bY2S1u.png)

```python=
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)       # {1, 2, 3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
# order of a and b does not matter
```

---

### Set operations
#### Intersection `(a & b)`
Only elements in *both* a and b

![set_operations](https://i.imgur.com/dyvvZAv.png)
```python=
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)              # {3}
print(a.intersection(b))  # {3}
# order of a and b does not matter
```

---

### Code from "Combining Data Structures"

```python=
# posts is a list of dictionaries, some of the values in that list
posts = [
    {
        "title": "All About Lists",
        "tags": ("fun", "informative", "lists")
    },
    {
        "title": "Tuple Trouble",
        "tags": ("fun", "tuples")
    },
    {
        "title": "Sparkling Sets",
        "tags": ("informative", "numbers")
    },
]

all_tags = []  # list to hold all tags
for i in range(len(posts)):
    print(posts[i]["tags"])
    all_tags.extend(posts[i]["tags"])

print(all_tags)
print(set(all_tags))
all_tags = list(set(all_tags))
all_tags.sort()
print(all_tags)
```

---

### Code example from "Stack and Queue Overview"
#### Interuption stack
```python=
teller = []

teller.append("Greet Customer")
print(teller)
teller.pop()
print(teller)
teller.append("Process Deposit")
print(teller)
teller.append("Phone Ringing")
print(teller)
teller.pop()
teller.append("Greet Caller, Listen, Answer Question")
print(teller)
teller.pop()
print(teller)
teller.pop()
print(teller)
```

---

### Code example from "Stack and Queue Overview"
#### Processing queue
```python=
processor = []
processor.append({'type':'page','path':'','header':[],'cookies':[]}),
processor.append({'type':'api', 'function':'', 'parameters':[]})
processor.append({'email':'email','address':'bob@gmail.com','subject':''})
print("PROCESSOR LIST", processor)

for i in range(len(processor)):
    item = processor.pop(0)
    print("PROCESSING ITEM", item)
    print("REMAINING LIST", processor)
```

---

## Part 7: `input()`

---

### The `input()` function

`input()` receives input from the user via standard input and returns it as a string.

It takes an optional string prompt as an argument that is printed to standard output.

```python=
name = input("What's your name? ")
print(name)
```