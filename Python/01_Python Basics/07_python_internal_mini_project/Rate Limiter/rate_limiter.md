  # Rate Limiter in Python — Complete Beginner Guide

## 1. Project Name

**Sliding Window Rate Limiter in Python**

This mini project teaches how APIs control traffic and prevent too many requests from one user or system.

---

## 2. Problem Statement

Build a Python class that controls how many requests are allowed within a specific time window.

Example requirement:

```text
Allow only 3 requests every 10 seconds.
```

If a user sends more than 3 requests within 10 seconds, the extra request should be blocked.

Example:

```python
limiter = RateLimiter(max_requests=3, window_seconds=10)

print(limiter.allow_request())  # True
print(limiter.allow_request())  # True
print(limiter.allow_request())  # True
print(limiter.allow_request())  # False
```

Output:

```text
True
True
True
False
```

---

## 3. What Is a Rate Limiter?

A **rate limiter** controls how many actions are allowed in a given time period.

In simple words:

> It prevents users from doing something too many times too quickly.

Examples:

```text
Only 5 login attempts per minute.
Only 100 API requests per hour.
Only 3 OTP requests every 30 seconds.
```

---

## 4. Real-World Use Cases

Rate limiters are used in:

- APIs
- Login systems
- Payment systems
- OTP systems
- Banking apps
- OpenAI API limits
- Google APIs
- Stripe APIs
- Web scraping protection
- DDoS protection

Example:

```text
Too many login attempts. Try again later.
```

---

## 5. Why Do We Need a Rate Limiter?

Without a rate limiter:

```text
User sends 1000 requests per second
↓
Server becomes overloaded
↓
Database slows down
↓
Application may crash
```

With a rate limiter:

```text
User sends too many requests
↓
Only allowed requests pass
↓
Extra requests are blocked
↓
Server stays safe
```

---

## 6. What Will You Learn?

By building this project, you will learn:

### Python Concepts

- Classes
- Objects
- Constructors
- Methods
- `time` module
- `deque` from collections
- Conditional logic
- While loops

### Backend Concepts

- API protection
- Request limiting
- Sliding window algorithm
- Time-based logic
- Queue-based tracking

### System Design Concepts

- Rate limiting
- Traffic control
- Server protection
- Request throttling

---

## 7. Core Idea

We need to track request times.

Every time a request comes in:

```text
1. Get current time.
2. Remove old request timestamps.
3. Count recent requests.
4. If count is less than limit, allow request.
5. Otherwise, block request.
```

---

## 8. Sliding Window Concept

The algorithm used here is called the **Sliding Window Rate Limiter**.

Suppose:

```text
Max requests = 3
Window = 10 seconds
Current time = 100 seconds
```

The valid window is:

```text
90 seconds to 100 seconds
```

Because:

```text
current_time - window_seconds = 100 - 10 = 90
```

We only care about requests that happened after 90 seconds.

Example request timestamps:

```text
85, 91, 95, 98
```

Current time:

```text
100
```

Window:

```text
90 → 100
```

Expired request:

```text
85
```

Valid requests:

```text
91, 95, 98
```

So we remove 85.

---

## 9. Why Is It Called Sliding Window?

Because the time window keeps moving forward as time passes.

Example:

At time 100:

```text
Window = 90 to 100
```

At time 105:

```text
Window = 95 to 105
```

At time 110:

```text
Window = 100 to 110
```

The window slides with current time.

---

## 10. Why Use `deque`?

We use:

```python
from collections import deque
```

A `deque` means:

```text
Double Ended Queue
```

It allows fast insertion and deletion from both ends.

For this project, we need:

```python
append()
```

to add new request timestamps.

And:

```python
popleft()
```

to remove old request timestamps.

---

## 11. Why Not Use a List?

If we use a list:

```python
requests.pop(0)
```

This is slow because Python must shift all elements to the left.

Time complexity:

```text
O(n)
```

If we use deque:

```python
requests.popleft()
```

It removes from the left very fast.

Time complexity:

```text
O(1)
```

So `deque` is better for this project.

---

## 12. Deque Example

```python
from collections import deque

dq = deque()

dq.append(10)
dq.append(20)
dq.append(30)

print(dq)

dq.popleft()

print(dq)
```

Output:

```text
deque([10, 20, 30])
deque([20, 30])
```

In our rate limiter:

```text
Left side = oldest request
Right side = newest request
```

---

## 13. Why Use `time.time()`?

We use:

