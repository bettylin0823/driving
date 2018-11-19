country = input('你所在的國家為/Please enter your country: ')
age = input('請輸入你的年齡/Please enter your age: ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif country == '美國':
	if age >= 16:
		print('You can get the drivers licenses.')
	else:
		print('You are not old enough to drive.')
else:
	print('只能輸入台灣/美國')