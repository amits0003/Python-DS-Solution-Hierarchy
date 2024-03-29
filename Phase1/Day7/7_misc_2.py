""" multi threading example """

import threading
import time

exitFlag = 0
threads = []
threadLock = threading.Lock()


def print_time(threadName, delay,  counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s :  %s" % (threadName, time.ctime(time.time())))
        counter = counter - 1


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting : ", self.name)

        # Get Lock to Sync Threads
        threadLock.acquire()

        print_time(self.name, self.counter, 3)

        # free Lock to release next thread

        threadLock.release()


# Generating new thread
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start New Thread
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()

print("Exiting the thread")
