# Write your solution for algorithm 1 below
sample_list = [1, 5, 2, 6, 7]

def bubble_sort(lst):
    for i in range(len(lst)-1):
        print(f"interation ")
        for j in range(len(lst) - 1):
            print(f"comparing {lst[j], lst[j+1]}")

            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")

    

    

