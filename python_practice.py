"""
==========================================================
 PYTHON PRACTICE FILE
==========================================================
Generated from your Python notes.

HOW TO USE:
- Run this file:  python python_practice.py
- A menu will appear showing all 20 topics.
- Enter a topic number to run its examples.
- Read the short theory comment at the top of each topic,
  then study/run the code below it.
- Edit the code directly and re-run to practice!
==========================================================
"""


# ==========================================================
# 1. PYTHON BASICS
# ==========================================================
def topic_01_basics():
    """
    THEORY:
    - Python is high-level, easy to read, dynamically typed
      (type is decided automatically from the value).
    - It's an interpreter language -> runs line by line.
    - Case sensitive: Name != name
    - Variable names: letters/digits/underscore only,
      cannot start with a digit, cannot be a keyword.
    """
    print("\n--- 1. Python Basics ---")

    # Basic output / arithmetic
    print("Hello World")
    print(4 / 3)        # true division -> 1.333...
    print(2 ** 10)      # power -> 1024
    print(10 % 3)       # remainder -> 1

    # Statements
    x = 5               # assignment statement
    y = x + 10          # expression statement
    print(y)            # function call statement

    # Multiple statements on one line (valid, not recommended)
    a = 1; b = 2; c = 3
    print(a, b, c)

    # Valid variable names
    my_name = "Amin"
    age1 = 21
    _score = 99
    print(my_name, age1, _score)


# ==========================================================
# 2. DATA TYPES & TYPE CASTING
# ==========================================================
def topic_02_data_types():
    """
    THEORY:
    - Basic types: int, float, str, bool, None
    - Type casting: Explicit (you convert manually using
      int(), str(), float(), bool(), list() etc.)
      Implicit (Python converts automatically, e.g. int+float -> float)
    - Falsy values: 0, "", [], {}, None, False
    """
    print("\n--- 2. Data Types & Type Casting ---")

    x, name, pi, flag, val = 10, "Amin", 3.14, True, None
    print(type(x), type(name), type(pi), type(flag), type(val))

    # Explicit casting
    a = int("5")        # "5" -> 5
    b = str(10)         # 10 -> "10"
    c = float("3.14")   # "3.14" -> 3.14
    d = int(9.9)        # 9.9 -> 9  (decimal dropped, NOT rounded)
    e = bool(0)         # 0 -> False
    f = bool("hello")   # non-empty string -> True
    print(a, b, c, d, e, f)

    # Implicit casting
    result = 5 + 2.0    # int + float -> float
    print(result, type(result))

    # Truthy / falsy checks
    print(bool(0), bool(""), bool([]), bool(None), bool(42), bool("hi"))


