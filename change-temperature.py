print ('這是一個華氏/攝氏溫度轉換程式')

while True :
	print('華氏 : f','攝氏 : c', 'End : e')
	U = input('請輸入你想知道的溫度單位: ')
	
	if U != 'f' and U !='c' and U != 'e' :
		print ('輸入錯誤!!請輸入 "f" or "c" or "e"')
	else :
		if U =='e' :
			print ('謝謝使用')
			break
		else :
			T = input('請輸入要轉換的溫度: ')
			T = float(T)
			if U =='f' :
				Fahrenheit = T*9/5+32
				print ('等於華氏', Fahrenheit, '度')
			else :
				Celsius = (T-32)*5/9
				print ('等於攝氏', Celsius, '度')


