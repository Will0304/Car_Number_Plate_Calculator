import pandas as pd

def calculate_the_number_plate():
	try:
		vehicle_ID = int(input('Type in the vehicle ID number. It should be a whole number between 0 and 17558423 : '))

		series_number=vehicle_ID%999+1

		amount_of_switches = vehicle_ID//999

		right_letter = chr(97+amount_of_switches//26**2)
		#calculates the right letter, same as 'abcdefghijklmnopqrstuvwxyz'[amount_of_switches//26**2]

		middle_letter = chr(97+amount_of_switches%26**2//26)
		#calculates the middle letter, same as 'abcdefghijklmnopqrstuvwxyz'[amount_of_switches%26**2//26]

		left_letter = chr(97+amount_of_switches%26**2%26)
		#calculates the middle letter, same as 'abcdefghijklmnopqrstuvwxyz'[amount_of_switches%26**2%26]
	
		result = left_letter+middle_letter+right_letter+str(series_number).rjust(3,'0')

		return pd.DataFrame({'ID':[vehicle_ID],'NP':[result]})
		#returns the result as a data frame, containing the customer ID and the number plate itself
	
	except ValueError:
		#if the inut number is negative or contains non-digit characters or is bigger than 17558423 (the maximum value), a Value Error is returned
		return 'Invalid Input'