# ==========================================================
# 3. OPERATORS
# ==========================================================
def topic_03_operators():
    """
    THEORY:
    - Arithmetic: + - * / // % **
      (/ always gives float, // floors the result)
    - Comparison: == != > < >= <=  -> returns True/False
    - Logical: and, or, not
    - Identity: is / is not -> same object in memory (not same value)
    - Membership: in / not in -> checks inside iterable
    - Precedence (high->low): () ** unary */ //% +-
      comparisons -> not -> and -> or -> assignment
    """
    print("\n--- 3. Operators ---")

    # Arithmetic
    print(5 + 3, 5 - 3, 5 * 3, 5 / 2, 5 // 2, 5 % 2, 2 ** 3)
    print(10 % 2 == 0)   # even check

    # Comparison
    print(5 == 5, 5 != 3, 5 > 3, 5 < 3, 5 >= 5, 5 <= 4)

    # Logical
    age, has_id = 20, True
    print(age >= 18 and has_id)

    # Assignment operators
    x = 10
    x += 5   # 15
    x -= 3   # 12
    x *= 2   # 24
    print(x)

    # Identity vs equality
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    print(a is b)       # True - same object
    print(a is c)       # False - same value, different object

    # Membership
    fruits = ["apple", "banana"]
    print("apple" in fruits, "cherry" not in fruits)

    # Precedence examples
    print(2 + 3 * 4)          # 14 (* before +)
    print((2 + 3) * 4)        # 20 (() first)
    print(2 ** 3 ** 2)        # 512 (** is right-to-left -> 2**9)
    print(not True or False)  # False ('not' before 'or')


# ==========================================================
# 4. INPUT & OUTPUT
# ==========================================================
def topic_04_input_output():
    """
    THEORY:
    - input() ALWAYS returns a string -> typecast if needed.
    - Printing: + (string concat, needs str()), f-string (best),
      comma (auto adds space), .format()
    - print() options: sep=, end=
    """
    print("\n--- 4. Input & Output ---")

    name, age = "Amin", 21

    # Different ways to print
    print("Name: " + name + ", Age: " + str(age))   # needs str()
    print(f"Name: {name}, Age: {age}")              # f-string (best)
    print("Name:", name, "Age:", age)               # comma adds space
    print("Name: {}, Age: {}".format(name, age))    # .format()

    # f-string with expressions
    x = 10
    print(f"Double of x is {x * 2}")
    print(f"Pi is approximately {22/7:.2f}")

    # print() options
    print("Hello", "World", sep="-")   # Hello-World
    print("Hello", end=" ")            # stays on same line
    print("World")

    # Taking input (uncomment to try interactively)
    # a, b = input("Enter two numbers: ").split()
    # a, b = int(a), int(b)
    # print(f"Sum = {a + b}")

    # Using map() for multiple inputs
    # x, y = map(int, input("Enter two numbers: ").split())
    # print(x + y)


# ==========================================================
# MENU (will be completed at the bottom of the file)
# ==========================================================


# ==========================================================
# 5. CONDITIONAL STATEMENTS - if / elif / else
# ==========================================================
def topic_05_conditionals():
    """
    THEORY:
    - if/elif/else runs a block ONLY when the condition is True.
    - elif checks more conditions in order; else is the fallback.
    - Useful patterns: membership check (in), emptiness check
      (not name), None check (is None), chained comparison
      (10 < x < 20).
    """
    print("\n--- 5. Conditional Statements ---")

    # Basic if/else
    age = 18
    if age >= 18:
        print("Adult")
    else:
        print("Minor")

    # if/elif/else - grading
    score = 75
    if score >= 90:
        print("Grade: A+")
    elif score >= 80:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    else:
        print("Grade: F")

    # Nested if
    logged_in, is_admin = True, False
    if logged_in:
        if is_admin:
            print("Welcome, Admin!")
        else:
            print("Welcome, User!")
    else:
        print("Please log in.")

    # Useful condition patterns
    fruits = ["apple", "banana"]
    if "apple" in fruits:                 # membership check
        print("Found!")

    name = ""
    if not name:                          # empty string -> False
        print("Name is empty")

    val = None
    if val is None:                       # None check
        print("No value assigned")

    x = 15
    if 10 < x < 20:                       # chained comparison
        print("x is between 10 and 20")

    # Practical: number categorizer
    def categorize(n):
        if n > 0:
            return "positive"
        elif n < 0:
            return "negative"
        else:
            return "zero"

    print(categorize(5), categorize(-3), categorize(0))

    # Practical: grade function with validation
    def grade(s):
        if not isinstance(s, (int, float)):
            raise TypeError("Score must be a number")
        if s < 0 or s > 100:
            raise ValueError("Score must be between 0 and 100")
        if s >= 90:
            return "A+"
        elif s >= 80:
            return "A"
        elif s >= 70:
            return "B"
        elif s >= 60:
            return "C"
        else:
            return "F"

    print(grade(95), grade(72), grade(55))


# ==========================================================
# 6. STRINGS
# ==========================================================
def topic_06_strings():
    """
    THEORY:
    - Strings are IMMUTABLE, ordered, indexed (start at 0,
      negative index counts from the end -1).
    - Slicing: str[start:stop:step] -> stop is EXCLUDED.
    - String methods return a NEW string, original is unchanged.
    """
    print("\n--- 6. Strings ---")

    # Indexing
    s = "Python"
    print(s[0], s[-1], s[2], s[-2])   # P n t o

    # Slicing
    print(s[1:4])     # yth
    print(s[2:])      # thon
    print(s[:4])      # Pyth
    print(s[-3:-1])   # ho
    print(s[::-1])    # nohtyP  (reverse, step=-1)
    print(s[::2])     # Pto     (every 2nd char)

    # Escape sequences
    print("Hello\nWorld")     # \n = new line
    print("Hello\tWorld")     # \t = tab
    print("He said \"Hi\"")   # \" = quote inside string

    # String methods (return new string)
    text = "  Hello World  "
    print(text.lower())
    print(text.upper())
    print(text.strip())                 # remove surrounding whitespace
    print(text.find("World"))           # index of substring, -1 if missing
    print(text.replace("World", "Python"))
    print("a,b,c".split(","))           # -> ['a','b','c']
    print("-".join(["a", "b", "c"]))    # -> "a-b-c"

    # Check methods
    print("hello".isalpha(), "123".isdigit(), "hello1".isalnum())

    # Practical: count vowels
    sentence = "Hello World"
    vowels = "aeiouAEIOU"
    count = sum(1 for ch in sentence if ch in vowels)
    print(f"Vowels: {count}")

    # Practical: reverse words in a sentence
    sentence2 = "I love Python"
    reversed_sentence = " ".join(sentence2.split()[::-1])
    print(reversed_sentence)   # Python love I


# ==========================================================
# 7. DATA STRUCTURES (List, Tuple, Dict, Set)
# ==========================================================
def topic_07_data_structures():
    """
    THEORY:
    - List []  : mutable, ordered, allows duplicates -> changing data
    - Tuple (): immutable, ordered, allows duplicates -> fixed data
                single-element tuple needs a trailing comma (5,)
    - Dict {} : mutable, key:value pairs, keys must be unique &
                immutable (no list as key)
    - Set {}  : mutable, unordered, NO duplicates, elements must
                be immutable. Empty set = set(), NOT {}
    """
    print("\n--- 7. Data Structures ---")

    # ---------- LIST ----------
    li = [3, 1, 4, 1, 5, 9, 2, 6]
    li.append(7)            # add at end
    li.insert(2, 99)        # insert 99 at index 2
    li.sort()                # ascending, in place
    print(li)
    print(li.pop())          # remove & return last item
    print(len(li))

    students = ["Amin", "Bob", "Cara", "Dave"]
    students.append("Eve")
    students.remove("Bob")
    for i, name in enumerate(students):
        print(f"{i+1}. {name}")

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix[1][2])      # 6  (row 1, col 2)

    # ---------- TUPLE ----------
    t = (10, 20, 30, 20)
    print(t[0], t.count(20))

    t2 = (5,)                # single element tuple needs comma
    print(type(t2))

    # Swapping values via tuple unpacking
    a, b = 10, 20
    a, b = b, a
    print(a, b)               # 20 10

    # Return multiple values (returned as tuple)
    def min_max(nums):
        return min(nums), max(nums)
    low, high = min_max([3, 1, 7, 2, 9])
    print(low, high)

    # ---------- DICTIONARY ----------
    person = {"name": "Amin", "age": 21, "city": "Dhaka"}
    print(person["name"])             # direct access
    print(person.get("email", "N/A")) # safe access with default
    person["age"] = 25                # update
    person["email"] = "a@b.com"       # add new key
    del person["city"]                # delete a key
    print(person)

    # Count character frequency
    word = "mississippi"
    freq = {}
    for ch in word:
        freq[ch] = freq.get(ch, 0) + 1
    print(freq)

    # Merge dictionaries (Python 3.9+)
    d1, d2 = {"a": 1, "b": 2}, {"c": 3, "d": 4}
    print(d1 | d2)

    # ---------- SET ----------
    s = {1, 2, 3, 3, 4, 4}
    print(s)                  # duplicates removed automatically

    s2 = {3, 4, 5, 6}
    print(s.union(s2))        # all unique elements
    print(s.intersection(s2)) # common elements
    print(s.difference(s2))   # in s but not in s2

    # Remove duplicates from a list using set
    nums = [1, 2, 2, 3, 3, 4, 5, 5]
    print(list(set(nums)))


