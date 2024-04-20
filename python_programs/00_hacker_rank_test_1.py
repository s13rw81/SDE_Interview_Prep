import asyncio
async def task1():
	await asyncio.sleep(10)
	print('Task1 completed')
	return None # 'taskl'

async def task2():
	await asyncio.sleep(2)
	print('Task2 completed')
	return 'task2'

async def task3():
	await asyncio.sleep(3)
	print('Task3 completed')
	return 'task3'

"""
async def main():
	task1_result = await task1()
	task2_result = await task2() if task1_result else None
	task3_result = await task3() if task1_result and task2_result else None
asyncio.run(main())


async def main():
	task1_result = asyncio.create_task(task1())
	task2_result = asyncio.create_task(task2())
	task3_result = asyncio.create_task(task3())
	await task1_result
	await task2_result
	await task3_result
asyncio.run(main())
"""

async def main():

	task1_result = asyncio.ensure_future (task1())
	await task1_result
	task2_result = asyncio.ensure_future (task2()) if task1_result else None
	await task2_result
	task3_result = asyncio.ensure_future (task3()) if task2_result else None
	await task3_result

asyncio.run(main())