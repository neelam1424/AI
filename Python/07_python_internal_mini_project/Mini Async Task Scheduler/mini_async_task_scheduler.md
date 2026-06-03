
# Mini Async Task Scheduler in Python — Complete Beginner Guide

## What You Will Learn

- Generators
- yield keyword
- Cooperative Multitasking
- Event Loop Fundamentals
- Task Scheduling
- Round Robin Scheduling
- Async Programming Basics
- asyncio Internals

---

# Problem Statement

Build a mini scheduler that:

1. Stores multiple tasks.
2. Runs one step of a task.
3. Pauses the task.
4. Runs another task.
5. Resumes paused tasks later.
6. Continues until all tasks finish.

Example Output:

Task 1: start
Task 2: start
Task 1: middle
Task 2: end
Task 1: end

---

# Why Build This Project?

This project teaches the core idea behind:

- asyncio
- FastAPI async endpoints
- Event loops
- Coroutines
- await
- Non-blocking programming

When you understand this project, async programming becomes much easier.

---

# Real World Analogy

Imagine making tea.

1. Start boiling water.
2. While waiting, toast bread.
3. While bread toasts, cut fruit.
4. Return to water.

Instead of waiting idly, you switch between tasks.

That is the basic idea behind async scheduling.

---

# Synchronous Execution

Normal execution:

Task 1:
- start
- middle
- end

Task 2:
- start
- end

Output:

Task 1: start
Task 1: middle
Task 1: end
Task 2: start
Task 2: end

Task 2 waits for Task 1.

---

# Async Scheduler Execution

Output:

Task 1: start
Task 2: start
Task 1: middle
Task 2: end
Task 1: end

Tasks take turns.

---

# Core Concept: yield

Generator:

```python
def task():
    print("start")
    yield

    print("middle")
    yield

    print("end")
```

Calling:

```python
t = task()
```

does NOT execute immediately.

First:

```python
next(t)
```

Output:

start

Pauses at yield.

Second:

```python
next(t)
```

Output:

middle

Third:

```python
next(t)
```

Output:

end

Then generator finishes.

---

# What Is a Scheduler?

A scheduler decides:

Which task should run next?

Our scheduler uses:

Round Robin Scheduling

Process:

1. Run one task.
2. Pause it.
3. Put it back.
4. Run next task.
5. Repeat.

---

# Why Use deque?

```python
from collections import deque
```

deque allows:

```python
append()
popleft()
```

Perfect for rotating tasks.

Example:

```text
[Task1, Task2]
```

Run Task1:

```text
[Task2, Task1]
```

Run Task2:

```text
[Task1, Task2]
```

---

# Architecture

```text
Scheduler

      |
      v

 Task Queue

      |
      v

 Task1 Task2 Task3

      |
      v

 Run One Step

      |
      v

 Requeue If Not Finished
```

---

# Algorithm

Initialization:

1. Create empty task queue.

Add Task:

1. Receive task.
2. Add task to queue.

Run Scheduler:

1. While queue is not empty:
2. Remove first task.
3. Execute one step using next().
4. If task pauses:
   - put it back into queue.
5. If task finishes:
   - remove permanently.
6. Repeat.

---

# Complete Code

```python
from collections import deque


class Scheduler:
    def __init__(self):
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def run(self):
        while self.tasks:

            task = self.tasks.popleft()

            try:
                next(task)

                self.tasks.append(task)

            except StopIteration:
                pass
```

---

# Example Tasks

```python
def task_one():
    print("Task 1: start")
    yield

    print("Task 1: middle")
    yield

    print("Task 1: end")


def task_two():
    print("Task 2: start")
    yield

    print("Task 2: end")
```

---

# Test Code

```python
scheduler = Scheduler()

scheduler.add_task(task_one())
scheduler.add_task(task_two())

scheduler.run()
```

---

# Complete Program

```python
from collections import deque


class Scheduler:
    def __init__(self):
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def run(self):
        while self.tasks:

            task = self.tasks.popleft()

            try:
                next(task)

                self.tasks.append(task)

            except StopIteration:
                pass


def task_one():
    print("Task 1: start")
    yield

    print("Task 1: middle")
    yield

    print("Task 1: end")


def task_two():
    print("Task 2: start")
    yield

    print("Task 2: end")


scheduler = Scheduler()

scheduler.add_task(task_one())
scheduler.add_task(task_two())

scheduler.run()
```

---

# Dry Run

Initial Queue:

```text
[Task1, Task2]
```

Round 1:

Run Task1

Output:

```text
Task 1: start
```

Queue:

```text
[Task2, Task1]
```

Round 2:

Run Task2

Output:

```text
Task 2: start
```

Queue:

```text
[Task1, Task2]
```

Round 3:

Run Task1

Output:

```text
Task 1: middle
```

Queue:

```text
[Task2, Task1]
```

Round 4:

Run Task2

Output:

```text
Task 2: end
```

Task2 finished.

Queue:

```text
[Task1]
```

Round 5:

Run Task1

Output:

```text
Task 1: end
```

Queue:

```text
[]
```

Scheduler stops.

---

# Understanding StopIteration

When a generator finishes:

Python automatically raises:

```python
StopIteration
```

Example:

```python
try:
    next(task)
except StopIteration:
    pass
```

Meaning:

Task completed.

Do not put it back into queue.

---

# Why This Is Not Threading

Threading:

Multiple workers.

Async Scheduler:

Single thread.

Tasks voluntarily pause using:

```python
yield
```

This is called:

Cooperative Multitasking.

---

# Relation To asyncio

Mini Scheduler:

```python
yield
```

Real asyncio:

```python
await
```

Mini Scheduler:

```python
next(task)
```

Real asyncio:

Resume coroutine.

Mini Scheduler:

```python
deque
```

Real asyncio:

Ready queue.

---

# Time Complexity

Adding Task:

O(1)

Taking Task:

O(1)

Requeue Task:

O(1)

Scheduling Loop:

Depends on total yield points.

---

# Space Complexity

O(number_of_tasks)

Because queue stores active tasks.

---

# Common Mistakes

1. Forgetting yield.
2. Calling task function instead of generator.
3. Not handling StopIteration.
4. Using normal function instead of generator.

---

# Mental Model

Remember:

Scheduler = Traffic Controller

Tasks = Cars

yield = Red Light

Scheduler decides who moves next.

---

# Resume Bullet

Built a mini async task scheduler in Python using generators and deque to simulate event-loop behavior, cooperative multitasking, and task scheduling fundamentals behind asyncio.
