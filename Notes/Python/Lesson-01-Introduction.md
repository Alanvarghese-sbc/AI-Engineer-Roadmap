
01 introduction to python · MD
# Lesson 1: Introduction to Python
 
**Estimated Time:** 30–45 minutes
**Difficulty:** ⭐☆☆☆☆
 
## 🎯 Goal
 
By the end of this lesson, be able to answer:
 
- What is Python?
- Why is Python so popular?
- Where is Python used?
- How does Python execute code?
- What is an interpreter?
- How do we write and run our first Python program?
## 1. What is Python?
 
> Python is a **high-level, interpreted, general-purpose, object-oriented** programming language created by Guido van Rossum, first released in 1991.
 
### High-Level Language
 
Easy for humans to read and write, as opposed to raw machine code (`10101010...`).
 
```python
print("Hello, World!")
```
 
### Interpreted Language
 
Two common ways code gets executed:
 
**Compiled languages** (e.g. C, C++)
 
```
Source Code → Compiler → Machine Code → Program Runs
```
The whole program is translated before it runs.
 
**Interpreted languages** (e.g. Python)
 
```
Python Code → Python Interpreter → Executed Line by Line
```
 
> **Note:** CPython (the standard implementation) actually compiles code to **bytecode** (`.pyc`) first, then runs it on the Python Virtual Machine (PVM). "Interpreted" is a fine mental model for now, but this extra step is worth knowing about.
 
### General-Purpose Language
 
Python is used across many domains: web development, AI, data science, machine learning, deep learning, web scraping, automation, game dev, desktop apps, cloud computing, cybersecurity, APIs, testing.
 
### Object-Oriented Language
 
Python lets you organize code using **objects and classes**, which helps build larger, maintainable applications. (Covered in depth in a later module.)
 
## 2. Why is Python So Popular?
 
- **Easy to learn** — much less boilerplate than languages like Java:
```python
  print("Hello")
```
  vs.
```java
  public class Main {
      public static void main(String[] args){
          System.out.println("Hello");
      }
  }
```
 
- **Huge community** — tutorials, libraries, documentation, support.
- **Massive ecosystem** of libraries:
  | Area | Libraries |
  |---|---|
  | Data Analysis | NumPy, Pandas |
  | Visualization | Matplotlib, Plotly |
  | Machine Learning | Scikit-learn |
  | Deep Learning | PyTorch, TensorFlow |
  | Web | FastAPI, Django, Flask |
  | AI | LangChain, LlamaIndex, Transformers |
  | APIs | Requests |
  | Automation | Selenium |
## 3. Where is Python Used?
 
| Domain | Example Project |
|---|---|
| Automation | Auto file organizer |
| Web | Blog API |
| AI | Chatbot |
| ML | House price prediction |
| Data | Sales dashboard |
| Backend | FastAPI REST API |
| RAG | PDF chatbot |
| Voice AI | Voice assistant |
 
## 4. How Python Runs Your Code
 
```
hello.py
   ↓
Python Interpreter (CPython)
   ↓
Python Bytecode
   ↓
Python Virtual Machine (PVM)
   ↓
Output
```
 
Don't memorize this — just understand the general flow.
 
## 5. Installing / Checking Python
 
```bash
python --version     # or: py --version
pip --version
```
 
## 6. Your First Program
 
Create `hello.py`:
 
```python
print("Hello, World!")
```
 
Run it:
 
```bash
python hello.py
```
 
Expected output:
 
```
Hello, World!
```
 
## 7. Understanding `print()`
 
`print()` displays information on screen.
 
```python
print("Alan")
print(25)
print(True)
```
 
```
Alan
25
True
```
 
## 8. Comments
 
Ignored by Python at runtime.
 
```python
# This is a comment
print("Hello")
```
 
> Good comments explain **why** code exists, not what obvious code is doing.