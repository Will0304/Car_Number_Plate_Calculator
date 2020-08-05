import pandas as pd

def calculate_the_number_plate():
	try:
		customer_ID = int(input('Type in the customer ID number. It should be a whole number between 0 and 17558423 : '))

		series_number=customer_ID%999+1

		amount_of_switches = customer_ID//999

		right_letter = chr(97+amount_of_switches//26**2)
		#calculates the right letter, same as 'abcdefghijklmnopqrstuvwxyz'[amount_of_switches//26**2]

		middle_letter = chr(97+amount_of_switches%26**2//26)
		#calculates the middle letter, same as 'abcdefghijklmnopqrstuvwxyz'[amount_of_switches%26**2//26]

		left_letter = chr(97+amount_of_switches%26**2%26)
		#calculates the middle letter, same as 'abcdefghijklmnopqrstuvwxyz'[amount_of_switches%26**2%26]
	
		result = left_letter+middle_letter+right_letter+str(series_number).rjust(3,'0')

		return pd.DataFrame({'ID':[customer_ID],'NP':[result]})
		#returns the result as a data frame, containing the customer ID and the number plate itself
	
	except ValueError:
		#if the inut number is negative or contains non-digit characters or is bigger than 17558423 (the maximum value), a Value Error is returned
		return 'Invalid Input'

# some test cases:
test.assert_equals(calculate_the_number_plate(651),'aaa652')
test.assert_equals(calculate_the_number_plate(867819),'khb688')
test.assert_equals(calculate_the_number_plate(65192),'nca258')
