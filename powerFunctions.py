def power_recursive(base, exponent):
	
	if exponent == 0:
		return 1

	output = base * power_recursive(base, exponent - 1)

	return output
	


def int_input(prompt):
	answer = raw_input(prompt)
	
	try:
		return int(answer)
	except ValueError:
		return (int_input("That wasn't a valid integer number. Try again."))
	
	
def float_input(prompt):
	answer = raw_input(prompt)
	
	try:
		return float(answer)
	except ValueError:
		return (float_input("That wasn't a valid decimal number. Try again."))
	
	