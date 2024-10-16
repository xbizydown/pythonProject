laps = 0
boolean = True

while boolean:
	if laps == 0:
		runner = input(f"Would you like to run a lap (y/n): ")
	else:
		runner = input(f"Would you like to run another lap? (y/n): ")
	if runner == "y":
		laps += 1
		print(f"You have run {laps} lap(s)")
	elif runner == "n":
		print(f"You ended the run with {laps} lap(s)")
		boolean = False
	else:
		print(f"Invalid input. Please enter either 'y' or 'n'.")
print(f"You have run {laps} laps")