def quicksort_extra_storage(S, a, b):
    if a >= b:
        return  # Base case: one element or empty segment

    pivot = S[b]  # Choose the pivot
    # Create new arrays for the partitions
    left_partition = []
    right_partition = []

    for i in range(a, b):  # Iterate only until b (exclude the pivot)
        if S[i] < pivot:
            left_partition.append(S[i])
        else:
            right_partition.append(S[i])

    # recursively go into the left_partition list, beteen 0 and length of partition - 1 (because a new pivot in the recursion)
    quicksort_extra_storage(left_partition, 0, len(left_partition) - 1)

    # recursively go into the right_partition list, beteen 0 and length of partition - 1 (because a new pivot in the recursion)
    quicksort_extra_storage(right_partition, 0, len(right_partition) - 1)

    # combine the sorted right and left partition with the pivot from the first iteration
    S[a:b + 1] = left_partition + [pivot] + right_partition

    return S
print(quicksort_extra_storage([1,2,54,1,2,4,5,1,2,6,7,8,99], 0, 12)) #example