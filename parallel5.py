import asyncio
import time

Delays = [1, 2, 3, 4, 5]

#Функция, которая запустит задачи асинхронно
async def async_task(delay, task_id):
    print(f"Task {task_id} started ")
    await asyncio.sleep(delay)
    print(f"Task {task_id} ended ")


async def run_async():
    print("ASYNC")
    start_time = time.time()
    
    tasks = [async_task(delay, i + 1) for i, delay in enumerate(Delays)]
    await asyncio.gather(*tasks)
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time: {total_time:.7f} sec")
    return total_time

#Функция, которая запустит задачи последовательно
def run_sequential():
    print("SEQUENTIALLY")
    start_time = time.time()
    
    for i, delay in enumerate(Delays):
        print(f"Task{i + 1} started ")
        time.sleep(delay)
        print(f"Task{i + 1} ended")
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time: {total_time:.7f} sec")
    return total_time

#Функция, котрая вывыодит результаты
async def result():
    async_time = await run_async()
    sequential_time = run_sequential()
    
    difference = sequential_time - async_time
    
    print("Results:")
    print(f"ASYNC: {async_time:.7f} sec")
    print(f"SEQUENTIALLY: {sequential_time:.7f} sec")
    print(f"Difference: {difference:.7f} sec")


def main():
    asyncio.run(result())

if __name__ == "__main__":
    main()