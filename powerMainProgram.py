from powerFunctions import int_input
from powerFunctions import float_input
from powerFunctions import power_recursive



userBase = float_input("Tell me a base: ")
userExponent = int_input("Tell me an exponent: ")


print(power_recursive(userBase,userExponent))