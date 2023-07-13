def calc():
	try:
		result = eval(input('input: '))
	except SyntaxError :
		print ("Syntax Error")
	except NameError :
		print ("NameError")
	except ZeroDivisionError:
		print("can't divide by zero")
	except TypeError:
		print('OperatorError')
	else:
		print (result)
calc()