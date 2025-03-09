from threading import Thread, Lock

counter = 0
rounds = 100_000
lock = Lock()

class Counter(Thread):
    def run(self):
        global counter
        for _ in range(rounds):
            with lock:
                counter += 1 


thread1 = Counter()
thread2 = Counter()
thread3 = Counter()

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()


print(f"Final counter value: {counter}")