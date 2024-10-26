nums = [5, 4, 9, 3, 7, 2, 8, 6, 1, 0]

def bubble_sort(ls):
    sort = False
    while not sort:
        sort = True
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                sort = False

bubble_sort(nums)
print(nums)