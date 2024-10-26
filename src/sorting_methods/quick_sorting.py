def quick_sort(ls):
    if len(ls) <= 1:
        return ls
    pivot = ls[len(ls) // 2]
    left = [x for x in ls if x < pivot]
    middle = [x for x in ls if x == pivot]
    right = [x for x in ls if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)