# ==========================================================
# 8. COMPREHENSIONS
# ==========================================================
def topic_08_comprehensions():
    """
    THEORY:
    - Short, one-line way to build a list/dict/set from a loop.
    - List:  [expr for item in iterable if condition]
    - Dict:  {key_expr: val_expr for item in iterable}
    - Set:   {expr for item in iterable}
    """
    print("\n--- 8. Comprehensions ---")

    # List comprehension
    squares = [x ** 2 for x in range(5)]
    print(squares)                                  # [0,1,4,9,16]

    evens = [x for x in range(10) if x % 2 == 0]    # with condition
    print(evens)

    # Flatten a nested list
    matrix = [[1, 2], [3, 4], [5, 6]]
    flat = [num for row in matrix for num in row]
    print(flat)

    # Dict comprehension
    nums = [1, 2, 3, 4, 5]
    sq_map = {x: x ** 2 for x in nums}
    print(sq_map)

    # Build dict from two lists with zip
    keys, values = ["name", "age", "city"], ["Amin", 21, "Dhaka"]
    d = {k: v for k, v in zip(keys, values)}
    print(d)

    # Swap keys and values
    original = {"a": 1, "b": 2, "c": 3}
    swapped = {v: k for k, v in original.items()}
    print(swapped)

    # Set comprehension - only vowels in a string
    text = "Hello World"
    vowels = {ch.lower() for ch in text if ch.lower() in "aeiou"}
    print(vowels)


