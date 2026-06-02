# Rate Limiter
# Step 1:- Get current time
# Step 2:- Remove all expired request
# Step 3:- Count remaning request
# Step 4:- If remainging request < max_request 
#            - Allow request
#            - Storerequest
# Step 5:- Else
#           - Block request



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
    

limiter = RateLimiter(max_requests=3, window_seconds=10)

print(limiter.allow_request())  # True
print(limiter.allow_request())  # True
print(limiter.allow_request())  # True
print(limiter.allow_request())  # False