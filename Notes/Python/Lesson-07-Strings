# Lesson 7: Strings (Part 1) — Notes

**Estimated Time:** 5–6 hours (spread over 2–3 days)
**Difficulty:** ⭐⭐⭐☆☆

## What is a String?

A **string** is a sequence of characters — letters, numbers, spaces, symbols, emojis, special characters.

```python
name = "Alan"
city = "Kottayam"
course = "MCA"
password = "Alan@123"
```

All of these are strings.

## Why Strings Matter for AI Engineering

Nearly everything in AI involves processing text: ChatGPT/LangChain prompts, PDF text, emails, API responses, user input, search queries, NLP, RAG systems, voice transcription. Strings are a foundational skill for this whole field.

## Creating Strings

**Double quotes:**
```python
name = "Alan"
```

**Single quotes** — equally valid:
```python
name = 'Alan'
```

**Triple quotes** — for multi-line strings:
```python
message = """
Hello
Welcome
to Python
"""
```

## Printing Strings

```python
name = "Alan"
print(name)   # Alan
```

## String Length — `len()`

```python
name = "Alan"
print(len(name))   # 4
```

```python
print(len("Python"))   # 6
print(len(""))            # 0   — empty string
print(len(" "))             # 1   — a space still counts as a character
```

## String Indexing

Every character has a position, starting at `0`:

```
Character :  P  y  t  h  o  n
Index     :  0  1  2  3  4  5
```

```python
name = "Python"
print(name[0])   # P
print(name[1])    # y
print(name[5])     # n
```

## Negative Indexing

Python can count backwards from the end, starting at `-1`:

```
Character :  P  y  t  h  o  n
Index     : -6 -5 -4 -3 -2 -1
```

```python
print(name[-1])   # n
print(name[-2])    # o
print(name[-6])     # P
```

Negative indexing is very handy for grabbing the last character(s) without needing to know the string's length.

## Index Error

```python
name = "Alan"
print(name[10])
```

```
IndexError: string index out of range
```

`"Alan"` only has 4 characters (valid indices `0`–`3`, or `-1`–`-4`), so index `10` doesn't exist.

## 📚 New Concepts

String · Character · Index · Positive Index · Negative Index · `len()`

# Lesson 7 (Part 2): String Slicing — Notes

**Estimated Time:** 4–5 hours
**Difficulty:** ⭐⭐⭐☆☆

## What is Slicing?

**Slicing** means extracting a portion of a string — like cutting a few slices from a loaf of bread, instead of grabbing just one crumb (a single character via indexing).

```python
name = "Python"
print(name[0])   # 'P' — indexing gives ONE character
```

Slicing lets you grab a **range** of characters at once.

## Slice Syntax

```python
string[start : stop]
```

> **Golden rule: `start` is included, `stop` is excluded.**

## Basic Examples

```
Character : P  y  t  h  o  n
Index     : 0  1  2  3  4  5
```

```python
word = "Python"

print(word[0:2])   # "Py"   — index 0 included, index 2 excluded
print(word[0:4])    # "Pyth"
print(word[2:5])     # "tho"
print(word[1:6])      # "ython"
```

## Omitting Start or Stop

```python
word[:4]     # same as word[0:4] → "Pyth"
word[2:]      # same as word[2:6] (to the end) → "thon"
word[:]        # entire string → "Python"
```

## Negative Slicing

```
Character : P  y  t  h  o  n
Index     : -6 -5 -4 -3 -2 -1
```

```python
word = "Python"

print(word[-3:])   # "hon"
print(word[:-2])    # "Pyth"
```

## The Step Parameter

```python
string[start:stop:step]
```

```python
word = "Python"

print(word[::2])   # "Pto"   — every 2nd character
print(word[::3])    # "Ph"    — every 3rd character
```

## Reversing a String

One of the most famous Python tricks:

```python
word = "Python"
print(word[::-1])   # "nohtyP"
```

`start` defaults to the end, `stop` defaults to the beginning, and `step = -1` walks backwards.

```python
print(word[::-2])   # "nhy"  — every 2nd character, walking backwards
```

## Visual Trick

Whenever slicing is confusing, draw the string out with its indices:

```
Python

0 1 2 3 4 5
P y t h o n
```

Then mark where `start` and `stop` point, remembering that `stop` is never included. This is a habit even professional developers use when debugging string logic.

# Lesson 7 (Part 3): String Methods — Notes

**Estimated Time:** 6–8 hours
**Difficulty:** ⭐⭐⭐☆☆

## What are String Methods?

A **method** is a function that belongs to an object. Strings have many built-in methods that make text processing easy.

```python
string.method()
```

```python
name = "alan"
print(name.upper())   # ALAN
```

## The Methods

### `upper()` — uppercase everything
```python
name = "Alan Varghese"
print(name.upper())   # ALAN VARGHESE
```
Useful for: login systems, case-insensitive comparisons/searches.

### `lower()` — lowercase everything
```python
email = "Alan@Gmail.COM"
print(email.lower())   # alan@gmail.com
```
Useful for: email validation, searching, comparing usernames.

### `title()` — capitalize the first letter of every word
```python
name = "alan varghese"
print(name.title())   # Alan Varghese
```

