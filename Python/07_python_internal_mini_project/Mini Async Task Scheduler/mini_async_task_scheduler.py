from collections import deque

class Scheduler:
    def __init__(self):
        self.tasks = deque()

    def add_task(self,task):
        self.tasks.append(task)
    
    def run(self):
        while self.tasks:
            task =self.tasks.popleft()

            try:
                next(task)
                self.tasks.append(task)
            except StopIteration:
                pass
