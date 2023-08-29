import threading

class ThreadSafeCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    
    def increment(self):
        with self.lock:
            self.value += 1

def worker(counter, iterations):
    for _ in range(iterations):
        counter.increment()
    
counter = ThreadSafeCounter()
iterations_per_thread = 10000
num_threads = 4

threads = []

for _ in range(num_threads):
    thread = threading.Thread(target = worker, args = (counter, iterations_per_thread))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f'Final counter value: {counter.value}')