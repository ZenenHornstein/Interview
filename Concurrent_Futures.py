
import random, time
import concurrent.futures

def do_work(thread_id: int):
    """
    A placeholder target function to be run on each thread
     """
    delay = random.randint(1, 5)
    print(thread_id, f"sleeping for {delay}")
    time.sleep(delay)
    print(f"{thread_id} had finished")
    return thread_id




def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        print("Starting threads")
        futures = [executor.submit(do_work, i) for i in range(5)]
        print("All threads Started")
        for f in concurrent.futures.as_completed(futures):
            pass



    

if __name__ == "__main__":
    main()