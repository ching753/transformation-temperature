print ('這是一個華氏/攝氏溫度轉換程式')
while True :
	U = input('請輸入你想知道的溫度單位: ')
	if U != '華氏' and U !='攝氏' and U != 'close' :
		print ('輸入錯誤!!請輸入華氏 or 攝氏 or close')
	else :
		if U =='close' :
			print ('謝謝使用')
			break
		else :
			T = input('請輸入要轉換的溫度: ')
			T = float(T)
			if U =='華氏' :
				W = T*9/5-32
				print ('等於華氏', W, '度')
			else :
				C = (T-32)*5/9
				print ('等於攝氏', C, '度')


