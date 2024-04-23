import asyncio


async def count_multiplication(clusters):
    clusters = clusters

    multiplication = 1

    for i in range(1, clusters + 1):
        value = i
        multiplication = multiplication * value
    
    print(multiplication)
    print()
    print()

    return multiplication

async def function(clusters):
    clusters = clusters
    multiplication = await count_multiplication(clusters)

async def main():
    cluster1 = [51, 994, 62, 14, 1, 922]
    cluster2 = [    253, 181, 971, 811, 3, 35, 63, 1, 22, 43,
                    21, 14, 115, 914, 817, 914, 771, 912, 911,
                    14, 914, 911, 914, 814, 141, 941, 141, 14,
                    841, 96, 844, 814, 11, 34, 12, 441, 3, 4, 25, 4     ]    
    cluster3 = [151, 1, 452, 214, 2, 45, 8, 34, 3]
    cluster4 = [52, 55, 1, 77, 3, 144, 67, 3]
    cluster5 = [51, 14, 124, 2341]

    cluster = cluster2
    tasks = []
    number_of_graphs = len(cluster)
    if number_of_graphs > 0:
        for i in range(number_of_graphs):
            task = asyncio.create_task(function(cluster[i]))
            tasks.append(task)

    for task in tasks:
        await task


asyncio.run(main())