```python
import time

current_time = time.time()
```

`time.time()` returns the current time in seconds.

Example:

```text
1760000000.45
```

We do not need to understand the exact number.

We only use it to compare time differences.

Example:

```python
current_time - self.window_seconds
```

This tells us the starting point of the current valid window.

---

## 14. Algorithm

When a request comes:

```text
1. Get current time.

2. Remove all expired timestamps:
   while requests exist and oldest request is outside the window:
       remove oldest request

3. Check how many valid requests are left.

4. If valid request count < max_requests:
       add current request timestamp
       return True

5. Else:
       return False
```

---

## 15. Complete Code

```python
import time
from collections import deque


class RateLimiter:
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = deque()

    def allow_request(self):
        current_time = time.time()

        while self.requests and self.requests[0] <= current_time - self.window_seconds:
            self.requests.popleft()

        if len(self.requests) < self.max_requests:
            self.requests.append(current_time)
            return True

        return False
```

---

## 16. Code Explanation Line by Line

### Import time

```python
import time
```

We need this to get the current time.

---

### Import deque

```python
from collections import deque
```

We need `deque` to store request timestamps efficiently.

---

### Create Class

```python
class RateLimiter:
```

This creates a blueprint for our rate limiter.

Example:

```python
limiter = RateLimiter(3, 10)
```

This creates an object that allows 3 requests every 10 seconds.

---

### Constructor

```python
def __init__(self, max_requests, window_seconds):
```

This runs automatically when we create the object.

Example:

```python
RateLimiter(3, 10)
```

Here:

```text
max_requests = 3
window_seconds = 10
```

---

### Store Maximum Requests

```python
self.max_requests = max_requests
```

This stores the maximum number of allowed requests.

---

### Store Time Window

```python
self.window_seconds = window_seconds
```

This stores the time window.

---

### Create Empty Queue

```python
self.requests = deque()
```

This stores timestamps of allowed requests.

Initially:

```text
[]
```

---

### Method to Check Request

```python
def allow_request(self):
```

This method decides whether a request is allowed or blocked.

It returns:

```text
True  → allowed
False → blocked
```

---

### Get Current Time

```python
current_time = time.time()
```

This stores the current timestamp.

---

### Remove Expired Requests

```python
while self.requests and self.requests[0] <= current_time - self.window_seconds:
    self.requests.popleft()
```

This removes old requests outside the current time window.

Example:

```text
current_time = 100
window_seconds = 10
current_time - window_seconds = 90
```

Any request timestamp less than or equal to 90 is expired.

Example queue:

```text
[85, 91, 95, 98]
```

85 is expired.

After removing:

```text
[91, 95, 98]
```

---

### Check Limit

```python
if len(self.requests) < self.max_requests:
```

If the number of valid requests is less than the maximum allowed, allow the request.

Example:

```text
len(self.requests) = 2
max_requests = 3
2 < 3 → True
```

---

### Add Current Request

```python
self.requests.append(current_time)
```

If request is allowed, store its timestamp.

Before:

```text
[91, 95]
```

After:

```text
[91, 95, 100]
```

---

### Return True

```python
return True
```

This means request is allowed.

---

### Return False

```python
return False
```

This means request is blocked.

---

## 17. Dry Run Example

Code:

```python
limiter = RateLimiter(max_requests=3, window_seconds=10)

print(limiter.allow_request())
print(limiter.allow_request())
print(limiter.allow_request())
print(limiter.allow_request())
```

Assume all requests happen quickly within 10 seconds.

### Initial State

```text
requests = []
```

### Request 1

```text
0 < 3 → allowed
requests = [100]
output = True
```

### Request 2

```text
1 < 3 → allowed
requests = [100, 101]
output = True
```

### Request 3

```text
2 < 3 → allowed
requests = [100, 101, 102]
output = True
```

### Request 4

```text
3 < 3 → False
request blocked
requests = [100, 101, 102]
output = False
```

---

## 18. Example With Waiting

```python
import time

limiter = RateLimiter(max_requests=3, window_seconds=10)

print(limiter.allow_request())  # True
print(limiter.allow_request())  # True
print(limiter.allow_request())  # True
print(limiter.allow_request())  # False

time.sleep(10)

print(limiter.allow_request())  # True
```

The last request returns True because after 10 seconds, old request timestamps expire.

---

## 19. Debug Version

This version prints internal queue state.

