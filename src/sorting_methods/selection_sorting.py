nums = [5, 4, 9, 3, 7, 2, 8, 6, 1, 0]

def selection_sort(ls):
    n = len(ls)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if ls[j] < ls[min_idx]:
                min_idx = j
        ls[i], ls[min_idx] = ls[min_idx], ls[i]
    return ls

selection_sort(nums)
print(nums)