# ==========================================================
# 9. BUILT-IN FUNCTIONS
# ==========================================================
def topic_09_builtin_functions():
    """
    THEORY:
    - len, min, max, sum, sorted, abs, round, pow
    - any(): True if AT LEAST ONE item is True
    - all(): True if ALL items are True
    - enumerate(): gives (index, value) while looping
    - zip(): combines iterables pair by pair, stops at shortest
    - map(): apply a function to every item
    - filter(): keep items where function returns True
    """
    print("\n--- 9. Built-in Functions ---")

    nums = [3, 1, 7, 2, 9, 4]
    print(len(nums), min(nums), max(nums), sum(nums))
    print(sorted(nums))            # new sorted list, original unchanged
    print(abs(-5), round(3.14159, 2), pow(2, 8))

    # any() / all()
    print(any(x % 2 != 0 for x in nums))  # True - at least one odd
    print(all(x % 2 == 0 for x in nums))  # False - not all even

    # enumerate()
    fruits = ["apple", "banana", "cherry"]
    for i, fruit in enumerate(fruits, start=1):
        print(f"{i}. {fruit}")

    # zip()
    names, scores = ["Amin", "Bob", "Cara"], [90, 85, 92]
    for name, score in zip(names, scores):
        print(f"{name}: {score}")

    # Create dict from two lists via zip
    d = dict(zip(["a", "b", "c"], [1, 2, 3]))
    print(d)

    # map() and filter()
    doubled = list(map(lambda x: x * 2, [1, 2, 3, 4]))
    evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
    print(doubled, evens)

    # sorted() with custom key
    words = ["banana", "fig", "cherry", "apple"]
    print(sorted(words, key=len))                       # sort by length

    students = [("Amin", 90), ("Bob", 85), ("Cara", 92)]
    print(sorted(students, key=lambda s: s[1]))         # sort by score


# ==========================================================
# 10. LOOPS
# ==========================================================
def topic_10_loops():
    """
    THEORY:
    - while: use when you have a stopping condition (not a fixed count)
    - for: traverse a list/string/tuple/dict/range
    - break: exit loop completely
    - continue: skip rest of current iteration
    - pass: placeholder, does nothing
    - for...else: else runs only if loop completes WITHOUT break
    """
    print("\n--- 10. Loops ---")

    # While loop
    i = 0
    while i < 5:
        print(i, end=" ")
        i += 1
    print()

    # Find first number divisible by both 3 and 7
    n = 1
    while n <= 100:
        if n % 3 == 0 and n % 7 == 0:
            print(f"Found: {n}")
            break
        n += 1

    # For loop with range
    for i in range(1, 6):
        print(i, end=" ")
    print()

    # Loop through dictionary
    person = {"name": "Amin", "age": 21}
    for key, value in person.items():
        print(f"{key}: {value}")

    # for...else
    for i in range(5):
        if i == 10:        # never true here
            break
        print(i, end=" ")
    else:
        print("\nLoop completed without break")

    # Nested loop - multiplication table
    for a in range(1, 4):
        for b in range(1, 4):
            print(f"{a} x {b} = {a*b}")
        print("---")

    # Pattern printing
    for i in range(1, 6):
        print("*" * i)

    # break / continue / pass
    for i in range(10):
        if i == 5:
            break          # stop loop entirely
        print(i, end=" ")
    print()

    for i in range(6):
        if i % 2 == 0:
            continue        # skip even numbers
        print(i, end=" ")
    print()

    for i in range(3):
        pass                # placeholder - does nothing


# ==========================================================
# 11. UNPACKING & MULTIPLE ASSIGNMENT
# ==========================================================
def topic_11_unpacking():
    """
    THEORY:
    - Unpacking assigns values from a list/tuple to variables
      directly: a, b, c = 1, 2, 3
    - * collects "leftover" values into a list while unpacking.
    - Use _ as a throwaway variable for values you don't need.
    - * can also "spread" a list into separate function arguments.
    """
    print("\n--- 11. Unpacking & Multiple Assignment ---")

    # Basic unpacking
    a, b, c = 1, 2, 3
    print(a, b, c)

    nums = [10, 20, 30]
    x, y, z = nums
    print(x, y, z)

    # Swap without temp variable
    a, b = 10, 20
    a, b = b, a
    print(a, b)

    # Extended unpacking with *
    first, *rest = [1, 2, 3, 4, 5]
    print(first, rest)          # 1 [2, 3, 4, 5]

    *start, last = [1, 2, 3, 4, 5]
    print(start, last)          # [1, 2, 3, 4] 5

    a, *middle, b = [1, 2, 3, 4, 5]
    print(a, middle, b)         # 1 [2, 3, 4] 5

    # Ignore values with _
    name, _, city = ("Amin", 21, "Dhaka")
    print(name, city)

    # Unpack returned tuple from a function
    def get_range(values):
        return min(values), max(values)
    low, high = get_range([3, 1, 9, 2, 7])
    print(low, high)

    # Spread a list into a function call using *
    def add(a, b, c):
        return a + b + c
    nums2 = [1, 2, 3]
    print(add(*nums2))   # same as add(1, 2, 3)