```python
import time
from collections import deque


class RateLimiter:
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = deque()

    def allow_request(self):
        current_time = time.time()

        print("\nCurrent time:", current_time)
        print("Before cleanup:", list(self.requests))

        while self.requests and self.requests[0] <= current_time - self.window_seconds:
            removed = self.requests.popleft()
            print("Removed expired request:", removed)

        print("After cleanup:", list(self.requests))

        if len(self.requests) < self.max_requests:
            self.requests.append(current_time)
            print("Request allowed")
            print("After adding:", list(self.requests))
            return True

        print("Request blocked")
        return False


limiter = RateLimiter(max_requests=3, window_seconds=10)

print(limiter.allow_request())
print(limiter.allow_request())
print(limiter.allow_request())
print(limiter.allow_request())
```

Use this version when learning because it shows how the sliding window works internally.

---

## 20. Where to Write Test Code?

Write test code at the bottom of the same file.

File structure:

```text
rate_limiter.py

1. imports
2. RateLimiter class
3. test code
```

Example:

```python
import time
from collections import deque


class RateLimiter:
    ...


limiter = RateLimiter(max_requests=3, window_seconds=10)

print(limiter.allow_request())
print(limiter.allow_request())
print(limiter.allow_request())
print(limiter.allow_request())
```

---

## 21. How to Run

Open terminal in the project folder.

Run:

```bash
python3 rate_limiter.py
```

Expected output:

```text
True
True
True
False
```

---

## 22. Time Complexity

### `allow_request()`

In normal usage:

```text
Amortized O(1)
```

Each request timestamp is added once and removed once.

The cleanup loop may remove multiple old timestamps sometimes, but over time every timestamp is removed only one time.

---

## 23. Space Complexity

```text
O(max_requests)
```

Because we only store request timestamps within the allowed window.

---

## 24. Important Mental Model

Remember:

```text
Deque stores timestamps of allowed requests.
Left side = oldest request.
Right side = newest request.
Remove expired timestamps from left.
If remaining count is below limit, allow.
Otherwise, block.
```

---

## 25. Visual Summary

```text
Current time = 100
Window = 10 seconds

Valid range:
90 to 100

Queue:
[85, 91, 95, 98]

85 is expired.

After cleanup:
[91, 95, 98]

Count = 3
Limit = 3

New request:
Blocked
```

---

## 26. Common Mistakes

### Mistake 1: Forgetting imports

Wrong:

```python
self.requests = deque()
```

without:

```python
from collections import deque
```

Error:

```text
NameError: name 'deque' is not defined
```

---

### Mistake 2: Using `pop(0)` with list

Avoid:

```python
requests.pop(0)
```

Use:

```python
requests.popleft()
```

---

### Mistake 3: Forgetting to append current time

If you forget:

```python
self.requests.append(current_time)
```

then the limiter will always allow requests.

---

### Mistake 4: Wrong condition

Correct:

```python
if len(self.requests) < self.max_requests:
```

Wrong:

```python
if len(self.requests) <= self.max_requests:
```

If max is 3, then length 3 should be blocked, not allowed.

---

## 27. Practice Tasks

### Task 1

Create a limiter that allows:

```text
5 requests every 60 seconds
```

### Task 2

Print:

```text
Allowed
```

instead of True.

Print:

```text
Blocked
```

instead of False.

### Task 3

Add a method:

```python
get_remaining_requests()
```

It should return how many requests are still allowed.

### Task 4

Add a method:

```python
get_retry_after()
```

It should tell how many seconds the user must wait.

### Task 5

Create different limiters for different users.

Example:

```python
user_limiters = {
    "user1": RateLimiter(3, 10),
    "user2": RateLimiter(5, 10)
}
```

---

## 28. Resume / GitHub Description

Project title:

```text
Sliding Window Rate Limiter in Python
```

GitHub description:

```text
Implemented a sliding window rate limiter in Python using deque and timestamps to control request frequency within a fixed time window.
```

Resume bullet:

```text
Built a sliding window rate limiter in Python using deque-based timestamp tracking, supporting efficient request throttling with amortized O(1) operations.
```

---

## 29. Final Understanding

This mini project teaches how real backend systems protect APIs from excessive traffic.

The core logic is:

```text
Store request timestamps.
Remove expired timestamps.
Allow only if active request count is below limit.
```

Once you understand this, you can later build:

- FastAPI middleware rate limiter
- Redis-based distributed rate limiter
- Login attempt limiter
- OTP request limiter
- API gateway rate limiter

This is a strong beginner-to-backend-engineering project.
