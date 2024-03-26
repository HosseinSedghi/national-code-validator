# National code


from cities_code import cities_code


def is_valid(number):
	control_number = number[-1]
	
	multip = 10
	output = 0
	for i in number[0: 9]:
		output += (int(i) * multip)
		multip -= 1

	if (output % 11) < 2:
		return True if int(control_number) == 0 or int(control_number) == 1 else False
	else:
		return True if int(control_number) == (11 - (output % 11)) else False



def find_city(number):
	city_code = number[0:3]
	try:
		location = cities_code[city_code]
	except KeyError:
		return False, None, None

	return True, location[0], location[1]
		



def find_code(city_name):
	cities = [code for code, cities in cities_code.items() if city_name in cities]
	return cities




if __name__ == '__main__':
	national_code = input('Enter national code : ')
	if len(national_code) <= 10 and len(national_code) > 7:
		national_code = ('0' * (abs(10 - len(national_code)))) + national_code
		
		if is_valid(national_code):
			status, state, city = find_city(national_code)
			if status:
				print('\ncode : {}'.format(national_code))
				print('state : {}'.format(state))
				print('city : {}'.format(city))
			else:
				print('not found !!')
		else:
			print('code is invalid !!')
	elif len(national_code) == 3:
		status, city, state = find_city(national_code)
		if status:
			print('\ncode : {}'.format(national_code))
			print('state : {}'.format(state))
			print('city : {}'.format(city))
		else:
			print('not found !!')
	else:
		print('code length most be 10')