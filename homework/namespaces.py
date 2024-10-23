# get_square = input("Enter a number: ")
#
# def square(x):
#     try:
#         x = int(x)
#         result = x ** x
#         return result
#     except ValueError:
#         print("Error, you can't get a square of a text!")
#         return None
#
# def check_even_odd(x):
#     try:
#         if x % 2 == 0:
#             print("Even number")
#         else:
#             print("Odd number")
#     except TypeError:
#         print("Error, input is not a number!")
#
# result = square(get_square)
# check_even_odd(result)
#
# if result is not None:
#     print(f"Your number squared is {result}")
#
# bank = {}
#
# bank['department1'] = {}
# bank['department2'] = {}
#
# bank['department1']['account1'] = {'balance': 1000, 'owner': 'John Doe'}
# bank['department1']['account2'] = {'balance': 500, 'owner': 'Jane Doe'}
# bank['department2']['account3'] = {'balance': 2000, 'owner': 'Bob Smith'}
# bank['department2']['account4'] = {'balance': 1500, 'owner': 'Alice Johnson'}
#
# def print_accounts(department):
#     print(f"Accounts in {department}:")
#     for account, info in bank[department].items():
#         print(f"Account {account}: balance={info['balance']}, owner={info['owner']}")
#
# print_accounts('department1')
# print_accounts('department2')
















def test_function():
    print("This is a test function.")
    global inner_function
    def inner_function():
        print("This is an inner function.")
    inner_function()
test_function()
# inner_function() # If you will try to call the local function globally you will have an Error! Because it is not defined
# But I  added the "global inner_function" so it has to work!

inner_function()