# ==========================================================
# 12. FUNCTIONS
# ==========================================================
def topic_12_functions():
    """
    THEORY:
    - def function_name(parameters): ... return value
    - Default values: used when no argument is passed.
    - Ternary: value_if_true if condition else value_if_false
    - *args  -> collects extra positional args into a TUPLE
    - **kwargs -> collects extra keyword args into a DICT
    - Scope: local var (inside function) vs global var.
      Use 'global' to MODIFY a global variable inside a function.
    - nonlocal: lets a nested function modify the enclosing
      function's variable.
    - lambda: small anonymous one-line function.
    - Recursion: function calling itself, MUST have a base case.
    """
    print("\n--- 12. Functions ---")

    # Basic function + default values
    def greet(name="stranger", greeting="Hello"):
        print(f"{greeting}, {name}!")
    greet("Amin")
    greet()
    greet(greeting="Hey")

    # Ternary operator
    x = 10
    label = "even" if x % 2 == 0 else "odd"
    print(label)

    # *args
    def add_all(*args):
        print("args:", args)        # tuple
        return sum(args)
    print(add_all(1, 2, 3, 4))

    # **kwargs
    def show_info(**kwargs):
        print("kwargs:", kwargs)    # dict
        for k, v in kwargs.items():
            print(f"{k}: {v}")
    show_info(name="Amin", age=21, city="Dhaka")

    # global keyword
    count = 0
    def increment():
        nonlocal count   # 'count' is enclosed in this function's scope
        count += 1
    increment()
    increment()
    print("count:", count)

    # Nested function + nonlocal (closure / counter)
    def make_counter():
        c = 0
        def step():
            nonlocal c
            c += 1
            return c
        return step
    counter = make_counter()
    print(counter(), counter(), counter())   # 1 2 3

    # Lambda functions
    square = lambda n: n ** 2
    classify = lambda n: "even" if n % 2 == 0 else "odd"
    print(square(4), classify(4))

    # Recursion - factorial
    def factorial(n):
        if n <= 1:                 # base case
            return 1
        return n * factorial(n - 1)
    print(factorial(5))            # 120

    # Recursion - fibonacci sequence
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)
    print([fib(i) for i in range(8)])


# ==========================================================
# 13. TYPE CHECKING - isinstance()
# ==========================================================
def topic_13_isinstance():
    """
    THEORY:
    - isinstance(obj, type) -> True/False. Better than
      type(x) == int because it also works with inheritance.
    - isinstance(x, (int, float)) -> check against multiple types.
    - issubclass(Child, Parent) -> True if Child inherits Parent.
    """
    print("\n--- 13. Type Checking (isinstance) ---")

    x = 42
    print(isinstance(x, int))             # True
    print(isinstance(x, (int, float)))    # True

    li = [1, 2, 3]
    print(isinstance(li, (list, tuple)))  # True

    # Validate input type inside a function
    def double(n):
        if not isinstance(n, (int, float)):
            raise TypeError(f"Expected a number, got {type(n).__name__}")
        return n * 2
    print(double(5), double(3.5))

    # isinstance with inheritance
    class Animal:
        pass
    class Dog(Animal):
        pass
    d = Dog()
    print(isinstance(d, Dog), isinstance(d, Animal))

    # issubclass
    print(issubclass(Dog, Animal), issubclass(Animal, Dog))


