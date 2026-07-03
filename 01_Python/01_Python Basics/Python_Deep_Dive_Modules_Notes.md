# Python Deep Dive Notes

# Module 1: Python Memory & Object Model

## 1. Python Memory Model
In Python, everything is an object. Variables store references to objects, not raw values.

Example:
```python
a = [1, 2, 3]
b = a
b.append(4)

print(a)
print(b)
```

Diagram:
```text
a ----\
       ---> [1,2,3,4]
b ----/
```

## 2. Mutability
Mutable:
- list
- dict
- set

Immutable:
- int
- float
- str
- tuple
- bool

Example:
```python
nums = [1,2,3]
nums.append(4)
```

## 3. Reference Counting
Python tracks how many references point to an object.

Example:
```python
import sys

a = [1,2,3]
b = a

print(sys.getrefcount(a))
```

## 4. Garbage Collection
Garbage collector removes unused objects and circular references.

Example:
```python
import gc
gc.collect()
```

## 5. CPython Internals
CPython stores:
- reference count
- type info
- object value

Diagram:
```text
PyObject
├── ref count
├── type
└── value
```

# Module 2: Functions, Iteration & Python Internals

## 1. Iterators
Iterator returns one item at a time.

Example:
```python
numbers = [10,20,30]
it = iter(numbers)

print(next(it))
```

## 2. Generators
Generators use `yield` and produce values lazily.

Example:
```python
def count():
    yield 1
    yield 2
```

Useful for large datasets and file streaming.

## 3. Decorators
Decorators modify function behavior.

Example:
```python
def deco(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
```

FastAPI uses decorators:
```python
@app.get("/")
```

## 4. Context Managers
Handle setup and cleanup automatically.

Example:
```python
with open("file.txt") as f:
    data = f.read()
```

Custom:
```python
class MyContext:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        print("cleanup")
```

## 5. Descriptors
Descriptors control attribute access.

Methods:
- __get__
- __set__
- __delete__

Used behind:
- @property
- classmethod
- staticmethod

## 6. Metaclasses
Metaclass creates classes.

Diagram:
```text
object <- class <- metaclass(type)
```

Example:
```python
class MyMeta(type):
    pass
```

## 7. Data Classes
Reduce boilerplate.

Example:
```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    marks: int
```

## 8. Typing System
Type hints improve readability and tooling.

Example:
```python
def add(a:int,b:int)->int:
    return a+b
```

# Module 3: Concurrency & Performance

## 1. GIL
Global Interpreter Lock.

Only one thread executes Python bytecode at a time in CPython.

Diagram:
```text
Threads -> GIL -> Interpreter
```

## 2. Threading vs Multiprocessing

Threading:
- shared memory
- good for I/O

Example:
```python
import threading
```

Multiprocessing:
- separate memory
- good for CPU tasks

Example:
```python
import multiprocessing
```

## 3. Async Internals
Async handles waiting tasks efficiently.

Example:
```python
import asyncio

async def task():
    await asyncio.sleep(1)
```

## 4. Event Loop
Manages async tasks.

Diagram:
```text
Event Loop
├── task1
├── task2
└── task3
```

## 5. Concurrency
Concurrency:
- multiple tasks managed together

Parallelism:
- multiple tasks running simultaneously

## 6. Profiling
Find performance bottlenecks.

Example:
```python
import cProfile
cProfile.run("func()")
```

## 7. Optimization
Improve speed and memory usage.

Prefer:
- list comprehensions
- NumPy vectorization
- profiling before optimization

# Module 4: Production Python Engineering

## 1. Packaging
Typical structure:

```text
project/
├── pyproject.toml
├── src/
└── tests/
```

## 2. Virtual Environments

Create:
```bash
python -m venv .venv
```

Activate:
```bash
source .venv/bin/activate
```

## 3. uv / pip / poetry

pip:
```bash
pip install pandas
```

poetry:
```bash
poetry add pandas
```

uv:
```bash
uv add pandas
```

## 4. Logging
Use logging instead of print.

Example:
```python
import logging
logging.info("started")
```

Levels:
- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

## 5. Testing
Example:
```python
def test_add():
    assert add(2,3)==5
```

## 6. pytest
Run:
```bash
pytest
```

## 7. Pydantic
Validation and parsing.

Example:
```python
from pydantic import BaseModel

class Student(BaseModel):
    name:str
    age:int
```

## 8. FastAPI Internals
FastAPI uses:
- decorators
- Pydantic
- type hints
- Starlette
- ASGI

Example:
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello"}
```

Request Flow:
```text
Request
↓
Route matching
↓
Validation
↓
Python function
↓
JSON response
```

# Suggested Learning Order
1. Memory model
2. Mutability
3. Iterators
4. Generators
5. Decorators
6. Context managers
7. Typing
8. Dataclasses
9. Logging
10. Testing + pytest
11. Pydantic
12. FastAPI
13. Threading
14. Asyncio
15. Multiprocessing
16. Profiling
17. Descriptors
18. Metaclasses
19. CPython internals
