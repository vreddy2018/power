def power(originalBase, exponent):
	count = 0
	notconverted = True
	base = 1
	while notconverted == True:
		try:
			originalBase = float(originalBase)
			exponent = int(exponent)
			
		except ValueError:
			print('sorry not a number try again.')

		else: 
			notconverted = False
	
	while count < exponent:
		base = base * originalBase
		count += 1
		
	return base
 
 
originalBase = raw_input("Base: ")
exponent = raw_input("Exponent: ")
output = power(originalBase, exponent)
print(output)