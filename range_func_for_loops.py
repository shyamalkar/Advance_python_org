#range() - built-in function used to generate sequence of integers in a given into
#range(start, stop, step) stop is not included 
#range(start, stop) => step = 1 by default
#range(stop) => to stop-1 with a step of 1, start = 0 by default

profits = [9, 11, 6, 10]

for index in range(len(profits)):
    q = index + 1
    print(f"profit for quater {q} is {profits[index]}")
    