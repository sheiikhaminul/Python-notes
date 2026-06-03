# 🐍 Python Complete Notes
> Beginner to Intermediate+ · Add your own notes below each section

---

## Table of Contents

> 🟢 Must know  ·  🟡 Good to know

1. [🟢 Python Basics](#1-python-basics)
2. [🟢 Data Types & Type Casting](#2-data-types--type-casting)
3. [🟢 Operators](#3-operators)
4. [🟢 Input & Output](#4-input--output)
5. [🟢 Conditional Statements](#5-conditional-statements--if--elif--else)
6. [🟢 Strings](#6-strings)
7. [🟢 Data Structures](#7-data-structures)
8. [🟢 Comprehensions](#8-comprehensions)
9. [🟢 Built-in Functions](#9-built-in-functions)
10. [🟢 Loops](#10-loops)
11. [🟡 Unpacking & Multiple Assignment](#11-unpacking--multiple-assignment)
12. [🟢 Functions](#12-functions)
13. [🟡 Type Checking — isinstance()](#13-type-checking--isinstance)
14. [🟢 File I/O](#14-file-io)
15. [🟢 Error Handling](#15-error-handling)
16. [🟢 Modules & Imports](#16-modules--imports)
17. [🟡 Generators & yield](#17-generators--yield)
18. [🟡 Shallow vs Deep Copy](#18-shallow-vs-deep-copy)
19. [🟡 \_\_name\_\_ == "\_\_main\_\_"](#19-__name__--__main__)
20. [🟢 OOP — Object Oriented Programming](#20-oop--object-oriented-programming)
---

## 1. Python Basics

- Developed by **Guido van Rossum**
- **High-level language** — easy to read, close to English
- **Case sensitive** — `Name` and `name` are different variables
- **Dynamically typed** — variable type is set automatically based on the value stored in it
- Uses an **interpreter** — reads and runs code line by line (not all at once like a compiler)

```python
# Check Python version in terminal
python --version

# Run a Python file
python filename.py

# Basic output
print("Hello World")
print(4 / 3)           # 1.3333...
print(2 ** 10)         # 1024
print(10 % 3)          # 1
```

### Comments
```python
# This is a single line comment

"""
This is a multi-line comment.
Also used as a docstring to describe functions or classes.
"""

# VS Code tip: Select lines → Ctrl + /  to toggle comments on all selected lines
```

### Python Statement
A line or group of lines that form one complete instruction.
```python
x = 5              # assignment statement
y = x + 10         # expression statement
print(y)           # function call statement

# Multiple statements on one line (not recommended but valid)
a = 1; b = 2; c = 3
```

### Variable Naming Rules
1. Only letters, digits, and underscores — no spaces or hyphens
2. Cannot start with a digit
3. Cannot be a reserved keyword
4. Case sensitive — `score` and `Score` are different

```python
# Valid names
my_name  = "Amin"
age1     = 21
_score   = 99
totalSum = 100     # camelCase (valid but snake_case preferred in Python)

# Invalid names
# 1name = "x"      → starts with digit — Error
# my-name = "x"    → hyphen not allowed — Error
# True = 5         → keyword — Error
```

> 📝 **Your notes here:**

---

## 2. Data Types & Type Casting

### Basic Data Types

| Type    | Example            | Notes                              |
|---------|--------------------|------------------------------------|
| `int`   | `x = 5`            | Whole numbers, positive or negative|
| `float` | `x = 5.5`          | Decimal numbers                    |
| `str`   | `x = "hello"`      | Text — inside quotes               |
| `bool`  | `x = True`         | Only `True` or `False` (capital T/F)|
| `None`  | `x = None`         | Represents no value / empty        |

```python
x    = 10
name = "Amin"
pi   = 3.14
flag = True
val  = None

print(type(x))     # <class 'int'>
print(type(name))  # <class 'str'>
print(type(pi))    # <class 'float'>
print(type(flag))  # <class 'bool'>
print(type(val))   # <class 'NoneType'>
```

### Type Casting
- **Explicit** — you manually convert one type to another
- **Implicit** — Python converts automatically when needed

```python
# Explicit — manual conversion
x = int("5")           # str → int  → 5
y = str(10)            # int → str  → "10"
z = float("3.14")      # str → float→ 3.14
a = int(9.9)           # float→ int → 9   (decimal part is dropped, NOT rounded)
b = bool(0)            # int → bool → False  (0 = False, anything else = True)
c = bool("hello")      # str → bool → True  (non-empty string = True)
d = list((1, 2, 3))    # tuple→ list

# Implicit — Python does it automatically
result = 5 + 2.0       # int + float → Python makes it float
print(result)          # 7.0
print(type(result))    # <class 'float'>
```

```python
# Common use — convert input (always returns string) to int
age = int(input("Enter age: "))

# Checking truthy/falsy values
print(bool(0))         # False
print(bool(""))        # False  (empty string)
print(bool([]))        # False  (empty list)
print(bool(None))      # False
print(bool(42))        # True
print(bool("hi"))      # True
```

### Keywords (Reserved Words)
Cannot be used as variable names — Python already uses them.
```
def, del, True, False, None, if, else, elif, while, for,
in, not, and, or, is, pass, return, break, continue,
lambda, class, import, from, try, except, finally, raise,
yield, with, as, assert, global, nonlocal
```

> 📝 **Your notes here:**

---

## 3. Operators

### Arithmetic Operators
```python
print(5 + 3)    # 8   — addition
print(5 - 3)    # 2   — subtraction
print(5 * 3)    # 15  — multiplication
print(5 / 2)    # 2.5 — division (always returns float)
print(5 // 2)   # 2   — floor division (removes decimal, rounds down)
print(5 % 2)    # 1   — modulus (remainder)
print(2 ** 3)   # 8   — power / exponent

# Practical use of modulus — check even or odd
print(10 % 2 == 0)   # True  → even
print(7  % 2 == 0)   # False → odd
```

### Comparison Operators — returns True or False
```python
print(5 == 5)    # True  — equal to
print(5 != 3)    # True  — not equal to
print(5 > 3)     # True  — greater than
print(5 < 3)     # False — less than
print(5 >= 5)    # True  — greater than or equal
print(5 <= 4)    # False — less than or equal
```

### Logical Operators
```python
print(True and False)   # False — both must be True
print(True or  False)   # True  — at least one must be True
print(not True)         # False — flips the value

# Practical
age = 20
has_id = True
print(age >= 18 and has_id)   # True — both conditions met

x = 0
print(x == 0 or x == 1)      # True — one condition met
```

### Assignment Operators
```python
x  = 10
x += 5     # x = x + 5  → 15
x -= 3     # x = x - 3  → 12
x *= 2     # x = x * 2  → 24
x /= 4     # x = x / 4  → 6.0
x //= 2    # x = x // 2 → 3.0
x **= 3    # x = x ** 3 → 27.0
x %= 5     # x = x % 5  → 2.0
```

### Identity & Membership Operators
```python
# Identity — checks if two variables point to the SAME object in memory
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)      # True  — same object
print(a is c)      # False — same value but different object
print(a is not c)  # True

# Membership — checks if value is inside an iterable
fruits = ["apple", "banana"]
print("apple"  in fruits)      # True
print("cherry" in fruits)      # False
print("cherry" not in fruits)  # True

name = "Aminul"
print("min" in name)           # True
```

### Operator Precedence (High → Low)
```
()  →  **  →  +x,-x,~x(unary)  →  *,/,//,%  →  +,-
→  <<,>>  →  &  →  ^  →  |
→  ==,!=,>=,<=, is, is not, in, not in
→  not  →  and  →  or  →  =,+=,-=,*=,/=
```
```python
result  = 2 + 3 * 4         # * first  → 14
result2 = (2 + 3) * 4       # () first → 20
result3 = 2 ** 3 ** 2       # ** right→left → 2**9 → 512
result4 = not True or False  # 'not' before 'or' → False or False → False
print(result, result2, result3, result4)
```

> 📝 **Your notes here:**

---

## 4. Input & Output

```python
# input() always returns a string — typecast if you need a number
name = input("Enter your name: ")
age  = int(input("Enter your age: "))
gpa  = float(input("Enter GPA: "))

print(type(name))  # <class 'str'>
print(type(age))   # <class 'int'>
```

### Print — Multiple Ways
```python
name = "Amin"
age  = 21

# 1. Using +  (non-strings must be converted with str())
print("Name: " + name + ", Age: " + str(age))

# 2. Using f-string — recommended, clean, no typecast needed
print(f"Name: {name}, Age: {age}")

# 3. Using , — adds space automatically between items
print("Name:", name, "Age:", age)

# 4. Using .format()
print("Name: {}, Age: {}".format(name, age))

# f-string with expressions
x = 10
print(f"Double of x is {x * 2}")       # Double of x is 20
print(f"Pi is approximately {22/7:.2f}")  # Pi is approximately 3.14

# print options
print("Hello", "World", sep="-")    # Hello-World
print("Hello", end=" ")             # doesn't go to new line
print("World")                      # Hello World
```

```python
# Taking multiple inputs on one line
a, b = input("Enter two numbers: ").split()
a, b = int(a), int(b)
print(f"Sum = {a + b}")

# Or using map
x, y = map(int, input("Enter two numbers: ").split())
print(x + y)
```

> 📝 **Your notes here:**


---

## 5. Conditional Statements — if / elif / else

The most fundamental decision-making structure in Python.
Runs a block of code only when a condition is `True`.

### Basic if / else
```python
age = 18

if age >= 18:
    print("Adult")    # runs if condition is True
else:
    print("Minor")    # runs if condition is False
```

### if / elif / else — Multiple Conditions
```python
score = 75

if score >= 90:
    print("Grade: A+")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")   # runs if none of the above matched
# Output: Grade: B
```

### Nested if
```python
logged_in = True
is_admin  = False

if logged_in:
    if is_admin:
        print("Welcome, Admin!")
    else:
        print("Welcome, User!")
else:
    print("Please log in.")
# Output: Welcome, User!
```

### Useful Condition Patterns
```python
# Membership check
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Found!")

# Emptiness check — empty string / list / 0 / None all evaluate to False
name = ""
if not name:
    print("Name is empty")

# None check
val = None
if val is None:
    print("No value assigned")

# Chained comparison (Python exclusive)
x = 15
if 10 < x < 20:
    print("x is between 10 and 20")

# Multiple conditions
if x > 10 and x % 2 != 0:
    print("Greater than 10 and odd")
```

```python
# Practical examples

# Login system
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
elif username == "admin":
    print("Wrong password")
else:
    print("Unknown user")

# Number categorizer
def categorize(n):
    if n > 0:    return "positive"
    elif n < 0:  return "negative"
    else:        return "zero"

print(categorize(5))     # positive
print(categorize(-3))    # negative
print(categorize(0))     # zero

# Grade function with validation
def grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:    return "A+"
    elif score >= 80:  return "A"
    elif score >= 70:  return "B"
    elif score >= 60:  return "C"
    else:              return "F"

print(grade(95))    # A+
print(grade(72))    # B
print(grade(55))    # F
```

> 📝 **Your notes here:**

---

## 6. Strings

- **Immutable** — cannot be changed after creation; any "change" creates a new string
- **Ordered** — characters have fixed positions
- **Indexed** — each character has an index (starts at 0)
- **Allow duplicates**

### Ways to Write a String
```python
s1 = 'single quotes'
s2 = "double quotes"
s3 = '''spans
multiple lines'''
s4 = """also spans
multiple lines"""
```

### Escape Sequences
```python
print("Hello\nWorld")       # \n = new line
print("Hello\tWorld")       # \t = tab space
print("He said \"Hi\"")     # \" = quote inside string
print("C:\\Users\\Amin")    # \\ = literal backslash
print("Line1\nLine2\nLine3")
```

### Indexing
```
String:   P  y  t  h  o  n
Index:    0  1  2  3  4  5
Negative:-6 -5 -4 -3 -2 -1
```
```python
s = "Python"
print(s[0])    # P   — first character
print(s[-1])   # n   — last character
print(s[2])    # t
print(s[-2])   # o
```

### Slicing → `str[start : stop : step]`
- `stop` index is **excluded** (it goes up to, not including stop)
- Default `step` is 1

```python
s = "Python"
print(s[1:4])    # yth   — index 1, 2, 3
print(s[2:])     # thon  — index 2 to end
print(s[:4])     # Pyth  — start to index 3
print(s[-3:-1])  # ho    — 3rd last to 2nd last
print(s[::-1])   # nohtyP — reverse (step = -1 means go backwards)
print(s[::2])    # Pto   — every 2nd character

word = "programming"
print(word[0:7:2])    # porm  — every 2nd char from index 0 to 6
print(word[::-1])     # gnimmargorp — reversed
```

### String Methods
> These do **NOT** change the original string. They return a new one.

```python
s = "  Hello World  "

# Case methods
print(s.lower())          # "  hello world  "
print(s.upper())          # "  HELLO WORLD  "
print(s.capitalize())     # "  hello world  " — only first letter of whole string
print(s.title())          # "  Hello World  " — first letter of each word
print(s.swapcase())       # "  hELLO wORLD  " — swaps upper↔lower

# Strip methods
print(s.strip())          # "Hello World"   — removes surrounding whitespace
print(s.lstrip())         # "Hello World  " — removes left whitespace only
print(s.rstrip())         # "  Hello World" — removes right whitespace only

# Search methods
print(s.find("World"))    # index of first occurrence (returns -1 if not found)
print(s.index("World"))   # same as find (but raises error if not found)
print(s.count("l"))       # count how many times 'l' appears
print(s.startswith("  H"))# True or False
print(s.endswith("  "))   # True or False

# Modify methods
print(s.replace("World", "Python"))  # "  Hello Python  "
print(s.strip().replace(" ", "_"))   # "Hello_World"

# Split & Join
print("a,b,c".split(","))     # ['a', 'b', 'c']
print(s.split())               # ['Hello', 'World']
print("-".join(["a","b","c"])) # "a-b-c"  — joins list into string

# Check methods — return True or False
print("hello".isalpha())   # True  — all letters
print("123".isdigit())     # True  — all digits
print("hello1".isalnum())  # True  — letters and digits
print("  ".isspace())      # True  — all whitespace
print(len(s))              # 15    — length (spaces count)
```

```python
# Practical examples
email = "  user@example.com  "
clean = email.strip().lower()
print(clean)                     # user@example.com

sentence = "The quick brown fox"
words    = sentence.split(" ")
print(words)                     # ['The', 'quick', 'brown', 'fox']
print(words[2])                  # brown

# Count vowels in a string
text   = "Hello World"
vowels = "aeiouAEIOU"
count  = sum(1 for ch in text if ch in vowels)
print(f"Vowels: {count}")        # Vowels: 3

# Reverse words in a sentence
sentence  = "I love Python"
reversed_sentence = " ".join(sentence.split()[::-1])
print(reversed_sentence)         # Python love I
```

> 📝 **Your notes here:**

---

## 7. Data Structures

---

### 7.1 List `[]`
- **Mutable** — can be changed (in the original)
- **Ordered** — items keep their position
- **Allows duplicates** — same value can appear multiple times
- **Indexed access** — use `list[index]`
- Can store any data type, even mixed types
- Use case: **variable / changing data**

```python
# Creating lists
nums    = [1, 2, 3, 4, 5]
names   = ["Alice", "Bob", "Charlie"]
mixed   = [1, "hello", 3.14, True, None]
nested  = [[1, 2], [3, 4], [5, 6]]   # list inside a list

print(nums[0])          # 1
print(names[-1])        # Charlie
print(nested[1][0])     # 3  — row 1, column 0
```

### List Methods
> Modify the original list. Most return `None` (except `pop()` and `copy()`).

```python
li = [3, 1, 4, 1, 5, 9, 2, 6]

li.append(7)             # add 7 at end
li.insert(2, 99)         # insert 99 at index 2
li.sort()                # sort ascending (in place)
li.sort(reverse=True)    # sort descending (in place)
li.reverse()             # reverse the list (in place)
li.remove(1)             # remove FIRST occurrence of value 1
val = li.pop(0)          # remove & return item at index 0
val = li.pop()           # remove & return last item
li.clear()               # removes all elements
copy_li = li.copy()      # returns a shallow copy
print(li.index(4))       # index of first occurrence of 4
print(li.count(1))       # how many times 1 appears
print(len(li))           # length of list
```

```python
# Practical examples
students = ["Amin", "Bob", "Cara", "Dave"]

# Add and remove
students.append("Eve")
students.remove("Bob")
print(students)          # ['Amin', 'Cara', 'Dave', 'Eve']

# Sort alphabetically
students.sort()
print(students)          # ['Amin', 'Cara', 'Dave', 'Eve']

# Loop through
for i, name in enumerate(students):
    print(f"{i+1}. {name}")
# 1. Amin
# 2. Cara
# 3. Dave
# 4. Eve

# Check membership
print("Amin" in students)   # True

# Combine two lists
extra = ["Frank", "Grace"]
all_students = students + extra
print(all_students)

# Nested list access
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])   # 6 (row 1, col 2)
```

> 📝 **Your notes here:**

---

### 7.2 Tuple `()`
- **Immutable** — cannot be changed after creation
- **Ordered** — items keep their position
- **Allows duplicates**
- **Indexed access**
- Use case: **fixed / constant data** (coordinates, RGB colors, DB records)
- Single element needs trailing comma: `(value,)` — without comma it's just parentheses

```python
t  = (10, 20, 30, 20)
print(t[0])      # 10
print(t[-1])     # 20

# Single element
t2 = (5,)
t3 = (5)         # NOT a tuple — just int in parentheses
print(type(t2))  # <class 'tuple'>
print(type(t3))  # <class 'int'>

# Tuple unpacking
x, y, z = (1, 2, 3)
print(x, y, z)   # 1 2 3
```

### Tuple Methods
```python
t = (1, 2, 3, 2, 4, 2)
print(t.index(2))    # 1   — index of first occurrence
print(t.count(2))    # 3   — how many times 2 appears
print(len(t))        # 6
```

```python
# Practical examples

# Use tuple for fixed data — e.g., coordinates
point  = (4, 7)
color  = (255, 128, 0)   # RGB

# Swapping values using tuple (no temp variable needed)
a, b = 10, 20
a, b = b, a
print(a, b)              # 20 10

# Return multiple values from a function (returns as tuple)
def min_max(nums):
    return min(nums), max(nums)

low, high = min_max([3, 1, 7, 2, 9])
print(low, high)         # 1 9

# Uppercase all strings in a tuple (since tuples are immutable, create new)
tup   = ("hello", "world")
upper = tuple(item.upper() for item in tup)
print(upper)             # ('HELLO', 'WORLD')
```

#### List ↔ Tuple Conversion
```python
li  = [1, 2, 3]
t   = tuple(li)    # list → tuple

t2  = (4, 5, 6)
li2 = list(t2)     # tuple → list
```

> 📝 **Your notes here:**

---

### 7.3 Dictionary `{key: value}`
- **Mutable** — can be changed
- **Ordered** (Python 3.7+) — insertion order is maintained
- **No duplicate keys** — duplicate key overwrites previous value
- **Key** can be: string, int, float, tuple — NOT a list (must be immutable)
- **Value** can be: anything

```python
person = {
    "name" : "Amin",
    "age"  : 21,
    "city" : "Dhaka"
}

print(person["name"])         # Amin — direct access (KeyError if missing)
print(person.get("age"))      # 21   — safe access (None if missing, no error)
print(person.get("email", "N/A"))  # N/A — default value if key missing

person["age"]   = 25          # update existing key
person["email"] = "a@b.com"   # add new key-value pair
del person["city"]            # delete a key-value pair
```

### Nested Dictionary
```python
school = {
    "student1": {"name": "Amin", "roll": 1},
    "student2": {"name": "Bob",  "roll": 2}
}
print(school["student1"]["name"])   # Amin
```

### Dictionary Methods
```python
d = {"a": 1, "b": 2, "c": 3}

print(d.keys())              # dict_keys(['a', 'b', 'c'])
print(d.values())            # dict_values([1, 2, 3])
print(d.items())             # dict_items([('a',1), ('b',2), ('c',3)])
print(d.get("a"))            # 1
print(d.get("z", 0))         # 0  — default if missing
d.update({"d": 4, "a": 99}) # add new + overwrite existing
d.pop("b")                   # remove key "b" and return its value
print("a" in d)              # True — check if key exists
print(len(d))                # number of key-value pairs
```

```python
# Practical examples

# Count frequency of characters
word   = "mississippi"
freq   = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)   # {'m': 1, 'i': 4, 's': 4, 'p': 2}

# Loop through dictionary
for key, value in freq.items():
    print(f"'{key}' appears {value} time(s)")

# Merge two dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2
print(merged)   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Or use update
dict1.update(dict2)
```

> 📝 **Your notes here:**

---

### 7.4 Set `{values}`
- **Mutable** — you can add/remove items
- **Elements must be immutable** — no lists or dicts inside a set
- **Unordered** — no fixed position, no index
- **No duplicates** — duplicates are automatically removed
- Empty set: `set()` — NOT `{}` (that creates an empty dict!)

```python
s = {1, 2, 3, 3, 4, 4}
print(s)             # {1, 2, 3, 4}  — duplicates removed

empty_set = set()    # correct
empty_dict = {}      # this is a dict, NOT a set!
```

### Set Methods
```python
s  = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s.add(10)                    # add element
s.remove(2)                  # remove (error if not found)
s.discard(99)                # remove (no error if not found)
s.clear()                    # empty the set
s.pop()                      # remove and return a random element

# Set operations
print(s.union(s2))           # {1,2,3,4,5,6} — all unique elements
print(s.intersection(s2))    # {3,4}  — common elements only
print(s.difference(s2))      # {1,2}  — in s but NOT in s2
print(s.issubset(s2))        # True if all of s is inside s2
```

```python
# Practical examples

# Remove duplicates from a list
nums    = [1, 2, 2, 3, 3, 4, 5, 5]
unique  = list(set(nums))
print(unique)   # [1, 2, 3, 4, 5] (order not guaranteed)

# Find common items between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = set(list1).intersection(set(list2))
print(common)   # {3, 4, 5}

# Find items in list1 but not in list2
only_in_1 = set(list1).difference(set(list2))
print(only_in_1)   # {1, 2}
```

> 📝 **Your notes here:**

---

## 8. Comprehensions

A short, clean, one-line way to create lists, dictionaries, or sets — instead of a loop.

### List Comprehension
```python
# Syntax
new_list = [expression for item in iterable]
new_list = [expression for item in iterable if condition]

# Without comprehension
squares = []
for x in range(5):
    squares.append(x ** 2)

# With comprehension — same result, one line
squares = [x ** 2 for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]
```

```python
# With condition
evens    = [x for x in range(10) if x % 2 == 0]
print(evens)      # [0, 2, 4, 6, 8]

# Transform strings
words    = ["hello", "world", "python"]
upper    = [w.upper() for w in words]
print(upper)      # ['HELLO', 'WORLD', 'PYTHON']

# Filter and transform together
nums     = [1, 2, 3, 4, 5, 6]
even_sq  = [x**2 for x in nums if x % 2 == 0]
print(even_sq)    # [4, 16, 36]

# Flatten a nested list
matrix   = [[1, 2], [3, 4], [5, 6]]
flat     = [num for row in matrix for num in row]
print(flat)       # [1, 2, 3, 4, 5, 6]
```

---

### Dictionary Comprehension
```python
# Syntax
new_dict = {key_expr: value_expr for item in iterable}
new_dict = {key_expr: value_expr for item in iterable if condition}

# Simple example — square each number
nums   = [1, 2, 3, 4, 5]
sq_map = {x: x**2 for x in nums}
print(sq_map)    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# From two lists using zip
keys   = ["name", "age", "city"]
values = ["Amin", 21, "Dhaka"]
d      = {k: v for k, v in zip(keys, values)}
print(d)         # {'name': 'Amin', 'age': 21, 'city': 'Dhaka'}

# Filter — only keep items with value > 2
data      = {"a": 1, "b": 3, "c": 2, "d": 5}
filtered  = {k: v for k, v in data.items() if v > 2}
print(filtered)  # {'b': 3, 'd': 5}

# Swap keys and values
original  = {"a": 1, "b": 2, "c": 3}
swapped   = {v: k for k, v in original.items()}
print(swapped)   # {1: 'a', 2: 'b', 3: 'c'}
```

---

### Set Comprehension
```python
# Syntax
new_set = {expression for item in iterable}

nums    = [1, 2, 2, 3, 3, 4]
unique  = {x for x in nums}
print(unique)    # {1, 2, 3, 4}

# Squares, duplicates removed
sq_set  = {x**2 for x in [1, -1, 2, -2, 3]}
print(sq_set)    # {1, 4, 9}

# Only vowels in a string
text    = "Hello World"
vowels  = {ch.lower() for ch in text if ch.lower() in "aeiou"}
print(vowels)    # {'e', 'o'}
```

> 📝 **Your notes here:**

---

## 9. Built-in Functions

Python comes with many ready-to-use functions. The most important ones:

### Numeric Functions
```python
nums = [3, 1, 7, 2, 9, 4]

print(len(nums))          # 6   — length
print(min(nums))          # 1   — smallest value
print(max(nums))          # 9   — largest value
print(sum(nums))          # 26  — total sum
print(sorted(nums))       # [1,2,3,4,7,9] — returns new sorted list (does NOT change original)
print(abs(-5))            # 5   — absolute value
print(round(3.7))         # 4   — round to nearest int
print(round(3.14159, 2))  # 3.14 — round to 2 decimal places
print(pow(2, 8))          # 256 — same as 2**8
```

### any() and all()
```python
# any() — returns True if AT LEAST ONE item is True
print(any([False, False, True]))     # True
print(any([False, False, False]))    # False

nums = [2, 4, 5, 6]
print(any(x % 2 != 0 for x in nums))   # True  — 5 is odd

# all() — returns True if ALL items are True
print(all([True, True, True]))       # True
print(all([True, False, True]))      # False

nums = [2, 4, 6, 8]
print(all(x % 2 == 0 for x in nums))   # True  — all even

# Practical use
passwords = ["abc123", "xyz456", "pass789"]
print(all(len(p) >= 6 for p in passwords))   # True — all are 6+ chars
```

### enumerate()
Gives you both the **index** and the **value** while looping. Avoids manual counter variables.

```python
fruits = ["apple", "banana", "cherry"]

# Without enumerate
for i in range(len(fruits)):
    print(i, fruits[i])

# With enumerate — cleaner
for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry

# Start index from 1 instead of 0
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry
```

### zip()
Combines two or more iterables **side by side**, pair by pair. Stops at the shortest one.

```python
names  = ["Amin", "Bob", "Cara"]
scores = [90,     85,    92]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Amin: 90
# Bob: 85
# Cara: 92

# Create a dictionary from two lists
keys   = ["a", "b", "c"]
vals   = [1, 2, 3]
d      = dict(zip(keys, vals))
print(d)   # {'a': 1, 'b': 2, 'c': 3}

# Unzip — separate zipped data
pairs  = [(1, "a"), (2, "b"), (3, "c")]
nums, letters = zip(*pairs)
print(nums)     # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')
```

### map(), filter(), sorted()
```python
# map() — apply function to every item
numbers  = ['1', '2', '3']
result   = list(map(int, numbers))
print(result)    # [1, 2, 3]

doubled  = list(map(lambda x: x*2, [1, 2, 3, 4]))
print(doubled)   # [2, 4, 6, 8]

# filter() — keep items where function returns True
evens    = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6]))
print(evens)     # [2, 4, 6]

# sorted() — returns new sorted list (does NOT change original)
nums     = [3, 1, 4, 1, 5, 9]
print(sorted(nums))               # [1, 1, 3, 4, 5, 9]
print(sorted(nums, reverse=True)) # [9, 5, 4, 3, 1, 1]

# Sort by custom key
words    = ["banana", "fig", "cherry", "apple"]
print(sorted(words, key=len))     # ['fig', 'apple', 'banana', 'cherry']

students = [("Amin", 90), ("Bob", 85), ("Cara", 92)]
print(sorted(students, key=lambda s: s[1]))   # sorted by score
```

> 📝 **Your notes here:**

---

## 10. Loops

- `break`    — exits the loop completely
- `continue` — skips the rest of the current iteration
- `pass`     — placeholder, does nothing

### While Loop
Use when you have a variable to update and a stopping condition.

```python
# Structure
i = 0
while i < 5:
    print(i)
    i += 1
# Output: 0 1 2 3 4

# Real example — find first number divisible by both 3 and 7
n = 1
while n <= 100:
    if n % 3 == 0 and n % 7 == 0:
        print(f"Found: {n}")
        break
    n += 1
# Found: 21

# Input validation loop
while True:
    age = int(input("Enter age (must be > 0): "))
    if age > 0:
        break
    print("Invalid! Try again.")
print(f"Age accepted: {age}")
```

### For Loop
Use to traverse (go through) a data structure — list, string, tuple, dict, range.

```python
# Loop with range
for i in range(1, 6):
    print(i)    # 1 2 3 4 5

# Loop through list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop through string
for ch in "Python":
    print(ch)

# Loop through dictionary
person = {"name": "Amin", "age": 21}
for key, value in person.items():
    print(f"{key}: {value}")

# Loop with else (else runs only if loop ends without break)
for i in range(5):
    if i == 10:     # condition never true
        break
    print(i)
else:
    print("Loop completed without break")
```

### Nested Loops
A loop inside another loop. Outer loop runs once; inner loop runs fully each time.

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")

# Print a pattern
for i in range(1, 6):
    print("*" * i)
# *
# **
# ***
# ****
# *****
```

### break, continue, pass
```python
# break — stop loop entirely
for i in range(10):
    if i == 5:
        break
    print(i)    # 0 1 2 3 4

# continue — skip current step, go to next
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)    # 1 3 5 (even numbers skipped)

# pass — placeholder (no operation)
for i in range(3):
    pass    # no error, nothing happens
```

> 📝 **Your notes here:**

---

## 11. Unpacking & Multiple Assignment

**Unpacking** means assigning values from a list, tuple, or any iterable directly to variables in one line.

### Basic Unpacking
```python
# Multiple assignment
a, b, c = 1, 2, 3
print(a, b, c)     # 1 2 3

# From a list
nums   = [10, 20, 30]
x, y, z = nums
print(x, y, z)     # 10 20 30

# From a tuple (very common)
point  = (4, 7)
px, py = point
print(px, py)      # 4 7

# Swap values without a temp variable
a, b   = 10, 20
a, b   = b, a
print(a, b)        # 20 10
```

### Extended Unpacking with `*`
The `*` collects leftover values into a list.

```python
first, *rest = [1, 2, 3, 4, 5]
print(first)   # 1
print(rest)    # [2, 3, 4, 5]

*start, last   = [1, 2, 3, 4, 5]
print(start)   # [1, 2, 3, 4]
print(last)    # 5

a, *middle, b  = [1, 2, 3, 4, 5]
print(a)       # 1
print(middle)  # [2, 3, 4]
print(b)       # 5

# Ignore values with _ (convention for "don't care")
name, _, city  = ("Amin", 21, "Dhaka")
print(name, city)   # Amin Dhaka
```

```python
# Practical examples

# Unpack returned tuple from function
def get_range(nums):
    return min(nums), max(nums)

low, high = get_range([3, 1, 9, 2, 7])
print(low, high)      # 1 9

# Unpack in a for loop
pairs = [(1, "a"), (2, "b"), (3, "c")]
for num, letter in pairs:
    print(f"{num} → {letter}")

# Spread a list into a function call using *
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))     # 6  — same as add(1, 2, 3)
```

> 📝 **Your notes here:**


---

## 12. Functions

- **Built-in** — already in Python: `print()`, `len()`, `type()`, etc.
- **User-defined** — written by you using `def`

```python
# Structure
def function_name(parameters):
    """Optional docstring — describes the function"""
    # logic
    return value    # optional

# Example
def greet(name):
    print(f"Hello, {name}!")

greet("Amin")    # Hello, Amin!
```

### Parameters vs Arguments
- **Parameter** — variable in the function definition
- **Argument** — actual value passed when calling

```python
def add(a, b):       # a, b are parameters
    return a + b

result = add(3, 5)   # 3, 5 are arguments
print(result)        # 8
```

### Default Values
Used when no argument is passed.
```python
def greet(name="stranger", greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Amin")               # Hello, Amin!
greet()                     # Hello, stranger!
greet("Bob", "Hi")          # Hi, Bob!
greet(greeting="Hey")       # Hey, stranger!  — keyword argument
```

### Ternary Operator (Inline if/else)
A one-line way to write a simple if/else.

```python
# Syntax:  value_if_true  if  condition  else  value_if_false

x     = 10
label = "even" if x % 2 == 0 else "odd"
print(label)    # even

# Practical
age   = 20
msg   = "adult" if age >= 18 else "minor"
print(msg)      # adult

# In a function
def absolute(n):
    return n if n >= 0 else -n

print(absolute(-7))   # 7
print(absolute(5))    # 5
```

### *args — Variable Number of Arguments
`*args` lets a function accept **any number of positional arguments**. They come in as a **tuple**.

```python
def add(*args):
    print(args)         # tuple of all passed values
    return sum(args)

print(add(1, 2))        # (1, 2)  → 3
print(add(1, 2, 3, 4))  # (1, 2, 3, 4)  → 10

def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

greet("Amin", "Bob", "Cara")
# Hello, Amin!
# Hello, Bob!
# Hello, Cara!
```

### **kwargs — Variable Keyword Arguments
`**kwargs` lets a function accept **any number of keyword arguments**. They come in as a **dictionary**.

```python
def show_info(**kwargs):
    print(kwargs)         # dict of all passed keyword args
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Amin", age=21, city="Dhaka")
# {'name': 'Amin', 'age': 21, 'city': 'Dhaka'}
# name: Amin
# age: 21
# city: Dhaka

# Combining all parameter types
def demo(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

demo(1, 2, 3, 4, 5, name="Amin", city="Dhaka")
# a=1, b=2
# args=(3, 4, 5)
# kwargs={'name': 'Amin', 'city': 'Dhaka'}
```

### Variable Scope — Local vs Global
- **Local variable** — defined inside a function. Only accessible inside that function.
- **Global variable** — defined outside all functions. Accessible anywhere.

```python
x = 10    # global variable

def show():
    x = 99    # local variable — does NOT affect the global x
    print(x)  # 99

show()
print(x)  # 10 — global x unchanged
```

### `global` Keyword
Use `global` inside a function to modify a **global variable** (not just read it).

```python
count = 0    # global

def increment():
    global count    # tell Python to use the global 'count'
    count += 1

increment()
increment()
print(count)   # 2

# Without global, this would cause an error:
def wrong():
    count += 1    # UnboundLocalError — Python thinks it's local
```

### Nested Functions & `nonlocal`
A function defined inside another function. `nonlocal` lets the inner function modify the outer function's variable.

```python
def outer():
    msg = "hello"      # outer function's variable

    def inner():
        nonlocal msg   # access the outer variable
        msg = "world"  # modify it
        print("inner:", msg)

    inner()
    print("outer:", msg)

outer()
# inner: world
# outer: world      ← changed because of nonlocal
```

```python
# Practical — counter using nested function + nonlocal
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
print(counter())   # 1
print(counter())   # 2
print(counter())   # 3
```

### Lambda Functions
Small, anonymous (nameless) one-liner functions.

```python
# Syntax: lambda arguments: expression

square  = lambda x: x ** 2
add     = lambda x, y: x + y

print(square(4))     # 16
print(add(3, 5))     # 8

# Lambda with conditional
classify = lambda x: "even" if x % 2 == 0 else "odd"
print(classify(4))   # even

# Lambda used with sorted
students = [("Amin", 90), ("Bob", 75), ("Cara", 85)]
by_score = sorted(students, key=lambda s: s[1])
print(by_score)      # [('Bob', 75), ('Cara', 85), ('Amin', 90)]

# Lambda with map/filter
nums     = [1, 2, 3, 4, 5]
doubled  = list(map(lambda x: x*2, nums))
evens    = list(filter(lambda x: x % 2 == 0, nums))
print(doubled)   # [2, 4, 6, 8, 10]
print(evens)     # [2, 4]
```

### Recursion
A function that **calls itself**. Must always have a **base case** (stopping condition) to avoid infinite loop.

```python
# Call stack — LIFO (Last In, First Out)
# Each function call is "stacked"; when base case hits, they resolve in reverse

# Factorial — n! = n × (n-1) × ... × 1
def factorial(n):
    if n <= 1:                   # base case
        return 1
    return n * factorial(n - 1) # recursive call

print(factorial(5))   # 120  →  5×4×3×2×1

# Sum of a list
def list_sum(lst):
    if len(lst) == 0:             # base case — empty list
        return 0
    return lst[0] + list_sum(lst[1:])   # first + sum of rest

print(list_sum([1, 2, 3, 4]))    # 10

# Fibonacci — 0 1 1 2 3 5 8 13 ...
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print([fib(i) for i in range(8)])   # [0, 1, 1, 2, 3, 5, 8, 13]
```

> 📝 **Your notes here:**

---

## 13. Type Checking — isinstance()

`isinstance(object, type)` — checks if an object is of a certain type. Returns `True` or `False`.
Much better than `type(x) == int` because it also works with inheritance.

```python
x = 42
print(isinstance(x, int))       # True
print(isinstance(x, float))     # False
print(isinstance(x, (int, float)))  # True — check against multiple types

name = "Amin"
print(isinstance(name, str))    # True

li   = [1, 2, 3]
print(isinstance(li, list))     # True
print(isinstance(li, (list, tuple)))  # True

# In a function — validate input type
def double(x):
    if not isinstance(x, (int, float)):
        raise TypeError(f"Expected a number, got {type(x).__name__}")
    return x * 2

print(double(5))       # 10
print(double(3.5))     # 7.0
# double("hi")        # TypeError: Expected a number, got str
```

```python
# isinstance with inheritance
class Animal: pass
class Dog(Animal): pass

d = Dog()
print(isinstance(d, Dog))       # True
print(isinstance(d, Animal))    # True — Dog inherits from Animal
```

### issubclass()
Checks if a class is a subclass (child) of another class.

```python
class Animal: pass
class Dog(Animal): pass

print(issubclass(Dog, Animal))   # True
print(issubclass(Animal, Dog))   # False
```

> 📝 **Your notes here:**

---

## 14. File I/O

- **RAM** — temporary; data lost when program ends
- **Files** — permanent storage on disk
  - Text files: `.txt`, `.log`, `.csv`
  - Binary files: `.jpg`, `.mp4`, `.pdf`

### File Opening Modes

| Mode  | Description                                                |
|-------|------------------------------------------------------------|
| `'r'` | Read (default). Error if file not found                    |
| `'w'` | Write. Creates if not exists. **Overwrites** existing      |
| `'x'` | Create new. **Error** if file already exists               |
| `'a'` | Append to end. Creates if not exists                       |
| `'r+'`| Read + write. Pointer at start. No truncate                |
| `'w+'`| Read + write. Deletes all content first                    |
| `'a+'`| Read + append. Pointer at end                              |
| `'rb'`| Read binary (images, videos)                               |

### Opening Files
```python
# Method 1 — Manual (always call close())
f    = open("file.txt", "r")
data = f.read()
f.close()

# Method 2 — with statement (RECOMMENDED — auto closes)
with open("file.txt", "r") as f:
    data = f.read()
    print(data)
# File is closed automatically after the with block
```

### Reading
```python
with open("notes.txt", "r") as f:
    content   = f.read()            # reads entire file as one string
    print(content)

with open("notes.txt", "r") as f:
    line      = f.readline()        # reads one line at a time
    print(line)

with open("notes.txt", "r") as f:
    all_lines = f.readlines()       # returns list of all lines
    for line in all_lines:
        print(line.strip())         # .strip() removes \n at end
```

### Writing & Appending
```python
# Write — creates new or overwrites
with open("output.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

# Write multiple lines at once
lines = ["Apple\n", "Banana\n", "Cherry\n"]
with open("fruits.txt", "w") as f:
    f.writelines(lines)

# Append — adds to end without deleting
with open("output.txt", "a") as f:
    f.write("This line is appended\n")
```

### Deleting a File
```python
import os
if os.path.exists("output.txt"):    # check first to avoid error
    os.remove("output.txt")
    print("File deleted")
else:
    print("File does not exist")
```

### CSV Files
CSV = Comma-Separated Values. Each row is a line; columns separated by commas.

```
Name,Age,City
Alice,25,New York
Bob,30,Los Angeles
```

```python
import csv

# Reading CSV
with open("data.csv", "r", newline='') as f:
    reader = csv.reader(f)
    next(reader)              # skip header row
    for row in reader:
        print(row)            # each row is a list

# Reading as dictionary (key = column header)
with open("data.csv", "r", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Age"])   # access by column name

# Writing CSV
with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])        # one row
    writer.writerows([
        ["Alice", 25, "New York"],
        ["Bob",   30, "LA"]
    ])                                              # multiple rows
```

```python
# Practical — read CSV and find average age
import csv

total = 0
count = 0
with open("data.csv", "r", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        total += int(row["Age"])
        count += 1

print(f"Average age: {total/count:.1f}")
```

> 📝 **Your notes here:**

---

## 15. Error Handling

Prevents the program from crashing when something goes wrong.

### Basic Structure
```python
try:
    # Code that might cause an error
    x = int(input("Enter a number: "))
    print(10 / x)
except ValueError:
    print("That is not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:       # catch anything not listed above
    print(f"Unexpected error: {type(e).__name__} — {e}")
```

### else & finally
```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    # Runs ONLY if try block had NO error
    print("Success! Result:", result)
finally:
    # ALWAYS runs — error or not (use for cleanup: close file, DB, etc.)
    print("Done.")
```

```python
# Real example — safe file reading
try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("No permission to read this file!")
else:
    print("File read successfully:")
    print(content)
finally:
    print("File operation finished.")
```

### raise — Trigger an Error Manually
```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is out of valid range (0-150)")
    return age

try:
    print(set_age(25))      # 25
    print(set_age(-5))      # ValueError
except ValueError as e:
    print(e)
```

### Custom Exception Classes
You can create your own error types by inheriting from `Exception`.

```python
# Define custom exceptions
class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    def __init__(self, amount, message="Amount must be positive"):
        self.amount  = amount
        super().__init__(f"{message}: {amount}")

# Use them
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        if amount > self.balance:
            raise InsufficientFundsError(f"Cannot withdraw {amount}, balance is {self.balance}")
        self.balance -= amount
        return self.balance

acc = BankAccount(500)
try:
    acc.withdraw(200)
    print("Balance:", acc.balance)   # Balance: 300
    acc.withdraw(1000)               # raises InsufficientFundsError
except InsufficientFundsError as e:
    print(e)
except InvalidAmountError as e:
    print(e)
```

### Common Error Types

| Error                | Description                   | Example                  |
|----------------------|-------------------------------|--------------------------|
| `ZeroDivisionError`  | Divide by zero                | `10 / 0`                 |
| `FileNotFoundError`  | File not found                | `open("no.txt")`         |
| `ValueError`         | Wrong value type              | `int("abc")`             |
| `IndexError`         | Index out of range            | `[1,2][5]`               |
| `KeyError`           | Missing key in dict           | `d["bad_key"]`           |
| `TypeError`          | Wrong type                    | `"2" + 2`                |
| `NameError`          | Variable not defined          | `print(x)` (x unknown)   |
| `AttributeError`     | Object has no such attribute  | `"hi".push("!")`         |
| `ImportError`        | Module not found              | `import xyz`             |
| `RecursionError`     | Too many recursive calls      | Infinite recursion        |

> 📝 **Your notes here:**

---

## 16. Modules & Imports

A **module** is a `.py` file containing reusable code (functions, classes, variables).
Python has many built-in modules. You can also install external ones.

```python
# Import full module
import math
print(math.sqrt(16))      # 4.0
print(math.pi)            # 3.14159...
print(math.ceil(3.2))     # 4
print(math.floor(3.9))    # 3

# Import specific functions only
from math import sqrt, pi, factorial
print(sqrt(25))           # 5.0
print(factorial(5))       # 120

# Import with alias (nickname)
import math as m
print(m.pow(2, 8))        # 256.0

# Import everything (not recommended — can cause name conflicts)
from math import *
```

### Useful Built-in Modules

```python
# os — file & folder operations
import os
print(os.getcwd())          # current working directory
print(os.listdir("."))      # list files in current folder
os.mkdir("new_folder")      # create a folder
os.remove("file.txt")       # delete a file
print(os.path.exists("x"))  # check if file/folder exists

# random — random values
import random
print(random.randint(1, 10))         # random int 1–10
print(random.choice(["a","b","c"]))  # random item from list
print(random.random())               # random float 0.0–1.0
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)                 # shuffle list in place
print(nums)

# datetime — dates and times
import datetime
today = datetime.date.today()
print(today)                         # 2025-06-01
now   = datetime.datetime.now()
print(now)                           # 2025-06-01 14:30:00.123456

# sys — system operations
import sys
print(sys.version)                   # Python version
print(sys.platform)                  # 'win32' or 'linux' or 'darwin'
sys.exit()                           # exit the program
```

### Creating Your Own Module
Any `.py` file is a module. Save functions in one file, import in another.

```python
# File: myutils.py
def greet(name):
    return f"Hello, {name}!"

def square(n):
    return n ** 2

PI = 3.14159
```

```python
# File: main.py — import from myutils.py
import myutils
print(myutils.greet("Amin"))   # Hello, Amin!
print(myutils.square(4))       # 16

# Or
from myutils import greet, PI
print(greet("Bob"))            # Hello, Bob!
print(PI)                      # 3.14159
```

> 📝 **Your notes here:**

---

## 17. Generators & yield

A **generator** is a special function that produces values **one at a time** instead of all at once.
It uses `yield` instead of `return`.
- **Memory efficient** — does not store all values at once
- **Lazy evaluation** — only computes the next value when asked

```python
# Regular function — creates entire list in memory
def get_squares(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Generator — produces one value at a time
def gen_squares(n):
    for i in range(n):
        yield i ** 2     # pauses here, returns value, resumes on next call

# Using the generator
gen = gen_squares(5)
print(next(gen))    # 0
print(next(gen))    # 1
print(next(gen))    # 4
print(next(gen))    # 9
print(next(gen))    # 16
# print(next(gen)) → StopIteration — no more values

# Loop through a generator
for val in gen_squares(5):
    print(val)
# 0 1 4 9 16

# Convert to list
print(list(gen_squares(5)))   # [0, 1, 4, 9, 16]
```

### Why Use Generators?
```python
# Bad — loads 1 million numbers into memory
def big_list(n):
    return [i for i in range(n)]

# Good — generates one number at a time, almost no memory used
def big_gen(n):
    for i in range(n):
        yield i

# Generator expression (like list comprehension, but with ())
gen = (x**2 for x in range(10))
print(list(gen))    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

```python
# Practical — reading a huge file line by line (memory efficient)
def read_lines(filepath):
    with open(filepath, "r") as f:
        for line in f:
            yield line.strip()

for line in read_lines("big_file.txt"):
    print(line)     # processes one line at a time, not entire file
```

> 📝 **Your notes here:**

---

## 18. Shallow vs Deep Copy

When you copy a mutable object (like a list), you need to be careful about **what kind of copy** you get.

### The Problem
```python
# Assignment — NO copy is made; both variables point to the same object
a = [1, 2, 3]
b = a
b.append(4)
print(a)   # [1, 2, 3, 4] — a also changed! They're the same object.
```

### Shallow Copy
Copies the outer object, but **nested objects are still shared** (same reference).

```python
import copy

original = [1, 2, [3, 4]]

# 3 ways to shallow copy a list
shallow1 = original.copy()
shallow2 = list(original)
shallow3 = copy.copy(original)

shallow1.append(99)
print(original)    # [1, 2, [3, 4]]  — outer list not affected

shallow1[2].append(99)           # modifying the nested list
print(original)    # [1, 2, [3, 4, 99]]  — AFFECTED! nested list is shared
```

### Deep Copy
Copies **everything** — outer and nested objects are completely independent.

```python
import copy

original = [1, 2, [3, 4]]
deep     = copy.deepcopy(original)

deep[2].append(99)
print(original)    # [1, 2, [3, 4]]  — NOT affected
print(deep)        # [1, 2, [3, 4, 99]]
```

### Summary

| Type         | Outer Object | Nested Objects |
|--------------|-------------|----------------|
| Assignment   | Same         | Same           |
| Shallow copy | New          | Same (shared)  |
| Deep copy    | New          | New (independent)|

```python
# When shallow copy is enough
nums  = [1, 2, 3, 4]     # no nesting
copy1 = nums.copy()
copy1.append(99)
print(nums)    # [1, 2, 3, 4]   — fine, no nesting

# When you NEED deep copy
matrix    = [[1, 2], [3, 4]]   # nested list
safe_copy = copy.deepcopy(matrix)
safe_copy[0][0] = 99
print(matrix)     # [[1, 2], [3, 4]]   — original untouched
```

> 📝 **Your notes here:**

---

## 19. `__name__ == "__main__"`

Every Python file has a built-in variable called `__name__`.
- If the file is **run directly**, `__name__` equals `"__main__"`
- If the file is **imported** by another file, `__name__` equals the **file's name** (without `.py`)

### Why it matters
Without this guard, code at the top level of a module runs **automatically when imported**, which is usually not what you want.

```python
# File: greet.py

def greet(name):
    print(f"Hello, {name}!")

def farewell(name):
    print(f"Goodbye, {name}!")

# This block runs ONLY when you run greet.py directly
# It does NOT run when another file imports greet.py
if __name__ == "__main__":
    greet("Amin")
    farewell("Bob")
```

```python
# File: main.py
import greet           # imports greet.py, but the if block does NOT run

greet.greet("Cara")    # Hello, Cara!
```

```python
# Practical pattern — every script you write should use this

def process_data(data):
    # ... your logic
    pass

def main():
    data = [1, 2, 3, 4, 5]
    result = process_data(data)
    print(result)

if __name__ == "__main__":
    main()    # runs only when this file is executed directly
```

> 📝 **Your notes here:**


---

## 20. OOP — Object Oriented Programming

OOP organizes code using **classes** and **objects**.
- **Class** — a blueprint/template. Contains attributes (data) and methods (functions).
- **Object** — an instance (copy) created from that blueprint.

---

### Access Modifiers
Control who can access a variable and from where.

| Modifier  | Syntax  | Access                                               |
|-----------|---------|------------------------------------------------------|
| Public    | `var`   | Anywhere — inside class, outside class, subclass     |
| Protected | `_var`  | Inside class + subclass (accessible outside but not recommended) |
| Private   | `__var` | Inside class only — needs getter/setter from outside |

```python
class Person:
    def __init__(self, name, age, salary):
        self.name     = name      # public
        self._age     = age       # protected
        self.__salary = salary    # private

    def show(self):
        print(f"{self.name}, {self._age}, {self.__salary}")   # all accessible inside

p = Person("Amin", 21, 50000)
print(p.name)       # Amin   — works fine
print(p._age)       # 21     — works but bad practice to use outside class
# print(p.__salary) # AttributeError — private!
p.show()            # Amin, 21, 50000 — accessible inside class
```

---

### Class & Object

```python
class Student:
    school = "Green Valley"    # class attribute — shared by ALL objects

    def __init__(self, name, roll):
        self.name = name       # object attribute — unique per object
        self.roll = roll

st1 = Student("Amin", 1)
st2 = Student("Bob",  2)

print(st1.name)          # Amin
print(st2.name)          # Bob
print(st1.school)        # Green Valley — class attribute
print(Student.school)    # Green Valley — access class attr directly via class
```

---

### Constructor `__init__()`
- Called **automatically** when a new object is created
- First parameter must be `self` — represents the object itself
- **Default constructor** — only `self`
- **Parameterized constructor** — `self` + extra parameters

```python
class Car:
    total_cars = 0    # class attribute

    def __init__(self, brand, model, year):
        self.brand  = brand      # object attributes
        self.model  = model
        self.year   = year
        Car.total_cars += 1      # update class attribute on every new object

    def info(self):
        print(f"{self.year} {self.brand} {self.model}")

c1 = Car("Toyota", "Corolla", 2020)
c2 = Car("Honda",  "Civic",   2022)
c3 = Car("BMW",    "X5",      2023)

c1.info()                  # 2020 Toyota Corolla
print(Car.total_cars)      # 3
```

---

### Methods

#### Instance Method
Normal method. Uses `self`. Accesses/modifies the object's data.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def scale(self, factor):
        self.width  *= factor
        self.height *= factor

r = Rectangle(4, 6)
print(r.area())         # 24
print(r.perimeter())    # 20
r.scale(2)
print(r.area())         # 96 (8 × 12)
```

#### Class Method
- Works at the class level
- Uses `cls` instead of `self`
- Uses `@classmethod` decorator
- Modifies or reads class-level variables

```python
class Employee:
    company  = "TechCorp"
    headcount = 0

    def __init__(self, name):
        self.name = name
        Employee.headcount += 1

    @classmethod
    def change_company(cls, name):
        cls.company = name

    @classmethod
    def get_headcount(cls):
        return cls.headcount

e1 = Employee("Amin")
e2 = Employee("Bob")
print(Employee.get_headcount())     # 2
Employee.change_company("InnoTech")
print(Employee.company)             # InnoTech
```

#### Static Method
- No `self` or `cls`
- Does not depend on object or class data
- Uses `@staticmethod` decorator
- Used for utility/helper logic related to the class

```python
class MathHelper:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def clamp(value, min_val, max_val):
        return max(min_val, min(value, max_val))

print(MathHelper.is_even(4))         # True
print(MathHelper.clamp(15, 0, 10))   # 10
print(MathHelper.clamp(-5, 0, 10))   # 0
```

---

### Object Relationships

#### Association
One class's method takes another class's object as a **parameter**. Both exist independently. Loosest relationship.

```python
class Car:
    def __init__(self, name):
        self.name = name

class Driver:
    def __init__(self, name):
        self.name = name

    def drive(self, car):     # uses Car object as a parameter
        print(f"{self.name} is driving {car.name}")

car1    = Car("Tesla")
driver1 = Driver("Amin")
driver1.drive(car1)           # Amin is driving Tesla
# Both Car and Driver exist independently; no ownership
```

#### Aggregation
One class holds another class's object as an **instance variable**. Both can exist independently. Child survives if parent is deleted.

```python
class Engine:
    def __init__(self, horsepower):
        self.hp = horsepower

    def start(self):
        print(f"Engine started ({self.hp}hp)")

class Car:
    def __init__(self, name, engine):    # engine passed from OUTSIDE
        self.name   = name
        self.engine = engine

e1  = Engine(200)               # Engine exists on its own
car = Car("Toyota", engine=e1)  # Car holds a reference to the engine
car.engine.start()              # Engine started (200hp)
# If car object is deleted, e1 still exists
```

#### Composition
One class **creates** the other class's object inside itself. Child cannot exist without parent.

```python
class Heart:
    def beat(self):
        print("Heart is beating")

class Human:
    def __init__(self, name):
        self.name  = name
        self.heart = Heart()     # Heart is created INSIDE Human

    def live(self):
        self.heart.beat()

h = Human("Amin")
h.live()     # Heart is beating
# If h is deleted, the Heart object is also gone — tight coupling
```

---

### The 4 Pillars of OOP

---

#### Pillar 1 — Encapsulation
Bundle data + methods inside a class. Restrict direct access to internal data using private variables. Expose only what is necessary via getter/setter.

```python
# Normal getter/setter
class BankAccount:
    def __init__(self, holder, balance):
        self.__holder  = holder
        self.__balance = balance

    def get_balance(self):          # getter
        return self.__balance

    def deposit(self, amount):      # setter-style
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount

acc = BankAccount("Amin", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())    # 1300
```

```python
# Pythonic way — @property
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):            # getter
        return self.__celsius

    @celsius.setter
    def celsius(self, value):     # setter
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self.__celsius = value

    @property
    def fahrenheit(self):         # computed property (no setter needed)
        return self.__celsius * 9/5 + 32

t = Temperature(25)
print(t.celsius)       # 25
print(t.fahrenheit)    # 77.0
t.celsius = 100
print(t.fahrenheit)    # 212.0
# t.celsius = -300     # ValueError
```

---

#### Pillar 2 — Inheritance
Child class gets all properties and methods of the parent class. Promotes code reuse.

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says: Meow!")

dog = Dog("Rex", 3)
cat = Cat("Whiskers", 2)
dog.eat()     # Rex is eating     — inherited from Animal
dog.bark()    # Rex says: Woof!   — Dog's own method
cat.sleep()   # Whiskers is sleeping — inherited
cat.meow()    # Whiskers says: Meow!
```

#### Types of Inheritance
```python
# Single inheritance
class A: pass
class B(A): pass

# Multilevel — grandparent → parent → child
class Vehicle:
    def move(self): print("Moving")

class Car(Vehicle):
    def drive(self): print("Driving")

class SportsCar(Car):
    def turbo(self): print("Turbo boost!")

sc = SportsCar()
sc.move()     # Moving  — from Vehicle
sc.drive()    # Driving — from Car
sc.turbo()    # Turbo boost! — own method

# Multiple inheritance
class Flyable:
    def fly(self): print("Flying")

class Swimmable:
    def swim(self): print("Swimming")

class Duck(Flyable, Swimmable):
    def quack(self): print("Quack!")

d = Duck()
d.fly()     # Flying
d.swim()    # Swimming
d.quack()   # Quack!
```

#### super() — Access Parent Class
```python
class Shape:
    def __init__(self, color):
        self.color = color

    def info(self):
        print(f"Color: {self.color}")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)    # call parent __init__
        self.radius = radius

    def info(self):
        super().info()             # call parent info()
        print(f"Radius: {self.radius}")
        print(f"Area: {3.1416 * self.radius**2:.2f}")

c = Circle("Red", 5)
c.info()
# Color: Red
# Radius: 5
# Area: 78.54
```

---

#### Pillar 3 — Polymorphism
Same method name, **different behavior** depending on the class. "Many forms."

```python
class Shape:
    def area(self): return 0

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.1416 * self.r ** 2

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h

class Triangle(Shape):
    def __init__(self, b, h): self.b, self.h = b, h
    def area(self): return 0.5 * self.b * self.h

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

for shape in shapes:
    print(f"{shape.__class__.__name__}: area = {shape.area():.2f}")
# Circle: area = 78.54
# Rectangle: area = 24.00
# Triangle: area = 12.00
```

#### Operator Overloading
Redefine built-in operators (`+`, `-`, `*`, `==`, etc.) for your own objects using dunder methods.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):       # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):       # v1 - v2
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):      # v1 * 3
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):        # v1 == v2
        return self.x == other.x and self.y == other.y

    def __str__(self):              # print(v1)
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)    # Vector(4, 6)
print(v1 - v2)    # Vector(-2, -2)
print(v1 * 3)     # Vector(3, 6)
print(v1 == v2)   # False
```

---

#### Pillar 4 — Abstraction
Hide internal details. Show only what is needed. Achieved using **abstract classes**.
Abstract methods have **no body** — child classes are **forced** to implement them.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass        # no body — must be implemented

    @abstractmethod
    def perimeter(self): pass   # no body — must be implemented

    def describe(self):         # regular method — shared, not abstract
        print(f"I am a {self.__class__.__name__} with area {self.area():.2f}")

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):       return 3.1416 * self.r**2
    def perimeter(self):  return 2 * 3.1416 * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):       return self.w * self.h
    def perimeter(self):  return 2 * (self.w + self.h)

# Shape()   → TypeError: Can't instantiate abstract class
c = Circle(5)
r = Rectangle(4, 6)

c.describe()   # I am a Circle with area 78.54
r.describe()   # I am a Rectangle with area 24.00
```

---

### Property Decorator
Makes a method behave like a variable. Auto-recalculates when attributes change.

```python
class Student:
    def __init__(self, phy, chem, math):
        self.phy  = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return (self.phy + self.chem + self.math) / 3

    @property
    def grade(self):
        p = self.percentage
        if p >= 90: return "A+"
        elif p >= 80: return "A"
        elif p >= 70: return "B"
        else: return "C"

st = Student(88, 92, 91)
print(st.percentage)   # 90.33  — accessed like a variable, not st.percentage()
print(st.grade)        # A+     — auto computed, no call needed

st.phy = 60
print(st.percentage)   # 81.0   — auto updated
print(st.grade)        # A
```

---

### Dunder / Magic Methods
Built-in special methods starting and ending with `__`. Define how objects behave in built-in operations.

```python
class Book:
    def __init__(self, title, author, pages):
        self.title  = title
        self.author = author
        self.pages  = pages

    def __str__(self):            # print(book)
        return f'"{self.title}" by {self.author}'

    def __repr__(self):           # repr(book) — developer representation
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):            # len(book)
        return self.pages

    def __add__(self, other):     # book1 + book2 — total pages
        return self.pages + other.pages

    def __eq__(self, other):      # book1 == book2
        return self.title == other.title

    def __lt__(self, other):      # book1 < book2 — compare by pages
        return self.pages < other.pages

    def __contains__(self, word): # "python" in book
        return word.lower() in self.title.lower()

b1 = Book("Python Basics",  "Amin", 300)
b2 = Book("OOP in Python",  "Bob",  200)
b3 = Book("Python Basics",  "Amin", 300)

print(b1)             # "Python Basics" by Amin
print(repr(b1))       # Book('Python Basics', 'Amin', 300)
print(len(b1))        # 300
print(b1 + b2)        # 500 (total pages)
print(b1 == b3)       # True (same title)
print(b1 < b2)        # False (300 > 200)
print("Python" in b1) # True
```

| Dunder Method | Triggered by                |
|---------------|-----------------------------|
| `__init__`    | `obj = MyClass()`           |
| `__str__`     | `print(obj)`, `str(obj)`    |
| `__repr__`    | `repr(obj)`                 |
| `__len__`     | `len(obj)`                  |
| `__add__`     | `obj1 + obj2`               |
| `__sub__`     | `obj1 - obj2`               |
| `__mul__`     | `obj1 * val`                |
| `__eq__`      | `obj1 == obj2`              |
| `__lt__`      | `obj1 < obj2`               |
| `__contains__`| `item in obj`               |
| `__del__`     | object is deleted           |

---

### Deleting Objects & Attributes
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} object deleted")

d = Dog("Rex")
print(d.name)     # Rex
del d.name        # deletes just the attribute
# print(d.name)   # AttributeError — attribute is gone

del d             # deletes the whole object → prints "Rex object deleted"
```

---

### OOP Practice Problems

#### Problem 1 — Student Result System
```python
class Student:
    def __init__(self, name, roll):
        self.__name  = name
        self.roll    = roll
        self.marks   = {}

    @property
    def name(self): return self.__name

    @name.setter
    def name(self, val): self.__name = val

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def average(self):
        if not self.marks: return 0
        return sum(self.marks.values()) / len(self.marks)

    @property
    def grade(self):
        avg = self.average()
        return "A+" if avg >= 90 else "A" if avg >= 80 else "B" if avg >= 70 else "C"

    def report(self):
        print(f"\n--- Report: {self.name} (Roll: {self.roll}) ---")
        for sub, mark in self.marks.items():
            print(f"  {sub}: {mark}")
        print(f"  Average: {self.average():.2f}  |  Grade: {self.grade}")

s = Student("Amin", 101)
s.add_mark("Math",    92)
s.add_mark("English", 85)
s.add_mark("Science", 90)
s.report()
```

#### Problem 2 — Shape Area Calculator (Abstraction)
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, r):         self.r = r
    def area(self):                return 3.1416 * self.r**2
    def perimeter(self):           return 2 * 3.1416 * self.r

class Rectangle(Shape):
    def __init__(self, w, h):      self.w, self.h = w, h
    def area(self):                return self.w * self.h
    def perimeter(self):           return 2 * (self.w + self.h)

class Triangle(Shape):
    def __init__(self, a, b, c):   self.a, self.b, self.c = a, b, c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
    def perimeter(self):           return self.a + self.b + self.c

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for s in shapes:
    print(f"{s.__class__.__name__}: area={s.area():.2f}, perimeter={s.perimeter():.2f}")
```

#### Problem 3 — Employee & Manager (Inheritance)
```python
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name    = name
        self.emp_id  = emp_id
        self.salary  = salary

    def details(self):
        print(f"ID: {self.emp_id} | Name: {self.name} | Salary: {self.salary}")

    def annual_salary(self):
        return self.salary * 12

class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department
        self.team       = []

    def add_member(self, emp):
        self.team.append(emp)

    def details(self):
        super().details()
        print(f"Department: {self.department} | Team size: {len(self.team)}")

e1 = Employee("Bob",  "E001", 50000)
e2 = Employee("Cara", "E002", 45000)
m1 = Manager("Amin",  "M001", 80000, "Engineering")
m1.add_member(e1)
m1.add_member(e2)
m1.details()
print(f"Annual salary: {m1.annual_salary()}")
```

#### Problem 4 — Vehicle Rental (Polymorphism)
```python
class Vehicle:
    def __init__(self, name):
        self.name = name
    def calculate_rent(self, days): return 0

class Car(Vehicle):
    def calculate_rent(self, days): return 40 * days

class Bike(Vehicle):
    def calculate_rent(self, days): return 20 * days

class Bus(Vehicle):
    def calculate_rent(self, days): return 60 * days

vehicles = [Car("Toyota"), Bike("Yamaha"), Bus("Volvo")]
days     = 5

for v in vehicles:
    rent = v.calculate_rent(days)
    print(f"{v.name} for {days} days: {rent} Taka")
```

> 📝 **Your notes here:**

---

## Extra — C++ Comparison

| Concept               | Python                           | C++                            |
|-----------------------|----------------------------------|--------------------------------|
| Overloading           | `__add__`, `__mul__`, etc.       | Same name, different params    |
| Overriding            | Child redefines parent method    | `virtual` keyword              |
| Pure virtual function | `@abstractmethod`                | `virtual void f() = 0`         |
| Friend function       | Not in Python                    | Access private without inheriting|
| Destructor            | `__del__(self)`                  | `~ClassName()`                 |

---

*End of notes — add anything you want below* ↓

---
