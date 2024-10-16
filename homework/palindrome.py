while True:
	palindrome: str = input("Enter a palindrome (or 'exit' to end the program): ")
	if palindrome.lower() == 'exit':
		print("Exiting the program.")
		break

	if palindrome == palindrome[::-1]:
		print("The word", palindrome, "is a palindrome")
	else:
		print("The word", palindrome, "is not a palindrome")