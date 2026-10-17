import asyncio
import time

tasks = [
    ("Downloading data", 3),
    ("Processing data", 2),
    ("Sending notification", 1),
    ("Saving results", 4),
]


async def run_single_task(name: str, duration: int):
    print(f"Task started: {name}")
    await asyncio.sleep(duration)
    print(f"Task finished: {name}")
    return f"{name} result"


async def run_sequentially(task_list):
    """ყველა task-ის თანმიმდევრულად შესრულება"""
    print("--- Sequential Execution Started ---")
    start_time = time.time()
    results = []
    for name, duration in task_list:
        result = await run_single_task(name, duration)
        results.append(result)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"--- Sequential Execution Finished in {total_time:.2f} seconds ---\n")
    return total_time


async def run_concurrently(task_list):
    """ყველა task-ის ასინქრონულად შესრულება"""
    print("--- Concurrent Execution Started ---")
    start_time = time.time()
    coroutine = [run_single_task(name, duration) for name, duration in task_list]
    await asyncio.gather(*coroutine)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"--- Concurrent Execution Finished in {total_time:.2f} seconds ---\n")
    return total_time


async def main():
    seq_time = await run_sequentially(tasks)
    conc_time = await run_concurrently(tasks)
    print("=== Execution Comparison ===")
    print(f"Sequential execution time: {seq_time:.2f} seconds")
    print(f"Concurrent execution time: {conc_time:.2f} seconds")



asyncio.run(main())