import time
import random
import threading


def do_work(thread_id: int):
    """
    A placeholder target function to be run on each thread
     """
    delay = random.randint(1, 5)
    print(thread_id, f"sleeping for {delay}")
    time.sleep(delay)
    print(f"{thread_id} had finished")


def main():
    _threads = [ threading.Thread(target=do_work, args=[i]) for i in range(5)]
    
    #Start the threads
    for t in _threads:
        t.start()
    print("Threads started")

    for t in _threads:
        t.join()
        
    print("All threads finished")
    


if __name__ == "__main__":
    main()

