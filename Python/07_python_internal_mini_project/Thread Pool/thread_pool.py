import threading
from queue import Queue


class ThreadPool:
    def __init__(self, num_workers):
        self.tasks = Queue()
        self.workers = []


        for _ in range(num_workers):
            worker = threading.Thread(target=self.worker_loop)
            worker.start()
            self.workers.append(worker)

    def worker_loop(self):
        while True:
            task = self.tasks.get()


            if task is None:
               break

            function, args, kwargs = task
            function(*args, **kwargs) 

            self.tasks.task_done()

    def submit(self, function, *args, **kwargs):
        self.tasks.put((function, args, kwargs))

    
    def shutdown(self):
        for _ in self.workers:
            self.tasks.put(None)

        for worker in self.workers:
            worker.join()