# ==========================================================
# 14. FILE I/O
# ==========================================================
def topic_14_file_io():
    """
    THEORY:
    - 'with open(...) as f:' is the RECOMMENDED way - it
      auto-closes the file even if an error happens.
    - Modes: 'r' read, 'w' write (overwrite), 'a' append,
      'x' create new (errors if exists), 'r+' read+write.
    - read() -> whole file as string, readline() -> one line,
      readlines() -> list of lines.
    - csv module: csv.reader / csv.writer / csv.DictReader.
    """
    print("\n--- 14. File I/O ---")

    # Writing to a file (creates/overwrites)
    with open("output.txt", "w") as f:
        f.write("Line 1\n")
        f.write("Line 2\n")

    # Appending to a file
    with open("output.txt", "a") as f:
        f.write("This line is appended\n")

    # Reading the whole file
    with open("output.txt", "r") as f:
        content = f.read()
        print(content)

    # Reading line by line
    with open("output.txt", "r") as f:
        for line in f:
            print(line.strip())     # .strip() removes the trailing \n

    # Deleting a file (only if it exists)
    import os
    if os.path.exists("output.txt"):
        os.remove("output.txt")
        print("File deleted")

    # ---- CSV example ----
    import csv
    # Write CSV
    with open("data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "City"])
        writer.writerows([["Alice", 25, "New York"], ["Bob", 30, "LA"]])

    # Read CSV as dictionaries (key = column header)
    with open("data.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row["Name"], row["Age"])

    if os.path.exists("data.csv"):
        os.remove("data.csv")


# ==========================================================
# 15. ERROR HANDLING
# ==========================================================
def topic_15_error_handling():
    """
    THEORY:
    - try: code that might fail
      except SpecificError: handle that error
      except Exception as e: catch-all (use last)
      else: runs ONLY if no error occurred
      finally: ALWAYS runs (use for cleanup)
    - raise: trigger an error manually (with a message)
    - Custom exceptions: inherit from Exception class.
    """
    print("\n--- 15. Error Handling ---")

    # Basic try/except/else/finally
    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("Error!")
    else:
        print("Success! Result:", result)
    finally:
        print("Done.")

    # raise - manual validation
    def set_age(age):
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")
        if age < 0 or age > 150:
            raise ValueError(f"Age {age} is out of valid range (0-150)")
        return age

    try:
        print(set_age(25))
        print(set_age(-5))     # triggers ValueError
    except ValueError as e:
        print(e)

    # Custom exception classes
    class InsufficientFundsError(Exception):
        pass

    class InvalidAmountError(Exception):
        def __init__(self, amount, message="Amount must be positive"):
            self.amount = amount
            super().__init__(f"{message}: {amount}")

    class BankAccount:
        def __init__(self, balance):
            self.balance = balance

        def withdraw(self, amount):
            if amount <= 0:
                raise InvalidAmountError(amount)
            if amount > self.balance:
                raise InsufficientFundsError(
                    f"Cannot withdraw {amount}, balance is {self.balance}")
            self.balance -= amount
            return self.balance

    acc = BankAccount(500)
    try:
        acc.withdraw(200)
        print("Balance:", acc.balance)
        acc.withdraw(1000)     # raises InsufficientFundsError
    except InsufficientFundsError as e:
        print(e)
    except InvalidAmountError as e:
        print(e)


# ==========================================================
# 16. MODULES & IMPORTS
# ==========================================================
def topic_16_modules():
    """
    THEORY:
    - import module          -> use module.function()
    - from module import x    -> use x() directly
    - import module as alias  -> shorter name
    - Useful built-in modules: math, random, datetime, os, sys
    - Any .py file is itself a module and can be imported.
    """
    print("\n--- 16. Modules & Imports ---")

    # math module
    import math
    print(math.sqrt(16), math.pi, math.ceil(3.2), math.floor(3.9))

    # from ... import specific names
    from math import sqrt, factorial
    print(sqrt(25), factorial(5))

    # import with alias
    import math as m
    print(m.pow(2, 8))

    # os module
    import os
    print(os.getcwd())                 # current working directory
    print(os.path.exists("nofile.txt"))  # check existence

    # random module
    import random
    print(random.randint(1, 10))       # random int 1-10
    print(random.choice(["a", "b", "c"]))
    nums = [1, 2, 3, 4, 5]
    random.shuffle(nums)                # shuffles in place
    print(nums)

    # datetime module
    import datetime
    print(datetime.date.today())


# ==========================================================
# 17. GENERATORS & yield
# ==========================================================
def topic_17_generators():
    """
    THEORY:
    - A generator produces values ONE AT A TIME using 'yield'
      instead of 'return'. Memory efficient (lazy evaluation) -
      it does not build the whole result in memory at once.
    - next(gen) gets the next value; raises StopIteration when done.
    - Generator expression: (expr for item in iterable) - like a
      list comprehension but with () instead of [].
    """
    print("\n--- 17. Generators & yield ---")

    # A generator function
    def gen_squares(n):
        for i in range(n):
            yield i ** 2     # pauses here, resumes on next call

    gen = gen_squares(5)
    print(next(gen), next(gen), next(gen))   # 0 1 4

    # Loop through a generator (continues from where it left off)
    for val in gen:
        print(val, end=" ")
    print()

    # Convert a fresh generator to a list
    print(list(gen_squares(5)))

    # Generator expression
    gen2 = (x ** 2 for x in range(10))
    print(list(gen2))

    # Practical - process a file line by line (memory efficient)
    def read_lines(filepath):
        with open(filepath, "r") as f:
            for line in f:
                yield line.strip()

    # demo file
    with open("temp_lines.txt", "w") as f:
        f.write("line1\nline2\nline3\n")
    for line in read_lines("temp_lines.txt"):
        print(line)

    import os
    os.remove("temp_lines.txt")


# ==========================================================
# 18. SHALLOW vs DEEP COPY
# ==========================================================
def topic_18_copy():
    """
    THEORY:
    - Assignment (b = a): NO copy - both names point to the SAME
      object. Changing one changes the other.
    - Shallow copy (a.copy(), list(a), copy.copy(a)): copies the
      outer object, but NESTED objects are still SHARED.
    - Deep copy (copy.deepcopy(a)): copies EVERYTHING, including
      nested objects - fully independent.
    """
    print("\n--- 18. Shallow vs Deep Copy ---")

    # Assignment - same object
    a = [1, 2, 3]
    b = a
    b.append(4)
    print("assignment:", a)        # [1, 2, 3, 4] - a changed too!

    # Shallow copy
    import copy
    original = [1, 2, [3, 4]]
    shallow = original.copy()
    shallow.append(99)
    print("shallow outer:", original)     # unaffected

    shallow[2].append(99)                  # modify nested list
    print("shallow nested:", original)     # AFFECTED - nested is shared!

    # Deep copy
    original2 = [1, 2, [3, 4]]
    deep = copy.deepcopy(original2)
    deep[2].append(99)
    print("deep - original:", original2)   # NOT affected
    print("deep - copy:", deep)


# ==========================================================
# 19. __name__ == "__main__"
# ==========================================================
def topic_19_main_guard():
    """
    THEORY:
    - Every file has a built-in '__name__' variable.
    - If the file is run DIRECTLY, __name__ == "__main__".
    - If the file is IMPORTED by another file, __name__ equals
      the module's filename (without .py).
    - The guard "if __name__ == '__main__':" prevents code from
      running automatically when the file is imported elsewhere.
    - Standard pattern: put your script logic inside main() and
      call it only under this guard.
    """
    print("\n--- 19. __name__ == '__main__' ---")
    print("current __name__ value here is:", __name__)

    def process_data(data):
        return sum(data)

    def main_demo():
        data = [1, 2, 3, 4, 5]
        result = process_data(data)
        print("Result:", result)

    # In a real script this call would be guarded like:
    #   if __name__ == "__main__":
    #       main_demo()
    main_demo()


# ==========================================================
# 20. OOP - OBJECT ORIENTED PROGRAMMING
# ==========================================================
def topic_20_oop():
    """
    THEORY:
    - Class = blueprint, Object = instance of that blueprint.
    - Access modifiers: public (var), protected (_var),
      private (__var, only accessible inside the class).
    - __init__ = constructor, runs automatically on creation.
    - Instance method (self), classmethod (cls, @classmethod),
      staticmethod (@staticmethod, no self/cls).
    - Object relationships: Association (uses another object as
      a parameter), Aggregation (holds another object created
      OUTSIDE), Composition (creates the object INSIDE itself).
    - 4 Pillars: Encapsulation, Inheritance, Polymorphism, Abstraction.
    - super() calls the parent class's method/constructor.
    - Dunder methods (__str__, __add__, __eq__ ...) define how
      built-in operations (print, +, ==) behave for your objects.
    - @property turns a method into a read-like attribute.
    """
    print("\n--- 20. OOP ---")

    # ---- Class, object, constructor, access modifiers ----
    class Person:
        def __init__(self, name, age, salary):
            self.name = name          # public
            self._age = age           # protected
            self.__salary = salary    # private

        def show(self):
            print(f"{self.name}, {self._age}, {self.__salary}")

    p = Person("Amin", 21, 50000)
    print(p.name)
    p.show()

    # ---- Class attribute + classmethod + staticmethod ----
    class Employee:
        company = "TechCorp"
        headcount = 0

        def __init__(self, name):
            self.name = name
            Employee.headcount += 1

        @classmethod
        def change_company(cls, name):
            cls.company = name

        @staticmethod
        def is_even_id(emp_id):
            return emp_id % 2 == 0

    e1, e2 = Employee("Amin"), Employee("Bob")
    print(Employee.headcount)
    Employee.change_company("InnoTech")
    print(Employee.company, Employee.is_even_id(4))

    # ---- Inheritance + super() ----
    class Shape:
        def __init__(self, color):
            self.color = color

        def info(self):
            print(f"Color: {self.color}")

    class Circle(Shape):
        def __init__(self, color, radius):
            super().__init__(color)     # call parent constructor
            self.radius = radius

        def info(self):
            super().info()              # call parent method
            print(f"Radius: {self.radius}")
            print(f"Area: {3.1416 * self.radius ** 2:.2f}")

    Circle("Red", 5).info()

    # ---- Polymorphism ----
    class Rectangle(Shape):
        def __init__(self, color, w, h):
            super().__init__(color)
            self.w, self.h = w, h

        def info(self):
            print(f"Rectangle area = {self.w * self.h}")

    for shape in [Circle("Blue", 3), Rectangle("Green", 4, 6)]:
        shape.info()    # same method name, different behaviour

    # ---- Encapsulation with @property ----
    class Temperature:
        def __init__(self, celsius):
            self.__celsius = celsius

        @property
        def celsius(self):
            return self.__celsius

        @celsius.setter
        def celsius(self, value):
            if value < -273.15:
                raise ValueError("Below absolute zero!")
            self.__celsius = value

        @property
        def fahrenheit(self):
            return self.__celsius * 9 / 5 + 32

    t = Temperature(25)
    print(t.celsius, t.fahrenheit)
    t.celsius = 100
    print(t.fahrenheit)

    # ---- Abstraction ----
    from abc import ABC, abstractmethod

    class AbstractShape(ABC):
        @abstractmethod
        def area(self):
            pass

        def describe(self):
            print(f"I am a {self.__class__.__name__} with area {self.area():.2f}")

    class Square(AbstractShape):
        def __init__(self, side):
            self.side = side

        def area(self):
            return self.side ** 2

    Square(4).describe()

    # ---- Dunder / magic methods (operator overloading) ----
    class Vector:
        def __init__(self, x, y):
            self.x, self.y = x, y

        def __add__(self, other):           # v1 + v2
            return Vector(self.x + other.x, self.y + other.y)

        def __eq__(self, other):             # v1 == v2
            return self.x == other.x and self.y == other.y

        def __str__(self):                   # print(v1)
            return f"Vector({self.x}, {self.y})"

    v1, v2 = Vector(1, 2), Vector(3, 4)
    print(v1 + v2, v1 == v2)

    # ---- Mini practice: Student result system ----
    class Student:
        def __init__(self, name, roll):
            self.name = name
            self.roll = roll
            self.marks = {}

        def add_mark(self, subject, mark):
            self.marks[subject] = mark

        def average(self):
            return sum(self.marks.values()) / len(self.marks) if self.marks else 0

        @property
        def grade(self):
            avg = self.average()
            return "A+" if avg >= 90 else "A" if avg >= 80 else "B" if avg >= 70 else "C"

        def report(self):
            print(f"--- Report: {self.name} (Roll: {self.roll}) ---")
            for sub, mark in self.marks.items():
                print(f"  {sub}: {mark}")
            print(f"  Average: {self.average():.2f} | Grade: {self.grade}")

    s = Student("Amin", 101)
    s.add_mark("Math", 92)
    s.add_mark("English", 85)
    s.add_mark("Science", 90)
    s.report()


# ==========================================================
# INTERACTIVE MENU
# ==========================================================
TOPICS = {
    "1":  ("Python Basics",                    topic_01_basics),
    "2":  ("Data Types & Type Casting",        topic_02_data_types),
    "3":  ("Operators",                        topic_03_operators),
    "4":  ("Input & Output",                   topic_04_input_output),
    "5":  ("Conditional Statements",           topic_05_conditionals),
    "6":  ("Strings",                          topic_06_strings),
    "7":  ("Data Structures (List/Tuple/Dict/Set)", topic_07_data_structures),
    "8":  ("Comprehensions",                   topic_08_comprehensions),
    "9":  ("Built-in Functions",               topic_09_builtin_functions),
    "10": ("Loops",                            topic_10_loops),
    "11": ("Unpacking & Multiple Assignment",  topic_11_unpacking),
    "12": ("Functions",                        topic_12_functions),
    "13": ("Type Checking - isinstance()",     topic_13_isinstance),
    "14": ("File I/O",                         topic_14_file_io),
    "15": ("Error Handling",                   topic_15_error_handling),
    "16": ("Modules & Imports",                topic_16_modules),
    "17": ("Generators & yield",               topic_17_generators),
    "18": ("Shallow vs Deep Copy",             topic_18_copy),
    "19": ('__name__ == "__main__"',           topic_19_main_guard),
    "20": ("OOP - Object Oriented Programming", topic_20_oop),
}


def show_menu():
    print("\n" + "=" * 50)
    print(" PYTHON PRACTICE MENU")
    print("=" * 50)
    for key, (title, _) in TOPICS.items():
        print(f"{key:>2}. {title}")
    print(" 0. Exit")
    print("=" * 50)


def main():
    while True:
        show_menu()
        choice = input("Enter topic number to run (0 to exit): ").strip()

        if choice == "0":
            print("Goodbye! Happy practicing.")
            break

        if choice in TOPICS:
            title, func = TOPICS[choice]
            print(f"\nRunning Topic {choice}: {title}")
            func()
        else:
            print("Invalid choice. Please enter a number from the menu.")


if __name__ == "__main__":
    main()
