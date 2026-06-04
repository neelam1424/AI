# Thread Pool in Python — Complete Beginner Guide

## What You Will Learn

- Threading
- Concurrency
- Queue data structure
- Producer Consumer Pattern
- Worker Threads
- Task Scheduling
- Background Jobs
- Server Design Basics

---

## Problem Statement

Build a Thread Pool that:

1. Creates fixed worker threads.
2. Stores tasks in a queue.
3. Lets workers continuously execute tasks.
4. Supports task submission.
5. Supports graceful shutdown.

Example:

```python
pool = ThreadPool(3)

pool.submit(download_file, "file1.pdf")
pool.submit(download_file, "file2.pdf")
pool.submit(download_file, "file3.pdf")
pool.submit(download_file, "file4.pdf")

pool.shutdown()
```

---

## What Is a Thread?

A thread is a worker inside a process.

Without threads:

Task1 -> Task2 -> Task3 -> Task4

With threads:

Worker1 -> Task1
Worker2 -> Task2
Worker3 -> Task3

Multiple tasks can progress concurrently.

---

## What Is a Thread Pool?

A Thread Pool is a group of reusable worker threads.

Instead of creating a new thread for every task, we create a fixed number of workers and reuse them.

Benefits:

- Better performance
- Lower memory usage
- Less thread creation overhead
- Easier management

---

## Real World Uses

- Web scraping
- File downloads
- Image processing
- Email sending
- Background jobs
- FastAPI background tasks
- Request handling in servers

---

## Core Idea

Main Thread
    |
    v
Task Queue
    |
    v
Worker Threads
    |
    v
Execute Tasks

Workers continuously pull tasks from the queue.

---

## Algorithm

### Initialization

1. Create task queue.
2. Create worker list.
3. Start N worker threads.
4. Each worker runs worker_loop().
5. Store workers.

### Submit Task

1. Receive function and arguments.
2. Package task.
3. Put task into queue.

### Worker Loop

1. Wait for task.
2. Take task from queue.
3. If task is None:
   stop worker.
4. Otherwise:
   execute task.
5. Mark task completed.
6. Repeat.

### Shutdown

1. Wait for all tasks to finish.
2. Send stop signals.
3. Join workers.
4. Exit.

---

## Complete Code

```python
import threading
from queue import Queue


class ThreadPool:
    def __init__(self, num_workers):
        self.tasks = Queue()
        self.workers = []

        for _ in range(num_workers):
            worker = threading.Thread(
                target=self.worker_loop
            )

            worker.start()

            self.workers.append(worker)

    def worker_loop(self):
        while True:

            task = self.tasks.get()

            if task is None:
                self.tasks.task_done()
                break

            function, args, kwargs = task

            function(*args, **kwargs)

            self.tasks.task_done()

    def submit(self, function, *args, **kwargs):
        self.tasks.put(
            (function, args, kwargs)
        )

    def shutdown(self):

        self.tasks.join()

        for _ in self.workers:
            self.tasks.put(None)

        for worker in self.workers:
            worker.join()
```

---

## Constructor Explanation

```python
def __init__(self, num_workers):
```

Runs when:

```python
pool = ThreadPool(3)
```

Creates:

- Queue
- Worker list
- Worker threads

---

## Why Queue?

Queue is thread-safe.

Workers can safely call:

```python
get()
```

Main thread can safely call:

```python
put()
```

---

## Why Workers?

Workers continuously process tasks.

Instead of:

Create thread -> execute -> destroy

We do:

Create worker once -> reuse forever.

---

## Why task_done()?

It tells Queue:

Task finished.

Needed because:

```python
self.tasks.join()
```

waits until all tasks are completed.

---

## Why None?

None is used as a stop signal.

Example:

Queue:

file1
file2
None

Worker sees None:

stop.

---

## Test Program

```python
import time


def download_file(file_name):
    print(f"Downloading {file_name}")

    time.sleep(2)

    print(f"Finished {file_name}")


pool = ThreadPool(3)

pool.submit(download_file, "file1.pdf")
pool.submit(download_file, "file2.pdf")
pool.submit(download_file, "file3.pdf")
pool.submit(download_file, "file4.pdf")

pool.shutdown()

print("All downloads completed")
```

---

## Dry Run

Workers:

Worker1
Worker2
Worker3

Queue:

file1
file2
file3
file4

Execution:

Worker1 -> file1
Worker2 -> file2
Worker3 -> file3

Queue:

file4

First free worker:

Worker1 -> file4

---

## Possible Output

```text
Downloading file1.pdf
Downloading file2.pdf
Downloading file3.pdf

Finished file1.pdf
Downloading file4.pdf

Finished file2.pdf
Finished file3.pdf
Finished file4.pdf

All downloads completed
```

Order may vary because threads run concurrently.

---

## Time Complexity

Submit:

O(1)

Queue Put:

O(1)

Queue Get:

O(1)

Task execution:

Depends on task.

---

## Space Complexity

O(number_of_tasks)

Queue stores pending tasks.

---

## Common Mistakes

1. Using:

```python
target=self.worker_loop()
```

Instead of:

```python
target=self.worker_loop
```

2. Forgetting task_done()

3. Not shutting down workers

4. Using list instead of Queue

---

## Mental Model

Main Thread produces tasks.

Queue stores tasks.

Workers consume tasks.

This is the Producer Consumer Pattern.

---

## Resume Bullet

Built a custom Thread Pool in Python using threading and Queue, enabling concurrent task execution through reusable worker threads and safe task scheduling.
