# FIRST VERSION

# def calculate_structure_sum(data):
#     total_sum = 0
#
#     if isinstance(data, dict):
#         for key, value in data.items():
#             if isinstance(key, str):
#                 total_sum += len(key)
#             total_sum += calculate_structure_sum(value)
#     elif isinstance(data, list):
#         for item in data:
#             total_sum += calculate_structure_sum(item)
#     elif isinstance(data, tuple):
#         for item in data:
#             total_sum += calculate_structure_sum(item)
#     elif isinstance(data, (int, float)):
#         total_sum += data
#     elif isinstance(data, str):
#         total_sum += len(data)
#
#     return total_sum
#
# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
# print(result)

# SECOND VERSION

# def calculate_structure_sum(*data):
#     total_sum = 0
#
#     for item in data:
#
#         if isinstance(item, dict):
#             for key, value in item.items():
#                 total_sum += calculate_structure_sum(key)
#                 total_sum += calculate_structure_sum(value)
#
#         elif isinstance(item, (list, tuple, set)):
#             total_sum += calculate_structure_sum(*item)
#
#         elif isinstance(item,(int, float)):
#             total_sum += item
#
#         elif isinstance(item, str):
#             total_sum += len(item)
#
#     return total_sum
#
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
# print(result)
#


def get_summ(data):

    # Base case
    if isinstance(data, (float, int)):
        return data
    elif isinstance(data, str):
        return len(data)

    # Recursive case
    count = 0
    if isinstance(data, (list, tuple, set)):
        for value in data:
            count += get_summ(value)

    elif isinstance(data, dict):
        for key, value in data.items():
            count += get_summ(key)
            count += get_summ(value)

    return count


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = get_summ(data_structure)

print("Result:", result)