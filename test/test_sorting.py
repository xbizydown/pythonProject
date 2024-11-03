from src.sorting_methods.bubble_sorting import bubble_sort
from src.sorting_methods.selection_sorting import selection_sort
from src.sorting_methods.quick_sorting import quick_sort

def sort_and_print():
    values = list(map(int, input("Enter list of numbers: ").split()))
    print("Original list:", values)

    bubble_numbers = values[:]
    selection_numbers = values[:]
    quick_sorted_numbers = values[:]

    bubble_sort(bubble_numbers)
    selection_sort(selection_numbers)
    quick_sorted_numbers = quick_sort(quick_sorted_numbers)

    print("Bubble sort:", bubble_numbers)
    print("Selection sort:", selection_numbers)
    print("Quick sort:", quick_sorted_numbers)

sort_and_print()