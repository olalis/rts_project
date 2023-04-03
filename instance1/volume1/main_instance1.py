import time

while True:    
    try:
        with open("../storage/test.txt", "a") as f:
            f.write(f"instance 1: {time.perf_counter_ns()}\n")
            f.close()

    except:
        pass