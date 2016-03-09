def power(originalBase, exponent):
	count = 0
	notconverted = True
	base = 1
	while notconverted == True:
		try:
			originalBase = float(originalBase)
			exponent = int(exponent)
			
		except ValueError:
			print('Sorry not a valid number. Run again.')
			quit()
		else: 
			notconverted = False
			
	while count < exponent:
		base = base * originalBase
		count += 1
		
	return base
 
 
originalBase = raw_input("Enter a base (can be decimal or negative): ")
exponent = raw_input("Enter an exponent (must be an integer): ")
output = power(originalBase, exponent)
print(output)