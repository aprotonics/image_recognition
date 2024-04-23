import asyncio


rectangles_areas_list = ["juhuhg", 'asfaspc', "kaosk", "jkjkcs"]


async def create_graph(graph_number):
    graph_number = graph_number
    i = 0

    print(graph_number)

    i += 1

    return graph_number + 1

async def main(rectangles_areas_list):
    rectangles_areas_list = rectangles_areas_list

    tasks = []
    number_of_graphs = len(rectangles_areas_list)

    if number_of_graphs > 0:
        for i in range(number_of_graphs):
            graph_number = i + 1
            task = asyncio.create_task(create_graph(graph_number))
            tasks.append(task)

    for task in tasks:
        await task
    
    results = []

    for task in tasks:
        task_result = task.result()
        results.append(task_result)
    
    for value in results:
        print(value)

asyncio.run(main(rectangles_areas_list))
