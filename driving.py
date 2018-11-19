country = input('你所在的國家為: ')
age = input('請輸入你的年齡: ')
age = int(age)
if country == 'Taiwan' or '台灣' or '臺灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')