import threading
import time

def simulate_io_task(file_name, duration):
  print(f"Simulating I/O task for {file_name}")
  time.sleep(duration)  
  print(f"Completed I/O task for {file_name}")

def run_io_tasks():
  threads = []
  tasks = [
        ("file1.txt", 2),
        ("file2.txt", 3),
        ("file3.txt", 1)
  ]

  for file_name, duration in tasks:
        thread = threading.Thread(target=simulate_io_task, args=(file_name, duration))
        threads.append(thread)
        thread.start()
        
  for thread in threads:
        thread.join()
