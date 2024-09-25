import asyncio
import aiofiles

async def async_write_to_file(filename, data, duration):
    print(f"Starting async write to {filename}")
    await asyncio.sleep(duration) 
    async with aiofiles.open(filename, 'w') as f:
        await f.write(data)
    print(f"Finished async write to {filename}")

async def run_async_tasks():
    tasks = [
        async_write_to_file("async_file1.txt", "Data for file 1", 2),
        async_write_to_file("async_file2.txt", "Data for file 2", 1),
        async_write_to_file("async_file3.txt", "Data for file 3", 3),
    ]
    await asyncio.gather(*tasks)