### `capitalize()` — capitalize only the first character
```python
sentence = "python is awesome"
print(sentence.capitalize())   # Python is awesome
```

### `strip()` — remove leading/trailing spaces
```python
name = "   Alan   "
print(name.strip())   # "Alan"
```
Extremely useful when cleaning user input.

### `lstrip()` / `rstrip()` — strip from one side only
```python
"    Hello".lstrip()    # "Hello"
"Hello     ".rstrip()     # "Hello"
```

### `replace()` — replace one piece of text with another
```python
text = "I love Java"
print(text.replace("Java", "Python"))   # I love Python

phone = "987-654-3210"
print(phone.replace("-", ""))            # 9876543210
```

### `find()` — locate the first occurrence of a substring
```python
text = "Python Programming"
print(text.find("Program"))   # 7

print(text.find("Java"))       # -1  (means "not found")
```

### `count()` — count occurrences
```python
text = "banana"
print(text.count("a"))    # 3
print(text.count("na"))     # 2
```

### `startswith()` / `endswith()`
```python
filename = "resume.pdf"
print(filename.startswith("res"))   # True
print(filename.endswith(".pdf"))     # True
```
Useful for checking file types, URL prefixes, etc.

### `split()` — split a string into a list
```python
text = "Python Java C++"
print(text.split())   # ['Python', 'Java', 'C++']

fruits = "Apple,Mango,Banana"
print(fruits.split(","))   # ['Apple', 'Mango', 'Banana']
```

### `join()` — join a list of strings into one string
```python
words = ["I", "Love", "Python"]
print(" ".join(words))   # "I Love Python"
```

## Summary Table

| Method | Purpose | Example Output |
|---|---|---|
| `upper()` | Uppercase | `ALAN` |
| `lower()` | Lowercase | `alan` |
| `title()` | Every word capitalized | `Alan Varghese` |
| `capitalize()` | First letter capitalized | `Python` |
| `strip()` | Remove surrounding spaces | `Alan` |
| `replace()` | Replace text | `I love Python` |
| `find()` | Find position | `7` |
| `count()` | Count occurrences | `3` |
| `startswith()` | Check beginning | `True` |
| `endswith()` | Check ending | `True` |
| `split()` | Split into list | `['a', 'b']` |
| `join()` | Join strings | `"a b"` |

## Why This Matters for AI Work

These methods come up constantly in prompt engineering (cleaning user input), LangChain prompt processing, RAG document splitting/cleaning, chatbot text normalization, NLP tokenization, and FastAPI input validation.

# Lesson 7 (Part 4): Escape Characters & Advanced String Formatting — Notes

**Estimated Time:** 3–4 hours
**Difficulty:** ⭐⭐☆☆☆

## 🎯 Learning Objectives

- Escape characters
- New lines, tabs
- Quotes inside strings
- Backslashes
- Advanced f-strings
- String formatting (decimal places, alignment)

## What are Escape Characters?

An escape character starts with `\` and tells Python "the next character has a special meaning" instead of being printed literally.

## `\n` — New Line

```python
print("Hello\nWorld")
```
```
Hello
World
```

```python
print("Name : Alan\nAge : 23")
```
```
Name : Alan
Age : 23
```

## `\t` — Tab Space

```python
print("Name\tAlan")
print("Age\t23")
```
```
Name    Alan
Age     23
```
Useful for aligning simple table-like output.

## `\"` — Escaped Double Quote

```python
print("Python is "Awesome"")   # ❌ Error — Python thinks the string ends early
print("Python is \"Awesome\"")  # ✅
```
```
Python is "Awesome"
```

## `\'` — Escaped Single Quote

```python
print('It\'s a beautiful day')
```
```
It's a beautiful day
```

## `\\` — Escaped Backslash

```python
print("C:\Users\Alan")     # ❌ Python reads \U as the start of a unicode escape
print("C:\\Users\\Alan")    # ✅
```
```
C:\Users\Alan
```

### Raw Strings — an Alternative

```python
print(r"C:\Users\Alan")
```
```
C:\Users\Alan
```

The `r` prefix tells Python to treat backslashes literally — no escape processing at all. Common for file paths and regex patterns.

## Advanced f-Strings

Basic usage:
```python
name = "Alan"
print(f"Hello {name}")
```

**Multiple variables:**
```python
name = "Alan"
age = 23
city = "Kottayam"

print(f"My name is {name}. I am {age} years old and I live in {city}.")
```

**Expressions inside f-strings:**
```python
a = 10
b = 20
print(f"Sum = {a+b}")   # Sum = 30
```

**Method calls inside f-strings:**
```python
name = "alan"
print(f"{name.upper()}")   # ALAN
```

**Formatting numbers — decimal places:**
```python
pi = 3.14159265
print(f"{pi:.2f}")   # 3.14
```
`.2f` means "2 digits after the decimal point."

**Alignment:**
```python
name = "Alan"

print(f"{name:>10}")   # right aligned  → "      Alan"
print(f"{name:<10}")    # left aligned   → "Alan      "
print(f"{name:^10}")     # center aligned → "   Alan   "
```

## 🏆 Wrap-Up

Escape characters and f-strings round out the core Strings module — a foundation used constantly in prompt engineering, document processing, search systems, RAG pipelines, chatbots, FastAPI backends, and data cleaning.